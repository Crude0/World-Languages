# Sürüm geçmişi

Numaralandırma [semantik sürümleme](https://semver.org/lang/tr/) mantığını izler,
1.0 öncesi ölçekte:

- **0.0.x** — hata düzeltmesi, veri düzeltmesi. Görünüm ve davranış aynı kalır.
- **0.x.0** — yeni bir yetenek ya da uygulamanın genelini elden geçiren bir
  değişiklik kümesi. Tek tek görünür düzeltmeler değil; "epey şey değişmiş"
  denecek kadarı.
- **1.0.0** — veri katmanı oturduğunda, kaynakların tamamı belgelenip il
  rakamlarının anket temelli olanları ayrıştırıldığında.

## v0.9.2 — 16 Ağustos 2026

**Yayımlanan sürüm ikinci yenilemeye kadar görünmüyordu.** Hizmet çalışanı
sayfayı önce önbellekten veriyor, ağ kopyasını arka planda tazeliyordu; yani
yeni bir sürüm çıktığında ilk açılışta hâlâ eskisi geliyordu. 0.9.0 çıktıktan
sonra tam olarak bu oldu.

Ölçüldü: sahte bir sitede eski sayfa önbelleğe alınıp sunucudaki dosya
değiştirildiğinde yeni sürüm **2. yenilemede** geliyordu. Sayfa istekleri artık
önce ağdan gidiyor, ağ yoksa önbelleğe düşülüyor — aynı ölçümde **1. yenileme**.
Sunucu tamamen kapalıyken sayfa yine açılıyor, yani çevrimdışı çalışma duruyor.
İkon ve manifest gibi sürümle değişmeyen dosyalarda önbellek yine önce.

## v0.9.1 — 16 Ağustos 2026

Tablo açıkken harita alanı gizleniyor; tam ekran düğmesi de o sırada
görünmüyor. Ama macOS menüsündeki **Yalnız Harita (⇧⌘F)** düğmeye doğrudan
basıyor, yani menüden girilince ekranı boş bir okyanus kaplıyordu. Tam ekran
artık her zaman önce tabloyu kapatıyor.

Pencere yeniden boyutlandırılınca harita gereksiz yere yeniden çiziliyor ve
adres çubuğuna yazılıyordu; bu iş yalnız tam ekranda gerekli, orada
sarmalayıcının ölçüsünü biz veriyoruz.

## v0.9.0 — 16 Ağustos 2026

**Masaüstü arayüzü elden geçti.** Denetimler haritanın üstüne taşındı,
tam ekran kipi eklendi, "Bildiğim diller" katmanının rengi ve ipucu
yeniden yapıldı.

### Başlık şeridi on altı düğme taşıyordu

Dört katman, üç boyama, üç ayrıntı düzeyi, süzgeci kaldır, tablo,
bağlantı, PNG, SVG ve üç yakınlaştırma — hepsi tek bir sırada yan yana.
Her yeni harita kipi bunu biraz daha karıştırdı.

Şeritte artık yalnız başlık var. Haritanın sol üstünde üç düğmelik bir cam
çubuk duruyor: **Görünüm**, **Tablo**, **Paylaş** (süzgeç açıkken bir de
"Süzgeci kaldır"). Katman, renk ve ayrıntı seçenekleri Görünüm yaprağında
gruplanmış, her grubun ne işe yaradığını anlatan birer satırla. Dışa
aktarma Paylaş yaprağında. Karşı köşede yakınlaştırma yığını.

### Tam ekran

Harita bazen ekranda küçük kalıyordu. **⛶** düğmesi haritayı görünümün
tamamına açıyor — sayfa, kenar çubuğu, kartlar kalkıyor. Fullscreen API
varsa gerçek tam ekrana geçiliyor (tarayıcı çerçevesi de kalkıyor),
yoksa sabit konumlu bir kaplamaya düşülüyor. Denetimler zaten haritanın
içinde olduğu için iki kipte de aynı yerleşim geçerli. macOS uygulamasında
Görünüm menüsünde **Yalnız Harita (⇧⌘F)** olarak da var.

**Paneller sol ya da sağ kenarda durabiliyor** (⇄), seçim tarayıcıda
saklanıyor.

Yüzen yüzeyler buzlu cam — altındaki harita sızıyor, böylece panelin
nereye denk geldiği görünüyor. `backdrop-filter` desteklenmiyorsa ya da
kullanıcı saydamsızlık istiyorsa düz panel rengine düşüyor: okunurluk
her durumda camdan önce geliyor. Sayfanın geri kalanı eskisi gibi düz ve
keskin.

### "Bildiğim diller": ipucunda yüzde, yeni renk şeridi

Bir ülkenin üstünde dururken artık **halkın yüzde kaçıyla
anlaşabileceğiniz**, kaç kişiye denk geldiği ve bu paya en çok katkı veren
üç dil yazıyor.

Renk şeridi de değişti. Eskisi tek tonun koyudan açığa gitmesiydi; komşu
kutular arasındaki en küçük CIEDE2000 farkı **4,5** idi, yani Çin ile
Afganistan ayırt edilemiyordu. Yenisi kırmızıdan yeşile gidiyor ve en kötü
komşu farkı **9,5** — normal görme ve üç renk körlüğü türünün hepsinde
ölçüldü. Düz kırmızı–yeşil şerit de denendi ama protanopide fark **1,1**'e
düşüyor, uçlar arasında yalnız 3,1 kalıyordu; onun yerine parlaklığı da tek
yönlü artan, OKLCH'te aranmış düzgün bir eğri kullanıldı (uçlar arası
50,7–77,3).

### macOS "Hakkında" penceresi

Telif satırı yoktu ve uygulamanın simgesi yerine genel bir klasör
görüntüsü çıkıyordu. Artık **© 2026 Crude** yazıyor, uygulamanın kendi
simgesi görünüyor ve sürümün yanındaki parantez kalktı — oraya
osascript'in derleme numarası sızıyordu. Yayım iş akışı bu üçünü de
gerçek macOS koşucusunda doğruluyor.

### Yol boyunca çıkan hatalar

- Tablo açılınca harita alanı tümden gizleniyordu; denetimler oraya
  taşınınca tabloyu kapatan düğme de kayboluyordu.
- İpucu kapalıyken yalnız saydamlığı sıfırlanıyordu; kutu yerleşimde
  kalıyor ve pencere daraltılınca sayfayı yana taşırıyordu.
- `hover()` içinde yerel bir değişken dil sözlüğü erişimcisini
  gölgeliyordu.
- Bölge verisi olan ülke sayısı üç yerde hâlâ 12 yazıyordu; 0.7.0'da 18
  olmuştu.

Telefon arayüzü bu sürümde değişmedi.

## v0.8.0 — 16 Ağustos 2026

### 0,94 milyar kişinin dili görünmüyordu

0.7.0'ı yazarken not ettiğim eksik, bakınca sandığımdan çok daha büyük
çıktı. Dağılım tablolarında satırı olan ama dil tablosunda karşılığı
bulunmayan **186 dil** vardı; eşleşmeyen satır sessizce düşüyordu ve
düşenlerin toplamı **0,94 milyar kişiydi**. En büyükleri Cava dili
(90 milyon), Wu Çincesi (85), Bhojpuri (74), Yorubaca (48), Lingala (44),
Oromoca (44), Sunda dili (42), Sindhi (40).

İki ayrı sorun çıktı. Bir kısmı gerçekten kayıtsızdı; bir kısmı ise
**aynı dilin iki yazımıydı** — tablolar yıllar içinde farklı adlarla
yazılmış: "Vu Çincesi" ile "Wu Çincesi", "Yoruba" ile "Yorubaca",
"Tayvanca (Hokkien)" ile "Min Çincesi", "Fulfulde" ve "Pulaar" ile
"Fulaca". Bunlar için bir takma ad tablosu kuruldu.

2 milyondan çok konuşanı olan 63 dilin hepsi kaydedildi; düşen 0,94
milyardan geriye **0,057 milyar** kaldı (89 küçük dil, en büyüğü
2 milyon). Dil sayısı **219'dan 270'e**, aile etiketi 54'ten 55'e çıktı;
ana dili sayılan nüfus 7,19 milyardan **7,98 milyara**.

### Karşılaştırma

Ülke kartındaki **"… ile karşılaştır"** düğmesi bir yeri sabitliyor;
ikinci bir yer seçilince kart iki sütuna dönüyor. Altta **iki yerde de
konuşulan diller** listeleniyor, oranlar iki paydan küçüğü — yani o dille
kaç kişiyle anlaşılabileceğinin alt sınırı. Türkiye ile Almanya'yı
karşılaştırınca ortak liste Türkçe %2, Kürtçe %1,2, Arapça %1,2 çıkıyor.
Ülkeler kadar bölgeler de karşılaştırılabiliyor — Tataristan ile
Çuvaşistan, Québec ile Ontario.

### Bildiğim diller

Dördüncü bir katman: **Bildiğim**. Dil listesinden bildiğiniz dilleri
seçiyorsunuz, harita her ülkeyi o dillerden en az birini konuşan nüfusun
payıyla boyuyor — ana dil ya da ikinci dil olarak. Türkçe + İngilizce
seçince dünyada ≈1,81 milyar kişi çıkıyor. Seçim tarayıcıda saklanıyor ve
bağlantıya giriyor (`#k=know&kn=tr.en`), yani paylaşılabiliyor.

Katmanın iki okuma biçimi var. **Pay** yukarıdaki gibi çalışıyor. **Ana dil**
ise yalnız seçtiğiniz dillerden birinin *evde konuşulan çoğunluk dili* olduğu
ülkeleri yakıyor — her biri kendi dil ailesinin renginde, öbürleri sönük.
Türkçe + İngilizce seçince 38 ülke, ≈538 milyon kişi. "Nerede anlaşırım" ile
"nerede benim dilim konuşulur" ayrı sorular; ikisi ayrı kipte duruyor.

Pay kipinde paylar toplanıp %100'de kırpılıyor: iki dili birden bilenler iki
kez sayıldığı için rakam bir üst sınır. Bu kartta ve göstergede yazıyor.

### PNG ve SVG olarak indirme

Üst çubuğa **PNG** ve **SVG** düğmeleri geldi; o anki görünüm — yakınlık,
katman, süzgeç, seçim — tek dosya olarak iniyor. SVG tek başına duruyor:
sayfanın stil sayfasından yalnız haritayı ilgilendiren kurallar ve
kullanılan renkler içine kopyalanıyor, budanmış yollar hiç yazılmıyor.
Dosya adı görünümden türetiliyor (`dunya-dilleri-off-french.svg`).
Telefonda ikisi de katman menüsünde.

### macOS menü çubuğu

Uygulamanın menü çubuğunda ad olarak **"osascript"** yazıyordu ve
Hakkında, Dosya, Görünüm menüleri hiç yoktu. Sebebi: uygulama menüsünün
başlığı `NSMenuItem`'dan değil çalışan sürecin paket adından geliyor,
pencere de osascript'in içinde açılıyor. Paket sözlüğündeki ad artık
açılışta değiştiriliyor.

Menü de tamamlandı: **Hakkında** (sürüm numarasıyla), Gizle / Diğerlerini
Gizle / Tümünü Göster, **Dosya** (bağlantıyı kopyala, pencereyi kapat),
**Düzen** (geri al, kes, kopyala, yapıştır, tümünü seç), **Görünüm**
(yakınlaş, uzaklaş, sığdır, tabloyu aç/kapat, tam ekran), **Pencere**.
Görünüm menüsü sayfanın kendi düğmelerini tetikliyor, yani menü ile araç
çubuğu aynı işi yapıyor. "Çık" artık kendi seçicisini kullanıyor: eskiden
macOS başlığı "Quit and Keep Windows" diye değiştiriyordu, üstelik
İngilizce.

Mac'e erişimim olmadığı için bunu körlemesine göndermek istemedim:
betiğe menüyü kurup yazdıran bir denetim kipi eklendi ve yayım iş akışı
bunu **macOS koşucusunda çalıştırıp** paket adının ve beş menünün
yerinde olduğunu doğruluyor. Doğrulama düşerse sürüm yayımlanmıyor.

## v0.7.0 — 16 Ağustos 2026

**Bölge verisi 12 ülkeden 18'e, 313 bölgeden 507'ye çıktı.** Haritanın en
büyük boş lekeleri kapandı.

**Rusya · 83 federal özne.** Federasyonda 30'dan fazla dil cumhuriyet
düzeyinde resmî; harita bugüne kadar Rusya'yı tek renk çiziyordu. Artık
Tataristan Tatarca, Çuvaşistan Çuvaşça, Saha Sahaca, Tuva Tuvaca ile Türk
dilleri renginde; Çeçenistan, İnguşetya, Dağıstan ve Kabardey-Balkar kendi
Kafkas dilleriyle ayrı duruyor. Kaynak 2021 sayımı. 32 yeni dil geldi:
Tatarca, Başkurtça, Çuvaşça, Sahaca, Tuvaca, Çeçence, Avarca, Lezgice,
Osetçe, Marice, Udmurtça, Buryatça, Kalmukça, Çukçice ve diğerleri.

**Çin · 31 eyalet.** "Çince" tek bir dil değil: Mandarin, Kantonca, Wu, Min,
Hakka, Xiang ve Gan karşılıklı anlaşılmaz. Harita bunları ilk kez ayırıyor —
Şanghay ve Zhejiang Wu, Fujian ve Hainan Min, Jiangxi Gan, Hunan Xiang,
Guangdong Kantonca. Sincan Uygurca, Tibet Tibetçe, İç Moğolistan Moğolca,
Guangxi'de Zhuangca.

**Nijerya · 37 eyalet.** Ülkenin çoğunluk dili yok; asıl dağılım eyalet
düzeyinde. Kuzey Hausa, güneybatı Yorubaca, güneydoğu İgboca, Nijer Deltası
ise Nijerya Pidgini kuşağı.

**Güney Afrika · 9 il.** 12 resmî dilin hiçbiri ülke genelinde çoğunluk
değil. Census 2022: KwaZulu-Natal'da Zuluca %78, Doğu Cape'te Xhosa %77,
Batı Cape'te Afrikaanca %41, Limpopo'da Sepedi %52.

**Fransa · 18 bölge** (Korsikaca, Bretonca, Oksitanca, denizaşırı kreoller)
ve **Almanya · 16 eyalet** (Zensus 2022 hane dili; Berlin'de Türkçe %5,
doğu eyaletlerinde %1'in altında).

**Brezilya bilerek dışarıda:** 27 eyaletin hepsinde Portekizce ~%98, yani
2389 nokta karşılığında tek renkli bir yüzey. Kırım, Sivastopol ve Paracel
Adaları da alınmadı — Natural Earth bunları Rusya'ya ve Çin'e bağlıyor, bu
depo ise sınırlarda taraf tutmuyor. Bölge kipine geçmek artık hiçbir
yarımadanın hangi ülkeye sayıldığını değiştirmiyor.

**Dil sayısı 155'ten 219'a çıktı**; 64'ü bu turda geldi. Aile etiketi 44'ten
54'e: Nah-Dağıstan, Kuzeybatı Kafkas, Tunguz, Çukçi-Kamçatka, Hmong-Mien,
Nil-Sahra ve Nijer-Kongo'nun dört yeni kolu.

### Ve kasma geri gelmedi — tersine hızlandı

Geometri %83 büyüdü (21.628 → 39.683 nokta). Ölçüm yapılmadan eklenseydi
bölge kipi iki katı pahalıya gelecekti; ilk ölçüm Rusya'ya yakınlaşınca
1956 → 3772 ms gösterdi. Katman katman ölçülünce iki ayrı sebep çıktı.

**Birincisi `stroke-linejoin: round`.** Sınır ağlarında duruyordu ve tek
başına maliyetin **%29**'unu tutuyordu: on beş bin köşenin her birinde
yuvarlak birleşim geometrisi üretiliyor, 1,2 piksellik bir çizgide gözle
ayırt edilemeyen bir fark için. Kaldırıldı. (Aynı turda 0.4.0 planında
şüpheli olarak duran `vector-effect: non-scaling-stroke` da denendi;
ölçüm 6 ms fark gösterdi, yani etkisiz — o madde kapandı.)

**İkincisi budamanın çalışmaması.** Sınır ağı ülke başına *tek* bir yoldu:
Rusya'nın 153 zincirlik dış çeperi, ekranda yüzde onu görünse bile
bütünüyle konturlanıyordu. Zincirler artık kaba bir ızgarada kovalara
dağıtılıyor (40 svg birimlik hücreler, toplam 260 kova) ve ekran dışında
kalan kovalar eleniyor. Bu, yalnız yeni ülkelere değil Kanada'nın 5957
noktalık çeperine de yarıyor.

İkisi birlikte, %83 daha fazla geometriye rağmen:

| durum | 0.6.1 | 0.7.0 |
|---|---|---|
| dünya · ülke kipi | 878 ms | 647 ms |
| dünya · bölge kipi zorlanmış | 1951 ms | **1506 ms** |
| Rusya yakın · bölge zorlanmış | 1845 ms | **1503 ms** |
| Rusya yakın · varsayılan kip | 1608 ms | **1241 ms** |
| Moskova çevresi · varsayılan | 1455 ms | **967 ms** |
| Çin · varsayılan | 1153 ms | 1082 ms |

Yani Rusya'nın 83 öznesi ve Çin'in 31 eyaleti çizilirken bile harita,
bunları hiç çizmeyen 0.6.1'den hızlı. Sayfa 1442 KB'den 1931 KB'ye çıktı
(sıkıştırılmış 585 → 735 KB).

## v0.6.1 — 15 Ağustos 2026

**Ülke kartındaki boşluklar.** 0.6.0'da resmî dil bölümü kartın üç sütunlu
ızgarasına dördüncü öğe olarak girdi; ızgara ikinci satır açtı ve tek rozetlik
bir bölüm koca bir sütun kapladı. Resmî dil zaten ülkenin kimlik bilgisi —
aile ve yazı sistemi satırlarının olduğu ana sütuna, ince bir çizgiyle ayrılmış
olarak taşındı. Kart yeniden üç sütun.

Bunu düzeltirken **0.6.0'dan eski bir boşluk** da kapandı: eylem bağlantıları
("Türkiye'yi bölgelere ayır", "… konuşulan ülkeleri göster") ızgaranın birinci
sütununa sıkışıyor, dolayısıyla en uzun sütunun altını bekliyordu — Türkiye
kartında arada 205 piksel boşluk kalıyordu. Artık son satırda, bütün sütunları
kaplayacak şekilde yan yana duruyorlar. Türkiye kartı 840 pikselden 467'ye indi.

Bir de gereksiz bir kutu kalktı: resmî dili hukuken ilan edilmiş ve evin diliyle
uyuşan ülkelerde artık boş bir rozet satırı çizilmiyor.

## v0.6.0 — 15 Ağustos 2026

**İki yeni harita katmanı.** Harita bugüne kadar tek bir soruyu yanıtlıyordu:
burada evde hangi dil konuşuluyor? Artık üst çubuktaki **Katman** düğmesiyle
aynı ülkelere iki soru daha sorulabiliyor.

**Yazı** — o dil hangi alfabeyle yazılıyor? Aile haritasının söylemediği bir
şey söylüyor: Türkçe, Vietnamca ve Endonezce akraba değil ama üçü de Latin
yazıyor; Sırpça ile Hırvatça karşılıklı anlaşılacak kadar yakın ama biri Kiril
biri Latin. Dokuz gösterge girdisi: Latin (175 ülke), Arap (25), Kiril (10),
Doğu Asya (7), Güneydoğu Asya Brahmi'si (5), diğer alfabeler (5), Güney Asya
Brahmi'si (4), Ge'ez (2), diğer (1).

Yazı verisi elle yazılmadı: dilin kendi dilindeki adının harfleri Unicode
bloklarına göre sayılıyor. 155 dilin hepsi kendiliğinden kapsanıyor, elde
bakım gerektiren bir tablo kalmıyor; yalnız altı istisna elle duruyor.
**İki yazılı 13 dil** ayrıca işaretli — Sırpça, Pencapça, Kazakça, Kürtçe,
Özbekçe, Moğolca… Ülke kartında ikinci yazı ve nedeni yazıyor.

**Resmî dil** — devletin dili ile evin dili aynı mı? Afrika'nın yarısında
değil. Katman açılınca kıta değişiyor: batı ve orta Afrika Fransızcanın
kırmızısına, güney ve doğu İngilizcenin mavisine dönüyor. İngilizce **51**
ülkede resmî ama yalnız 36'sında evin dili; Fransızca 18'de resmî, 13'ünde
evin dili.

**Evin dili resmî dil listesinde hiç olmayan 23 ülke** haritada çapraz
taramayla işaretli: Nijerya (evde Pidgin, resmî İngilizce), Senegal (Volofça /
Fransızca), Sierra Leone (Krio / İngilizce), Güney Sudan (Cuba Arapçası /
İngilizce), Mauritius, Jamaika, Solomon Adaları ve diğerleri. Yeni Zelanda
ters yönde: İngilizce hiç resmî ilan edilmedi, hukuken resmî diller Maorice
(1987) ve Yeni Zelanda İşaret Dili (2006).

Resmî dil tablosu 234 ülkenin tamamını kapsıyor ve **yasal önceliğe** göre
sıralı — günlük kullanıma göre değil. İrlanda'da Anayasa İrlandacayı birinci
resmî dil sayar, günlük dil İngilizcedir; ikisi de listede, sıra anayasanınki.
Hukuken resmî dil ilan etmemiş 16 ülke ayrıca işaretli. 38 ülkede katmanın
anlattığı ayrıntı bir notla açıklanıyor.

**Dil sayısı 142'den 155'e çıktı.** Yalnız resmî dil olarak geçen 13 dil
tabloya eklendi: Peştuca, Afrikaanca, Belarusça, İrlandaca, Maorice,
Tamazight, Fiji Hintçesi, Çamorroca, Xhosa, Ndebele, Romanşça, Hiri Motu,
Latince. Bunların çoğu zaten `lang_mix.py` içinde bir satırdı ama dil
tablosunda karşılığı olmadığı için sessizce düşüyordu — artık konuşan
sayıları da hesaplanıyor. Peştuca tek başına ~90 milyon kişi.

**Görünüm ve bağlantı.** Katman seçimi bağlantıya giriyor (`#k=scr`,
`#k=off`), yani paylaşılan görünüm hangi katmandaysa öyle açılıyor. Ülke
kartında yazı sistemi ve resmî dil satırları her katmanda görünüyor; resmî
dil rozetine basınca o dilin resmî olduğu ülkeler süzülüyor. Telefonda
katman menüsü renk anahtarını da gösteriyor.

Ana dil katmanı **piksel piksel** 0.5.3 ile aynı; yeni katmanlar mevcut
renklerin üstüne biniyor, ikinci bir palet aramasına gerek kalmadı.

## v0.5.3 — 15 Ağustos 2026

**DMG artık gerçek bir Mac'te üretiliyor.** Arka plan resmini iki sürüm
boyunca yerleştiremedim: 0.5.1'de alias kaydını elle kurdum, olmadı; 0.5.2'de
kaydı `mac_alias`'ın Mac'te ürettiği biçime getirip resmi de düz PNG yaptım,
yine olmadı. İkisinde de pencere ölçüsü ve ikon yerleri tutuyordu — yani
`.DS_Store` okunuyordu — ama arka plan gelmiyordu.

Sebebi artık açık: Finder'ın arka planı bulmak için kullandığı alias kaydı
dosyanın gerçek CNID'sini ve birimin gerçek oluşturma tarihini taşıyor. İkisi
de ancak imaj bağlıyken, macOS'un kendi çağrılarıyla üretilebiliyor; Linux'ta
ikisi de uydurma oluyor ve Finder kaydı çözemiyor. Elle daha fazla denemenin
anlamı yok.

Bu yüzden yayımlanan disk imajı artık GitHub'ın **macos koşucusunda**
`dmgbuild` ile üretiliyor: pencereyi, ikon yerlerini ve arka planı macOS'un
kendi kodu yazıyor. İki kazanç daha var:

- İmaj ISO9660 değil **HFS+**. Böylece `bless --openfolder` işe yarıyor:
  imaj takılınca penceresi **kendiliğinden açılıyor**. Bu, ISO9660'ta
  yapılamayan tek şeydi.
- Retina temsili `tiffutil` ile ekleniyor — arka plan hem 1x hem 2x, ve
  bunu üreten Apple'ın kendi aracı.

Depodaki `make desktop` hâlâ Linux'ta çalışıyor ve bir DMG üretiyor; o imaj
süssüz (düz ISO9660). Yayımlanan sürüm Mac'te üretilen.

## v0.5.2 — 15 Ağustos 2026

**Arka plan resmi gerçek Mac'te gelmemişti.** 0.5.1'i denediğimizde pencere
ölçüsü ve ikon yerleri tuttu — yani `.DS_Store` okunuyordu — ama arka plan
siyah kaldı. Sorun, Finder'ın resmi bulmak için kullandığı alias kaydındaydı.
`mac_alias`'ın gerçek bir Mac'te ne yazdığına satır satır bakıp aynısını
kurdum: posix yolu birimin köküne göre ve **başında bölü işaretiyle**
(`/.background/bg.png` — önceki denemede bölü yoktu), carbon yolu kütüphanenin
kendi birleştirme biçiminde. Yanına bir de `pBBk` yer imi yazılıyor: modern
Finder arka planı oradan da okuyabiliyor, hangisi tutarsa.

İkinci şüpheliyi de ortadan kaldırdım: arka plan artık çok temsilli, JPEG
sıkıştırmalı TIFF değil, **düz PNG**. Retina'da bir tık yumuşak duruyor ama
çözülemeyecek bir yanı kalmadı. Netliği, resmin geldiği doğrulandıktan sonra
geri getirmek kolay.

**OKU-BENI.txt DMG'den çıktı.** Pencerede üçüncü bir simge olarak sırıtıyordu
(ve "3 items" diye sayılıyordu). Metin uygulamanın içine taşındı:
`Dunya Dilleri Atlasi.app/Contents/Resources/OKU-BENI.txt`. Kurulum ve ilk
açılış notları ayrıca Releases sayfasında ve README'de duruyor.

**Disk imajı istemeyenler için .zip.** Uygulama zaten `.zip` olarak da
paketleniyordu ama yayımlanmıyordu; artık Releases'te. Açıp uygulamayı
Applications'a sürüklemek yeterli — hiç bağlama adımı yok. İmaj takılınca
penceresinin kendiliğinden açılmasını sağlayamıyorum (o bayrak HFS+ birim
başlığında, bizim imaj ISO9660 ve Linux'ta HFS+ üretecek araç yok; tek aday
olan `machfs` yalnızca Catalina'nın artık bağlamadığı eski HFS'i yazıyor),
bu yüzden bağlama adımından rahatsız olana verilecek gerçek cevap bu.

## v0.5.1 — 15 Ağustos 2026

**DMG artık düzgün bir kurulum penceresi açıyor.** Şimdiye kadar disk imajı
süssüz açılıyordu: ne arka plan vardı, ne ikonların bir yeri. Kullanıcı .app'i
kendisi bulup Applications klasörüne sürüklemek zorundaydı.

macOS'ta bir disk imajının nasıl göründüğü kökteki `.DS_Store` dosyasında
yazılı: pencerenin boyu, görünüm kipi, arka plan resmi ve her ikonun
koordinatı. Normalde bu dosya bir Mac'te Finder'a yazdırılır; Mac olmadığı için
`desktop/dmg_window.py` doğrudan üretiyor. Pencere 768×512, kenar çubuğu ve
araç çubuğu kapalı, uygulama solda, Applications sağda — ikisi de arka plandaki
kesikli çerçevelerin tam ortasında.

Arka plan resmi 1x ve 2x olarak tek TIFF'te; Retina ekranda bulanık görünmesin
diye. JPEG sıkıştırmayla 6,3 MB yerine 1,7 MB.

Bağlanan birim `.VolumeIcon.icns` ile uygulamanın simgesini taşıyor: Finder
kenar çubuğunda ve masaüstünde aranacak bir şey olmaktan çıkıyor.

**Uygulama simgesinde iki hata.** `make_icon.py` `.icns` yazarken parça
uzunluğuna 8 baytlık başlığı katmıyordu; dosya ikinci parçadan sonra
ayrıştırılamıyordu (sekiz boyuttan yalnızca ilki okunabiliyordu). Ayrıca simge
hâlâ 0.3.0 öncesinin soluk paletiyle çiziliyordu — uygulamanın kendi renklerine
geçirildi.

**Yapamadığım şey:** imaj takıldığında penceresinin kendiliğinden açılması.
O ayar HFS+ birim başlığında duruyor, bizim imaj ise ISO9660 ve Linux'ta HFS+
üretecek araç yok. Finder .dmg'ye çift tıklandığında birimi genelde kendisi
açıyor; açmadığı durumda zorlanamıyor.

## v0.5.0 — 15 Ağustos 2026

**Her görünümün artık bir bağlantısı var.** Şimdiye kadar haritada kurduğunuz
hiçbir şey paylaşılamıyordu: bir dili süzüp Anadolu'ya yaklaşsanız bile
karşınızdakine "sen de aynısını yap" demekten başka yol yoktu. Artık ne
gösterildiği adres çubuğunda duruyor —

```
#l=en&p=pct&d=on&f=l.tr&v=489,208,422
```

— arayüz dili, boyama ölçütü (aile / yoğunluk / kişi), ayrıntı düzeyi (ülke /
bölge), süzgeç, seçili ülke ya da il, tablo görünümü ve görüş kutusu. Araç
çubuğuna **Bağlantı** düğmesi eklendi: mevcut görünümün adresini panoya
kopyalıyor. Biçim iki arayüzde de aynı, yani masaüstünde üretilen bir bağlantı
telefon sürümünde de açılıyor.

İki karar bilinçli:

- **Tema bağlantıda yok.** Açık/koyu okuyanın kendi tercihi; linkle
  dayatılmamalı. Dil ise içeriğin bir parçası olduğu için taşınıyor ve kayıtlı
  tercihi eziyor.
- **Yazma geciktiriliyor.** Kaydırırken her karede `history.replaceState`
  çağırmak hem pahalı hem de Safari'nin oran sınırına takılıp hata veriyor;
  hareket durduktan 400 ms sonra bir kez yazılıyor.

Bozuk ya da uydurma bir bağlantı sayfayı kırmıyor: tanınmayan her alan sessizce
yok sayılıyor ve varsayılan görünüm açılıyor.

**Tarayıcı sürümü kurulabilir ve çevrimdışı hâle geldi.** `docs/` kopyalarına
manifest, hizmet çalışanı ve ikon eklendi; Chrome'da "Yükle", iOS'ta "Ana
ekrana ekle" dediğinizde adres çubuğu olmayan bir uygulama gibi açılıyor ve ağ
tamamen kapalıyken de çalışıyor (ölçtüm: sunucu kapalıyken sayfa açılıyor ve
tek istek gitmiyor). Masaüstü ve telefon arayüzleri ayrı manifest kullanıyor,
yoksa telefondan kurulan uygulama masaüstü sayfasını açardı.

Bu yalnızca yayımlanan siteyi ilgilendiriyor: paketlenen sürümler
(`dunya-dilleri.html`, masaüstü uygulaması, APK) dokunulmadan kalıyor — onlar
zaten çevrimdışı ve `file://` üzerinden hizmet çalışanı kaydı anlamsız.

**Sürekli tümleştirme eklendi.** Her itmede ve her PR'da: veri ve sayfalar
sıfırdan derleniyor, **yayımlanan kopyanın şablonlarla uyumlu olduğu**
doğrulanıyor ve iki arayüz Playwright'la denetleniyor. Bu oturumda elle
yakaladığım regresyonların çoğunu son adım yakalardı.

**`build_subs.py` artık kaynak dosyayı gerçekten indiriyor.** README uzun
süredir "ilk çalıştırmada 40 MB'lık Natural Earth dosyasını indirir" diyordu
ama kodda indirme yoktu; dosya elle indirilmişti ve temiz bir kopyada `make`
çalışmıyordu. İndirme sessizce yarıda kesilebildiği için (ilk denemede 40 MB
yerine 35 MB gelip JSON ortasından koptu) hem uzunluk hem de ayrıştırma
doğrulanıyor, tutmazsa yeniden deneniyor.

## v0.4.0 — 10 Ağustos 2026

**Kaydırırken kasma: sebebi bulundu ve ölçüldü.** Bu sorun turlardır tahminle
kovalanıyordu — compositor dönüşümü denendi (yanlıştı, kenarda boşluk
bırakıyordu), canvas düşünüldü (ölçüldü, daha yavaş çıktı), görüş alanı budaması
eklendi (doğruydu ama tek başına yetmedi). Bu kez tahmin edilmedi: Chrome'un iz
kayıtlarından, sabit bir 2 saniyelik kaydırma boyunca harcanan `RasterTask`
süresi ölçüldü. Her tekrar sayfayı baştan yükleyip aynı görüş kutusuna geliyor,
yoksa kaydırmanın bıraktığı yer bir sonraki ölçümü %25 kaydırıyor.

Sonuç net: **zamanın %70–80'i kontur çizmekte.** Dolgular, kreollerin tarama
desenleri, süslemeler ve paralel/meridyen ağı ölçülebilir bir yük getirmiyor —
hepsini düz renge çevirmek hiçbir şeyi değiştirmedi. Konturların hepsini
kapatmak ise dünya görünümünde 2 535 ms'yi 451 ms'ye indiriyor.

Konturun maliyeti iki şeye bağlı çıktı: boyadığı piksel sayısı (kalınlığı
1,2'den 0,5'e düşürmek maliyeti üçte ikisine indiriyor) ve nokta sayısı (20 547
noktayı 7 715'e indirmek %58 kazandırıyor). Buradan üç düzeltme çıktı:

- **Uzakta kaba geometri.** Dünya görünümünde bir harita birimi 0,74 piksel;
  ülke sınırlarının noktalarının çoğu piksel altı ayrıntı. Yakınlık 1,0
  piksel/birimin altındayken sadeleştirilmiş yol (20 547 → 10 417 nokta),
  üstündeyken tam yol kullanılıyor; arada histerezis var. Kaba sürüm açılıştan
  hemen sonra tarayıcıda bir kez hesaplanıyor — **veri dosyasına bir bayt bile
  eklemiyor.**
- **Jest sırasında kenar yumuşatma kapalı.** Telefon arayüzünde zaten vardı,
  masaüstünde yoktu. Hareket hâlindeki haritada fark görünmüyor; ölçümde tek
  başına %20–29 kazandırıyor.
- **Aynı çizgi bir kez konturlanıyor.** Bölge kipinde ülkenin dış çeperi
  eskiden şöyle elde ediliyordu: *tüm* il yolları konturlanıyor, sonra üstleri
  il dolgularıyla örtülüyordu. Yani her iç sınır iki kez çizilip saklanıyordu —
  21 628 noktalık kontur, yalnızca kenarda görünen ince bir çizgi için.
  `build_subs.py` zaten kenarları sayıyordu; artık bir kez geçen kenarları da
  ayrı bir ağ olarak veriyor (`outer`, 12 173 nokta) ve zemin yalnızca dolgu.
  Ayrıca bölge kipinde alt bölgeli ülkelerin ülke konturu çizilmiyor: aynı
  sınırı yeni ağ zaten çiziyor.

Ölçülen sonuç (1440×900, 2 sn kaydırma, rasterizasyon süresi):

| görünüm | eski | yeni |
|---|---|---|
| dünya (ülke kipi) | 2 535 ms | **1 234 ms** (−51%) |
| bölge kipi, 3,6 px/birim | 2 252 ms | **1 539 ms** (−32%) |
| bölge kipi, 8 px/birim | 1 404 ms | **1 212 ms** (−14%) |

**Denenip elenenler de var.** TopoJSON yayları zaten paylaşımlı olduğu için
ülke sınırlarını tekilleştirmek cazip görünüyordu; sayınca kazancın yalnızca
%20 geometri olduğu çıktı (yayların 1 841'inin 1 482'si tek ülkede geçiyor,
yani kıyı — zaten bir kez çiziliyor) ve ölçünce fark %2'de kaldı. Konturu
dolgulu yoldan ayırıp dolgusuz bir ağa taşımak da hiçbir şey kazandırmadı.
İkisi de yapılmadı.

**Yan kazanç: uluslararası sınır artık il sınırından ayırt ediliyor.** 0.3.1'de
bunun düzeltildiği yazılmıştı ama iş yarım kalmıştı — ABD–Kanada sınırı hâlâ
eyalet çizgisiyle aynı görünüyordu. Yeni dış çeper ağı bunu gerçekten çözüyor.

**Budama listesi hatası.** Görüş alanı dışındaki yolları eleyen liste, geometri
düzeyi değişince yeniden kuruluyor. `getBBox` gizli bir öğe için 0×0 döndüğü
için, o sırada ekran dışında olan yollar listeden düşüp bir daha geri
gelmiyordu (dünya görünümüne dönünce 234 ülkenin 19'u kayıp). Liste kurulmadan
önce gizlemeler kaldırılıyor artık.

**Harita klavyeyle geziliyor.** `#map` odaklanabilir oldu; ok tuşları
kaydırıyor (Shift ile büyük adım), `+`/`−` yakınlaştırıyor, `0` dünyaya
döndürüyor. Fare olmadan haritada yakınlaşmanın yolu yoktu.

Telefon arayüzünde küçük ülkelerin görünmez dokunma hedefleri de budama
listesine eklendi.

## v0.3.3 — 7 Ağustos 2026

**Fare tekerleği yakınlaştırmıyordu.** Tekerlek olayı `deltaMode === 0` ile
geliyor ve o dal doğrudan kaydırmaya gidiyordu — yakınlaştırma yalnızca satır
kipinde (Firefox/Windows) çalışıyormuş. Artık jest başına bir kez karar
veriliyor: seyrek, büyük ve tam sayı delta + yatay bileşen yok ise fare
tekerleği (yakınlaştırır), aksi hâlde dokunmatik yüzey (kaydırır). Karar jest
boyunca korunuyor, momentum evresindeki büyük deltalar kipi ortada değiştirmesin
diye. Kıstırma (ctrl + tekerlek) eskisi gibi.

**Görüş alanı dışındaki yollar artık çizilmiyor.** Sınırlayıcı kutular bir kez
hesaplanıyor, her karede yalnızca kutu kesişimi bakılıyor. Ölçtüm: 4 kat
yakınlıkta 616 yolun **582'si** (%94) çizim dışı kalıyor, 17 katta neredeyse
hepsi. Masaüstünde fps'i değiştirmiyor (zaten 60'a dayalı), kazanç dolgu hızına
takılan cihazlarda.

**Yayımlanan sayfanın `<head>`'i eksikti.** `docs/index.html`'e ham şablon
çıktısı kopyalanıyordu: `<!doctype>`, `<meta charset>`, `lang` ve viewport
meta'sı yoktu. GitHub Pages charset'i HTTP başlığında gönderdiği için sorun
görünmüyordu, ama charset göndermeyen bir sunucudan servis edilince Türkçe
karakterler bozulup sayfa çöküyordu (bunu ölçüm yaparken yakaladım) ve telefon
tarayıcısında viewport meta'sı olmadığı için ölçeklenmiyordu. Üç çıktı da artık
aynı tam belge.

## v0.3.2 — 7 Ağustos 2026

**Bir yere tıklayınca çıkan kalın çizgi düzeltildi.** 0.3.1'de iki hata birden
yaptım:

- İl sınırlarını ayrı bir katmana taşırken `.sub` kuralını `stroke: none` ile
  değiştirdim ve **`vector-effect: non-scaling-stroke`'u da düşürdüm**. Bu özellik
  olmadan seçim çizgisinin kalınlığı CSS pikseliyle değil harita birimiyle
  ölçülüyor: yakınlaşınca 2 birimlik çizgi ekranda onlarca piksele çıkıp seçili
  bölgeyi beyaz bir lekeye çeviriyordu. Özellik geri kondu; ölçtüm, çizgi artık
  her yakınlıkta 2 piksel.
- Seçim çizgisini kimse istemeden kalınlaştırmıştım (mobilde 2 → 2,6; masaüstünde
  1,6 → 2,4 ve imleç vurgusunda 1,2 → 1,8). Hepsi eski değerine döndü.

Sınır hiyerarşisinde bir değişiklik yok: ülke sınırı düz koyu, il sınırı koyu
kılıf üstünde beyaz çekirdek.

## v0.3.1 — 7 Ağustos 2026

**Sınır çizgileri okunur hâle geldi.** İl/eyalet sınırı %34 saydam beyaz bir
kıl çizgiydi; parlak dolguların üstünde görünmüyordu. Daha kötüsü, ülke sınırı
ile il sınırı ayırt edilemiyordu: Belçika'nın kuzeyi Hollanda'ya, güneyi
Fransa'ya bağlıymış gibi duruyordu.

Kökeninde bir katman hatası vardı. Ülke konturu diye çizilen şey, illerin
yollarının arka arkaya eklenmiş hâlinin konturuydu — yani ülke sınırını değil
**her il sınırını** çiziyordu, üstelik iller onun üstüne çizildiği için
ABD–Kanada sınırı da eyalet çizgisinden farksız kalıyordu. Kıyılar da bu yüzden
beyaz çerçeveli görünüyordu.

`build_subs.py` artık gerçek iç sınırları ayıklıyor: iki ilde birden geçen
kenarlar iç sınır, bir kez geçenler ülkenin çeperi. Noktalar zaten ızgaraya
oturtulduğu için kenarlar birebir eşleşiyor. Sonuçta:

- **ülke sınırı** — düz koyu çizgi,
- **il/eyalet sınırı** — aynı koyu kılıfın üstünde beyaz çekirdek,
- **kıyı** — temiz, çerçevesiz.

Anlam iki temada da sabit: koyu çizgi her zaman ülke. Ayrıca masaüstünde elle
koyu tema seçildiğinde `--sub-line` tanımsız kalıyordu, açık temanın koyu çizgi
değeri kullanılıyordu; o da düzeldi.

## v0.3.0 — 7 Ağustos 2026

**Renkler canlandı.** Palet aramasında kromayı 0,20'de sınırlamıştım; bu benim
"editoryal görünüm" tercihimdi, ayrım ölçütünün gereği değildi — tersine
doygunluk ayrımı artırıyor. İki şey değişti:

- Arama artık **iki kademeli**: önce ayrım eşiği tutsun, tutuyorsa doygunluğu
  maksimize etsin. Eskiden yalnızca en kötü çift büyütülüyordu, eşiği çoktan
  geçmiş renkler gereksiz yere soluk kalıyordu. Ortalama kroma 0,15 → 0,20.
- **Aydınlık bandı** genişletildi. Asıl darboğaz kroma değil bandmış: L ≤ 0,665
  içinde sRGB gamut'u canlı turuncu ve yeşil vermiyor, kahve ve zeytin veriyor.
  Koyu temada band 0,56–0,76'ya çıktı.

Sonuç ölçülebilir olarak da daha iyi: koyu temada en kötü çift ΔE 8,2 → **9,0**
(renk körlüğü), 15,3 → **17,4** (normal görüş), ve yüzeye karşı kontrast artık
uyarı vermeden geçiyor. Açık temada 11,2 → **9,1** / 20,6 → **17,3**; ikisi de
eşiğin üstünde.

> Not: koyu temada aydınlık bandı, dataviz kılavuzunun ince işaretler için
> önerdiği 0,48–0,67 aralığının üstüne çıkıyor. Bilinçli bir sapma: burada ince
> çizgiler değil, neredeyse siyah bir okyanus üstünde büyük dolgu alanları var;
> dar bantta sekiz canlı renk ayrım eşiğini tutturamıyordu (0,915). Güvenlikle
> ilgili denetimler — renk körlüğü ayrımı, normal görüş tabanı, kontrast —
> hepsi geçiyor.

## v0.2.3 — 7 Ağustos 2026

**Otomatik ülke/bölge geçişi düzeltildi.** Eşik "haritanın kaçta kaçını
görüyorsun" diye yazılmıştı (`W/1.5`), ama bu ekran oranını hesaba katmıyor.
Telefonda en geniş görünüm zaten haritanın çok küçük bir kesri olduğu için
eşiğin altına hiç çıkamıyordu: Android'de **en uzakta bile bölgeler açıktı**,
ilk sürümden beri. Masaüstünde ise 1,5 katlık bir yakınlıkta açılıyordu, yani
çok erken.

Ölçüt artık ekranın kesri değil, **bir harita biriminin kaç piksel ettiği**:
2,5 px/birim'de bölgeler açılıyor, 2,0'ın altına inince kapanıyor (histerezis,
eşiğin başında titremesin diye). Bu ölçü cihazdan bağımsız olduğu için telefonda
ve masaüstünde bölgeler artık aynı *görünür* ölçekte beliriyor — kabaca
Türkiye'nin ekranda ~170 piksel geldiği yakınlık. Masaüstünde eski eşiğin iki
katından fazla geç. Elle **Ülke / Bölge** seçimi her zaman bunu ezer.

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
