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

// katman menüsü
await p.tap("#btnLayers"); await p.waitForTimeout(300);
console.log("menü açık:", await p.$eval("#pop", (e) => !e.hidden));
await p.screenshot({ path: "m5-pop.png" });
await p.tap('#pop [data-paint="pct"]'); await p.waitForTimeout(400);
console.log("yoğunluk modunda ilk ülke dolgusu:", await p.$eval('#map [data-id="792"]', (e) => e.style.fill));
await p.tap("#btnLayers"); await p.waitForTimeout(200);

// paneli içerikten aşağı çekerek kapat
await p.tap("#grab"); await p.waitForTimeout(500);
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
