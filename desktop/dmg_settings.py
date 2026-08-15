# dmgbuild ayarları — DMG gerçek bir Mac'te (GitHub'ın macos koşucusu)
# üretiliyor. Linux'ta elle .DS_Store yazıp arka planı alias kaydıyla tanıtmayı
# iki kez denedik: pencere ölçüsü ve ikon yerleri tuttu ama arka plan hiç
# gelmedi. Alias normalde imaj bağlıyken, dosyanın gerçek CNID'si ve birimin
# gerçek oluşturma tarihiyle üretiliyor; ikisi de Linux'ta uydurma oluyor.
# Mac'te üretince bu iş macOS'un kendi kodu tarafından yapılıyor, ayrıca imaj
# ISO9660 yerine HFS+ oluyor — takılınca pencerenin kendiliğinden açılması da
# ancak orada mümkün.
#
# Kullanımı:
#   dmgbuild -s desktop/dmg_settings.py -D app=<yol/…app> -D bg=<arkaplan>
#            "Dunya Dilleri Atlasi" cikti.dmg
import os.path

application = defines["app"]
appname = os.path.basename(application)

format = defines.get("format", "UDZO")
size = defines.get("size", None)

files = [application]
symlinks = {"Applications": "/Applications"}
icon = defines.get("volicon", None)

background = defines["bg"]

# Pencere: arka plan resminin nokta cinsinden ölçüsüyle birebir aynı.
window_rect = ((180, 110), (768, 512))
default_view = "icon-view"
show_status_bar = False
show_tab_view = False
show_toolbar = False
show_pathbar = False
show_sidebar = False
sidebar_width = 0

arrange_by = None
grid_offset = (0, 0)
grid_spacing = 100
scroll_position = (0, 0)
label_pos = "bottom"
text_size = 12
icon_size = 96

# Arka plandaki iki kesikli çerçevenin ortası (kaynak resimde
# sol 372,376-624,641 · sağ 886,376-1137,641 — noktaya çevrilmiş hâli).
icon_locations = {
    appname: (249, 246),
    "Applications": (506, 246),
}
