**Türkçe** · [English](DATA.en.md)

# Veri: kaynaklar, yöntem ve sınırlar

Bu belge haritadaki her sayının nereden geldiğini, nasıl hesaplandığını ve nerede
zayıf olduğunu anlatır. Rakamların hepsi **yaklaşıktır**; büyüklük mertebesi
olarak okunmalı, ondalık hassasiyetle değil.

## Katmanlar

| Katman | Dosya | Kapsam | Ne anlatır |
|---|---|---|---|
| Çoğunluk dili | `build_data.py` içindeki `C` | 234/234 | Ülkede nüfusun en büyük bölümünün günlük hayatta konuştuğu dil |
| Evde konuşulan diller | `lang_mix.py` (`MIX`) | 234/234 | Ana dil paylarının dağılımı |
| Göçmen/azınlık kuyruğu | `diaspora.py` | 56 ülke, 440 satır | %1'in altında kalan topluluklar, %0,05'e kadar |
| İkinci dil | `lang_mix.py` (`L2`) | 189/234 | Ana dili olmadığı hâlde sohbet edecek düzeyde konuşulan diller |
| Nüfus | `population.py` | 234/234 | BM 2024 tahmini, bin kişi |
| Eyalet / il | `subdiv.py` | 313 bölge, 12 ülke | Bölge bazında dil dağılımı ve nüfus |
| Yazı sistemi | `layers.py` (`SCRIPT_FIX`, `SCRIPT2`) | 155/155 dil | Dilin hangi alfabeyle yazıldığı; iki yazılı dillerde ikincisi |
| Resmî dil | `layers.py` (`OFFICIAL`, `DE_FACTO`) | 234/234 | Devletin hukuken resmî dilleri; ilan edilmemişse fiilî olan |

## Kaynaklar

**Sınırlar** — [Natural Earth](https://www.naturalearthdata.com/): ülkeler için
1:50m, alt bölgeler için 1:10m. Kamu malı. Sınırlar hiçbir egemenlik iddiasını
yansıtmaz; Kosova, Kuzey Kıbrıs ve Somaliland ayrı gösterilir çünkü dil
dağılımları çevrelerinden farklıdır.

**Nüfus** — BM Nüfus Bölümü, *World Population Prospects 2024*. Bağımlı bölgeler
için ulusal istatistik kurumları.

**Dil payları** — ulusal nüfus sayımlarının dil soruları (Kanada, ABD ACS,
İsviçre yapısal anketi, Hindistan 2011, Avustralya, Yeni Zelanda, Ukrayna 2001,
Bolivya 2012 ve diğerleri), Ethnologue ve resmî dil politikaları derlenerek
yuvarlandı.

**İkinci dil** — Avrupa'da Eurobarometre 386 (2012), "bir sohbeti sürdürecek
düzeyde" ölçütü. Diğer bölgelerde ulusal sayım ve tahminler.

**Yazı sistemi** elle yazılmadı: dilin kendi dilindeki adının (endonim) harfleri
Unicode bloklarına göre sayılıyor, en çok geçen blok yazı sistemi kabul ediliyor.
Böylece 155 dilin hepsi kendiliğinden kapsanıyor ve elde bakım gerektiren bir
tablo kalmıyor. Yalnız altı istisna elle yazıldı (`SCRIPT_FIX`): Japoncanın
endonimi salt kanji görünür ama yazı kanji + hiragana + katakana'dır; Konkani'nin
resmî yazısı Goa'da Devanagari'dir; Çince ve Kantonca "CJK" bloğundan gelir;
Meitei ve İnuktitut'un Unicode blok adları yazı adına birebir çevrilmez.

**İki yazılı diller** (`SCRIPT2`) ayrı bir tablodur — 13 dil. Sırpçanın resmî
yazısı Kiril'dir ama Latin de her yerde kullanılır; Pencapça Hindistan'da
Gurmukhi, Pakistan'da Şahmukhi ile yazılır; Kazakça 2023–2031 arasında Latin'e
geçmektedir. Harita ana yazıyı boyar, ikincisi ülke kartında yazar.

**Resmî diller** ülkelerin anayasa ve dil yasalarından derlendi; sıralama
**yasal önceliğe** göredir, günlük kullanıma göre değil. İrlanda'da Anayasa
İrlandacayı "birinci resmî dil" sayar, günlük hayatın dili İngilizcedir — ikisi
de listede, sıralama anayasanınki. Hukuken resmî dil ilan etmemiş 16 ülke
(ABD hariç: 2025 kararnamesi) `DE_FACTO` tablosunda fiilî devlet diliyle durur
ve kartta "hukuken resmî dil yok" diye işaretlenir.

## Hesaplamalar

**Konuşan sayısı** = ülke (veya bölge) nüfusu × o dilin payı, tüm ülkeler
toplanarak. Yani "İspanyolca 503 milyon" demek, İspanyolca'nın ana dil payıyla
her ülkenin nüfusunun çarpımının toplamı demektir.

**Bir dilin toplamı** ana dil ve ikinci dil olarak ayrı tutulur. İngilizce'de
ana dil ≈ 418 milyon, ikinci dil ≈ 1,36 milyar; "Toplam" sıralaması ikisini
toplar (≈ 1,8 milyar).

**Yüzdeler %100'ü aşabilir.** Çok dilli ülkelerde pek çok kişi evde birden fazla
dil konuşur; İsviçre'nin yapısal anketi gibi kaynaklar çoklu yanıta izin verir.

## Bilinen sınırlar

**Ölçütler ülkeden ülkeye değişir.** Bir sayım "ana diliniz nedir" diye sorar,
diğeri "evde hangi dili konuşuyorsunuz". İkisi aynı şey değildir ve rakamlar
buna göre kayar. Ülkeler arası karşılaştırmalarda bunu hesaba katın.

**Köken ≠ dil.** Diaspora rakamları dili *evde konuşanları* sayar, o kökenden
gelen herkesi değil. Belçika'da Türk kökenli nüfus ~220 bin ama Türkçe'yi evde
konuşan ~150 bin; fark ikinci ve üçüncü kuşaktaki dil kaybından.

**Türkiye il rakamları tahmindir.** Türkiye'de resmî dil sayımı yapılmıyor; il
düzeyindeki Kürtçe, Zazaca ve Arapça payları anket temelli (KONDA benzeri)
çalışmalardan türetilmiş yaklaşık değerlerdir.

**Diaspora kapsamı eşitsiz.** Göçmen topluluk kuyruğu başlıca göç alan 56 ülke
için doldurulmuştur; her ülkedeki her küçük topluluk listelenmiş değildir.
Eksik gördüğünüz bir topluluk varsa `diaspora.py` içine eklenebilir.

**Şehir düzeyi veri yok.** Belediye bazında dil istatistiği çoğu ülkede
yayımlanmaz. İsveç örneğin belediye başına *doğum ülkesi* yayımlar, konuşulan
dili değil — bu farklı bir ölçüdür ve dil verisi gibi sunulması yanıltıcı olur.
Bu yüzden en ince ayrıntı düzeyi il/eyalet/kantonda bırakıldı.

**Savaş ve göç hareketleri hızlı eskir.** 2022 sonrası Ukrayna göçü Polonya,
Çekya, Almanya ve Baltık ülkelerinin rakamlarına yansıtıldı; bu sayılar
diğerlerinden daha oynaktır.

**"Dil" ile "lehçe" arasındaki çizgi tartışmalıdır.** Arapça tek satırda
toplanmıştır, oysa Fas ve Irak konuşmaları karşılıklı anlaşılır değildir. Çince
Mandarin ve Kantonca olarak ayrılmıştır ama Vu ve Min ayrı satırlarda durur.
Sırp-Hırvatça bazı ülkelerde tek, bazılarında ayrı sayılır. Bunlar veri
hatası değil, sınıflandırma tercihidir.

**Dil aileleri renk için gruplanmıştır.** Haritada sekiz aile rengi ve bir
"diğer" var; daha fazlası güvenilir biçimde ayırt edilemiyor (README'deki palet
notuna bakın). "Doğu ve Güney Asya dilleri" bu yüzden *coğrafi* bir gruptur —
Çin-Tibet, Japon, Kore, Dravit, Avustroasyatik ve Tai-Kadai ayrı ailelerdir ve
etiket aksini iddia etmez. Her dilin gerçek ailesi kendi satırında ve ipucunda
yazılıdır.

## Katkı

Bir rakamın yanlış olduğunu düşünüyorsanız, kaynağıyla birlikte bir issue açın.
Veri dosyaları düz Python sözlükleridir, düzenlemesi kolaydır:

- `lang_mix.py` — ülke başına ana dil ve ikinci dil dağılımı
- `diaspora.py` — küçük topluluklar
- `population.py` — nüfuslar
- `subdiv.py` — eyalet/il dağılımları
- `build_data.py` içindeki `L` ve `C` — dil listesi ve ülke başına çoğunluk dili

Değişiklikten sonra `make` yeterlidir; `build_data.py` tanımsız ülke veya dil
bulursa hata verip durur.
