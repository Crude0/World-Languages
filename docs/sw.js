// Dünya Dilleri Atlası — çevrimdışı önbellek.
// Sayfalar tek dosya (veri, fontlar, betik hepsi içinde), o yüzden liste kısa.
const CACHE = "wl-0.23.1";
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
