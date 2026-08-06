#!/usr/bin/env python3
"""TopoJSON (world-atlas 50m) -> projected SVG paths for the language map."""
import json
import math, sys
from anchor import label_anchor

SRC = "countries-50m.json"
OUT = "map_paths.json"

W = 1400.0          # target width in svg units
LAT_MIN = -58.0     # drop Antarctica
LAT_MAX = 84.0
TOL = 0.30          # RDP tolerance in svg units
MIN_RING_AREA = 1.2 # svg units^2 - drop specks (largest ring always kept)

# ---------- topojson decode ----------
topo = json.load(open(SRC))
sx, sy = topo["transform"]["scale"]
tx, ty = topo["transform"]["translate"]

arcs = []
for arc in topo["arcs"]:
    x = y = 0
    pts = []
    for dx, dy in arc:
        x += dx; y += dy
        pts.append((x * sx + tx, y * sy + ty))
    arcs.append(pts)

def arc_pts(i):
    if i < 0:
        return arcs[~i][::-1]
    return arcs[i]

def ring_coords(ring_arcs):
    pts = []
    for i in ring_arcs:
        seg = arc_pts(i)
        pts.extend(seg if not pts else seg[1:])
    return pts

# ---------- Natural Earth projection (Savric et al.) ----------
def project(lon, lat):
    lam = math.radians(lon)
    phi = math.radians(max(min(lat, 90.0), -90.0))
    p2 = phi * phi
    p4 = p2 * p2
    x = lam * (0.8707 - 0.131979 * p2 - 0.013791 * p4
               + 0.003971 * p4 * p4 * p2 - 0.001529 * p4 * p4 * p4)
    y = phi * (1.007226 + 0.015085 * p2 - 0.044475 * p2 * p4
               + 0.028874 * p4 * p4 - 0.005916 * p4 * p4 * p2)
    return x, y

# ---------- Ramer-Douglas-Peucker ----------
def rdp(pts, tol):
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    t2 = tol * tol
    while stack:
        a, b = stack.pop()
        if b <= a + 1:
            continue
        ax, ay = pts[a]; bx, by = pts[b]
        dx, dy = bx - ax, by - ay
        d2 = dx * dx + dy * dy
        worst = -1.0; idx = -1
        for i in range(a + 1, b):
            px, py = pts[i]
            if d2 == 0:
                dist = (px - ax) ** 2 + (py - ay) ** 2
            else:
                t = ((px - ax) * dx + (py - ay) * dy) / d2
                t = 0.0 if t < 0 else (1.0 if t > 1 else t)
                cx, cy = ax + t * dx, ay + t * dy
                dist = (px - cx) ** 2 + (py - cy) ** 2
            if dist > worst:
                worst = dist; idx = i
        if worst > t2:
            keep[idx] = True
            stack.append((a, idx)); stack.append((idx, b))
    return [p for p, k in zip(pts, keep) if k]

def split_antimeridian(pts):
    """Bir halka 180. meridyeni geçiyorsa kenardan kesip ayrı halkalara böl."""
    pieces, cur = [], [pts[0]]
    for i in range(1, len(pts)):
        lon1, lat1 = pts[i - 1]
        lon2, lat2 = pts[i]
        d = lon2 - lon1
        if -180 <= d <= 180:
            cur.append((lon2, lat2))
            continue
        if d < -180:                      # doğuya, +180 üzerinden
            lon2u, edge_out, edge_in = lon2 + 360, 180.0, -180.0
        else:                             # batıya, -180 üzerinden
            lon2u, edge_out, edge_in = lon2 - 360, -180.0, 180.0
        span = lon2u - lon1
        t = (edge_out - lon1) / span if span else 0.0
        latc = lat1 + t * (lat2 - lat1)
        cur.append((edge_out, latc))
        pieces.append(cur)
        cur = [(edge_in, latc), (lon2, lat2)]
    pieces.append(cur)
    if len(pieces) == 1:
        return [pts]
    merged = pieces[-1] + pieces[0][1:]   # halka kapalı: son parça ilkinin devamı
    return [merged] + pieces[1:-1]


def ring_area(pts):
    s = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % len(pts)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0

# ---------- scale setup ----------
x0, _ = project(-180, 0); x1, _ = project(180, 0)
_, ytop = project(0, LAT_MAX); _, ybot = project(0, LAT_MIN)
scale = W / (x1 - x0)
H = (ytop - ybot) * scale

def to_svg(lon, lat):
    x, y = project(lon, lat)
    return ((x - x0) * scale, (ytop - y) * scale)

# ---------- build ----------
geoms = topo["objects"]["countries"]["geometries"]
SYNTH = {"Kosovo": "900", "N. Cyprus": "901", "Somaliland": "902",
         "Indian Ocean Ter.": "903", "Siachen Glacier": "904"}
SKIP = {"010", "260", "334", "239", "904", "903"}  # Antarctica & sub-antarctic specks

feats = {}
for g in geoms:
    name = g["properties"]["name"]
    cid = g.get("id") or SYNTH.get(name)
    if not cid or cid in SKIP:
        continue
    polys = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]]
    rings = []
    for poly in polys:
        for k, ring in enumerate(poly):
            for part in split_antimeridian(ring_coords(ring)):
                raw = [to_svg(lon, lat) for lon, lat in part]
                if len(raw) < 4:
                    continue
                # küçük şekiller varsayılan toleransta kimliğini yitiriyor
                tol = TOL if ring_area(raw) > 4.0 else TOL / 6.0
                pts = rdp(raw, tol)
                if len(pts) < 4:
                    pts = raw
                rings.append((ring_area(pts), pts, k > 0))
    if not rings:
        continue
    entry = feats.setdefault(cid, {"name": name, "rings": []})
    entry["rings"].extend(rings)

out = {}
for cid, f in feats.items():
    rings = f["rings"]
    biggest = max(r[0] for r in rings)
    kept = [r for r in rings if r[0] >= MIN_RING_AREA or r[0] == biggest]
    d = []
    for area, pts, is_hole in kept:
        d.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z")
    # visual anchor: pole of inaccessibility of the largest solid ring — a
    # vertex mean lands offshore on concave coasts (Norway, Croatia, Vietnam)
    cx, cy = label_anchor(kept)
    total = sum(r[0] for r in kept if not r[2])
    out[cid] = {"n": f["name"], "d": "".join(d),
                "c": [round(cx, 1), round(cy, 1)], "a": round(total, 1)}

# ---------- graticule + projection outline ----------
def polyline(pts):
    return "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts)

grat = []
for lon in range(-150, 180, 30):
    grat.append(polyline([to_svg(lon, lat) for lat in
                          [LAT_MIN + i * (LAT_MAX - LAT_MIN) / 60 for i in range(61)]]))
for lat in range(-30, 90, 30):
    if lat < LAT_MIN or lat > LAT_MAX:
        continue
    grat.append(polyline([to_svg(-180 + i * 360 / 120, lat) for i in range(121)]))
equator = polyline([to_svg(-180 + i * 360 / 120, 0) for i in range(121)])

frame = ([to_svg(-180, LAT_MIN + i * (LAT_MAX - LAT_MIN) / 60) for i in range(61)]
         + [to_svg(-180 + i * 360 / 120, LAT_MAX) for i in range(121)]
         + [to_svg(180, LAT_MAX - i * (LAT_MAX - LAT_MIN) / 60) for i in range(61)]
         + [to_svg(180 - i * 360 / 120, LAT_MIN) for i in range(121)])

json.dump({"w": round(W, 1), "h": round(H, 1), "f": out,
           "grat": " ".join(grat), "eq": equator, "frame": polyline(frame) + "Z"},
          open(OUT, "w"), separators=(",", ":"), ensure_ascii=False)

tiny = sorted((v["a"], v["n"]) for v in out.values())[:30]
print(f"countries: {len(out)}  size: {len(json.dumps(out))/1024:.0f} KB  h={H:.1f}")
print("smallest:", ", ".join(f"{n}({a})" for a, n in tiny))
