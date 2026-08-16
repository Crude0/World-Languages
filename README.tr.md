**Türkçe** · [English](README.md)

# Dünya Dilleri Atlası

Dünyadaki 234 ülke ve bölgede hangi dilin konuşulduğunu gösteren, dile göre
süzülebilen etkileşimli harita. Tamamen çevrimdışı çalışır: tek dosyalık bir web
sayfası, masaüstü uygulaması (macOS · Windows) ve Android uygulaması olarak
paketlenir. Hiçbir ağ isteği yapmaz, hiçbir izin istemez.

**[▶ Tarayıcıda aç](https://crude0.github.io/World-Languages/)** ·
[📱 Telefon sürümü](https://crude0.github.io/World-Languages/mobile.html) ·
[⬇ İndirilebilir uygulamalar](#i̇ndir)

Arayüz **Türkçe ve İngilizce**; tema **otomatik, açık veya koyu** seçilebilir.

![Dünya haritası](docs/img/desktop-world.png)

---

## Ne gösteriyor?

| | |
|---|---|
| **234** | ülke ve bağımlı bölge |
| **270** | dil (121'i bir ülkede çoğunluk, 136'sı yalnızca bölge düzeyinde, 13'ü yalnız resmî) |
| **1.100+** | ülke × dil satırı — her ülkede evde konuşulan dillerin dağılımı |
| **507** | eyalet / il / kanton (18 ülkede) |
| **30** | yazı sistemi, dillerin kendi adlarından çıkarıldı |
| **8,09 milyar** | kapsanan nüfus |

Harita dört soruya cevap verir:

1. **Bu ülkede çoğunluk hangi dili konuşuyor?** Renkler dil ailesini gösterir.
2. **Geri kalanı ne konuşuyor?** Her ülkenin evde konuşulan dil dağılımı, %0,05'e
   kadar inen bir kuyrukla — Belçika'daki Türkçe (%1,3) ya da Almanya'daki
   Ukraynaca (%1,4) gibi topluluklar dâhil.
3. **Bu dil başka nerede konuşuluyor?** Bir dil seçince çoğunluk olduğu ülkeler
   koyu, azınlık olarak konuşulduğu ülkeler soluk renkle işaretlenir. Türkçe
   26 ülkede görünür.
4. **Kaç kişi konuşuyor?** Ülke nüfusu × dil payı ile hesaplanan konuşan sayıları;
   ana dil ve ikinci dil ayrı ayrı.

![Türkçe diasporası](docs/img/desktop-diaspora.png)

### Yoğunluk haritası

Bir dil seçiliyken renklendirmeyi **yoğunluğa** (nüfustaki pay) veya **kişi
sayısına** çevirebilirsiniz. İngilizce'de İrlanda ve Birleşik Krallık en koyu
tonda (>%85), ABD ve Avustralya bir kademe açık, Almanya ve İsveç en açık
kademede görünür.

![Yoğunluk haritası](docs/img/desktop-density.png)

### İki katman daha

Haritanın üstündeki **Görünüm** yaprağındaki **Katman** seçenekleri aynı
ülkelere iki soru daha soruyor.

**Yazı** — o dil hangi alfabeyle yazılıyor? Aile haritasının söylemediği bir şey
söylüyor: Türkçe, Vietnamca ve Endonezce akraba değil ama üçü de Latin yazıyor;
Sırpça ile Hırvatça karşılıklı anlaşılacak kadar yakın ama biri Kiril biri
Latin. Latin 175 ülkeyi, Arap yazısı 25'ini, Kiril 10'unu kapsıyor.

Yazı verisi elle yazılmadı: dilin kendi dilindeki adının harfleri Unicode
bloklarına göre sayılıyor. 155 dilin hepsi kendiliğinden kapsanıyor ve elde
bakım gerektiren bir tablo kalmıyor — yalnız altı istisna elle duruyor. **İki**
yazıyla yazılan 13 dil ayrıca işaretli: Pencapça Hindistan'da Gurmukhi,
Pakistan'da Şahmukhi; Kazakça 2023–2031 arasında Latin'e geçiyor; Kürtçe
Türkiye'de Latin, Irak'ta Arap yazısı.

![Yazı sistemleri](docs/img/desktop-scripts.png)

**Resmî dil** — devletin dili ile evin dili aynı mı? Afrika'nın yarısında değil.
Katman açılınca kıta değişiyor: batı ve orta Afrika Fransızcanın kırmızısına,
güney ve doğu İngilizcenin mavisine dönüyor. İngilizce **51** ülkede resmî ama
yalnız 36'sında evin dili; Fransızca 18'de resmî, 13'ünde evin dili.

**Evin dili resmî dil listesinde hiç olmayan 23 ülke** çapraz taramayla
işaretli: Nijerya (evde Pidgin, resmî İngilizce), Senegal (Volofça / Fransızca),
Sierra Leone (Krio / İngilizce), Güney Sudan (Cuba Arapçası / İngilizce),
Mauritius, Jamaika, Solomon Adaları ve diğerleri. Yeni Zelanda ters yönde:
İngilizce hiç resmî ilan edilmedi, hukuken resmî diller Maorice (1987) ve Yeni
Zelanda İşaret Dili (2006).

Tablo 234 ülkenin tamamını kapsıyor ve **yasal önceliğe** göre sıralı, günlük
kullanıma göre değil — İrlanda'da Anayasa İrlandacayı birinci resmî dil sayar,
günlük dil İngilizcedir; ikisi de bu sırayla listede. Hukuken resmî dil ilan
etmemiş 16 ülke ayrıca işaretli, 48 ülkede katmanın anlattığı ayrıntı bir notla
açıklanıyor.

![Resmî diller](docs/img/desktop-official.png)

### Eyalet / il düzeyi

18 ülkede harita il, eyalet ya da kanton düzeyine iner: Rusya, Çin, ABD,
Kanada, Hindistan, Nijerya, Güney Afrika, Fransa, Almanya, İspanya, İtalya,
Birleşik Krallık, Ukrayna, Türkiye, İsviçre, Belçika, Finlandiya, Bolivya.
Brezilya bilerek dışarıda: 27 eyaletin hepsinde Portekizce ~%98, yani
geometrisinin karşılığı tek renkli bir yüzey olurdu. Uzaktayken ülke,
yaklaşınca bölge görünür (Paradox oyunlarındaki gibi), ya da elle sabitlenebilir.

Québec'te Fransızca %78 ile British Columbia'da %1,1; Türkiye'nin güneydoğusunda
Kürtçe %82 ile batısında %3; Ukrayna'nın doğusunda Rusça %70 ile batısında %1 —
ülke ortalamasının sakladığı farklar.

**Rusya'nın 83 federal öznesi** en büyük ekleme. Federasyonda 30'dan fazla dil
cumhuriyet düzeyinde resmî ama harita bugüne kadar ülkeyi tek renk çiziyordu.
Artık Tataristan Tatarca, Çuvaşistan Çuvaşça, Saha Sahaca, Tuva Tuvaca ile Türk
dilleri renginde; Çeçenistan, İnguşetya, Dağıstan ve Kabardey-Balkar kendi
Kafkas dilleriyle ayrı duruyor.

**Çin'in 31 eyaleti** "Çince"yi gerçekte olduğu şeye ayırıyor: Mandarin,
Kantonca, Wu, Min, Hakka, Xiang ve Gan karşılıklı anlaşılmaz. Şanghay ve
Zhejiang Wu, Fujian ve Hainan Min, Jiangxi Gan, Hunan Xiang, Guangdong
Kantonca; yanında Sincan'da Uygurca, Tibet'te Tibetçe, İç Moğolistan'da
Moğolca, Guangxi'de Zhuangca.

**Nijerya'nın 37 eyaleti** ülke ortalamasının gösteremediğini gösteriyor:
ülkenin çoğunluk dili yok, asıl örüntü kuzeyde Hausa, güneybatıda Yorubaca,
güneydoğuda İgboca ve Nijer Deltası'nda bir Nijerya Pidgini kuşağı.
**Güney Afrika'nın 9 ili** Census 2022'den geliyor; 12 resmî dilin hiçbiri
ülke genelinde çoğunluk değil. **Fransa** Korsikaca, Bretonca, Oksitanca ve
denizaşırı kreolleri ekliyor; **Almanya'nın 16 eyaleti** ise hanede konuşulan
dili ilk kez soran 2022 sayımından.

![Bölge düzeyi](docs/img/desktop-regions.png)

![Rusya'nın federal özneleri](docs/img/desktop-russia.png)

### İki yeri karşılaştırma

Bir ülke seçip **"… ile karşılaştır"** düğmesine basıyorsunuz; ikinci bir yer
seçilince kart iki sütuna dönüyor ve iki dağılım yan yana geliyor. Altta
**iki yerde de konuşulan diller** listeleniyor, her biri iki paydan küçüğüyle —
yani o dille kaç kişiyle anlaşılabileceğinin alt sınırıyla. Ülkeler kadar
bölgeler de karşılaştırılabiliyor: Tataristan ile Çuvaşistan, Québec ile Ontario.

### Bildiğim dillerle dünya

Dördüncü bir katman: **Bildiğim**. Listeden bildiğiniz dilleri seçiyorsunuz,
harita her ülkeyi o dillerden en az birini konuşan nüfusun payıyla boyuyor —
ana dil ya da ikinci dil olarak. Türkçe ile İngilizce ≈1,81 milyar kişi ediyor.
Seçim tarayıcıda saklanıyor ve bağlantıya giriyor (`#k=know&kn=tr.en`).

Katmanın iki okuma biçimi var. **Pay** yukarıdaki gibi. **Ana dil** ise yalnız
seçtiğiniz dillerden birinin *evde konuşulan çoğunluk dili* olduğu ülkeleri
yakıyor — her biri kendi ailesinin renginde, öbürleri sönük. Türkçe + İngilizce
= 38 ülke, ≈538 milyon kişi. "Nerede anlaşırım" ile "nerede benim dilim
konuşulur" ayrı sorular.

Pay kipinde paylar toplanıp %100'de kırpılıyor: iki dili birden bilenler iki kez
sayıldığı için rakam bir üst sınır — panelde de böyle yazıyor.

Bir ülkenin üstünde durunca halkın yüzde kaçıyla anlaşabileceğiniz, kaç kişiye
denk geldiği ve bu paya en çok katkı veren üç dil yazıyor. Ölçek kırmızıdan
yeşile gidiyor; komşu kutuların en küçük farkı üç renk körlüğü türünde de
ΔE 9,5 (CIEDE2000).

![Bildiğim dillerle dünya](docs/img/desktop-know.png)

### Görünümü indirme

**Paylaş** yaprağındaki **PNG** ve **SVG** düğmeleri o anki görünümü — yakınlık, katman, süzgeç, seçim —
tek dosya olarak indiriyor. SVG tek başına duruyor: sayfanın stil sayfasından
yalnız haritayı ilgilendiren kurallar kopyalanıyor, budanmış yollar hiç
yazılmıyor. Dosya adı görünümden türetiliyor. Telefonda ikisi de katman
menüsünde.

### Denetimler ve tam ekran

Harita kipleri başlık şeridini doldurmuyor: haritanın üstünde yüzen üç düğmelik
bir cam çubuk var — **Görünüm**, **Tablo**, **Paylaş**. Katman, renk ve ayrıntı
seçenekleri Görünüm yaprağında gruplanmış, her grubun ne yaptığını anlatan birer
satırla. Karşı köşede yakınlaştırma yığını, altında paneli diğer yana alan
düğme (⇄) ve tam ekran (⛶).

**Tam ekran** haritayı görünümün tamamına açıyor; sayfa, kenar çubuğu ve kartlar
kalkıyor, denetimler haritanın üstünde kalıyor. Fullscreen API varsa gerçek tam
ekrana geçiliyor, yoksa sabit konumlu bir kaplamaya düşülüyor. macOS
uygulamasında Görünüm menüsünde **Yalnız Harita (⇧⌘F)** olarak da var.

Yüzen yüzeyler buzlu cam. `backdrop-filter` desteklenmiyorsa ya da işletim
sistemi ayarında saydamlık kapalıysa düz panel rengine düşüyor: okunurluk
camdan önce geliyor.

![Tam ekran harita](docs/img/desktop-fullscreen.png)

### Renkler

Lejantta dokuz satır var: sekiz dil ailesi rengi ve nötr bir "diğer". Palet elle
seçilmedi — sekiz ton OKLCH uzayında arandı ve renk körlüğü benzetimiyle
(Machado 2009; protanopi / döteranopi / tritanopi) doğrulandı; yalnızca komşular
değil **bütün çiftler** ayrılıyor; eşiği geçen paletler arasından da en doygun
olanı seçiliyor. En kötü çift: açık temada ΔE 9,1, koyuda 9,0 (normal görüşte
17,3 / 17,4).

Kreol diller kendi rengini almıyor: sözcük dağarcığını aldıkları kaynak dilin
renginde, üstünde çapraz taramayla çiziliyorlar. Böylece Haiti Kreolü taramalı
Roman kırmızısı, Nijerya Pidgini taramalı Cermen mavisi oluyor — renk dokuzuncu
bir ton olmak yerine fazladan bir bilgi taşıyor.

### İki dil, üç tema

Arayüz dili Türkçe ve İngilizce arasında geçiş yapar — yalnızca menüler değil,
270 dilin adı, 55 aile etiketi, 352 dağılım satırındaki dil adları, 137 ülke
notu, kıtalar ve sayı biçimi de çevrilir (1,2 milyar ↔ 1.2 billion). Tema
sistemi izler ama elle açık/koyu da seçilebilir; seçim tarayıcıda saklanır.
Bu depo da iki dilde: bu sayfanın İngilizcesi [README.md](README.md).

![İngilizce, koyu tema](docs/img/desktop-english-dark.png)

### Telefon sürümü

Android uygulaması masaüstü sayfasının küçültülmüş hâli değil; telefon için
ayrı yazılmış bir arayüz: tam ekran harita, üstünde yüzen cam katmanlar, alttan
çekilen üç duraklı panel, dokunmatik yüzey jestleri ve sistem yazı tipi.

<p>
  <img src="docs/img/mobile-home.png" width="230" alt="Ana ekran">
  <img src="docs/img/mobile-settings.png" width="230" alt="Görünüm menüsü">
  <img src="docs/img/mobile-detail.png" width="230" alt="Ülke kartı">
</p>

---

## İndir

En güncel sürüm **v0.9.2** — [Releases sayfasından indirin](https://github.com/Crude0/World-Languages/releases/latest), değişiklikler [CHANGELOG.md](CHANGELOG.md) içinde.

| Platform | Dosya | Boyut | Not |
|---|---|---|---|
| Android 7+ | [`Dunya-Dilleri-Atlasi.apk`](dist/Dunya-Dilleri-Atlasi.apk) | 665 KB | İnternet izni yok |
| macOS 10.15+ | [`Dunya-Dilleri-Atlasi.dmg`](dist/Dunya-Dilleri-Atlasi.dmg) | 8,7 MB | Evrensel (Intel + Apple Silicon) |
| macOS, disk imajsız | [`Dunya-Dilleri-Atlasi-mac.zip`](dist/Dunya-Dilleri-Atlasi-mac.zip) | 3,5 MB | Açıp uygulamayı sürükleyin |
| Windows 10+ | [`Dunya Dilleri Atlasi.exe`](dist/Dunya%20Dilleri%20Atlasi.exe) | 4,9 MB | Tek dosya, kurulum yok |
| Tarayıcı | [`docs/index.html`](docs/index.html) | 1,9 MB | Tek dosya, çift tıkla aç |

Tarayıcı sürümü **kurulabilir**: Chrome ya da Safari'de açıp "Yükle" /
"Ana ekrana ekle" dediğinizde uygulama gibi, çevrimdışı, adres çubuğu olmadan
çalışır. Kurduğunuz her görünümün — bir dil, bir ülke, bir yakınlık — kendi
bağlantısı var: **Bağlantı** düğmesine basıp paylaşabilirsiniz.

Uygulamalar imzalı değil (Apple/Microsoft geliştirici sertifikası yok):

- **macOS**: ilk açılışta uygulamaya sağ tıklayın → **Aç** → çıkan pencerede yine **Aç**.
  Ya da: `xattr -dr com.apple.quarantine "/Applications/Dunya Dilleri Atlasi.app"`
- **Windows**: SmartScreen uyarısında **Ek bilgi** → **Yine de çalıştır**.
- **Android**: bilinmeyen kaynaklardan kuruluma izin vermeniz gerekir.

Masaüstü uygulamaları işletim sisteminin kendi tarayıcı motorunu kullanır
(macOS'ta WKWebView, Windows'ta WebView2) — kendi pencerelerinde açılırlar,
tarayıcı gerekmez. Motor bulunamazsa kurulu bir tarayıcıyı adres çubuğu olmayan
uygulama kipinde açan bir yedek yol vardır.

---

## Veri

Rakamların nereden geldiği, nasıl hesaplandığı ve nerede zayıf olduğu
**[DATA.md](DATA.md)** dosyasında ayrıntılı yazıyor. Özetle:

- **Sınırlar**: [Natural Earth](https://www.naturalearthdata.com/) 1:50m (ülkeler)
  ve 1:10m (alt bölgeler), kamu malı.
- **Nüfus**: BM Nüfus Bölümü, 2024 tahminleri.
- **Dil payları**: ulusal nüfus sayımlarının dil soruları, Ethnologue ve resmî
  dil politikaları derlenerek yuvarlandı.
- **İkinci dil**: Avrupa'da Eurobarometre 386 (2012) "sohbet edecek düzeyde"
  ölçütü, diğer bölgelerde ulusal tahminler.

Bunlar yaklaşık değerlerdir ve ülkeler arası karşılaştırmalarda dikkat ister:
bir ülkenin sayımı "ana dil", diğerininki "evde konuşulan dil" sorar. Türkiye'de
resmî dil sayımı olmadığı için il rakamları anket temelli tahmindir.

**Şehir düzeyi veri yoktur** — belediye bazında dil istatistiği çoğu ülkede
yayımlanmıyor (örneğin İsveç belediye başına doğum ülkesi verir, konuşulan dili
değil). Uydurmak yerine boş bırakıldı.

---

## Derleme

Gereksinimler: Python 3.9+, Node 18+ (yalnızca doğrulama için), Go 1.21+
(masaüstü), Android SDK build-tools 34 + JDK 17+ (Android).

```bash
make            # veri + web sayfası (tarayıcıda açılabilir tek dosya)
make desktop    # macOS .dmg + .app, Windows .exe
make android    # imzalı APK
make check      # Playwright ile arayüz denetimi
```

Boru hattı:

```
countries-50m.json ──► build_map.py  ──► map_paths.json  ┐
ne_10m_admin_1…    ──► build_subs.py ──► sub_paths.json  ├─► build_data.py ──► data.json
lang_mix / diaspora / population / subdiv ───────────────┘                        │
                                                    page.tmpl.html   ◄────────────┤
                                                    mobile.tmpl.html ◄────────────┘
```

`build_subs.py` ilk çalıştırmada Natural Earth'ün 40 MB'lık alt bölge dosyasını
indirir (depoda tutulmuyor).

### Dosya düzeni

```
build_map.py        ülke sınırları → projeksiyonlu SVG yolları
build_subs.py       eyalet/il sınırları; topoloji koruyan sadeleştirme
build_data.py       tüm katmanları birleştirir, konuşan sayılarını hesaplar
build_page.py       masaüstü sayfası (gömülü fontlarla tek dosya)
build_mobile.py     telefon arayüzü (sistem fontları)
pwa.py              docs/ için manifest, hizmet çalışanı ve ikon bağlama
anchor.py           etiket çapaları (erişilmezlik kutbu)
VERSION             paketlerdeki sürüm numarasının tek kaynağı
page.tmpl.html      masaüstü arayüzü
mobile.tmpl.html    telefon arayüzü
layers.py           yazı sistemleri ve resmî diller (iki ek katman)
lang_mix.py         ülke başına dil dağılımı
diaspora.py         göçmen ve azınlık toplulukları (%0,05'e kadar)
population.py       ülke nüfusları
subdiv.py           eyalet/il dil dağılımları ve nüfusları
i18n.py             İngilizce dil adları, aile etiketleri, ülke notları
desktop/            Go başlatıcı + paketleme (WKWebView / WebView2)
android/            WebView kabuğu + APK derleme betiği
tools/              Playwright doğrulama betikleri
```

---

## Teknik notlar

Projede ilginç çıkan birkaç ayrıntı:

- **Projeksiyon** Natural Earth (Šavrič polinomu), Python'da elle uygulandı;
  harita dışa bağımlılığı olmayan düz SVG yolları olarak gömülü.
- **Topoloji koruyan sadeleştirme**: komşu illeri tek tek sadeleştirmek ortak
  sınırda farklı noktalar seçtirip aralarında kılcal boşluk bırakıyordu. TopoJSON'un
  kuralıyla (bir noktanın komşu çifti değişiyorsa orası yay başlangıcıdır) halkalar
  yaylara bölünüp her ortak yay bir kez sadeleştiriliyor.
- **Renk paleti** dil ailelerine göre; renk körlüğü benzetimiyle tüm çiftlerin
  ayırt edilebilirliği doğrulandı, yedinci grup ayrıca taramayla işaretlendi.
- **Etiket çapaları** merkez noktası değil, en büyük halkanın erişilmezlik
  kutbu. Köşe ortalaması içbükey kıyılarda denize düşüyordu: Norveç'in adı
  denizde, Hırvatistan'ınki Bosna'nın üstünde kalıyordu. 234 çapanın 228'i artık
  kesin olarak ülkenin içinde; kalan altısı piksel boyutunda (Vatikan, Monako,
  Macao…) ve zaten iğneyle çiziliyorlar.
- **Palet seçilmedi, hesaplandı.** OKLCH uzayında renk körlüğü modeliyle tavlama
  benzetimi, ardından tüm-çiftler eşiğine karşı denetim. On renk koyu temanın dar
  aydınlık bandında eşiği geçemedi — kreollerin kendi rengi yerine doku
  taşımasının sebebi bu.
- **Kaydırmadaki kasmanın sebebi konturmuş, dolgu değil.** Uzun süre tahminle
  kovalandı; sonunda Chrome'un iz kayıtlarından rasterizasyon süresi ölçüldü.
  Zamanın %70–80'i konturlarda: dolgular, tarama desenleri ve süslemeler
  ölçülebilir bir yük getirmiyor. Üç şey yapıldı — uzakta ülke sınırları kaba
  geometriyle çiziliyor (tarayıcıda açılışta hesaplanıyor, dosyaya bir bayt
  eklemiyor), jest sırasında kenar yumuşatma kapanıyor, ve bölge kipinde aynı
  çizgi birden çok kez konturlanmıyor. Rasterizasyon dünya görünümünde yarıya
  indi.
- **180. meridyen**: Rusya ve Fiji'nin halkaları kenardan kesilip ayrı parçalara
  bölünüyor, yoksa harita boyunca yatay bir şerit oluşuyor.
- **macOS'ta ISO9660 tuzağı**: DMG içindeki Türkçe karakterli dosya adları
  açılamıyordu (cd9660 sürücüsü Unicode normalizasyonu yapmıyor). Dosya adları
  ASCII, görünen ad ise yerelleştirilmiş `InfoPlist.strings` ile veriliyor.
- **Windows'ta DPI**: uygulama kendini DPI farkında ilan etmezse 2K/4K ekranda
  1080p'de çizilip büyütülüyor ve bulanık görünüyordu.

---

## Lisans

Kod [MIT](LICENSE) ile. Harita sınırları Natural Earth'ten gelir ve kamu malıdır.
Dil ve nüfus verileri kamuya açık kaynaklardan derlenmiştir; kaynak listesi
[DATA.md](DATA.md) içinde.
