#!/usr/bin/env python3
"""README'nin üstündeki bağlantı satırını düğmeye çevirir.

GitHub biçem sayfası kabul etmiyor, ama `<picture>` ile temaya göre resim
seçiyor ve depodaki SVG'leri gösteriyor. Yani düğme görüntüsünü kendimiz
üretmek zorundayız; shields.io gibi bir dış servise bağlanmıyoruz, çünkü
proje zaten "ağa çıkmayan tek dosya" iddiasında.

Yazı tipi sorunu: SVG içindeki metin görüntüleyenin yazı tipiyle çiziliyor
ve genişliği makineden makineye değişiyor — kapsül dar kalırsa yazı taşar.
Bu yüzden her etiket `textLength` ile sabit genişliğe kilitleniyor
(`lengthAdjust="spacingAndGlyphs"`), yani hangi yazı tipi bulunursa bulunsun
düğmenin boyu değişmiyor.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "docs" / "img"

H = 46          # düğme yüksekliği
PAD = 20        # yatay iç boşluk
GAP = 9         # simge ile yazı arası
ICON = 16       # simge kutusu
FS = 15         # punto
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

# Ölçü, gerçek yazı tipinden bağımsız olsun diye harf başına sabit bir
# oranla hesaplanıyor; metin sonra tam o genişliğe oturtuluyor.
def text_width(s: str) -> float:
    wide, thin = "MWmw@", "iljtIf.,'!| "
    w = 0.0
    for ch in s:
        w += 0.72 if ch in wide else 0.30 if ch in thin else 0.525
    return w * FS


ICONS = {
    # oynat üçgeni
    "play": "M3 1.7 13.2 8 3 14.3Z",
    # telefon
    "phone": "M4.4 0h7.2A1.9 1.9 0 0 1 13.5 1.9v12.2A1.9 1.9 0 0 1 11.6 16H4.4a1.9 1.9 0 0 1-1.9-1.9V1.9A1.9 1.9 0 0 1 4.4 0Zm0 1.5a.4.4 0 0 0-.4.4v12.2c0 .2.2.4.4.4h7.2c.2 0 .4-.2.4-.4V1.9a.4.4 0 0 0-.4-.4Zm2.1 11h3v1.1h-3Z",
    # indirme oku
    "down": "M7.2 0h1.6v8.6l3-3 1.1 1.1L8 12 3.1 6.7l1.1-1.1 3 3ZM2 13.4h12V15H2Z",
}

TEMA = {
    # (dolgu, yazı/simge, çerçeve)
    ("light", True):  ("#17181c", "#fbfbfa", None),
    ("light", False): (None,      "#1f2126", "#d3d3cc"),
    ("dark",  True):  ("#e9eaee", "#16181d", None),
    ("dark",  False): (None,      "#c9ced8", "#3a4048"),
}


def button(label: str, icon: str, primary: bool, theme: str) -> str:
    fill, fg, stroke = TEMA[(theme, primary)]
    tw = text_width(label)
    w = round(PAD + ICON + GAP + tw + PAD)
    r = H / 2
    ix, iy = PAD, (H - ICON) / 2
    tx = PAD + ICON + GAP
    body = (f'<rect x=".9" y=".9" width="{w - 1.8}" height="{H - 1.8}" rx="{r - .9}" '
            + (f'fill="{fill}"' if fill else 'fill="none"')
            + (f' stroke="{stroke}" stroke-width="1.5"' if stroke else "")
            + "/>")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{H}" '
        f'viewBox="0 0 {w} {H}" role="img" aria-label="{label}">'
        f"{body}"
        f'<g transform="translate({ix} {iy})" fill="{fg}">'
        f'<path d="{ICONS[icon]}"/></g>'
        f'<text x="{tx}" y="{H / 2}" dominant-baseline="central" '
        f'textLength="{tw:.1f}" lengthAdjust="spacingAndGlyphs" '
        f'font-family="{FONT}" font-size="{FS}" font-weight="600" '
        f'fill="{fg}">{label}</text></svg>'
    )


# ad -> (etiket, simge, birincil mi)
BUTTONS = {
    "open-en":  ("Open in your browser", "play",  True),
    "phone-en": ("Phone version",        "phone", False),
    "dl-en":    ("Downloads",            "down",  False),
    "open-tr":  ("Tarayıcıda aç",        "play",  True),
    "phone-tr": ("Telefon sürümü",       "phone", False),
    "dl-tr":    ("İndirmeler",           "down",  False),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (label, icon, primary) in BUTTONS.items():
        for theme in ("light", "dark"):
            p = OUT / f"btn-{name}-{theme}.svg"
            p.write_text(button(label, icon, primary, theme), encoding="utf-8")
            print(f"  {p.relative_to(HERE)}")


if __name__ == "__main__":
    main()
