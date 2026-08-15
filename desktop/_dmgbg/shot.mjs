
import { chromium } from "playwright";
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
for (const s of [1, 2]) {
  const p = await b.newPage({ viewport: { width: 660 * s, height: 440 * s },
                              deviceScaleFactor: 1 });
  await p.goto("file://" + process.cwd() + "/bg" + s + ".html");
  await p.waitForTimeout(400);
  await p.screenshot({ path: "bg" + s + ".png" });
  await p.close();
}
await b.close();
