#!/usr/bin/env python3
"""Natural Earth admin-1 (eyalet/il/kanton) sınırları -> projeksiyonlu SVG yolları.

Önemli ayrıntı: komşu bölgeler ortak sınırı paylaşır. Her halkayı tek tek
sadeleştirmek bu ortak sınırda farklı noktalar seçtirir ve aralarında yarık
(sliver) bırakır. Bu yüzden önce noktalar ızgaraya oturtulur, halkalar ortak
noktalarda yaylara (arc) bölünür ve her yay bir kez sadeleştirilir. RDP yön
bağımsız olduğu için iki komşu aynı yayda birebir aynı sonucu üretir.
"""
import json
import os
import shutil
import sys
import urllib.request
from anchor import label_anchor
from collections import defaultdict
from build_map import rdp, ring_area, to_svg, W, H   # aynı projeksiyon

SRC = "ne_admin1_10m.json"
URL = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
       "geojson/ne_10m_admin_1_states_provinces.geojson")
OUT = "sub_paths.json"
Q = 0.05              # ızgara: ortak noktaların birebir çakışması için
TOL = 0.22            # yay başına RDP toleransı (svg birimi)
MIN_AREA = 0.6

WANT = {
    "CAN": ("124", "self"), "USA": ("840", "self"), "CHE": ("756", "self"),
    "BEL": ("056", "self"), "ESP": ("724", "region"), "GBR": ("826", "nation"),
    "IND": ("356", "self"), "ITA": ("380", "region"), "TUR": ("792", "self"),
    "UKR": ("804", "self"), "FIN": ("246", "self"), "BOL": ("068", "self"),
    # 0.7.0'da eklendi. Brezilya bilerek dışarıda: 27 eyaletin hepsinde
    # Portekizce ~%98, yani 2389 nokta karşılığında tek renkli bir yüzey.
    "RUS": ("643", "self"), "CHN": ("156", "self"), "NGA": ("566", "self"),
    "ZAF": ("710", "self"), "FRA": ("250", "region"), "DEU": ("276", "self"),
}

# Natural Earth admin-1'de Kırım ve Sivastopol Rusya'ya bağlı görünüyor.
# Bu depo sınırlarda taraf tutmuyor (bkz. README): ülke katmanı Natural
# Earth 1:50m'i olduğu gibi çiziyor, alt bölge katmanı da bu iki birimi
# hiç almıyor. Böylece bölge kipine geçmek yarımadanın hangi ülkeye ait
# sayıldığını değiştirmiyor — 0.6.1'deki davranış birebir korunuyor.
# Paracel (Xisha) Adaları da aynı sebeple dışarıda: Çin, Vietnam ve Tayvan
# talep ediyor, üzerinde yerleşik nüfus yok.
SKIP = {("RUS", "Crimea"), ("RUS", "Sevastopol"), ("CHN", "Paracel Islands")}

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


def _chain(edges):
    """Kenar kümesini uçtan uca birleştirip polylinelara çevir."""
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
        paths.append(chain)
    return paths


CELL = 40.0            # kova ızgarası (svg birimi) — bkz. bucket()


def bucket(chains):
    """Zincirleri mekânsal kovalara ayırıp her kova için bir yol üretir.

    Sınır ağı eskiden ülke başına *tek* bir yoldu. Budama yol düzeyinde
    çalıştığı için Rusya'nın 153 zincirlik çeperi, ekranda yüzde onu
    görünse bile bütünüyle konturlanıyordu. Zincirler kaba bir ızgaraya
    dağıtılınca ekran dışında kalan kovalar eleniyor.
    """
    cells = defaultdict(list)
    for c in chains:
        cx = sum(x for x, _ in c) / len(c)
        cy = sum(y for _, y in c) / len(c)
        cells[(int(cx // CELL), int(cy // CELL))].append(c)
    return ["".join("M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in c) for c in group)
            for _, group in sorted(cells.items())]


def border_network(rings_by_country):
    """Bölgelerin kenarlarını sayıp iki ağa ayır: iç sınır ve dış çeper.

    Kenarın iki yanındaki *veri birimleri* karşılaştırılıyor, kaynak
    dosyadaki idari birimler değil: ikisi de aynı birime düşüyorsa o kenar
    hiç çizilmiyor.

    İki komşu il ortak sınırı paylaşınca o kenar iki kez sayılır; bir kez geçen
    kenarlar ise ülkenin dış çeperidir (kıyı ya da uluslararası sınır). Noktalar
    ızgaraya oturtulduğu için kenarlar birebir eşleşir.

    Bu ayrım iki işe yarıyor. Görsel olan: illerin yollarını olduğu gibi
    konturlamak ülke sınırını değil *her* sınırı aynı biçimde çizer —
    ABD–Kanada sınırı eyalet çizgisinden ayırt edilemiyordu. Artık ülke sınırı
    düz koyu, il sınırı koyu kılıf üstünde beyaz çekirdek.

    Performans olan: eskiden ülkenin dış çeperi, tüm il yollarının konturlanıp
    üstlerinin dolguyla örtülmesiyle elde ediliyordu (`.sbase`). Yani her iç
    sınır iki kez konturlanıp sonra saklanıyordu. Dış çeperi ayrı bir ağ olarak
    üretmek aynı görüntüyü, geometrinin yarısıyla veriyor.
    """
    inner, outer = {}, {}
    for cid, items in rings_by_country.items():
        count = defaultdict(int)
        owners = defaultdict(set)
        for sid, ring in items:
            n = len(ring)
            for i in range(n):
                a, b = ring[i], ring[(i + 1) % n]
                e = (a, b) if a <= b else (b, a)
                count[e] += 1
                owners[e].add(sid)
        # İki kez geçen ama iki yanı da AYNI veri birimi olan kenar hiç
        # çizilmiyor: Fransa'da bölge verisi var, département verisi yok;
        # yine de her département'ın sınırı çiziliyordu ve harita elle
        # seçilebilecek gibi duruyordu — üstüne gelince "Île-de-France"
        # yazıyordu. Aynısı Birleşik Krallık'ta ilçe/İngiltere için.
        inner[cid] = bucket(_chain([e for e, c in count.items()
                                    if c >= 2 and len(owners[e]) >= 2]))
        outer[cid] = bucket(_chain([e for e, c in count.items() if c == 1]))
    return inner, outer


def pts_of(res):
    return sum(v["d"].count("L") + v["d"].count("M") for v in res.values())


def rings_of(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    return geom["coordinates"]


def fetch_source():
    """Kaynak dosya yoksa indir. 40 MB, depoda tutulmuyor.

    README uzun süredir bunu vaat ediyordu ama kod yoktu: dosya elle
    indirilmişti ve temiz bir kopyada `make` çalışmıyordu.

    İndirme sessizce yarıda kesilebiliyor (ilk denemede 40 MB yerine 35 MB
    geldi ve JSON ortasından koptu). Bu yüzden hem uzunluk hem de ayrıştırma
    doğrulanıyor; tutmazsa yeniden deneniyor.
    """
    if os.path.exists(SRC):
        return
    tmp = SRC + ".part"
    last = ""
    for attempt in range(1, 4):
        print(f"· {SRC} yok, Natural Earth'ten indiriliyor (~40 MB, deneme {attempt})")
        try:
            req = urllib.request.Request(URL, headers={"User-Agent": "world-languages-build"})
            with urllib.request.urlopen(req, timeout=300) as r:
                want = int(r.headers.get("Content-Length") or 0)
                with open(tmp, "wb") as f:
                    shutil.copyfileobj(r, f)
            got = os.path.getsize(tmp)
            if want and got != want:
                last = f"eksik indi: {got} / {want} bayt"
                continue
            with open(tmp, encoding="utf-8") as f:
                json.load(f)                     # bozuksa burada patlar
            os.replace(tmp, SRC)
            print(f"· indirildi: {got/1024/1024:.0f} MB")
            return
        except Exception as e:                   # ağ ya da ayrıştırma hatası
            last = f"{type(e).__name__}: {e}"
    if os.path.exists(tmp):
        os.remove(tmp)
    sys.exit(f"{SRC} indirilemedi ({last}).\nElle indirip depo köküne koyun:\n  {URL}")


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
        if (iso3, name) in SKIP:
            continue
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
        by_country[cid].extend((sid, pts) for _, pts, _ in kept)
        cx, cy = label_anchor(kept)
        e = res.setdefault(sid, {"n": name, "p": cid, "d": "", "c": [0, 0], "a": 0.0})
        e["d"] += d
        if sum(p[0] for p in kept if not p[2]) > e["a"]:
            e["c"] = [cx, cy]
        e["a"] = round(e["a"] + sum(p[0] for p in kept if not p[2]), 1)

    inner, outer = border_network(by_country)
    json.dump({"w": round(W, 1), "h": round(H, 1), "s": res,
               "inner": inner, "outer": outer},
              open(OUT, "w"), separators=(",", ":"), ensure_ascii=False)
    npts = lambda net: sum(d.count("L") + d.count("M")
                           for paths in net.values() for d in paths)
    nbox = lambda net: sum(len(paths) for paths in net.values())
    print(f"  sınır ağı: iç {npts(inner)} nokta / {nbox(inner)} kova, "
          f"dış {npts(outer)} nokta / {nbox(outer)} kova "
          f"(eskiden dış çeper için {pts_of(res)} nokta konturlanıyordu)")
    per = defaultdict(int)
    for v in res.values():
        per[v["p"]] += 1
    pts = pts_of(res)
    print(f"alt bölge: {len(res)}  nokta: {pts}  "
          f"boyut: {len(json.dumps(res, ensure_ascii=False))/1024:.0f} KB")
    print("  ülke başına:", dict(per))


if __name__ == "__main__":
    main()
