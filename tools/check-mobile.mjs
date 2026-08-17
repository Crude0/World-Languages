import { chromium } from "playwright";
// PW_CHROME verilirse o tarayıcı kullanılır (CI ya da sistem Chromium'u),
// yoksa Playwright kendi indirdiği sürümü açar.
const b = await chromium.launch(process.env.PW_CHROME ? { executablePath: process.env.PW_CHROME } : {});
const ctx = await b.newContext({ viewport: { width: 393, height: 852 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
const p = await ctx.newPage();
const errs = [];
p.on("pageerror", (e) => errs.push(String(e)));
p.on("console", (m) => m.type() === "error" && errs.push(m.text()));
await p.goto("file://" + process.cwd() + "/../mobile-preview.html");
await p.waitForTimeout(600);
const cdp = await ctx.newCDPSession(p);
const touch = (t, pts) => cdp.send("Input.dispatchTouchEvent", { type: t, touchPoints: pts });
const vb = () => p.$eval("#map", (e) => e.getAttribute("viewBox").split(" ").map(Number));

console.log("açılış viewBox:", (await vb()).map(Math.round));
// sonuna kadar uzaklaştırmayı dene: boşluk kalmamalı (h <= 612.8)
for (let i = 0; i < 6; i++) { await p.click("#btnOut"); await p.waitForTimeout(120); }
const v = await vb();
console.log("en uzak:", v.map(Math.round), "· dikey boşluk var mı:", v[3] > 612.9);

// alt sekme çubuğu: dört varış noktası, hepsi tek dokunuşla
for (const [tab, ad] of [["map", "harita"], ["langs", "diller"], ["know", "bildiğim"], ["settings", "ayarlar"]]) {
  await p.tap(`#tabs [data-tab="${tab}"]`); await p.waitForTimeout(450);
  // En alçak duraklarda panelin gövdesi çubuğun *arkasından* aşağı kayıyor;
  // önemli olan çubuğun her durumda görünür ve dokunulabilir kalması.
  const r = await p.evaluate(() => {
    const t = document.querySelector("#tabs [aria-selected=true]");
    const hit = [...document.querySelectorAll("#tabs [data-tab]")].every((b) => {
      const q = b.getBoundingClientRect();
      const el = document.elementFromPoint(q.x + q.width / 2, q.y + q.height / 2);
      return !!(el && el.closest("#tabs [data-tab]") === b);
    });
    return { sekme: t && t.dataset.tab, hit,
             gövde: document.querySelector("#body").scrollHeight };
  });
  console.log(`  ${ad.padEnd(9)} seçili=${r.sekme} · gövde=${r.gövde}px · çubuk ${
    r.hit ? "dokunulabilir" : "ERİŞİLEMİYOR"}`);
}
await p.screenshot({ path: "m5-tabs.png" });

// Paylaş simgesi her sekmede erişilebilir mi ve dışa aktarma o an ekranda ne
// varsa onu mu çekiyor: Ayarlar'a geçmek katmanı bozuyordu.
for (const tab of ["know", "langs", "settings"]) {
  await p.tap(`#tabs [data-tab="${tab}"]`); await p.waitForTimeout(400);
  const r = await p.evaluate(() => {
    const q = document.querySelector("#btnShare").getBoundingClientRect();
    const el = document.elementFromPoint(q.x + q.width / 2, q.y + q.height / 2);
    return { hit: !!(el && el.closest("#btnShare")),
             boyalı: [...document.querySelectorAll("#map .cty")].filter((n) => n.style.fill).length };
  });
  console.log(`  ${tab.padEnd(9)} paylaş ${r.hit ? "dokunulabilir" : "ERİŞİLEMİYOR"} · boyalı ülke ${r.boyalı}`);
}

// Ayarlar sekmesinden yoğunluk boyaması. Önce Harita sekmesine dönülüyor:
// katman artık Ayarlar'a geçerken sıfırlanmıyor (geçerken sıfırlanması dışa
// aktarmanın yanlış haritayı çekmesine yol açıyordu) ve yoğunluk yalnız ana
// dil katmanında geçerli.
await p.tap('#tabs [data-tab="map"]'); await p.waitForTimeout(400);
await p.tap('#tabs [data-tab="settings"]'); await p.waitForTimeout(400);
await p.tap('#body [data-paint="pct"]'); await p.waitForTimeout(400);
console.log("yoğunluk modunda ilk ülke dolgusu:", await p.$eval('#map [data-id="792"]', (e) => e.style.fill));

// paneli içerikten aşağı çekerek kapat
await p.tap('#tabs [data-tab="langs"]'); await p.waitForTimeout(450);
const before = await p.$eval("#sheet", (e) => Math.round(e.getBoundingClientRect().top));
const bb = await p.$eval("#body", (e) => { const r = e.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + 60 }; });
await touch("touchStart", [{ x: bb.x, y: bb.y, id: 1 }]);
for (let i = 1; i <= 8; i++) { await touch("touchMove", [{ x: bb.x, y: bb.y + i * 40, id: 1 }]); await p.waitForTimeout(25); }
await touch("touchEnd", []);
await p.waitForTimeout(500);
const after = await p.$eval("#sheet", (e) => Math.round(e.getBoundingClientRect().top));
console.log("panel üstü:", before, "->", after, "· içerikten kapandı mı:", after > before + 100);
console.log("hata:", errs.length ? errs : "yok");
await b.close();
