# Sürüm geçmişi

Numaralandırma [semantik sürümleme](https://semver.org/lang/tr/) mantığını izler,
1.0 öncesi ölçekte:

- **0.0.x** — hata düzeltmesi, veri düzeltmesi. Görünüm ve davranış aynı kalır.
- **0.x.0** — yeni bir yetenek ya da uygulamanın genelini elden geçiren bir
  değişiklik kümesi. Tek tek görünür düzeltmeler değil; "epey şey değişmiş"
  denecek kadarı.
- **1.0.0** — veri katmanı oturduğunda, kaynakların tamamı belgelenip il
  rakamlarının anket temelli olanları ayrıştırıldığında.

## v0.2.2 — 7 Ağustos 2026

**Katman menüsü yarım açılıyordu.** Menü araç sütununun üstüne konumlanıyor,
araç sütunu da panele bağlıydı; panel yukarıdayken menü ekranın 169 piksel
üstünden taşıyor ve yalnızca alt yarısı görünüyordu. Artık menü açılınca panel
en alt durağa iniyor, menü de tam sığacağı yerde kendi animasyonuyla açılıyor.
Sığmayan ekranlarda yüksekliği görünür alana göre kısılıyor.

**Araç sütunu ekrandan kırpılıyordu.** Aynı sebep: panel tam açıkken sütun üst
çubuğun altına giriyordu. Artık üst çubuğun altına inmiyor, panelle birlikte
yumuşak kayıyor (sürüklerken de anlık takip ediyor) ve yer kalmadığında
görünmez oluyor.

**Buzlu cam panele geri döndü.** 0.2.0'da tamamen kaldırmıştım; doğrusu ikisi
arasında bir yerdeydi. Panel haritanın üstünde yüzerken (en alt durak) cam,
yukarı çekilince — metin yoğunlaştığı ve okunurluk öne geçtiği için — opak.
Pahalı olan durum "geniş bulanık alan + hareket eden harita"ydı, o hiç oluşmuyor;
değişim de harita sürüklenirken değil, paneli çekerken ve onun animasyonuyla
birlikte oluyor. 0.2.0 öncesindeki ani opaklık sıçraması geri gelmiyor.

## v0.2.1 — 7 Ağustos 2026

**Haritayı sürüklerken kayma düzeltildi.** 0.2.0'da jest boyunca `viewBox`
yazmayı bırakıp katmanı CSS dönüşümüyle kaydırmaya başlamıştım. Hızlıydı ama
yanlıştı: compositor yalnızca zaten çizilmiş pikselleri taşıyabildiği için
masaüstünde harita kartının dışına taşıyor (ölçtüm: 219 piksel), kaydırılan
yönde de içerik olmayan boş alan kalıyordu; parmak/fare kalkınca yerine
oturuyordu. Mobilde de aynısı vardı, kenarda 140 piksel boşluk bırakıyordu.

Bu numara kaydırma için doğru değil, kaldırıldı. Artık her karede gerçek
`viewBox` yazılıyor — ama `requestAnimationFrame` ile kareye bir kez, yani fare
bir karede kaç kez kıpırdarsa kıpırdasın tek çizim yapılıyor (masaüstünde bu
eskiden yoktu). 0.2.0'ın akıcılık kazancının büyük kısmı zaten panelin ve
menünün camdan opak yüzeye geçmesinden geliyordu, o duruyor.

## v0.2.0 — 7 Ağustos 2026

**Dokuz renkli lejant.** Gri "diğer aileler" yığını 47 dilden 11'e indi: Türk
dilleri ve Doğu-Güney Asya dilleri kendi renklerini aldı. Palet elle seçilmedi —
sekiz ton OKLCH uzayında arandı ve renk körlüğü benzetimiyle (Machado 2009)
doğrulandı; yalnızca komşular değil bütün çiftler ayrılıyor. Kreol diller kendi
rengi yerine kaynak dilin renginde, çapraz taramayla çiziliyor.

**Etiketler artık ülkenin üstünde.** Ad konumu merkez noktası yerine erişilmezlik
kutbundan hesaplanıyor; köşe ortalaması içbükey kıyılarda denize düşüyordu
(Norveç'in adı denizde, Hırvatistan'ınki Bosna'da). 234 çapanın 228'i kesin
olarak ülke içinde. Etiket ve nokta boyutları da CSS pikseline sabitlendi —
telefonda 3 piksellik yazılar bu yüzden çıkıyordu.

**Akıcılık.** Jest sırasında her karede `viewBox` yazmak 550 yolu yeniden
rasterize ettiriyordu. Artık hazır katman CSS dönüşümüyle kaydırılıp
ölçekleniyor, gerçek `viewBox` parmak kalkınca bir kez yazılıyor. Mobil panel ve
menü de cam olmaktan çıkıp opak yüzeye geçti: hem hareket sırasında opaklık
sıçraması bitti hem de en pahalı iş ortadan kalktı.

**Kıstırma düzeldi.** İki parmak değince harita bir "tık" sıçrayıp sonra
yakınlaşıyordu; görüş kutusu jestin başındaki orta noktaya ortalanıyordu. Artık
parmakların altındaki nokta yerinde kalıyor, iki parmakla kaydırma da çalışıyor.
Aynı hata masaüstünde de vardı, o da düzeldi.

**Yakınlaşma 22x'ten 160x'e.** Ayrıca küçük ülkelere 22 piksellik görünmez
dokunma hedefi eklendi — Singapur, Malta, Bahreyn artık ilk denemede seçiliyor.
Seçilen yer üst çubuğun altında kalmıyor.

**Açık tema Android'de tamamen açık.** Sayfa `color-scheme: light` bildirdiği
için WebView kendi algoritmik karartmasını uyguluyor, panel ve harita çevresi
koyu kalıyordu. `light dark` bildirildi.

**Masaüstü başlığı.** İstatistik satırı `<dt>/<dd>` üretiyordu ama CSS başka bir
yapı arıyordu; sayılar ve etiketler kayıyordu. Başlık da sağ sütunla aynı
hizadan başlıyor.

**Depo iki dilde.** Varsayılan README İngilizce, Türkçesi `README.tr.md`;
veri belgesi de öyle.

**Paket sürümleri artık etiketle aynı.** `.app`, `.exe` ve APK'nın içindeki
numara 1.0'da kalmıştı; üçü de artık depo kökündeki `VERSION` dosyasından
besleniyor.

> Bu sürüm kısa süre `v0.1.4` etiketiyle yayımlandı; değişikliğin kapsamı
> yama numarasına sığmadığı için `v0.2.0` olarak yeniden yayımlandı.

## v0.1.3 — 6 Ağustos 2026

**İngilizce arayüz.** Başlıktaki (mobilde görünüm menüsündeki) düğmeyle Türkçe ve
İngilizce arasında geçiş yapılır. Yalnızca menüler değil; 142 dilin adı, 44 dil
ailesi etiketi, dağılım satırlarındaki 352 dil adı, 137 ülke notu, kıta adları ve
sayı biçimi de çevrilir (1,2 milyar ↔ 1.2 billion). Seçim tarayıcıda saklanır,
ilk açılışta sistem diline bakılır.

**Tema seçici.** Otomatik (sistemi izler) davranışın üstüne elle **Açık** ve
**Koyu** seçenekleri eklendi. Üç durum da kalıcı.

**Mobil panel iyileştirmeleri.** Alttan çekilen panelin tutamağı büyütüldü:
dokunma alanı 44 px yüksekliğe çıktı, çizgi 44×6 px oldu ve sürüklerken 52 px'e
genişleyip soluklaşıyor — Apple'ın kendi uygulamalarındaki geri bildirimin aynısı.
Panel içeriği kaydırıldığında başlığın altında ince bir ayraç beliriyor.

Paketler: APK 433 KB · DMG 6,8 MB · EXE 4,1 MB.

## v0.1.2 — 6 Ağustos 2026

İlk yayımlanan sürüm.

- 234 ülke ve bağımlı bölge, 142 dil, 1.100'den fazla ülke × dil satırı.
- Dile göre süzme: çoğunluk olduğu ülkeler koyu, azınlık olarak konuşulduğu
  ülkeler soluk. Türkçe 26 ülkede görünüyor.
- Konuşan sayıları; ana dil ve ikinci dil ayrı ayrı.
- Yoğunluk (ısı haritası) modu: nüfustaki paya veya kişi sayısına göre renk.
- 12 ülkede eyalet / il / kanton düzeyi — 313 bölge. Uzaktayken ülke, yaklaşınca
  bölge sınırları (Paradox oyunlarındaki gibi), ya da elle sabitlenebilir.
- Masaüstü uygulamaları işletim sisteminin tarayıcı motoruyla kendi penceresinde
  açılır: macOS'ta WKWebView, Windows'ta WebView2.
- Telefon için ayrı yazılmış arayüz: tam ekran harita, cam katmanlar, üç duraklı
  alt panel, dokunmatik jestler.
- Tamamen çevrimdışı; ağ isteği ve izin yok.
