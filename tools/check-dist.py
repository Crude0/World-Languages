#!/usr/bin/env python3
"""dist/ içindeki paketler gerçekten bu sürüm mü?

0.9.0, 0.9.1 ve 0.9.2, 0.8.0 ikililerini yayımladı. Sebebi: `make desktop`
paketleri `desktop/dist/` altına yazıyor (orası .gitignore'da), yayım iş akışı
ise depodaki `dist/` klasörünü yüklüyordu. İkisi arasında kopyalayan bir şey
yoktu, yani `dist/` en son elle güncellendiği günde kalmıştı ve kimse fark
etmedi — sürüm numarası, notlar, etiket, hepsi doğruydu; yalnız dosyalar eskiydi.

Bu betik yayımdan önce koşar ve paketlerin içine bakar. Yalnız depoda izlenen
dosyaları kullanır, yani CI'da yeniden derlemeye gerek yok.
"""
import hashlib
import pathlib
import plistlib
import re
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent.parent
DIST = HERE / "dist"
VERSION = (HERE / "VERSION").read_text().strip()

MAC = DIST / "Dunya-Dilleri-Atlasi-mac.zip"
DMG = DIST / "Dunya-Dilleri-Atlasi.dmg"
EXE = DIST / "Dunya Dilleri Atlasi.exe"
APK = DIST / "Dunya-Dilleri-Atlasi.apk"

fail = []


def bad(msg: str) -> None:
    fail.append(msg)
    print("  HATA: " + msg)


def strip_pwa(html: str) -> str:
    """pwa.py'nin docs/ kopyasına eklediği manifest ve kayıt bloklarını çıkarır.

    APK ve masaüstü paketleri yamasız sayfayı gömüyor; docs/ kopyası yamalı.
    İkisini karşılaştırabilmek için yama geri alınıyor.
    """
    head = re.search(r'<link rel="manifest".*?</head>', html, re.S)
    if head:
        html = html.replace(head.group(0), "</head>", 1)
    reg = re.search(r"<script>\n// Hizmet çalışanı.*?</script></body>", html, re.S)
    if reg:
        html = html.replace(reg.group(0), "</body>", 1)
    return html


def desktop_page() -> bytes:
    """Masaüstü ikililerinde birebir geçmesi gereken sayfa.

    Sürüm dizgesinin ikilide bulunması paketin bu sürümde derlendiğini
    gösteriyordu ama sayfanın güncel olduğunu göstermiyordu: `-X main.version`
    ile gömülen numara, go:embed ile gömülen HTML'den bağımsız. APK'da sayfa
    zaten karşılaştırılıyordu, masaüstünde karşılığı yoktu.

    go:embed dosyayı sıkıştırmadan koyuyor, yani ikilinin içinde bayt bayt
    aranabiliyor. Karşılaştırma kaynağı depoda izlenen docs/index.html;
    pwa.py'nin oraya eklediği yama geri alınınca desktop/app.html ile aynı
    oluyor, dolayısıyla CI'da yeniden derlemeye gerek kalmıyor.
    """
    return strip_pwa((HERE / "docs" / "index.html").read_text(encoding="utf-8")).encode("utf-8")


def check_mac() -> None:
    print(f"{MAC.name}:")
    if not MAC.exists():
        return bad("dosya yok")
    z = zipfile.ZipFile(MAC)
    plist = plistlib.loads(z.read("Dunya Dilleri Atlasi.app/Contents/Info.plist"))
    got = plist.get("CFBundleShortVersionString")
    print(f"  paket sürümü: {got}")
    if got != VERSION:
        bad(f"paket sürümü {got}, beklenen {VERSION}")
    exe = [n for n in z.namelist() if "/MacOS/" in n and not n.endswith("/")]
    if not exe:
        return bad("çalıştırılabilir dosya yok")
    blob = z.read(exe[0])
    if VERSION.encode() not in blob:
        bad(f"ikilide {VERSION} dizgesi yok (-X main.version geçmemiş)")
    page = desktop_page()
    print(f"  ikili: {len(blob)} bayt · gömülü sayfa {'güncel' if page in blob else 'BAYAT'}")
    if page not in blob:
        bad("ikilideki sayfa docs/index.html ile aynı değil — paket bayat")


def check_exe() -> None:
    print(f"{EXE.name}:")
    if not EXE.exists():
        return bad("dosya yok")
    blob = EXE.read_bytes()
    if VERSION.encode() not in blob:
        bad(f"ikilide {VERSION} dizgesi yok")
    page = desktop_page()
    print(f"  {len(blob)} bayt · gömülü sayfa {'güncel' if page in blob else 'BAYAT'}")
    if page not in blob:
        bad("ikilideki sayfa docs/index.html ile aynı değil — paket bayat")


def check_apk() -> None:
    print(f"{APK.name}:")
    if not APK.exists():
        return bad("dosya yok")
    z = zipfile.ZipFile(APK)
    if "assets/app.html" not in z.namelist():
        return bad("assets/app.html yok")
    inside = z.read("assets/app.html").decode("utf-8")
    want = strip_pwa((HERE / "docs" / "mobile.html").read_text(encoding="utf-8"))
    h1 = hashlib.sha256(inside.encode()).hexdigest()[:16]
    h2 = hashlib.sha256(want.encode()).hexdigest()[:16]
    print(f"  gömülü sayfa {h1} · depodaki {h2}")
    if inside != want:
        bad("APK içindeki sayfa docs/mobile.html ile aynı değil — APK bayat")


def check_dmg() -> None:
    print(f"{DMG.name}:")
    if not DMG.exists():
        return bad("dosya yok")
    # DMG'nin içi burada açılamıyor (HFS+); boyutu mac zip'ten büyük olmalı ve
    # ondan eski olmamalı. Asıl doğrulama zip üzerinden yapılıyor; ikisi de aynı
    # package.py koşusunda üretiliyor.
    if MAC.exists() and DMG.stat().st_mtime + 1 < MAC.stat().st_mtime:
        bad("mac zip'ten eski — aynı derlemeden gelmiyor olabilir")
    print(f"  {DMG.stat().st_size} bayt")


def main() -> int:
    print(f"VERSION = {VERSION}\n")
    check_mac()
    check_exe()
    check_apk()
    check_dmg()
    print()
    if fail:
        print(f"{len(fail)} sorun — yayımlanmamalı")
        return 1
    print("dist/ bu sürümle tutarlı")
    return 0


if __name__ == "__main__":
    sys.exit(main())
