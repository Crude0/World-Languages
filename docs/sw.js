// Dünya Dilleri Atlası — çevrimdışı önbellek.
// Sayfalar tek dosya (veri, fontlar, betik hepsi içinde), o yüzden liste kısa.
const CACHE = "wl-0.6.1";
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

// Önce önbellek: sayfa değişmiyorsa anında açılsın. Ağ kopyası arka planda
// tazeleniyor, yeni sürüm bir sonraki açılışta görünüyor.
self.addEventListener("fetch", (e) => {
  const r = e.request;
  if (r.method !== "GET" || new URL(r.url).origin !== location.origin) return;
  e.respondWith(caches.match(r).then((hit) => {
    const net = fetch(r).then((res) => {
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(r, copy));
      }
      return res;
    }).catch(() => hit);
    return hit || net;
  }));
});
