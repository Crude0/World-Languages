#!/usr/bin/env python3
"""Telefon arayüzü: şablon + veri -> tek dosyalık sayfa.

Masaüstü sürümünden farkı: gömülü font yok (sistem yazı tipi kullanılır, hem
yerel görünür hem ~295 KB tasarruf) ve düzen tam ekran harita + alt panel.
"""
import json, pathlib

HERE = pathlib.Path(__file__).parent
data = json.load(open(HERE / "data.json"))
tmpl = (HERE / "mobile.tmpl.html").read_text()
body = tmpl.replace("__DATA__", json.dumps(data, separators=(",", ":"), ensure_ascii=False))

html = (
    '<!doctype html><html lang="tr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,'
    'maximum-scale=1,user-scalable=no,viewport-fit=cover">'
    "<title>Dünya Dilleri</title>"
    '<meta name="color-scheme" content="light dark">'
    '<style>*,*::before,*::after{box-sizing:border-box}</style>'
    f"</head><body>{body}</body></html>")

out = HERE / "android" / "assets" / "app.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html)
(HERE / "mobile-preview.html").write_text(html)
print(f"{out.name}: {len(html)/1024:.0f} KB")
