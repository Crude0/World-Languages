#!/usr/bin/env python3
"""DMG penceresinin görünümü: arka plan resmi, ikon yerleşimi, pencere ölçüsü.

macOS'ta bir disk imajının nasıl göründüğü kök dizindeki `.DS_Store`
dosyasında yazılıdır: pencerenin ekrandaki yeri ve boyu, görünüm kipi, arka
plan resmi ve her ikonun koordinatı. Normalde bu dosyayı Finder'a yazdırırsınız
(bir Mac'te AppleScript ile); burada Mac yok, o yüzden doğrudan üretiliyor.

Arka plan resmi HTML'den Chromium'la çekiliyor ve uygulamanın kendi harita
verisini kullanıyor: parşömen üstünde ince mürekkeple çizilmiş dünya. İki
çözünürlükte üretilip tek bir TIFF'e konuyor (1x + 2x); Retina ekranda
bulanık görünmesin diye.

Gereken paketler: ds_store, mac_alias, Pillow. Yoksa DMG yine üretilir,
yalnızca penceresi süssüz olur.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent

# Pencere içeriğinin nokta (point) cinsinden ölçüsü. Arka plan resmi de tam
# bu boyutta; Finder resmi ölçeklemez, olduğu yere koyar.
W, H = 660, 440
ICON_SIZE = 128
# İkon merkezleri. Sol: uygulama, sağ: Applications kısayolu.
APP_XY = (176, 214)
DEST_XY = (484, 214)
BG_NAME = "bg.tiff"


# --------------------------------------------------------------- arka plan
def _map_paths(max_len=90000):
    """Haritanın ülke yollarını, ince mürekkep çizimi için al."""
    data = json.load(open(ROOT / "data.json"))
    out, total = [], 0
    # Büyük kara parçaları önce: yer kalmazsa kaybolan küçük adalar olsun
    for c in sorted(data["countries"].values(), key=lambda c: -(c.get("a") or 0)):
        d = c.get("d")
        if not d:
            continue
        if total + len(d) > max_len:
            break
        out.append(d)
        total += len(d)
    return data["w"], data["h"], out


def _html(scale):
    mw, mh, paths = _map_paths()
    w, h = W * scale, H * scale
    fonts = ROOT / "fonts"
    serif = (fonts / "newsreader-latin-ext-400-normal.woff2").as_uri()
    serif6 = (fonts / "newsreader-latin-ext-600-normal.woff2").as_uri()
    ink = "#3c2f21"
    # Harita pencerenin ortasına, iki hedef karesinin arkasından geçecek
    # şekilde yerleşiyor; mürekkep soluk, çünkü asıl iş ikonlarda.
    map_svg = (
        f'<svg viewBox="0 0 {mw} {mh}" preserveAspectRatio="xMidYMid meet">'
        f'<g fill="none" stroke="{ink}" stroke-width="0.9" stroke-linejoin="round">'
        + "".join(f'<path d="{d}"/>' for d in paths)
        + "</g></svg>"
    )
    # Kâğıt dokusu: düzenli noktalar yerine gerçek gürültü. feTurbulence
    # Chromium'da destekleniyor ve elyaflı bir parşömen dokusu veriyor.
    grain_svg = (
        '<svg xmlns="http://www.w3.org/2000/svg">'
        '<filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.9"'
        ' numOctaves="4" stitchTiles="stitch"/>'
        '<feColorMatrix type="saturate" values="0"/></filter>'
        '<rect width="100%" height="100%" filter="url(#g)"/></svg>'
    )
    import base64 as _b64
    grain_uri = "data:image/svg+xml;base64," + _b64.b64encode(grain_svg.encode()).decode()
    # Pusula gülü: köşede, ince mürekkep
    rose = "".join(
        f'<line x1="50" y1="50" x2="{50 + 34 * __import__("math").cos(a)}"'
        f' y2="{50 + 34 * __import__("math").sin(a)}"/>'
        for a in [i * 3.14159265 / 4 for i in range(8)])
    compass = (
        f'<svg viewBox="0 0 100 100" fill="none" stroke="{ink}" stroke-opacity=".5">'
        f'<circle cx="50" cy="50" r="36" stroke-width="1.2"/>'
        f'<circle cx="50" cy="50" r="29" stroke-width=".7"/>'
        f'<g stroke-width=".7">{rose}</g>'
        f'<path d="M50 8 L57 50 L50 92 L43 50 Z" stroke-width="1.1"/>'
        f'<path d="M8 50 L50 43 L92 50 L50 57 Z" stroke-width="1.1"/>'
        f'<path d="M50 8 L57 50 L50 50 Z" fill="{ink}" fill-opacity=".45" stroke="none"/>'
        f'</svg>'
    )
    return f"""<!doctype html><meta charset="utf-8"><style>
@font-face {{ font-family: Old; src: url("{serif}"); font-weight: 400; }}
@font-face {{ font-family: Old; src: url("{serif6}"); font-weight: 600; }}
* {{ margin: 0; box-sizing: border-box; }}
html, body {{ width: {w}px; height: {h}px; }}
body {{
  position: relative; overflow: hidden;
  font-family: Old, Georgia, serif; color: {ink};
  /* Parşömen: sıcak taban + köşelere doğru koyulaşan lekeler */
  background:
    radial-gradient(120% 90% at 18% 12%, #f6ecd6 0%, #efe1c4 42%, #e6d3ae 100%),
    #eadfc4;
}}
.grain {{
  position: absolute; inset: 0; opacity: .17; mix-blend-mode: multiply;
  background: url("{grain_uri}");
}}
.vig {{
  position: absolute; inset: 0;
  background: radial-gradient(110% 80% at 50% 45%, transparent 55%, rgba(92,68,38,.22) 100%);
}}
.map {{
  position: absolute; left: {14*scale}px; right: {14*scale}px;
  top: {70*scale}px; bottom: {36*scale}px; opacity: .3;
}}
.map svg {{ width: 100%; height: 100%; display: block; }}
.frame {{
  position: absolute; inset: {10*scale}px;
  border: {1*scale}px solid rgba(92,68,38,.55);
  outline: {1*scale}px solid rgba(92,68,38,.28); outline-offset: {3*scale}px;
  border-radius: {2*scale}px;
}}
.title {{
  position: absolute; left: 0; right: 0; top: {34*scale}px; text-align: center;
  font-weight: 600; font-size: {23*scale}px; letter-spacing: {.4*scale}px;
}}
.title small {{ display: block; font-weight: 400; font-size: {12.5*scale}px;
  letter-spacing: {.2*scale}px; opacity: .72; margin-top: {5*scale}px; }}
.rule {{
  position: absolute; top: {84*scale}px; left: 50%; transform: translateX(-50%);
  width: {150*scale}px; height: {1*scale}px; background: rgba(92,68,38,.45);
}}
.rule::before, .rule::after {{
  content: ""; position: absolute; top: {-2*scale}px; width: {5*scale}px; height: {5*scale}px;
  background: rgba(92,68,38,.45); transform: rotate(45deg);
}}
.rule::before {{ left: {-8*scale}px; }} .rule::after {{ right: {-8*scale}px; }}
/* Bırakma hedefleri: ikonlar tam bunların ortasına oturuyor */
.slot {{
  position: absolute; width: {152*scale}px; height: {152*scale}px;
  transform: translate(-50%, -50%);
  border: {1.5*scale}px dashed rgba(92,68,38,.5);
  border-radius: {10*scale}px;
  background: rgba(252,246,232,.62);
  box-shadow: 0 0 {14*scale}px {10*scale}px rgba(252,246,232,.55);
}}
.arrow {{
  position: absolute; top: {214*scale}px; left: 50%; transform: translate(-50%, -50%);
  width: {104*scale}px; height: {26*scale}px;
}}
.foot {{
  position: absolute; left: 0; right: 0; bottom: {26*scale}px; text-align: center;
  font-size: {11.5*scale}px; opacity: .66;
}}
.compass {{
  position: absolute; right: {30*scale}px; bottom: {52*scale}px;
  width: {66*scale}px; height: {66*scale}px; opacity: .75;
}}
.compass svg {{ width: 100%; height: 100%; display: block; }}
</style>
<div class="grain"></div>
<div class="map">{map_svg}</div>
<div class="vig"></div>
<div class="frame"></div>
<div class="title">Dünya Dilleri Atlası<small>Kurmak için soldaki simgeyi sağdaki klasöre sürükleyin</small></div>
<div class="rule"></div>
<div class="slot" style="left:{APP_XY[0]*scale}px; top:{APP_XY[1]*scale}px"></div>
<div class="slot" style="left:{DEST_XY[0]*scale}px; top:{DEST_XY[1]*scale}px"></div>
<svg class="arrow" viewBox="0 0 104 26">
  <g fill="none" stroke="{ink}" stroke-opacity=".62" stroke-width="1.6"
     stroke-linecap="round" stroke-dasharray="7 5">
    <path d="M4 13 H84"/>
  </g>
  <path d="M84 5 L100 13 L84 21 Z" fill="{ink}" fill-opacity=".62"/>
</svg>
<div class="compass">{compass}</div>
<div class="foot">İlk açılışta uygulamaya sağ tıklayıp “Aç” deyin · ayrıntılar OKU-BENI.txt içinde</div>
"""


def render_background(dest_dir, chrome):
    """1x ve 2x PNG çekip tek TIFF'te birleştir."""
    from PIL import Image
    tmp = HERE / "_dmgbg"
    tmp.mkdir(exist_ok=True)
    shots = []
    for scale in (1, 2):
        (tmp / f"bg{scale}.html").write_text(_html(scale), encoding="utf-8")
        shots.append((scale, tmp / f"bg{scale}.png"))
    # Playwright tools/node_modules altında kurulu; betik oradan çalıştırılıyor,
    # dosya yolları mutlak veriliyor.
    launch = f'{{ executablePath: "{chrome}" }}' if chrome else "{}"
    script = f"""
import {{ chromium }} from "playwright";
const b = await chromium.launch({launch});
for (const s of [1, 2]) {{
  const p = await b.newPage({{ viewport: {{ width: {W} * s, height: {H} * s }},
                              deviceScaleFactor: 1 }});
  await p.goto("file://{tmp}/bg" + s + ".html");
  await p.waitForTimeout(400);
  await p.screenshot({{ path: "{tmp}/bg" + s + ".png" }});
  await p.close();
}}
await b.close();
"""
    subprocess.run(["node", "--input-type=module", "-e", script],
                   cwd=ROOT / "tools", check=True)
    one = Image.open(tmp / "bg1.png").convert("RGB")
    two = Image.open(tmp / "bg2.png").convert("RGB")
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / BG_NAME
    # Çok temsilli TIFF: NSImage 1x ve 2x arasından ekrana uyanı seçiyor.
    # Sıkıştırmasız 4,4 MB, LZW 2,1 MB, JPEG 0,4 MB. Parşömen dokusunda
    # JPEG'in izi görünmüyor; DMG'yi 2 MB şişirmeye değmez.
    one.save(out, format="TIFF", save_all=True, append_images=[two],
             compression="jpeg", quality=88, resolution_unit=2, dpi=(72, 72))
    return out


# ------------------------------------------------------------- .DS_Store
def write_ds_store(root, volume_name, app_name):
    """Pencere ölçüsü, görünüm ayarları, arka plan ve ikon koordinatları."""
    import datetime
    from ds_store import DSStore
    from mac_alias import (Alias, VolumeInfo, TargetInfo, ALIAS_KIND_FILE,
                           ALIAS_FIXED_DISK, ALIAS_HFS_VOLUME_SIGNATURE)

    # Finder arka plan resmini bir "alias" kaydından çözüyor. Alias normalde
    # macOS'ta, imaj bağlıyken üretilir ve dosyanın CNID'sini taşır; burada
    # Mac yok, o yüzden kayıt elle kuruluyor. CNID tutmayacağı için Finder
    # yol üzerinden çözecek — birim adı ve yollar bu yüzden birebir doğru.
    epoch = datetime.datetime(2000, 1, 1, tzinfo=datetime.timezone.utc)
    vol = VolumeInfo(volume_name, epoch, ALIAS_HFS_VOLUME_SIGNATURE,
                     ALIAS_FIXED_DISK, 0, b"\0\0")
    vol.posix_path = f"/Volumes/{volume_name}"
    target = TargetInfo(ALIAS_KIND_FILE, BG_NAME, 0, 0, epoch,
                        b"\0\0\0\0", b"\0\0\0\0")
    target.folder_name = ".background"
    target.carbon_path = f"{volume_name}:.background:{BG_NAME}"
    target.posix_path = f".background/{BG_NAME}"
    alias = Alias(volume=vol, target=target)

    # Pencerenin ekrandaki yeri: sol üst (200, 120)
    x0, y0 = 200, 120
    bwsp = {
        "ShowStatusBar": False, "ShowTabView": False, "ShowPathbar": False,
        "ShowSidebar": False, "ShowToolbar": False,
        "WindowBounds": f"{{{{{x0}, {y0}}}, {{{W}, {H}}}}}",
        "PreviewPaneVisibility": False, "SidebarWidth": 0,
    }
    icvp = {
        "viewOptionsVersion": 1, "backgroundType": 2,
        "backgroundImageAlias": alias.to_bytes(),
        "arrangeBy": "none", "gridOffsetX": 0.0, "gridOffsetY": 0.0,
        "gridSpacing": 100.0, "iconSize": float(ICON_SIZE), "textSize": 13.0,
        "labelOnBottom": True, "showIconPreview": False, "showItemInfo": False,
        "scrollPositionX": 0.0, "scrollPositionY": 0.0,
    }

    with DSStore.open(str(root / ".DS_Store"), "w+") as d:
        # ds_store bu kodlar için codec'i kendi seçiyor: bwsp/icvp bplist,
        # Iloc ise (x, y) noktası olarak veriliyor.
        d["."]["bwsp"] = bwsp
        d["."]["icvp"] = icvp
        d["."]["vSrn"] = ("long", 1)
        d["."]["ICVO"] = ("bool", True)
        d[app_name]["Iloc"] = APP_XY
        d["Applications"]["Iloc"] = DEST_XY
        # Salt okunur bir birimde Finder'a "bunu gizle" diyemiyoruz, ama
        # yerini söyleyebiliyoruz: OKU-BENI.txt pencerenin altına, görünür
        # alanın dışına konuyor. Aşağı kaydıran bulur, kimseye çarpmaz.
        d["OKU-BENI.txt"]["Iloc"] = (W // 2, H + 260)


def build(root, volume_name, app_name, chrome):
    """DMG kökünü süsle. Bir şey eksikse sessizce vazgeç, paket yine çıksın."""
    try:
        render_background(root / ".background", chrome)
        write_ds_store(root, volume_name, app_name)
    except Exception as e:                     # ds_store/Pillow/Chromium yoksa
        print(f"  uyarı: DMG penceresi süslenemedi ({type(e).__name__}: {e})")
        return False
    return True


if __name__ == "__main__":
    dest = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "_dmgpreview")
    dest.mkdir(parents=True, exist_ok=True)
    render_background(dest, "/opt/pw-browsers/chromium")
    print("arka plan:", dest / BG_NAME)
