#!/usr/bin/env python3
"""Şablon + veri + gömülü fontlar -> tek dosyalık sayfa."""
import base64, json, pathlib
import pathlib
# Kaynaklar src/ altında, üretilen ara dosyalar ve çıktılar depo kökünde.
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,"
         "U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")
LATIN_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,"
             "U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,"
             "U+2113,U+2C60-2C7F,U+A720-A7FF")

FACES = [
    ("Newsreader", 400, "newsreader"),
    ("Newsreader", 600, "newsreader"),
    ("Plex Sans", 400, "ibm-plex-sans"),
    ("Plex Sans", 500, "ibm-plex-sans"),
    ("Plex Sans", 600, "ibm-plex-sans"),
    ("Plex Mono", 400, "ibm-plex-mono"),
]

css = []
for family, weight, stem in FACES:
    for sub, rng in (("latin", LATIN), ("latin-ext", LATIN_EXT)):
        f = ROOT / "fonts" / f"{stem}-{sub}-{weight}-normal.woff2"
        b64 = base64.b64encode(f.read_bytes()).decode()
        css.append(f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weight};'
                   f'font-display:swap;src:url(data:font/woff2;base64,{b64}) format("woff2");'
                   f'unicode-range:{rng};}}')

data = json.load(open(ROOT / "data.json"))
tmpl = (HERE / "page.tmpl.html").read_text()
# Sürüm numarası sayfaya giriyor: tanıtım balonu her yeni sürümde bir kez
# çıksın diye "görüldü" işareti sürümle birlikte saklanıyor.
version = (ROOT / "VERSION").read_text().strip()
html = tmpl.replace("__FONTS__", "\n".join(css)) \
           .replace("__VERSION__", version) \
           .replace("__DATA__", json.dumps(data, separators=(",", ":"), ensure_ascii=False))

# Tam bir HTML belgesi kur. Eskiden ham şablon çıktısı (doctype'sız,
# charset'siz) ayrıca yazılıyor ve docs/index.html'e o kopyalanıyordu; charset
# göndermeyen bir sunucudan servis edilince Türkçe karakterler bozulup sayfa
# çöküyordu, telefon tarayıcısında da viewport meta'sı olmadığı için
# ölçeklenmiyordu. Artık üç çıktı da aynı tam belge.
title = "Dünya Dilleri Atlası"
body = html.replace(f"<title>{title}</title>\n", "", 1)
standalone = (
    '<!doctype html><html lang="tr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    f"<title>{title}</title>"
    '<meta name="description" content="234 ülke ve bölgede çoğunluğun konuştuğu dil.">'
    '<meta name="color-scheme" content="light dark">'
    '<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}</style>'
    f"</head><body>{body}</body></html>")
out = ROOT / "dunya-dilleri.html"
out.write_text(standalone)
(ROOT / "preview.html").write_text(standalone)
(ROOT / "desktop" / "app.html").write_text(standalone)
print(f"{out.name}: {len(html)/1024:.0f} KB (font {sum(len(c) for c in css)/1024:.0f} KB)")
