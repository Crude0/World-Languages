#!/usr/bin/env python3
"""Uygulama ikonu: haritanın Avrupa–Afrika kesitinden .icns ve .ico üretir."""
import json, math, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).parent
SC = HERE.parent

data = json.load(open(SC / "data.json"))
C, LG = data["countries"], data["langs"]

COL = {"rom": "#a83d09", "ger": "#3ab1f8", "ine": "#6a55c8", "afa": "#a2bb45",
       "nkg": "#12a077", "aus": "#e37ab3", "oth": "#8d949e"}
OCEAN = "#141821"
EDGE = "#0e1116"

# --- kırpma penceresi: lon -22..58, lat -36..60 (Avrupa + Afrika + Arabistan)
W, H = data["w"], data["h"]
LAT_MAX = 84.0


def project(lon, lat):
    lam, phi = math.radians(lon), math.radians(lat)
    p2 = phi * phi
    p4 = p2 * p2
    x = lam * (0.8707 - 0.131979 * p2 - 0.013791 * p4
               + 0.003971 * p4 * p4 * p2 - 0.001529 * p4 * p4 * p4)
    y = phi * (1.007226 + 0.015085 * p2 - 0.044475 * p2 * p4
               + 0.028874 * p4 * p4 - 0.005916 * p4 * p4 * p2)
    return x, y


x0, _ = project(-180, 0)
x1, _ = project(180, 0)
_, ytop = project(0, LAT_MAX)
scale = W / (x1 - x0)


def to_svg(lon, lat):
    x, y = project(lon, lat)
    return (x - x0) * scale, (ytop - y) * scale


ax, ay = to_svg(-22, 60)
bx, by = to_svg(58, -36)
cx, cy = (ax + bx) / 2, (ay + by) / 2
side = max(bx - ax, by - ay)
vb = f"{cx - side / 2:.1f} {cy - side / 2:.1f} {side:.1f} {side:.1f}"

paths = "".join(
    f'<path d="{c["d"]}" fill="{COL[LG[c["l"]]["g"]]}"/>' for c in C.values())

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="1024" height="1024">'
       f'<rect x="{cx - side:.1f}" y="{cy - side:.1f}" width="{side * 2:.1f}" height="{side * 2:.1f}" fill="{OCEAN}"/>'
       f'<g stroke="{EDGE}" stroke-width="{side / 900:.3f}">{paths}</g></svg>')

# --- iki varyant: tam kare (Windows) ve iç boşluklu squircle (macOS)
tpl = """<!doctype html><meta charset="utf-8"><style>
html,body{{margin:0;background:transparent}}
.stage{{width:1024px;height:1024px;display:grid;place-items:center}}
.art{{width:{size}px;height:{size}px;border-radius:{radius}px;overflow:hidden;
  box-shadow:inset 0 0 0 {ring}px rgba(255,255,255,.10)}}
.art svg{{width:100%;height:100%;display:block}}
</style><div class="stage"><div class="art">{svg}</div></div>"""

(HERE / "icon_mac.html").write_text(tpl.format(size=824, radius=185, ring=3, svg=svg))
(HERE / "icon_win.html").write_text(tpl.format(size=1000, radius=110, ring=3, svg=svg))

shot = HERE / "shoticon.mjs"
shot.write_text("""
import { chromium } from "playwright";
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
for (const name of ["mac", "win"]) {
  const p = await b.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: 1 });
  await p.goto("file://" + process.cwd() + "/icon_" + name + ".html");
  await p.waitForTimeout(300);
  await p.screenshot({ path: "icon_" + name + ".png", omitBackground: true });
  await p.close();
}
await b.close();
""")
subprocess.run(["node", "shoticon.mjs"], cwd=HERE, check=True)

from PIL import Image

mac = Image.open(HERE / "icon_mac.png").convert("RGBA")
win = Image.open(HERE / "icon_win.png").convert("RGBA")

# --- .icns (PNG taşıyan modern tipler)
ICNS = [("ic11", 32), ("ic12", 64), ("ic07", 128), ("ic13", 256),
        ("ic08", 256), ("ic14", 512), ("ic09", 512), ("ic10", 1024)]
chunks = b""
for typ, px in ICNS:
    buf = HERE / f"_tmp{px}.png"
    mac.resize((px, px), Image.LANCZOS).save(buf, "PNG")
    raw = buf.read_bytes()
    buf.unlink()
    chunks += typ.encode("ascii") + len(raw).to_bytes(4, "big") + raw
icns = b"icns" + (len(chunks) + 8).to_bytes(4, "big") + chunks
(HERE / "AppIcon.icns").write_bytes(icns)

# --- .ico
win.save(HERE / "AppIcon.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

print(f"icns {len(icns)/1024:.0f} KB · ico {(HERE / 'AppIcon.ico').stat().st_size/1024:.0f} KB · viewBox {vb}")
