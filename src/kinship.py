#!/usr/bin/env python3
"""Karşılıklı anlaşılırlık — "kimlerle anlaşabilirsin" sorusunun eksik yarısı.

Harita bu soruyu dilin adı birebir eşleşiyor mu diye cevaplıyordu. Bunun
sonucu şuydu: Türkçe seçen biri Azerbaycan'da %0 görüyordu. Azerbaycan'ın
verisi eksik değil — nüfusun %92'si Azerbaycanca konuşuyor, kayıtlı — ama
model iki dili birbirine tamamen yabancı sayıyordu. Aynı hata Çekçe/Slovakça,
Hintçe/Urduca, Sırpça/Hırvatça, Danca/Norveççe, Endonezce/Malayca,
Farsça/Darice ve bir düzine başka çiftte de var.

Buradaki sayı, A'yı bilen birinin B konuşulan bir yerde ne kadar
anlaşabildiğinin kaba oranı. Ölçüt kelime örtüşmesi değil, "hazırlıksız
karşılıklı konuşma" — dilbilim yayınlarında bildirilen karşılıklı
anlaşılırlık ölçümlerinin ALT ucundan alındı, çünkü fazla iyimser bir sayı
haritayı yine yanlış yapar, sadece diğer yöne.

Yön önemli: anlaşılırlık her zaman simetrik değildir. Portekizce bilen bir
kişi İspanyolcayı, İspanyolca bilenin Portekizceyi anladığından daha iyi
anlar (yazı örtüşüyor, ses örtüşmüyor). Danca/İsveççe de böyle. Tablo bu
yüzden yönlü: (bilen, karşılaşılan, oran).

Karşılıklı olduğu yerlerde iki satır yazılıyor; ÇİFT listesi ikisini de
üretiyor, TEK listesi yalnız yazıldığı yönü.
"""

# Simetrik kabul edilenler: (a, b, oran) -> hem a→b hem b→a
CIFT = [
    # --- Türk dilleri ---------------------------------------------------
    # Oğuz kolu içinde (tr/az/tk) konuşma düzeyinde yüksek; Kıpçak (kk/ky)
    # ve Karluk (uz) kollarına geçince ortak sözcük kalsa da anlaşma zor.
    ("tr", "az", .75), ("tr", "tk", .55), ("az", "tk", .60),
    ("kk", "ky", .85), ("kk", "uz", .45), ("ky", "uz", .45),
    ("tr", "kk", .25), ("tr", "uz", .25), ("tr", "ky", .25),
    ("az", "kk", .25), ("az", "uz", .25),
    ("tr", "tt", .30), ("tt", "ba", .85), ("kk", "tt", .55),
    ("uz", "ug", .70),

    # --- Güney Slav -----------------------------------------------------
    # Sırpça/Hırvatça/Boşnakça/Karadağca pratikte tek dil.
    ("sr", "hr", .95), ("sr", "bs", .95), ("hr", "bs", .95),
    ("bg", "mk", .80), ("sr", "mk", .55), ("sl", "hr", .45),

    # --- Batı Slav ------------------------------------------------------
    ("cs", "sk", .90), ("pl", "sk", .40), ("pl", "cs", .35),

    # --- Doğu Slav ------------------------------------------------------
    ("uk", "be", .80), ("ru", "be", .65), ("ru", "uk", .50),

    # --- İskandinav -----------------------------------------------------
    ("da", "no", .85), ("no", "sv", .80),

    # --- Hint-Aryan -----------------------------------------------------
    # Hintçe ile Urduca konuşulduğunda aynı dil; yazı ayrı.
    ("hi", "ur", .90),

    # --- Malay ----------------------------------------------------------
    ("id", "ms", .88),

    # --- İran dilleri ---------------------------------------------------
    ("fa", "prs", .90), ("fa", "tg", .75), ("prs", "tg", .70),

    # --- Cermen ---------------------------------------------------------
    ("nl", "af", .70),

    # --- Bantu ----------------------------------------------------------
    ("zu", "xh", .75), ("zu", "nd", .85), ("xh", "nd", .70),
    ("sn", "nd", .30),

    # --- Roman ----------------------------------------------------------
    ("es", "gl", .75), ("pt", "gl", .85), ("es", "ca", .55),
    ("ca", "oc", .75),

    # --- Diğer ----------------------------------------------------------
    ("cs", "pl", .35),
]

# Yönlü olanlar: (bilen, karşılaşılan, oran)
TEK = [
    # Portekizce bilen İspanyolcayı daha iyi anlar; tersi daha zayıf.
    ("pt", "es", .60), ("es", "pt", .45),
    # Danca yazıda Norveççeye çok yakın ama söylenişi kapalı: İsveççe bilen
    # Dancayı, Danca bilenin İsveççeyi anladığından daha zor anlar.
    ("da", "sv", .60), ("sv", "da", .45),
    # Slovakça bilenler Çekçeye daha çok maruz kalıyor (medya), tersi değil.
    ("sk", "cs", .95),
    # Makedonca bilen Bulgarcayı biraz daha iyi anlıyor.
    ("mk", "bg", .85),
]


def build():
    """{slug: [[slug, oran], ...]} — yalnız 0'dan büyük olanlar."""
    out = {}

    def ekle(a, b, oran):
        if a == b or oran <= 0:
            return
        out.setdefault(a, {})
        if out[a].get(b, 0) < oran:
            out[a][b] = round(oran, 2)

    for a, b, oran in CIFT:
        ekle(a, b, oran)
        ekle(b, a, oran)
    for a, b, oran in TEK:
        ekle(a, b, oran)
    return {a: sorted(d.items(), key=lambda x: -x[1]) for a, d in sorted(out.items())}


if __name__ == "__main__":
    k = build()
    print(f"{len(k)} dilin akrabası var · toplam {sum(len(v) for v in k.values())} yönlü bağ")
    for a, v in list(k.items())[:8]:
        print(f"  {a}: {v}")
