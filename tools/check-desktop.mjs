import { chromium } from "playwright";
// PW_CHROME verilirse o tarayıcı kullanılır (CI ya da sistem Chromium'u),
// yoksa Playwright kendi indirdiği sürümü açar.
const b = await chromium.launch(process.env.PW_CHROME ? { executablePath: process.env.PW_CHROME } : {});
const errs = [];
const ctx = await b.newContext({ viewport: { width: 1600, height: 1050 }, deviceScaleFactor: 2 });
const p = await ctx.newPage();
p.on("pageerror", (e) => errs.push("PAGEERROR " + e.message));
p.on("console", (m) => { if (m.type() === "error") errs.push("CONSOLE " + m.text()); });
await p.goto("file://" + process.cwd() + "/../preview.html");
await p.waitForTimeout(700);
const stats = await p.evaluate(() => ({
  paths: document.querySelectorAll("#map .cty").length,
  dots: document.querySelectorAll("#map .dot").length,
  langRows: document.querySelectorAll("#idxList [data-l]").length,
  title: document.title,
  lang: document.documentElement.lang,
  bodyScrollX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  fonts: [...document.fonts].filter(f => f.status === "loaded").map(f => f.family + " " + f.weight).slice(0, 3),
}));
console.log(stats);

// Biçem sayfası bütün mü? Bir kuralda fazladan açılan tek bir süslü parantez,
// ondan sonraki bütün kuralları sessizce yutuyor: harita bembeyaz değil,
// bomboş siyah çıkıyordu ve ne konsolda hata vardı ne de sayfa çöküyordu.
// Ölçüt kural sayısı değil, işe yarayan bir sonuç: bilinen bir ülke bilinen
// ailenin rengini almalı, ve tam ekran bandı kendi yerinde olmalı.
const css = await p.evaluate(() => {
  const br = document.querySelector('#map [data-id="076"]');   // Brezilya · Roman
  const key = document.querySelector(".key-row");
  const sheet = [...document.styleSheets].find((s) => {
    try { return s.cssRules.length > 50; } catch (e) { return false; }
  });
  return {
    kural: sheet ? sheet.cssRules.length : 0,
    brezilya: br ? getComputedStyle(br).fill : "yok",
    gösterge: key ? getComputedStyle(key).display : "yok",
  };
});
const kara = /^rgb\(0, ?0, ?0\)$/.test(css.brezilya);
console.log(`biçem: ${css.kural} kural · Brezilya ${css.brezilya}${kara ? "  ← KURALLAR DÜŞMÜŞ" : ""}`);
if (kara || css.kural < 200) errs.push("CSS " + JSON.stringify(css));

// yatay taşma kontrolü (dar ekran)
await p.setViewportSize({ width: 360, height: 800 });
await p.waitForTimeout(400);
console.log("360px yatay taşma:", await p.evaluate(() => document.documentElement.scrollWidth > 360));
await p.setViewportSize({ width: 1600, height: 1050 });
await p.waitForTimeout(300);
await p.screenshot({ path: "shot-final.png" });
console.log(errs.length ? errs.join("\n") : "temiz: hata yok");
await b.close();
