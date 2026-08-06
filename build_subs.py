#!/usr/bin/env python3
"""Natural Earth admin-1 (eyalet/il/kanton) sınırları -> projeksiyonlu SVG yolları.

Önemli ayrıntı: komşu bölgeler ortak sınırı paylaşır. Her halkayı tek tek
sadeleştirmek bu ortak sınırda farklı noktalar seçtirir ve aralarında yarık
(sliver) bırakır. Bu yüzden önce noktalar ızgaraya oturtulur, halkalar ortak
noktalarda yaylara (arc) bölünür ve her yay bir kez sadeleştirilir. RDP yön
bağımsız olduğu için iki komşu aynı yayda birebir aynı sonucu üretir.
"""
import json, sys
from collections import defaultdict
from build_map import rdp, ring_area, to_svg, W, H   # aynı projeksiyon

SRC = "ne_admin1_10m.json"
OUT = "sub_paths.json"
Q = 0.05              # ızgara: ortak noktaların birebir çakışması için
TOL = 0.22            # yay başına RDP toleransı (svg birimi)
MIN_AREA = 0.6

WANT = {
    "CAN": ("124", "self"), "USA": ("840", "self"), "CHE": ("756", "self"),
    "BEL": ("056", "self"), "ESP": ("724", "region"), "GBR": ("826", "nation"),
    "IND": ("356", "self"), "ITA": ("380", "region"), "TUR": ("792", "self"),
    "UKR": ("804", "self"), "FIN": ("246", "self"), "BOL": ("068", "self"),
}

GBR_NATION = {
    "Northern Ireland": "Kuzey İrlanda",
    "West Wales and the Valleys": "Galler", "East Wales": "Galler",
    "Eastern": "İskoçya", "North Eastern": "İskoçya",
    "South Western": "İskoçya", "Highlands and Islands": "İskoçya",
}


def qz(x, y):
    return (round(x / Q) * Q, round(y / Q) * Q)


def clean(ring):
    """Izgaraya oturt, ardışık tekrarları at, halkayı kapat."""
    out = []
    for x, y in ring:
        p = qz(x, y)
        if not out or p != out[-1]:
            out.append(p)
    while len(out) > 1 and out[0] == out[-1]:
        out.pop()
    return out


def find_junctions(rings):
    """TopoJSON kuralı: komşu çifti farklılaşan nokta yay başlangıcıdır.

    Bir noktanın önceki+sonraki komşuları tüm halkalarda aynıysa o nokta ortak
    sınırın içinde kalır. Farklıysa orada bir sınır başlıyor/bitiyor demektir.
    Yalnızca 'kaç halkada geçiyor' saymak yetmez: A'nın B ve C ile sınırı
    ardışık olduğunda sayı değişmez ama kırılma noktası oradadır.
    """
    seen, junction = {}, set()
    for ring in rings:
        n = len(ring)
        for i, p in enumerate(ring):
            key = frozenset((ring[i - 1], ring[(i + 1) % n]))
            prev = seen.get(p)
            if prev is None:
                seen[p] = key
            elif prev != key:
                junction.add(p)
    return junction


def simplify(ring, junction):
    """Halkayı yaylara bölüp her yayı bir kez sadeleştir."""
    n = len(ring)
    if n < 8:
        return ring
    breaks = [i for i, p in enumerate(ring) if p in junction]
    if len(breaks) < 2:                       # tek parça: doğrudan sadeleştir
        s = rdp(ring + [ring[0]], TOL)
        return s[:-1] if len(s) > 4 else ring
    out = []
    for k, a in enumerate(breaks):
        b = breaks[(k + 1) % len(breaks)]
        seg, i = [], a
        while True:
            seg.append(ring[i])
            if i == b:
                break
            i = (i + 1) % n
        out.extend(rdp(seg, TOL)[:-1])        # bitiş noktası sonraki yayın başı
    return out


def rings_of(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    return geom["coordinates"]


NE_URL = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
          "master/geojson/ne_10m_admin_1_states_provinces.geojson")


def fetch_source():
    """Alt bölge sınırları ~40 MB tutuyor; depoda durmuyor, ilk derlemede
    Natural Earth deposundan indiriliyor."""
    import os, urllib.request
    if os.path.exists(SRC):
        return
    print(f"· {SRC} indiriliyor (~40 MB, bir kereye mahsus)")
    urllib.request.urlretrieve(NE_URL, SRC)


def main():
    fetch_source()
    data = json.load(open(SRC))
    feats = []                                # (sid, ad, ülke, kod, [halkalar])
    for feat in data["features"]:
        p = feat["properties"]
        iso3 = p.get("adm0_a3")
        if iso3 not in WANT:
            continue
        cid, mode = WANT[iso3]
        name = p.get("name") or p.get("name_en") or ""
        if mode == "region":
            key = p.get("region")
        elif mode == "nation":
            key = GBR_NATION.get(p.get("region"), "İngiltere")
        else:
            key = name
        if not key:
            continue
        rings = []
        for poly in rings_of(feat["geometry"]):
            for k, r in enumerate(poly):
                q = clean([to_svg(lo, la) for lo, la in r])
                if len(q) >= 4:
                    rings.append((q, k > 0))
        if rings:
            feats.append((f"{cid}-{key}", key, cid, rings))

    junction = find_junctions([r for _, _, _, rings in feats for r, _h in rings])

    res = {}
    for sid, name, cid, rings in feats:
        parts = []
        for r, hole in rings:
            s = simplify(r, junction)
            if len(s) < 4:
                s = r
            parts.append((ring_area(s), s, hole))
        biggest = max(p[0] for p in parts)
        kept = [p for p in parts if p[0] >= MIN_AREA or p[0] == biggest]
        d = "".join("M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "Z"
                    for _, pts, _ in kept)
        main_ring = max(kept, key=lambda p: p[0])[1]
        cx = sum(q[0] for q in main_ring) / len(main_ring)
        cy = sum(q[1] for q in main_ring) / len(main_ring)
        e = res.setdefault(sid, {"n": name, "p": cid, "d": "", "c": [0, 0], "a": 0.0})
        e["d"] += d
        if sum(p[0] for p in kept if not p[2]) > e["a"]:
            e["c"] = [round(cx, 1), round(cy, 1)]
        e["a"] = round(e["a"] + sum(p[0] for p in kept if not p[2]), 1)

    json.dump({"w": round(W, 1), "h": round(H, 1), "s": res},
              open(OUT, "w"), separators=(",", ":"), ensure_ascii=False)
    per = defaultdict(int)
    for v in res.values():
        per[v["p"]] += 1
    pts = sum(v["d"].count("L") + v["d"].count("M") for v in res.values())
    print(f"alt bölge: {len(res)}  nokta: {pts}  "
          f"boyut: {len(json.dumps(res, ensure_ascii=False))/1024:.0f} KB")
    print("  ülke başına:", dict(per))


if __name__ == "__main__":
    main()
