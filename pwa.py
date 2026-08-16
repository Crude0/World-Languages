#!/usr/bin/env python3
"""docs/ kopyalarını kurulabilir ve çevrimdışı hâle getirir.

Yalnızca `docs/` içindeki iki dosyaya dokunur. Paketlenen sürümler
(dunya-dilleri.html, desktop/app.html, android varlıkları) olduğu gibi kalır:
onlar zaten çevrimdışı, manifest ve hizmet çalışanı orada anlamsız — dahası
file:// üzerinden manifest 404 verir, kayıt da sessizce başarısız olur.

İkonlar depoda duruyor (docs/icon-*.png). Üretimleri tarayıcı gerektirdiği için
her derlemede yeniden yapılmıyor; palet değişirse elle yenilenmeleri gerekir.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).parent
DOCS = HERE / "docs"
VERSION = (HERE / "VERSION").read_text().strip()

BASE_ICONS = [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
    {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png",
     "purpose": "maskable"},
]

# Masaüstü ve telefon arayüzleri ayrı dosyalar, dolayısıyla ayrı manifestler:
# yoksa telefon arayüzünden kurulan uygulama masaüstü sayfasını açardı.
MANIFESTS = {
    "manifest.webmanifest": {
        "name": "Dünya Dilleri Atlası",
        "short_name": "Dil Atlası",
        "start_url": "./index.html",
        "scope": "./",
        "display": "standalone",
        "orientation": "any",
        "background_color": "#eef0f3",
        "theme_color": "#eef0f3",
        "description": "234 ülke ve bölgede çoğunluğun konuştuğu dil.",
        "lang": "tr",
        "icons": BASE_ICONS,
    },
    "manifest-mobile.webmanifest": {
        "name": "Dünya Dilleri Atlası",
        "short_name": "Dil Atlası",
        "start_url": "./mobile.html",
        "scope": "./",
        "display": "standalone",
        "orientation": "portrait",
        "background_color": "#12151b",
        "theme_color": "#12151b",
        "description": "234 ülke ve bölgede çoğunluğun konuştuğu dil.",
        "lang": "tr",
        "icons": BASE_ICONS,
    },
}

# Sayfalar tek dosya olduğu için önbellek listesi kısa. Sürüm değişince
# önbellek adı değişiyor ve eski kopyalar siliniyor.
SW = """\
// Dünya Dilleri Atlası — çevrimdışı önbellek.
// Sayfalar tek dosya (veri, fontlar, betik hepsi içinde), o yüzden liste kısa.
const CACHE = "wl-%(version)s";
const FILES = [
  "./", "./index.html", "./mobile.html",
  "./manifest.webmanifest", "./manifest-mobile.webmanifest",
  "./icon-192.png", "./icon-512.png", "./icon-maskable-512.png",
];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys()
    .then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});

const put = (r, res) => {
  if (res && res.ok) {
    const copy = res.clone();
    caches.open(CACHE).then((c) => c.put(r, copy));
  }
  return res;
};

self.addEventListener("fetch", (e) => {
  const r = e.request;
  if (r.method !== "GET" || new URL(r.url).origin !== location.origin) return;

  // Sayfanın kendisi için ÖNCE AĞ. Eskiden burada da önbellek önce geliyordu
  // ve ağ kopyası arka planda tazeleniyordu; yani yayımlanan bir sürüm ancak
  // ikinci yenilemede görünüyordu. Ölçüldü: yeni sürüm 2. yenilemede geliyordu.
  // Bir sürüm çıkarıp kullanıcının eskisini görmesi, çevrimdışı açılışın bir
  // saniye gecikmesinden çok daha kötü.
  if (r.mode === "navigate") {
    e.respondWith(
      fetch(r).then((res) => put(r, res))
        .catch(() => caches.match(r).then((hit) => hit || caches.match("./index.html"))));
    return;
  }

  // İkon ve manifest gibi sürümle değişmeyen dosyalarda önbellek önce kalsın:
  // her açılışta yeniden indirmenin anlamı yok, önbellek adı zaten sürümle
  // değişiyor ve eskiler activate'te siliniyor.
  e.respondWith(caches.match(r).then((hit) =>
    hit || fetch(r).then((res) => put(r, res))));
});
"""

HEAD = """\
<link rel="manifest" href="%(manifest)s">
<link rel="icon" href="icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#eef0f3">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#101318">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\
"""

REGISTER = """\
<script>
// Hizmet çalışanı yalnızca http(s) altında anlamlı; dosyadan açılan kopyada
// kayıt zaten başarısız olur, boş yere denemiyoruz.
if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
  addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>\
"""


def patch(path: pathlib.Path, manifest: str) -> None:
    html = path.read_text(encoding="utf-8")
    if "rel=\"manifest\"" in html:
        raise SystemExit(f"{path.name}: zaten yamalı, önce yeniden derleyin")
    html = html.replace("</head>", HEAD % {"manifest": manifest} + "</head>", 1)
    html = html.replace("</body>", REGISTER + "</body>", 1)
    path.write_text(html, encoding="utf-8")


def main() -> None:
    for name, body in MANIFESTS.items():
        (DOCS / name).write_text(
            json.dumps(body, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DOCS / "sw.js").write_text(SW % {"version": VERSION}, encoding="utf-8")
    patch(DOCS / "index.html", "manifest.webmanifest")
    patch(DOCS / "mobile.html", "manifest-mobile.webmanifest")
    missing = [n["src"] for n in BASE_ICONS if not (DOCS / n["src"]).exists()]
    if missing:
        raise SystemExit("ikon eksik: " + ", ".join(missing))
    print(f"pwa: manifest + sw (wl-{VERSION}) hazır")


if __name__ == "__main__":
    main()
