#!/usr/bin/env python3
"""README görsellerini paletli PNG'ye indirir.

Arayüz ekran görüntüleri düz renkli: harita dolguları, panel zeminleri, yazı.
Gerçek renk sayısı birkaç yüzü geçmiyor ama PNG onları 24 bit olarak
saklıyor — 14 kare 14 MB tutuyordu. 256 renklik uyarlanmış palet aynı
kareleri gözle ayırt edilemeyecek biçimde dörtte birine indiriyor; depoya
her sürümde yeni bir kare kümesi giren bir projede bu fark birikiyor.

Kayıp riski gradyanlarda; şeritlenmeyi Floyd-Steinberg dağıtması karşılıyor.
"""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent.parent
IMG = HERE / "docs" / "img"


def main() -> int:
    hedef = sys.argv[1:] or sorted(str(p) for p in IMG.glob("*.png"))
    önce = sonra = 0
    for yol in hedef:
        p = pathlib.Path(yol)
        if not p.exists():
            print(f"  yok: {p}")
            continue
        a = p.stat().st_size
        im = Image.open(p).convert("RGB")
        q = im.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG)
        q.save(p, optimize=True)
        b = p.stat().st_size
        önce, sonra = önce + a, sonra + b
        print(f"  {p.name:28} {a / 1024:7.0f} KB → {b / 1024:6.0f} KB")
    if önce:
        print(f"  toplam {önce / 1024 / 1024:.1f} MB → {sonra / 1024 / 1024:.1f} MB "
              f"(%{100 - sonra * 100 // önce} küçüldü)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
