# Sürüm geçmişi

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
