import { chromium } from "playwright";
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
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
// yatay taşma kontrolü (dar ekran)
await p.setViewportSize({ width: 360, height: 800 });
await p.waitForTimeout(400);
console.log("360px yatay taşma:", await p.evaluate(() => document.documentElement.scrollWidth > 360));
await p.setViewportSize({ width: 1600, height: 1050 });
await p.waitForTimeout(300);
await p.screenshot({ path: "shot-final.png" });
console.log(errs.length ? errs.join("\n") : "temiz: hata yok");
await b.close();
