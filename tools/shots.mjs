/* README görselleri — tek komutla yeniden üretilir.
 *
 * Ekran görüntüleri bugüne dek elle alınmıştı ve sürüm sürüm bayatladı:
 * 0.22 yayımlandığında README hâlâ 0.16'nın arayüzünü gösteriyordu. Artık
 * her kare buradan çıkıyor; durum da elle tıklanarak değil, sayfanın kendi
 * bağlantı biçimiyle (`#k=off&f=l.fr…`) kuruluyor, yani kareler kararlı.
 *
 *   PW_CHROME=/yol/chrome node tools/shots.mjs [ad ...]
 *
 * Ad verilirse yalnız o kareler alınır.
 */
import { chromium } from "playwright";
import { mkdirSync, readFileSync } from "fs";
import { fileURLToPath } from "url";
import path from "path";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
// Balonun "görüldü" damgası sürüm dizgesinin kendisi; başka bir değer
// yazmak onu görülmemiş sayar ve balon bütün karelere karışır.
const VER = readFileSync(ROOT + "/VERSION", "utf8").trim();
const OUT = ROOT + "/docs/img/";
mkdirSync(OUT, { recursive: true });

const DESK = "file://" + ROOT + "/docs/index.html";
const MOB = "file://" + ROOT + "/docs/mobile.html";

async function yakınlaş(p) {
  const b = await p.$("#dSub");
  if (b) { await b.click(); await p.waitForTimeout(900); }
}

// Masaüstü kareleri. hash: sayfanın kendi durum biçimi. after: ek adımlar.
const DESKTOP = [
  { ad: "desktop-world", tema: "dark", hash: "l=en",
    not: "dünya görünümü, dil ailesi renkleri" },
  { ad: "desktop-diaspora", tema: "light", hash: "l=en&f=l.tr",
    not: "Türkçe · konuşulduğu 26 ülke" },
  { ad: "desktop-density", tema: "light", hash: "l=en&f=l.es&p=pct",
    not: "İspanyolca · yoğunluk şeridi" },
  { ad: "desktop-scripts", tema: "dark", hash: "l=en&k=scr",
    not: "yazı sistemi katmanı" },
  { ad: "desktop-official", tema: "light", hash: "l=en&k=off",
    not: "resmî dil katmanı" },
  // Bağlantı ülkeyi seçiyor ama görüş kutusunu oynatmıyor; yakınlaştırmayı
  // kartın kendi "bölgelere ayır" düğmesi yapıyor.
  { ad: "desktop-regions", tema: "light", hash: "l=en&d=on&s=724",
    after: yakınlaş, not: "il düzeyi · İspanya" },
  // Rusya'ya "odaklanmak" neredeyse dünya görünümü demek (11 saat dilimi);
  // cumhuriyetlerin görüldüğü yer batı ve Ural, o yüzden çerçeve elle.
  { ad: "desktop-russia", tema: "light", hash: "l=en&d=on&s=643&v=760,10,400",
    not: "Rusya'nın federal özneleri" },
  { ad: "desktop-know", tema: "dark", hash: "l=en&k=know&kn=tr.en",
    not: "bildiğin dillerle dünya" },
  // 0.21–0.22'nin yeni yüzleri
  { ad: "desktop-card", tema: "dark", hash: "l=en&f=l.fr",
    not: "dil kartı (0.22)" },
  { ad: "desktop-questions", tema: "light", hash: "l=en", balon: true,
    kırp: "üst", not: "iki soru ve ilk ziyaret balonu (0.21–0.22)" },
  { ad: "desktop-tour", tema: "dark", hash: "l=en",
    after: async (p) => {
      await p.click("#btnTour");
      await p.waitForTimeout(700);
      await p.click("#tourNext");
      await p.waitForTimeout(900);
    }, not: "tanıtım · karartma ve delik" },
  { ad: "desktop-fullscreen", tema: "dark", hash: "l=en&f=l.ar",
    after: async (p) => {
      // Gerçek tam ekran API'si başsız tarayıcıda pencereyi büyütmüyor;
      // sayfanın yedek kaplaması aynı düzeni veriyor.
      await p.evaluate(() => document.querySelector("#btnFull").click());
      await p.waitForTimeout(900);
    }, not: "tam ekran · alttaki gösterge bandı (0.20)" },
];

const MOBILE = [
  { ad: "mobile-home", tema: "dark", hash: "l=en", not: "harita" },
  { ad: "mobile-detail", tema: "light", hash: "l=en&s=076", not: "ülke kartı" },
  { ad: "mobile-know", tema: "dark", hash: "l=en&k=know&kn=tr.en", not: "bildiğim diller" },
  { ad: "mobile-settings", tema: "light", hash: "l=en",
    after: async (p) => { await p.click('[data-tab="settings"]'); await p.waitForTimeout(400); },
    not: "ayarlar" },
];

const seç = process.argv.slice(2);
const istendi = (ad) => !seç.length || seç.includes(ad);

const b = await chromium.launch({ executablePath: process.env.PW_CHROME });
const errs = [];

async function çek(liste, url, viewport, dsf) {
  for (const s of liste) {
    if (!istendi(s.ad)) continue;
    const ctx = await b.newContext({ viewport, deviceScaleFactor: dsf });
    await ctx.addInitScript(([tema, balon, ver]) => {
      localStorage.setItem("wl-theme", tema);
      // Balon her yeni sürümde bir kez çıkıyor; onu isteyen kare dışında
      // görülmüş sayılıyor ki kareler arasında ortalıkta durmasın.
      if (!balon) localStorage.setItem("wl-seen-ask", ver);
    }, [s.tema, !!s.balon, VER]);
    const p = await ctx.newPage();
    p.on("pageerror", (e) => errs.push(`${s.ad}: ${e.message}`));
    p.on("console", (m) => { if (m.type() === "error") errs.push(`${s.ad}: ${m.text()}`); });
    await p.goto(url + "#" + s.hash);
    await p.waitForTimeout(1400);
    if (s.after) await s.after(p);
    // Kart içindeki düğmeye tıklamak sayfayı kaydırıyor; kare hep tepeden.
    await p.evaluate(() => window.scrollTo(0, 0));
    await p.waitForTimeout(400);
    const opt = { path: OUT + s.ad + ".png" };
    if (s.kırp === "üst") {
      // Manşetin kendi ölçüsünden kırpılıyor: sabit bir dikdörtgen dil ya da
      // yazı tipi değişince yanlış yeri kesiyordu.
      opt.clip = await p.evaluate(() => {
        const r = [...document.querySelectorAll("h1, #ask, #askTip")]
          .map((n) => n.getBoundingClientRect());
        const x0 = Math.min(...r.map((b) => b.left)) - 26;
        const y0 = Math.min(...r.map((b) => b.top)) - 26;
        return { x: Math.max(0, x0), y: Math.max(0, y0),
                 width: Math.max(...r.map((b) => b.right)) - x0 + 26,
                 height: Math.max(...r.map((b) => b.bottom)) - y0 + 26 };
      });
    }
    await p.screenshot(opt);
    console.log(`  ${s.ad}.png · ${s.not}`);
    await ctx.close();
  }
}

await çek(DESKTOP, DESK, { width: 1600, height: 1000 }, 2);
await çek(MOBILE, MOB, { width: 390, height: 844 }, 3);

await b.close();

// Kareler 24 bit çıkıyor ama içlerinde birkaç yüz renk var; paletlemek
// depoyu dörtte birine indiriyor ve gözle fark edilmiyor.
const { execFileSync } = await import("child_process");
const çekilen = [...DESKTOP, ...MOBILE].filter((s) => istendi(s.ad))
  .map((s) => OUT + s.ad + ".png");
execFileSync("python3", [ROOT + "/tools/shrink_png.py", ...çekilen], { stdio: "inherit" });

console.log(errs.length ? "\nHATA:\n" + [...new Set(errs)].join("\n") : "\ntemiz: hata yok");
