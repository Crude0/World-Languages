#!/usr/bin/env python3
"""Veri denetimi — haritanın çekirdeği burası, o yüzden kalıcı bir araç.

Tek tek örnekleri kovalamak yerine bütün veri kümesini sınıf sınıf tarar.
Her başlık, "şu ülkede şu dil eksik" gibi tekil bir gözlemin arkasındaki
YAPISAL soruyu soruyor:

  1. Karışım toplamları     — %100'e yakın mı, taşma/eksik var mı
  2. Sığ karışımlar         — tek satırlık mix gerçekçi değil
  3. Resmî ama evde yok     — resmî dil listesinde olup mix'te olmayanlar
  4. İkinci dil boşlukları  — l2 hiç olmayan ülkeler
  5. Komşu sızıntısı        — bir dil A'da çoğunluk, A'ya komşu B'de sıfır
  6. Karşılıklı anlaşılırlık— birbirinin yerine geçebilen diller ayrı sayılıyor
  7. Nüfus tutarlılığı      — mix'ten türeyen konuşan sayısı ile ilan edilen
  8. Diaspora matrisi       — büyük göçmen toplulukları işlenmiş mi

Çıktı, düzeltilecek işin listesi olacak şekilde önem sırasına göre yazılır.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
D = json.load(open(HERE / "data.json", encoding="utf-8"))
C, L = D["countries"], D["langs"]

# Ada ve slug arasında gidip gelmek gerekiyor: mix isimle, langs slug ile.
AD2SLUG = {}
for slug, l in L.items():
    AD2SLUG[l["n"]] = slug

bulgular = []


def yaz(baslik, satirlar, agirlik):
    if satirlar:
        bulgular.append((agirlik, baslik, satirlar))


# ---------------------------------------------------------------- 1. toplamlar
kotu = []
for cid, c in C.items():
    mix = c.get("mix") or []
    t = sum(p for _, p in mix)
    if t < 92 or t > 108:
        kotu.append(f"{c['n']:34} toplam %{t:.1f} · {len(mix)} satır")
yaz("Karışım toplamı %100'den uzak", sorted(kotu), 2)

# ------------------------------------------------------------ 2. sığ karışımlar
sig = []
for cid, c in C.items():
    mix = c.get("mix") or []
    if len(mix) <= 1 and c.get("pop", 0) > 300_000:
        sig.append(f"{c['n']:34} nüfus {c['pop']/1e6:6.1f}mn · mix {mix}")
yaz("Tek satırlık karışım (nüfus > 300 bin)", sorted(sig), 1)

# ------------------------------------------------------- 3. resmî ama evde yok
resmi_yok = []
for cid, c in C.items():
    evde = {ad for ad, _ in (c.get("mix") or [])}
    for slug in c.get("o") or []:
        l = L.get(slug)
        if not l:
            resmi_yok.append(f"{c['n']:30} resmî dil slug'ı tanımsız: {slug}")
            continue
        if l["n"] not in evde:
            ik = {ad for ad, _ in (c.get("l2") or [])}
            if l["n"] not in ik:
                resmi_yok.append(f"{c['n']:30} {l['n']:18} resmî ama ne evde ne ikinci dilde")
yaz("Resmî dil hiçbir listede yok", sorted(resmi_yok), 2)

# ------------------------------------------------------ 4. ikinci dil boşluğu
l2yok = [f"{c['n']:34} nüfus {c['pop']/1e6:6.1f}mn"
         for cid, c in C.items() if not c.get("l2") and c.get("pop", 0) > 1_000_000]
yaz("İkinci dil verisi hiç yok (nüfus > 1mn)", sorted(l2yok), 1)

# ------------------------------------------------- 5. atanmamış nüfus
# Asıl soru bu: bir ülkede kaç kişi hiçbir dile atanmamış? mix toplamı
# 100'ün altındaysa aradaki fark "diğer diller" olarak geçiyor, ama o fark
# 100 milyon kişiyse "diğer" demek veriyi olmamak demektir. Öncelik
# sıralaması buradan çıkıyor: eksik yüzde değil, eksik İNSAN.
atanmamis = []
toplam_bosluk = 0
for cid, c in C.items():
    mix = c.get("mix") or []
    t = sum(p for _, p in mix)
    if t >= 97:
        continue
    kisi = c["pop"] * (100 - t) / 100          # pop binlik
    toplam_bosluk += kisi
    atanmamis.append((kisi, f"{c['n']:32} %{t:5.1f} · {len(mix)} satır · "
                            f"atanmamış {kisi/1000:7.1f} milyon kişi"))
atanmamis.sort(reverse=True)
yaz(f"Nüfusu hiçbir dile atanmamış (toplam {toplam_bosluk/1000:.0f} milyon kişi)",
    [x for _, x in atanmamis], 2)

# Çok dilli ülkede sığ liste: satır sayısı nüfusa göre yetersiz mi?
sig_liste = []
for cid, c in C.items():
    mix = c.get("mix") or []
    if c["pop"] > 20_000 and len(mix) <= 5:     # 20 milyon üstü, 5 satır ve altı
        sig_liste.append((c["pop"], f"{c['n']:32} {c['pop']/1000:6.1f}mn nüfus · "
                                     f"yalnız {len(mix)} dil · {[m[0] for m in mix]}"))
sig_liste.sort(reverse=True)
yaz("Büyük ülke, sığ dil listesi (>20mn nüfus, ≤5 satır)",
    [x for _, x in sig_liste], 2)

# --------------------------------------------- 6. karşılıklı anlaşılırlık ağı
# "Kimlerle anlaşabilirsin" sorusu bugün dilin adı birebir eşleşiyor mu diye
# cevaplanıyor. Oysa aşağıdaki çiftler pratikte birbirinin yerine geçiyor;
# Türkçe seçen biri Azerbaycan'da %0 görüyor, ki bu yanlış.
# Oranlar: konuşanın karşı tarafı ne kadar anladığı (kaba, yayınlarda
# bildirilen karşılıklı anlaşılırlık ölçümlerinin alt ucundan).
YAKIN = [
    ("tr", "az", .75), ("tr", "tk", .60), ("az", "tk", .60),
    ("kk", "ky", .85), ("kk", "uz", .50), ("ky", "uz", .50),
    ("tr", "kk", .35), ("tr", "uz", .35), ("tr", "ky", .35),
    ("cs", "sk", .90), ("hr", "sr", .95), ("hr", "bs", .95), ("sr", "bs", .95),
    ("sr", "mk", .60), ("bg", "mk", .80),
    ("da", "no", .85), ("no", "sv", .85), ("da", "sv", .65),
    ("hi", "ur", .90), ("id", "ms", .85),
    ("es", "pt", .55), ("es", "gl", .80), ("pt", "gl", .85), ("es", "ca", .60),
    ("ru", "uk", .60), ("ru", "be", .70), ("uk", "be", .80),
    ("zu", "xh", .75), ("nl", "af", .70),
    ("fa", "tg", .80), ("fa", "prs", .90),
]
eksik_dil, hazir = [], []
for a, b, oran in YAKIN:
    ea, eb = a in L, b in L
    if not (ea and eb):
        eksik_dil.append(f"{a} ({'var' if ea else 'YOK'}) ↔ {b} ({'var' if eb else 'YOK'})")
    else:
        hazir.append(f"{L[a]['n']:14} ↔ {L[b]['n']:14} %{oran*100:.0f}")
yaz("Yakın dil çiftinde taraflardan biri kayıtlı değil", eksik_dil, 3)
yaz(f"Modellenmesi gereken yakın dil çifti ({len(hazir)} çift, bugün hepsi %0 sayılıyor)",
    hazir, 3)

# ------------------------------------------------------- 7. nüfus tutarlılığı
tutarsiz = []
for slug, l in L.items():
    if not l.get("s"):
        continue
    # pop da s de binlik birimde
    turetilen = sum(C[cid]["pop"] * p / 100 for cid, p in (l.get("in") or []) if cid in C)
    ilan = l["s"]
    if ilan and turetilen:
        oran = turetilen / ilan
        if oran < .55 or oran > 1.8:
            tutarsiz.append(f"{l['n']:22} ilan {ilan/1000:8.1f}mn · haritadan {turetilen/1000:8.1f}mn · oran {oran:.2f}")
yaz("İlan edilen konuşan sayısı ile haritadan türeyen tutmuyor", sorted(tutarsiz), 2)

# ---------------------------------------------------------- 8. büyük diaspora
# Göçmen nüfusu yüksek ülkelerde mix ne kadar derin?
GOC = {"784": "BAE", "634": "Katar", "414": "Kuveyt", "048": "Bahreyn",
       "682": "Suudi Arabistan", "512": "Umman", "702": "Singapur",
       "344": "Hong Kong", "446": "Makao", "036": "Avustralya",
       "124": "Kanada", "756": "İsviçre", "040": "Avusturya", "752": "İsveç",
       "578": "Norveç", "208": "Danimarka", "246": "Finlandiya",
       "372": "İrlanda", "620": "Portekiz", "300": "Yunanistan"}
sig_goc = []
for cid, ad in GOC.items():
    c = C.get(cid)
    if not c:
        sig_goc.append(f"{ad}: ülke kaydı yok")
        continue
    mix = c.get("mix") or []
    if len(mix) < 5:
        sig_goc.append(f"{ad:22} yalnız {len(mix)} satır · {[m[0] for m in mix]}")
yaz("Göçmen ağırlıklı ülkede sığ karışım (< 5 satır)", sorted(sig_goc), 2)


# ------------------------------------------------- 9. göçmen dili büyüklükleri
# "Almanya'da %2 Türkçe, yani 1,7 milyon — ama Almanya'da 3-4 milyon Türk var"
# itirazının sınıfı. İkisi farklı şey ölçüyor: harita EVDE KONUŞULAN DİLİ
# sayıyor, köken/soy sayısını değil; üçüncü kuşağın büyük bölümü evde ülke
# dilini konuşuyor. Yine de payların gerçek dil sayımlarıyla karşılaştırılması
# gerekiyor — Almanya için Mikrozensus 2023 %2,5 veriyordu, tabloda %2 yazıyordu.
# Burada otomatik doğru/yanlış kararı verilemez; liste gözle denetlenmek üzere,
# ima edilen kişi sayısıyla birlikte, büyükten küçüğe çıkarılıyor.
ANAYURT = {"tr": {"792", "901"}, "ar": None, "fa": {"364"}, "ur": {"586"},
           "hi": {"356"}, "pl": {"616"}, "ro": {"642"}, "pt": {"620", "076"},
           "es": None, "zh": None, "ku": None, "so": {"706", "902"},
           "vi": {"704"}, "tl": {"608"}, "id": {"360"}, "am": {"231"},
           "ti": {"232", "231"}, "ps": {"004"}, "prs": {"004"}, "ru": {"643"},
           "uk": {"804"}, "sq": {"008", "983"}, "bn": {"050"}, "ne": {"524"}}
goc = []
for slug, hedef in ANAYURT.items():
    l = L.get(slug)
    if not l or hedef is None:
        continue
    disarida = [(C[cid]["pop"] * p / 100, C[cid]["n"], p)
                for cid, p in (l.get("in") or [])
                if cid in C and cid not in hedef]
    disarida.sort(reverse=True)
    if not disarida:
        continue
    top = sum(k for k, _, _ in disarida)
    ilk = " · ".join(f"{ad} %{p}" for _, ad, p in disarida[:5])
    goc.append((top, f"{l['n']:14} yurt dışı toplam {top/1000:6.2f}mn · {len(disarida):2} ülke · {ilk}"))
goc.sort(reverse=True)
yaz("Göçmen dili payları — gözle denetlenecek (evde konuşulan dil, köken değil)",
    [x for _, x in goc], 1)

# ------------------------------------------------------------------- rapor
sira = {3: "MODEL HATASI", 2: "VERİ HATASI", 1: "VERİ EKSİĞİ"}
for agirlik in (3, 2, 1):
    for a, baslik, satirlar in bulgular:
        if a != agirlik:
            continue
        print(f"\n[{sira[a]}] {baslik} — {len(satirlar)}")
        for s in satirlar[:40]:
            print("   " + s)
        if len(satirlar) > 40:
            print(f"   … {len(satirlar) - 40} tane daha")

toplam = sum(len(s) for _, _, s in bulgular)
print(f"\ntoplam {toplam} bulgu")
sys.exit(0)
