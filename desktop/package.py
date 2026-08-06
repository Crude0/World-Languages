#!/usr/bin/env python3
"""macOS .app + .dmg ve Windows .exe paketleri."""
import os, pathlib, shutil, struct, subprocess, sys

HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"
DIST = HERE / "dist"
APP_NAME = "Dünya Dilleri Atlası"
BUNDLE = "Dunya Dilleri Atlasi"   # ISO9660 Unicode adları macOS'ta bozuyor
EXEC_NAME = "dunya-dilleri-atlasi"
VERSION = "1.0"

CPU_TYPE = {"amd64": (0x01000007, 0x00000003), "arm64": (0x0100000C, 0x00000000)}


def universal(slices, dest):
    """İki Mach-O dosyasını tek evrensel (fat) binary'de birleştirir."""
    align = 14                       # 2^14 = 16 KB, arm64 gereksinimi
    header = 8 + 20 * len(slices)
    offset = (header + (1 << align) - 1) & ~((1 << align) - 1)
    blobs, archs = [], []
    for arch, path in slices:
        data = path.read_bytes()
        cputype, cpusub = CPU_TYPE[arch]
        archs.append(struct.pack(">5I", cputype, cpusub, offset, len(data), align))
        blobs.append((offset, data))
        offset = (offset + len(data) + (1 << align) - 1) & ~((1 << align) - 1)
    buf = bytearray(offset)
    buf[0:8] = struct.pack(">2I", 0xCAFEBABE, len(slices))
    buf[8:8 + 20 * len(archs)] = b"".join(archs)
    for off, data in blobs:
        buf[off:off + len(data)] = data
    dest.write_bytes(bytes(buf))


PLIST = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key><string>tr</string>
	<key>CFBundleDisplayName</key><string>{APP_NAME}</string>
	<key>CFBundleExecutable</key><string>{EXEC_NAME}</string>
	<key>CFBundleIconFile</key><string>AppIcon</string>
	<key>CFBundleIdentifier</key><string>app.dunyadilleri.atlas</string>
	<key>CFBundleInfoDictionaryVersion</key><string>6.0</string>
	<key>CFBundleName</key><string>Dünya Dilleri</string>
	<key>CFBundlePackageType</key><string>APPL</string>
	<key>CFBundleShortVersionString</key><string>{VERSION}</string>
	<key>CFBundleVersion</key><string>{VERSION}</string>
	<key>LSApplicationCategoryType</key><string>public.app-category.education</string>
	<key>LSMinimumSystemVersion</key><string>10.15</string>
	<key>LSUIElement</key><true/>
	<key>NSHighResolutionCapable</key><true/>
	<key>NSHumanReadableCopyright</key><string>Açık veri · Natural Earth sınırları</string>
</dict>
</plist>
"""

README = """DÜNYA DİLLERİ ATLASI
====================

Her ülkede nüfusun çoğunluğunun konuştuğu dili gösteren interaktif harita.
İnternet bağlantısı gerektirmez; tüm veri uygulamanın içindedir.

KURULUM
-------
"Dunya Dilleri Atlasi" simgesini soldaki Applications (Uygulamalar)
klasörüne sürükleyin, sonra Launchpad'den ya da Uygulamalar klasöründen açın.

İLK AÇILIŞTA "GELİŞTİRİCİSİ DOĞRULANAMADI" UYARISI
--------------------------------------------------
Uygulama Apple tarafından imzalanmadığı için macOS ilk açılışta uyarır.
Şu yollardan biriyle açabilirsiniz:

  1) Uygulamaya sağ tıklayın (ya da Control basılı tıklayın) -> "Aç" ->
     çıkan pencerede yine "Aç".

  2) macOS 15 (Sequoia) ve sonrasında: uygulamayı bir kez açmayı deneyin,
     ardından Sistem Ayarları -> Gizlilik ve Güvenlik bölümünün altındaki
     "Yine de Aç" düğmesine basın.

  3) Terminal'den karantina etiketini kaldırın:
     xattr -dr com.apple.quarantine "/Applications/Dunya Dilleri Atlasi.app"

NASIL ÇALIŞIR
-------------
Uygulama, içindeki tek dosyalık haritayı
~/Library/Application Support/DunyaDilleriAtlasi/ klasörüne yazar ve
macOS'un kendi WebKit bileşeniyle (WKWebView) kendi penceresinde açar.
Tarayıcı gerekmez; Dock'ta uygulamanın kendi simgesi görünür.

Pencere herhangi bir sebeple açılamazsa uygulama kurulu bir tarayıcıyı
(Chrome/Edge/Brave) adres çubuğu olmayan uygulama kipinde açar. Bu kipi
elle zorlamak için Terminal'den:
  DUNYA_TARAYICI=1 "/Applications/Dunya Dilleri Atlasi.app/Contents/MacOS/dunya-dilleri-atlasi"

Arka planda hiçbir servis çalışmaz, ağ bağlantısı kurulmaz.

KALDIRMA
--------
Uygulamayı çöpe atın ve isterseniz yukarıdaki klasörü silin.
"""


def build_mac():
    app = DIST / f"{BUNDLE}.app"
    if app.exists():
        shutil.rmtree(app)
    macos = app / "Contents" / "MacOS"
    res = app / "Contents" / "Resources"
    macos.mkdir(parents=True)
    res.mkdir(parents=True)
    universal([("amd64", OUT / "mac-amd64"), ("arm64", OUT / "mac-arm64")], macos / EXEC_NAME)
    (macos / EXEC_NAME).chmod(0o755)
    (app / "Contents" / "Info.plist").write_text(PLIST)
    (app / "Contents" / "PkgInfo").write_text("APPL????")
    shutil.copy(HERE / "AppIcon.icns", res / "AppIcon.icns")
    # Finder ASCII dosya adı yerine bu adı gösterir
    strings = f'CFBundleDisplayName = "{APP_NAME}";\nCFBundleName = "Dünya Dilleri";\n'
    for loc in ("tr", "en", "Base"):
        d = res / f"{loc}.lproj"
        d.mkdir()
        (d / "InfoPlist.strings").write_bytes(strings.encode("utf-16"))
    return app


def build_dmg(app):
    root = HERE / "dmgroot"
    if root.exists():
        shutil.rmtree(root)
    root.mkdir()
    shutil.copytree(app, root / app.name, symlinks=True)
    os.symlink("/Applications", root / "Applications")
    (root / "OKU-BENI.txt").write_text(README)
    dmg = DIST / "Dunya-Dilleri-Atlasi.dmg"
    dmg.unlink(missing_ok=True)
    subprocess.run(["genisoimage", "-quiet", "-V", "Dunya Dilleri Atlasi",
                    "-D", "-r", "-o", str(dmg), str(root)], check=True)
    return dmg


def build_zip(app):
    z = DIST / "Dunya-Dilleri-Atlasi-mac.zip"
    z.unlink(missing_ok=True)
    subprocess.run(["zip", "-q", "-r", "-y", str(z), app.name], cwd=DIST, check=True)
    return z


def build_windows():
    exe = DIST / "Dunya Dilleri Atlasi.exe"
    shutil.copy(OUT / "win-amd64.exe", exe)
    return exe


DIST.mkdir(exist_ok=True)
app = build_mac()
dmg = build_dmg(app)
zp = build_zip(app)
exe = build_windows()
for f in (dmg, zp, exe):
    print(f"{f.name}: {f.stat().st_size/1024/1024:.1f} MB")
