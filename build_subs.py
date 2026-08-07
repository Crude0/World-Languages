#!/usr/bin/env python3
"""Natural Earth admin-1 (eyalet/il/kanton) sınırları -> projeksiyonlu SVG yolları.

Önemli ayrıntı: komşu bölgeler ortak sınırı paylaşır. Her halkayı tek tek
sadeleştirmek bu ortak sınırda farklı noktalar seçtirir ve aralarında yarık
(sliver) bırakır. Bu yüzden önce noktalar ızgaraya oturtulur, halkalar ortak
noktalarda yaylara (arc) bölünür ve her yay bir kez sadeleştirilir. RDP yön
bağımsız olduğu için iki komşu aynı yayda birebir aynı sonucu üretir.
"""
import json
import sys
from anchor import label_anchor
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


def inner_borders(rings_by_country):
    """Ülke içindeki il/eyalet sınırları: iki ilde birden geçen kenarlar.

    İki komşu il ortak sınırı paylaşınca o kenar iki kez sayılır; bir kez geçen
    kenarlar ise ülkenin dış çeperidir (kıyı ya da uluslararası sınır). Noktalar
    ızgaraya oturtulduğu için kenarlar birebir eşleşir.

    Bu ayrım gerekli: illerin yollarını olduğu gibi konturlamak ülke sınırını
    değil *her* sınırı aynı biçimde çizer — ABD–Kanada sınırı eyalet çizgisinden
    ayırt edilemiyordu, kıyılar da beyaz çerçeveli görünüyordu. Artık ülke sınırı
    düz koyu, il sınırı koyu kılıf üstünde beyaz çekirdek.
    """
    out = {}
    for cid, rings in rings_by_country.items():
        count = defaultdict(int)
        for ring in rings:
            n = len(ring)
            for i in range(n):
                a, b = ring[i], ring[(i + 1) % n]
                count[(a, b) if a <= b else (b, a)] += 1
        edges = [e for e, c in count.items() if c >= 2]
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b); adj[b].append(a)
        used, paths = set(), []
        for a, b in edges:
            key = (a, b)
            if key in used:
                continue
            used.add(key)
            chain = [a, b]
            # iki uçtan da büyüt
            for _ in range(2):
                while True:
                    tip, prev = chain[-1], chain[-2]
                    nxt = None
                    for q in adj[tip]:
                        k = (tip, q) if tip <= q else (q, tip)
                        if q != prev and k not in used:
                            nxt = q; used.add(k); break
                    if nxt is None:
                        break
                    chain.append(nxt)
                chain.reverse()
            if len(chain) > 2:
                paths.append(chain)
        out[cid] = "".join("M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in c) for c in paths)
    return out


def rings_of(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    return geom["coordinates"]


def main():
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
    by_country = defaultdict(list)          # ülke konturu için sadeleştirilmiş halkalar
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
        by_country[cid].extend(pts for _, pts, _ in kept)
        cx, cy = label_anchor(kept)
        e = res.setdefault(sid, {"n": name, "p": cid, "d": "", "c": [0, 0], "a": 0.0})
        e["d"] += d
        if sum(p[0] for p in kept if not p[2]) > e["a"]:
            e["c"] = [cx, cy]
        e["a"] = round(e["a"] + sum(p[0] for p in kept if not p[2]), 1)

    edge = inner_borders(by_country)
    json.dump({"w": round(W, 1), "h": round(H, 1), "s": res, "inner": edge},
              open(OUT, "w"), separators=(",", ":"), ensure_ascii=False)
    print("  iç sınır parçası:", {k: v.count("M") for k, v in edge.items()},
          f" toplam {sum(len(v) for v in edge.values())/1024:.0f} KB")
    per = defaultdict(int)
    for v in res.values():
        per[v["p"]] += 1
    pts = sum(v["d"].count("L") + v["d"].count("M") for v in res.values())
    print(f"alt bölge: {len(res)}  nokta: {pts}  "
          f"boyut: {len(json.dumps(res, ensure_ascii=False))/1024:.0f} KB")
    print("  ülke başına:", dict(per))


if __name__ == "__main__":
    main()
