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
BG_NAME = "bg.png"


def render_background(dest_dir):
    """Kaynak resmi pencere ölçüsünde düz PNG olarak yaz.

    Önce 1x+2x çok temsilli, JPEG sıkıştırmalı TIFF denendi — Retina'da net
    olsun diye. Gerçek Mac'te arka plan hiç görünmedi ve iki şüpheli vardı:
    elle kurulan alias kaydı ve TIFF'in kendisi. İkinci şüpheliyi tamamen
    ortadan kaldırmak için en sade biçim seçildi: tek çözünürlük, düz PNG.
    Retina'da bir tık yumuşak duruyor; önce çalışması önemli."""
    from PIL import Image
    im = Image.open(SOURCE).convert("RGB").resize((W, H), Image.LANCZOS)
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / BG_NAME
    im.save(out, format="PNG", optimize=True)
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
    # Alanların biçimi mac_alias'ın Mac'te ürettiğiyle birebir aynı olmalı:
    # posix yolu birimin köküne göre ve başında bölü işaretiyle, carbon yolu
    # ise ":\0" ile birleştirilmiş (kütüphanenin kendi tuhaflığı, ama gerçek
    # kayıtlarda böyle). Önceki denemede baştaki bölü yoktu ve arka plan
    # gelmedi.
    target.posix_path = f"/.background/{BG_NAME}"
    target.carbon_path = volume_name + ":" + ":\0".join([".background", BG_NAME])
    target.cnid_path = [16, 17]
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
        # Modern Finder arka planı "pBBk" (yer imi) alanından da okuyabiliyor.
        # Alias ile ikisi birden yazılıyor: hangisi tutarsa.
        d["."]["pBBk"] = _bookmark(volume_name)
        # ds_store bu kodlar için codec'i kendi seçiyor: bwsp/icvp bplist,
        # Iloc ise (x, y) noktası olarak veriliyor.
        d["."]["bwsp"] = bwsp
        d["."]["icvp"] = icvp
        d["."]["vSrn"] = ("long", 1)
        d["."]["ICVO"] = ("bool", True)
        d[app_name]["Iloc"] = APP_XY
        d["Applications"]["Iloc"] = DEST_XY


def _bookmark(volume_name):
    """Arka plan resmi için CFURL yer imi (kBookmark* alanları elle kuruluyor)."""
    import datetime
    from mac_alias import Bookmark, Data, URL
    from mac_alias.bookmark import (
        kBookmarkPath, kBookmarkCNIDPath, kBookmarkFileCreationDate,
        kBookmarkFileProperties, kBookmarkContainingFolder, kBookmarkVolumePath,
        kBookmarkVolumeIsRoot, kBookmarkVolumeURL, kBookmarkVolumeName,
        kBookmarkVolumeSize, kBookmarkVolumeCreationDate, kBookmarkVolumeUUID,
        kBookmarkVolumeProperties, kBookmarkCreationOptions,
        kBookmarkWasFileReference, kBookmarkUserName, kBookmarkUID,
        kCFURLResourceIsRegularFile, kCFURLVolumeSupportsPersistentIDs)
    import struct
    import uuid

    vol_path = f"/Volumes/{volume_name}"
    epoch = datetime.datetime(2000, 1, 1, tzinfo=datetime.timezone.utc)
    toc = {
        kBookmarkPath: [".background", BG_NAME],
        kBookmarkCNIDPath: [16, 17],
        kBookmarkFileCreationDate: epoch,
        kBookmarkFileProperties: Data(struct.pack(b"<QQQ", kCFURLResourceIsRegularFile, 0x0F, 0)),
        kBookmarkContainingFolder: 0,
        kBookmarkVolumePath: vol_path,
        kBookmarkVolumeIsRoot: False,
        kBookmarkVolumeURL: URL("file://" + vol_path),
        kBookmarkVolumeName: volume_name,
        kBookmarkVolumeSize: 0,
        kBookmarkVolumeCreationDate: epoch,
        kBookmarkVolumeUUID: str(uuid.uuid5(uuid.NAMESPACE_DNS, volume_name)).upper(),
        kBookmarkVolumeProperties: Data(struct.pack(
            b"<QQQ", 0x81 | kCFURLVolumeSupportsPersistentIDs,
            0x13EF | kCFURLVolumeSupportsPersistentIDs, 0)),
        kBookmarkCreationOptions: 512,
        kBookmarkWasFileReference: True,
        kBookmarkUserName: "unknown",
        kBookmarkUID: 99,
    }
    return Bookmark([(1, toc)])


def build(root, volume_name, app_name):
    """DMG kökünü süsle. Bir şey eksikse sessizce vazgeç, paket yine çıksın."""
    try:
        render_background(root / ".background")
        write_ds_store(root, volume_name, app_name)
    except Exception as e:                     # ds_store/mac_alias/Pillow yoksa
        print(f"  uyarı: DMG penceresi süslenemedi ({type(e).__name__}: {e})")
        return False
    return True
