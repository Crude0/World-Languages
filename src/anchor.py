"""Etiket çapası: bir çokgenin erişilmezlik kutbu (pole of inaccessibility).

Köşe ortalaması içbükey şekillerde çokgenin dışına düşer — Norveç'in adı denize,
Hırvatistan'ınki Bosna'nın üstüne gelir. Erişilmezlik kutbu ise kenarlara en uzak
*iç* nokta: tanımı gereği şeklin içinde ve etiketin en rahat sığdığı yer.

Mapbox'ın polylabel algoritması: kareleri öncelik kuyruğunda böl, bir karenin
üst sınırı (merkez uzaklığı + yarı köşegen) o ana kadarki en iyiden küçükse
dalı buda.
"""
import heapq
from math import sqrt

SQ2 = sqrt(2)


def _seg_dist2(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    if dx or dy:
        t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
        if t > 1:
            ax, ay = bx, by
        elif t > 0:
            ax, ay = ax + dx * t, ay + dy * t
    dx, dy = px - ax, py - ay
    return dx * dx + dy * dy


def _point_to_poly(px, py, rings):
    """İşaretli uzaklık: içeride pozitif, dışarıda negatif."""
    inside = False
    best = float("inf")
    for ring in rings:
        n = len(ring)
        j = n - 1
        for i in range(n):
            ax, ay = ring[i]
            bx, by = ring[j]
            if (ay > py) != (by > py) and px < (bx - ax) * (py - ay) / (by - ay + 1e-18) + ax:
                inside = not inside
            d = _seg_dist2(px, py, ax, ay, bx, by)
            if d < best:
                best = d
            j = i
    d = sqrt(best)
    return d if inside else -d


def pole_of_inaccessibility(rings, precision=None):
    """rings: [dış halka, delik, ...] — her biri [(x, y), ...]. (x, y, uzaklık) döner."""
    outer = rings[0]
    xs = [p[0] for p in outer]
    ys = [p[1] for p in outer]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    w, h = maxx - minx, maxy - miny
    cell = min(w, h)
    if cell == 0:
        return (minx, miny, 0.0)
    if precision is None:
        precision = max(cell / 400.0, 1e-3)

    half = cell / 2.0
    # (-öncelik, sayaç, x, y, h, d) — heapq en küçüğü verir, biz en büyüğü istiyoruz
    q = []
    tick = [0]

    def push(x, y, hh):
        d = _point_to_poly(x, y, rings)
        tick[0] += 1
        heapq.heappush(q, (-(d + hh * SQ2), tick[0], x, y, hh, d))
        return d

    y = miny + half
    while y < maxy:
        x = minx + half
        while x < maxx:
            push(x, y, half)
            x += cell
        y += cell

    # başlangıç adayı: gövde merkezi
    bx, by = minx + w / 2.0, miny + h / 2.0
    best = (bx, by, _point_to_poly(bx, by, rings))

    while q:
        top, _, x, y, hh, d = heapq.heappop(q)
        if d > best[2]:
            best = (x, y, d)
        if -top - best[2] <= precision:
            continue
        hh /= 2.0
        for sx in (-hh, hh):
            for sy in (-hh, hh):
                push(x + sx, y + sy, hh)
    return best


def label_anchor(parts):
    """parts: [(alan, noktalar, delik_mi), ...] — bir ülkenin/bölgenin tüm halkaları.

    En büyük *dolu* halkayı seçer, onun içine düşen delikleri de hesaba katıp
    erişilmezlik kutbunu döndürür.
    """
    solid = [p for p in parts if not p[2]] or parts
    area, main, _ = max(solid, key=lambda p: p[0])
    xs = [q[0] for q in main]
    ys = [q[1] for q in main]
    box = (min(xs), min(ys), max(xs), max(ys))

    def in_box(pts):
        return all(box[0] <= q[0] <= box[2] and box[1] <= q[1] <= box[3] for q in pts)

    rings = [main] + [p[1] for p in parts if p[2] and in_box(p[1])]
    x, y, _ = pole_of_inaccessibility(rings)
    return round(x, 1), round(y, 1)
