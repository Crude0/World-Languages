#!/usr/bin/env python3
"""DMG penceresinin görünümü: arka plan resmi, ikon yerleşimi, pencere ölçüsü.

macOS'ta bir disk imajının nasıl göründüğü kök dizindeki `.DS_Store`
dosyasında yazılıdır: pencerenin ekrandaki yeri ve boyu, görünüm kipi, arka
plan resmi ve her ikonun koordinatı. Normalde bu dosyayı bir Mac'te Finder'a
yazdırırsınız; burada Mac yok, o yüzden doğrudan üretiliyor.

Arka plan `dmg-background.jpg`: 1536x1024, yani pencerenin tam iki katı.
Resimdeki iki kesikli çerçevenin içi boş bırakıldı; uygulama ve Applications
ikonları tam ortalarına oturuyor. Resim TIFF'e iki çözünürlükte konuyor
(1x ve 2x), Retina ekranda bulanık görünmesin diye.

Gereken paketler: ds_store, mac_alias, Pillow. Yoksa DMG yine üretilir,
yalnızca penceresi süssüz olur.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
SOURCE = HERE / "dmg-background.jpg"

# Pencere içeriğinin nokta cinsinden ölçüsü: kaynak resmin tam yarısı, böylece
# 2x temsil yeniden örneklenmeden kullanılıyor.
W, H = 768, 512
ICON_SIZE = 96
# Kaynak resimdeki kesikli çerçeveler (piksel taramasıyla bulundu):
#   sol  (372, 376)-(624, 641)      sağ  (886, 376)-(1137, 641)
# Noktaya çevrilmiş merkezleri; ikonun altındaki etiket de çerçeveye sığsın
# diye merkez birkaç nokta yukarı alındı.
APP_XY = (249, 246)
DEST_XY = (506, 246)
BG_NAME = "bg.tiff"


def render_background(dest_dir):
    """Kaynak resmi 1x + 2x olarak tek TIFF'e koy."""
    from PIL import Image
    two = Image.open(SOURCE).convert("RGB")
    if two.size != (W * 2, H * 2):
        two = two.resize((W * 2, H * 2), Image.LANCZOS)
    one = two.resize((W, H), Image.LANCZOS)
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / BG_NAME
    # JPEG sıkıştırma: sıkıştırmasız TIFF 6,3 MB, q95 3,2 MB, q82 1,7 MB.
    # Parşömen dokusunda q82 ile q95 arasındaki farkı görmek mümkün değil.
    one.save(out, format="TIFF", save_all=True, append_images=[two],
             compression="jpeg", quality=82, resolution_unit=2, dpi=(72, 72))
    return out


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

    x0, y0 = 180, 110                      # pencerenin ekrandaki sol üst köşesi
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
        "gridSpacing": 100.0, "iconSize": float(ICON_SIZE), "textSize": 12.0,
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


def build(root, volume_name, app_name):
    """DMG kökünü süsle. Bir şey eksikse sessizce vazgeç, paket yine çıksın."""
    try:
        render_background(root / ".background")
        write_ds_store(root, volume_name, app_name)
    except Exception as e:                     # ds_store/mac_alias/Pillow yoksa
        print(f"  uyarı: DMG penceresi süslenemedi ({type(e).__name__}: {e})")
        return False
    return True
