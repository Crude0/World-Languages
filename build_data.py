#!/usr/bin/env python3
"""Ülke -> çoğunluk dili veri seti; map_paths.json ile birleştirip data.json üretir."""
import json, sys
from lang_mix import MIX, L2
from population import POP
from diaspora import DIASPORA
import i18n

# ---------------------------------------------------------------- diller
# slug: (Türkçe ad, kendi dilindeki ad, kol/aile etiketi, renk grubu)
R, G, I, A, N, U, O = "rom", "ger", "ine", "afa", "nkg", "aus", "oth"
# 2026-08: gri "diğer" yığını 47 dilden 11'e indi. Türk dilleri ve Doğu-Güney
# Asya kendi renklerini aldı; kreoller kaynak dilin rengini tarama dokusuyla
# taşıyor (dokuz. renk koyu modda ayrım eşiğini geçmiyordu — palfit.mjs).
T, S = "trk", "asi"
# Kreoller kendi rengini almıyor: kaynak (sözcük dağarcığını verdiği) dilin
# rengiyle çiziliyor, üstüne tarama dokusu geliyor. Böylece palet sekiz
# doğrulanmış renkte kalıyor ve renk "hangi dilden türemiş"i de söylüyor.
LEXIFIER = {
    "Kreol · İngilizce temelli": G,
    "Kreol · Fransızca temelli": R,
    "Kreol · Portekizce temelli": R,
    "Kreol · İber temelli": R,
    "Hint-Aryan temelli kreol": I,
}

# Hiçbir ülkede çoğunluk olmayan, ama bir eyalet/il/bölgede çoğunluk olan
# diller. Ülke haritasında yer almazlar; bölge katmanında ve süzgeçte varlar.
REGIONAL = {
    "ku":   ("Kürtçe", "Kurdî", "Hint-Avrupa · Hint-İran", I),
    "ta":   ("Tamilce", "தமிழ்", "Dravit dilleri", S),
    "te":   ("Telugu", "తెలుగు", "Dravit dilleri", S),
    "kn":   ("Kannada", "ಕನ್ನಡ", "Dravit dilleri", S),
    "ml":   ("Malayalam", "മലയാളം", "Dravit dilleri", S),
    "mr":   ("Marathi", "मराठी", "Hint-Avrupa · Hint-Aryan", I),
    "gu":   ("Gucaratça", "ગુજરાતી", "Hint-Avrupa · Hint-Aryan", I),
    "pa":   ("Pencapça", "ਪੰਜਾਬੀ", "Hint-Avrupa · Hint-Aryan", I),
    "or":   ("Oriya", "ଓଡ଼ିଆ", "Hint-Avrupa · Hint-Aryan", I),
    "as":   ("Assamca", "অসমীয়া", "Hint-Avrupa · Hint-Aryan", I),
    "ks":   ("Keşmirce", "کٲشُر", "Hint-Avrupa · Dard", I),
    "kok":  ("Konkani", "कोंकणी", "Hint-Avrupa · Hint-Aryan", I),
    "mni":  ("Meitei", "ꯃꯤꯇꯩꯂꯣꯟ", "Çin-Tibet dilleri", S),
    "lus":  ("Mizo", "Mizo ṭawng", "Çin-Tibet dilleri", S),
    "kha":  ("Kasi", "Khasi", "Avustroasyatik diller", S),
    "nag":  ("Nagamese", "Nagamese", "Hint-Aryan temelli kreol", I),
    "iu":   ("İnuktitut", "ᐃᓄᒃᑎᑐᑦ", "Eskimo-Aleut dilleri", O),
    "eu":   ("Baskça", "Euskara", "İzole dil", O),
    "gl":   ("Galiçyaca", "Galego", "Hint-Avrupa · Roman", R),
    "qu":   ("Keçuva", "Runa Simi", "Keçuva dilleri", O),
    "ay":   ("Aymara", "Aymar aru", "Aymara dilleri", O),
}

L = {
    # Hint-Avrupa · Roman
    "es":    ("İspanyolca", "Español", "Hint-Avrupa · Roman", R),
    "pt":    ("Portekizce", "Português", "Hint-Avrupa · Roman", R),
    "fr":    ("Fransızca", "Français", "Hint-Avrupa · Roman", R),
    "it":    ("İtalyanca", "Italiano", "Hint-Avrupa · Roman", R),
    "ro":    ("Romence", "Română", "Hint-Avrupa · Roman", R),
    "ca":    ("Katalanca", "Català", "Hint-Avrupa · Roman", R),
    # Hint-Avrupa · Cermen
    "en":    ("İngilizce", "English", "Hint-Avrupa · Cermen", G),
    "de":    ("Almanca", "Deutsch", "Hint-Avrupa · Cermen", G),
    "nl":    ("Felemenkçe", "Nederlands", "Hint-Avrupa · Cermen", G),
    "sv":    ("İsveççe", "Svenska", "Hint-Avrupa · Cermen", G),
    "da":    ("Danca", "Dansk", "Hint-Avrupa · Cermen", G),
    "no":    ("Norveççe", "Norsk", "Hint-Avrupa · Cermen", G),
    "is":    ("İzlandaca", "Íslenska", "Hint-Avrupa · Cermen", G),
    "fo":    ("Faroece", "Føroyskt", "Hint-Avrupa · Cermen", G),
    "lb":    ("Lüksemburgca", "Lëtzebuergesch", "Hint-Avrupa · Cermen", G),
    # Hint-Avrupa · diğer kollar
    "ru":    ("Rusça", "Русский", "Hint-Avrupa · Slav", I),
    "uk":    ("Ukraynaca", "Українська", "Hint-Avrupa · Slav", I),
    "pl":    ("Lehçe", "Polski", "Hint-Avrupa · Slav", I),
    "cs":    ("Çekçe", "Čeština", "Hint-Avrupa · Slav", I),
    "sk":    ("Slovakça", "Slovenčina", "Hint-Avrupa · Slav", I),
    "sl":    ("Slovence", "Slovenščina", "Hint-Avrupa · Slav", I),
    "hr":    ("Hırvatça", "Hrvatski", "Hint-Avrupa · Slav", I),
    "sr":    ("Sırpça", "Српски", "Hint-Avrupa · Slav", I),
    "bs":    ("Boşnakça", "Bosanski", "Hint-Avrupa · Slav", I),
    "cnr":   ("Karadağca", "Crnogorski", "Hint-Avrupa · Slav", I),
    "mk":    ("Makedonca", "Македонски", "Hint-Avrupa · Slav", I),
    "bg":    ("Bulgarca", "Български", "Hint-Avrupa · Slav", I),
    "el":    ("Yunanca", "Ελληνικά", "Hint-Avrupa · Helen", I),
    "sq":    ("Arnavutça", "Shqip", "Hint-Avrupa · Arnavut", I),
    "hy":    ("Ermenice", "Հայերեն", "Hint-Avrupa · Ermeni", I),
    "lv":    ("Letonca", "Latviešu", "Hint-Avrupa · Balt", I),
    "lt":    ("Litvanca", "Lietuvių", "Hint-Avrupa · Balt", I),
    "hi":    ("Hintçe", "हिन्दी", "Hint-Avrupa · Hint-İran", I),
    "ur":    ("Urduca", "اردو", "Hint-Avrupa · Hint-İran", I),
    "bn":    ("Bengalce", "বাংলা", "Hint-Avrupa · Hint-İran", I),
    "ne":    ("Nepalce", "नेपाली", "Hint-Avrupa · Hint-İran", I),
    "si":    ("Sinhalca", "සිංහල", "Hint-Avrupa · Hint-İran", I),
    "dv":    ("Divehi", "ދިވެހި", "Hint-Avrupa · Hint-İran", I),
    "fa":    ("Farsça", "فارسی", "Hint-Avrupa · Hint-İran", I),
    "prs":   ("Darice", "دری", "Hint-Avrupa · Hint-İran", I),
    "tg":    ("Tacikçe", "Тоҷикӣ", "Hint-Avrupa · Hint-İran", I),
    # Afro-Asyatik
    "ar":    ("Arapça", "العربية", "Afro-Asyatik · Sami", A),
    "ar_jb": ("Cuba Arapçası", "عربي جوبا", "Afro-Asyatik · Sami", A),
    "mt":    ("Maltaca", "Malti", "Afro-Asyatik · Sami", A),
    "he":    ("İbranice", "עברית", "Afro-Asyatik · Sami", A),
    "am":    ("Amharca", "አማርኛ", "Afro-Asyatik · Sami", A),
    "ti":    ("Tigrinya", "ትግርኛ", "Afro-Asyatik · Sami", A),
    "so":    ("Somalice", "Soomaali", "Afro-Asyatik · Kuşi", A),
    "ha":    ("Hausa", "Harshen Hausa", "Afro-Asyatik · Çad", A),
    # Nijer-Kongo
    "sw":    ("Svahili", "Kiswahili", "Nijer-Kongo · Bantu", N),
    "zu":    ("Zuluca", "isiZulu", "Nijer-Kongo · Bantu", N),
    "sn":    ("Şonaca", "chiShona", "Nijer-Kongo · Bantu", N),
    "rw":    ("Kinyarwanda", "Ikinyarwanda", "Nijer-Kongo · Bantu", N),
    "rn":    ("Kirundi", "Ikirundi", "Nijer-Kongo · Bantu", N),
    "st":    ("Sesotho", "Sesotho", "Nijer-Kongo · Bantu", N),
    "tn":    ("Setsvana", "Setswana", "Nijer-Kongo · Bantu", N),
    "ss":    ("Sisvati", "siSwati", "Nijer-Kongo · Bantu", N),
    "ny":    ("Çeva", "Chichewa", "Nijer-Kongo · Bantu", N),
    "kj":    ("Oşivambo", "Oshiwambo", "Nijer-Kongo · Bantu", N),
    "lg":    ("Ganda", "Luganda", "Nijer-Kongo · Bantu", N),
    "bem":   ("Bemba", "Ichibemba", "Nijer-Kongo · Bantu", N),
    "zdj":   ("Komorca", "Shikomori", "Nijer-Kongo · Bantu", N),
    "sg":    ("Sango", "Sängö", "Nijer-Kongo · Ubangi", N),
    "wo":    ("Volofça", "Wolof", "Nijer-Kongo · Atlantik", N),
    "ff":    ("Fulaca", "Pulaar / Fulfulde", "Nijer-Kongo · Atlantik", N),
    "bm":    ("Bambara", "Bamanankan", "Nijer-Kongo · Mande", N),
    "mnk":   ("Mandinka", "Mandinka", "Nijer-Kongo · Mande", N),
    "mos":   ("Moore", "Mòoré", "Nijer-Kongo · Gur", N),
    "ak":    ("Akanca", "Akan (Twi)", "Nijer-Kongo · Kva", N),
    "ee":    ("Eve", "Eʋegbe", "Nijer-Kongo · Kva", N),
    "fon":   ("Fon", "Fɔngbe", "Nijer-Kongo · Kva", N),
    # Avustronezya
    "id":    ("Endonezce", "Bahasa Indonesia", "Avustronezya · Malayo-Polinezya", U),
    "ms":    ("Malayca", "Bahasa Melayu", "Avustronezya · Malayo-Polinezya", U),
    "fil":   ("Filipince", "Filipino", "Avustronezya · Malayo-Polinezya", U),
    "mg":    ("Malgaşça", "Malagasy", "Avustronezya · Malayo-Polinezya", U),
    "tet":   ("Tetumca", "Tetun", "Avustronezya · Malayo-Polinezya", U),
    "fj":    ("Fiji dili", "Na Vosa Vakaviti", "Avustronezya · Okyanusya", U),
    "sm":    ("Samoaca", "Gagana Sāmoa", "Avustronezya · Okyanusya", U),
    "to":    ("Tongaca", "Lea faka-Tonga", "Avustronezya · Okyanusya", U),
    "gil":   ("Gilbertçe", "Taetae ni Kiribati", "Avustronezya · Okyanusya", U),
    "mh":    ("Marshallca", "Kajin M̧ajeļ", "Avustronezya · Okyanusya", U),
    "pau":   ("Palauca", "Tekoi er a Belau", "Avustronezya · Okyanusya", U),
    "chk":   ("Çuukça", "Chuuk", "Avustronezya · Okyanusya", U),
    "na":    ("Nauruca", "Dorerin Naoero", "Avustronezya · Okyanusya", U),
    "niu":   ("Niueca", "Vagahau Niuē", "Avustronezya · Okyanusya", U),
    "rar":   ("Cook Adaları Maoricesi", "Māori Kūki 'Āirani", "Avustronezya · Okyanusya", U),
    # Türk dilleri
    "tr":    ("Türkçe", "Türkçe", "Türk dilleri", T),
    "az":    ("Azerbaycanca", "Azərbaycan dili", "Türk dilleri", T),
    "kk":    ("Kazakça", "Қазақ тілі", "Türk dilleri", T),
    "ky":    ("Kırgızca", "Кыргызча", "Türk dilleri", T),
    "uz":    ("Özbekçe", "Oʻzbekcha", "Türk dilleri", T),
    "tk":    ("Türkmence", "Türkmençe", "Türk dilleri", T),
    # Doğu ve Güneydoğu Asya
    "zh":    ("Mandarin Çincesi", "普通话", "Çin-Tibet dilleri", S),
    "yue":   ("Kantonca", "廣東話", "Çin-Tibet dilleri", S),
    "my":    ("Birmanca", "မြန်မာဘာသာ", "Çin-Tibet dilleri", S),
    "dz":    ("Dzongkha", "རྫོང་ཁ", "Çin-Tibet dilleri", S),
    "ja":    ("Japonca", "日本語", "Japon dilleri", S),
    "ko":    ("Korece", "한국어", "Kore dilleri", S),
    "vi":    ("Vietnamca", "Tiếng Việt", "Avustroasyatik diller", S),
    "km":    ("Khmerce", "ភាសាខ្មែរ", "Avustroasyatik diller", S),
    "th":    ("Tayca", "ภาษาไทย", "Tai-Kadai", S),
    "lo":    ("Laoca", "ພາສາລາວ", "Tai-Kadai", S),
    "mn":    ("Moğolca", "Монгол хэл", "Moğol dilleri", O),
    # Diğer aileler
    "fi":    ("Fince", "Suomi", "Ural", O),
    "et":    ("Estonca", "Eesti keel", "Ural", O),
    "hu":    ("Macarca", "Magyar", "Ural", O),
    "ka":    ("Gürcüce", "ქართული", "Kartvel dilleri", O),
    "kl":    ("Grönlandca", "Kalaallisut", "Eskimo-Aleut dilleri", O),
    "gn":    ("Guaraní", "Avañe'ẽ", "Tupi-Guaraní", O),
    # Kreol diller
    "ht":    ("Haiti Kreolcesi", "Kreyòl ayisyen", "Kreol · Fransızca temelli", R),
    "crs":   ("Seyşel Kreolcesi", "Seselwa", "Kreol · Fransızca temelli", R),
    "mfe":   ("Mauritius Kreolcesi", "Kreol Morisien", "Kreol · Fransızca temelli", R),
    "jam":   ("Jamaika Patoisı", "Patwa", "Kreol · İngilizce temelli", G),
    "tpi":   ("Tok Pisin", "Tok Pisin", "Kreol · İngilizce temelli", G),
    "bi":    ("Bislama", "Bislama", "Kreol · İngilizce temelli", G),
    "pis":   ("Solomon Pijini", "Pijin", "Kreol · İngilizce temelli", G),
    "kri":   ("Krio", "Krio", "Kreol · İngilizce temelli", G),
    "pcm":   ("Nijerya Pidgini", "Naijá", "Kreol · İngilizce temelli", G),
    "kea":   ("Cabo Verde Kreolcesi", "Kriolu", "Kreol · Portekizce temelli", R),
    "pov":   ("Gine-Bissau Kreolcesi", "Kriol", "Kreol · Portekizce temelli", R),
    "pap":   ("Papiamentu", "Papiamentu", "Kreol · İber temelli", R),
}
L.update(REGIONAL)

GROUPS = {
    R: ("Roman dilleri", "İspanyolca, Portekizce, Fransızca, İtalyanca, Romence"),
    G: ("Cermen dilleri", "İngilizce, Almanca, Felemenkçe, İskandinav dilleri"),
    I: ("Hint-Avrupa · diğer kollar", "Slav, Hint-İran, Helen, Balt, Ermeni, Arnavut kolları"),
    T: ("Türk dilleri", "Türkçe, Azerice, Kazakça, Özbekçe, Kırgızca, Türkmence"),
    A: ("Afro-Asyatik diller", "Arapça, İbranice, Amharca, Somalice, Hausa, Maltaca"),
    N: ("Nijer-Kongo dilleri", "Svahili, Zuluca, Kinyarwanda, Volofça, Akanca"),
    S: ("Doğu ve Güney Asya dilleri", "Çince, Japonca, Korece, Tamilce, Vietnamca, Tayca"),
    U: ("Avustronezya dilleri", "Endonezce, Malayca, Filipince, Malgaşça, Okyanusya dilleri"),
    O: ("Diğer aileler", "Ural, Moğol, Kartvel, Eskimo-Aleut, And dilleri, izole diller"),
}

# ---------------------------------------------------------------- ülkeler
# id: (Türkçe ad, dil, ~%, çoğunluk mu (1/0), not, bölge, bağımlı toprak mı)
AV, AS, AF, KA, GA, OK = "Avrupa", "Asya", "Afrika", "Kuzey Amerika", "Güney Amerika", "Okyanusya"
C = {
 # --- Avrupa
 "008": ("Arnavutluk", "sq", 98, 1, "", AV, 0),
 "020": ("Andorra", "ca", 44, 0, "Resmî dil Katalanca; İspanyolca da çok yaygın konuşulur.", AV, 0),
 "040": ("Avusturya", "de", 93, 1, "", AV, 0),
 "056": ("Belçika", "nl", 60, 1, "Güneyde Fransızca (~%40), doğuda küçük bir Almanca bölgesi var.", AV, 0),
 "070": ("Bosna-Hersek", "bs", 53, 1, "Sırpça ve Hırvatça ile karşılıklı anlaşılır; üçü de resmî.", AV, 0),
 "100": ("Bulgaristan", "bg", 85, 1, "", AV, 0),
 "112": ("Belarus", "ru", 71, 1, "Belarusça resmî ve ulusal dil; günlük hayatta Rusça baskın.", AV, 0),
 "191": ("Hırvatistan", "hr", 95, 1, "", AV, 0),
 "196": ("Kıbrıs", "el", 79, 1, "Ada genelinde Türkçe de resmî dil.", AV, 0),
 "203": ("Çekya", "cs", 96, 1, "", AV, 0),
 "208": ("Danimarka", "da", 96, 1, "", AV, 0),
 "233": ("Estonya", "et", 68, 1, "Rusça konuşan azınlık nüfusun yaklaşık dörtte biri.", AV, 0),
 "234": ("Faroe Adaları", "fo", 95, 1, "", AV, 1),
 "246": ("Finlandiya", "fi", 86, 1, "İsveççe ikinci resmî dil (~%5).", AV, 0),
 "248": ("Åland", "sv", 98, 1, "", AV, 1),
 "250": ("Fransa", "fr", 97, 1, "", AV, 0),
 "268": ("Gürcistan", "ka", 88, 1, "", AS, 0),
 "276": ("Almanya", "de", 95, 1, "", AV, 0),
 "300": ("Yunanistan", "el", 99, 1, "", AV, 0),
 "304": ("Grönland", "kl", 88, 1, "Danca ikinci dil olarak yaygın.", KA, 1),
 "336": ("Vatikan", "it", 100, 1, "Resmî yazışma dili Latince.", AV, 0),
 "348": ("Macaristan", "hu", 99, 1, "", AV, 0),
 "352": ("İzlanda", "is", 97, 1, "", AV, 0),
 "372": ("İrlanda", "en", 98, 1, "İrlandaca ilk resmî dil; günlük kullanımı sınırlı.", AV, 0),
 "376": ("İsrail", "he", 76, 1, "Arapça özel statülü dil (~%20).", AS, 0),
 "380": ("İtalya", "it", 97, 1, "", AV, 0),
 "428": ("Letonya", "lv", 62, 1, "Rusça nüfusun yaklaşık üçte biri için ana dil.", AV, 0),
 "438": ("Liechtenstein", "de", 94, 1, "", AV, 0),
 "440": ("Litvanya", "lt", 82, 1, "", AV, 0),
 "442": ("Lüksemburg", "lb", 55, 1, "Fransızca ve Almanca da resmî; nüfusun yarısına yakını yabancı.", AV, 0),
 "470": ("Malta", "mt", 97, 1, "Maltaca, Latin alfabesiyle yazılan tek Sami dilidir.", AV, 0),
 "492": ("Monako", "fr", 97, 1, "", AV, 0),
 "498": ("Moldova", "ro", 80, 1, "Ülkede dilin adı resmen Romence.", AV, 0),
 "499": ("Karadağ", "cnr", 37, 0, "Nüfusun %43'ü dili Sırpça olarak adlandırıyor; ikisi karşılıklı anlaşılır.", AV, 0),
 "500": ("Montserrat", "en", 95, 1, "", KA, 1),
 "528": ("Hollanda", "nl", 96, 1, "Kuzeyde Frizce ikinci resmî dil.", AV, 0),
 "578": ("Norveç", "no", 95, 1, "", AV, 0),
 "616": ("Polonya", "pl", 97, 1, "", AV, 0),
 "620": ("Portekiz", "pt", 99, 1, "", AV, 0),
 "642": ("Romanya", "ro", 90, 1, "Macarca en büyük azınlık dili (~%6).", AV, 0),
 "643": ("Rusya", "ru", 98, 1, "Federasyon genelinde 30'dan fazla dil resmî statülü.", AV, 0),
 "674": ("San Marino", "it", 100, 1, "", AV, 0),
 "688": ("Sırbistan", "sr", 88, 1, "", AV, 0),
 "703": ("Slovakya", "sk", 84, 1, "", AV, 0),
 "705": ("Slovenya", "sl", 88, 1, "", AV, 0),
 "724": ("İspanya", "es", 99, 1, "Katalanca, Galiçyaca ve Baskça bölgesel resmî diller.", AV, 0),
 "752": ("İsveç", "sv", 95, 1, "", AV, 0),
 "756": ("İsviçre", "de", 62, 1, "Fransızca ~%23, İtalyanca ~%8, Romanşça ~%0,5.", AV, 0),
 "792": ("Türkiye", "tr", 88, 1, "Kürtçe en büyük ikinci dil (~%12).", AS, 0),
 "804": ("Ukrayna", "uk", 68, 1, "Rusça hâlâ geniş bir kesim için günlük dil.", AV, 0),
 "807": ("Kuzey Makedonya", "mk", 67, 1, "Arnavutça ikinci resmî dil (~%25).", AV, 0),
 "826": ("Birleşik Krallık", "en", 98, 1, "Galce, İskoçça ve Gaelce bölgesel diller.", AV, 0),
 "831": ("Guernsey", "en", 97, 1, "", AV, 1),
 "832": ("Jersey", "en", 97, 1, "", AV, 1),
 "833": ("Man Adası", "en", 99, 1, "", AV, 1),
 "900": ("Kosova", "sq", 92, 1, "Sırpça ikinci resmî dil.", AV, 0),
 "901": ("Kuzey Kıbrıs", "tr", 99, 1, "", AS, 0),
 # --- Asya
 "004": ("Afganistan", "prs", 77, 1, "Peştuca nüfusun ~%48'inin dili; ikisi de resmî.", AS, 0),
 "031": ("Azerbaycan", "az", 92, 1, "", AS, 0),
 "048": ("Bahreyn", "ar", 89, 1, "", AS, 0),
 "050": ("Bangladeş", "bn", 98, 1, "", AS, 0),
 "051": ("Ermenistan", "hy", 98, 1, "", AS, 0),
 "064": ("Butan", "dz", 24, 0, "Çoğunluk dili yok; Dzongkha resmî dil, doğuda Tshangla yaygın.", AS, 0),
 "096": ("Brunei", "ms", 82, 1, "", AS, 0),
 "104": ("Myanmar", "my", 68, 1, "100'den fazla azınlık dili konuşuluyor.", AS, 0),
 "116": ("Kamboçya", "km", 96, 1, "", AS, 0),
 "144": ("Sri Lanka", "si", 75, 1, "Tamilce ikinci resmî dil (~%25).", AS, 0),
 "156": ("Çin", "zh", 80, 1, "Kantonca, Vu, Min gibi diğer Çin dilleri onlarca milyon kişinin ana dili.", AS, 0),
 "158": ("Tayvan", "zh", 83, 1, "Tayvanca (Hokkien) evde yaygın olarak konuşuluyor.", AS, 0),
 "275": ("Filistin", "ar", 98, 1, "", AS, 0),
 "344": ("Hong Kong", "yue", 88, 1, "İngilizce ve Mandarin de resmî.", AS, 1),
 "356": ("Hindistan", "hi", 44, 0, "Çoğunluk dili yok; 22 resmî dil var, Hintçe en yaygın olanı.", AS, 0),
 "360": ("Endonezya", "id", 94, 1, "Ana dil olarak ~%20; ülke genelinde ortak dil olarak neredeyse herkes konuşuyor.", AS, 0),
 "364": ("İran", "fa", 79, 1, "Azerice, Kürtçe ve Lurca büyük azınlık dilleri.", AS, 0),
 "368": ("Irak", "ar", 79, 1, "Kürtçe ikinci resmî dil (~%18).", AS, 0),
 "392": ("Japonya", "ja", 99, 1, "", AS, 0),
 "398": ("Kazakistan", "kk", 74, 1, "Rusça hâlâ çok yaygın bir ortak dil.", AS, 0),
 "400": ("Ürdün", "ar", 98, 1, "", AS, 0),
 "408": ("Kuzey Kore", "ko", 100, 1, "", AS, 0),
 "410": ("Güney Kore", "ko", 99, 1, "", AS, 0),
 "414": ("Kuveyt", "ar", 68, 1, "Nüfusun büyük bölümü yabancı işçilerden oluşuyor.", AS, 0),
 "417": ("Kırgızistan", "ky", 78, 1, "Rusça resmî statülü ortak dil.", AS, 0),
 "418": ("Laos", "lo", 82, 1, "", AS, 0),
 "422": ("Lübnan", "ar", 93, 1, "Fransızca ve İngilizce eğitimde çok yaygın.", AS, 0),
 "446": ("Makao", "yue", 85, 1, "Portekizce de resmî dil.", AS, 1),
 "458": ("Malezya", "ms", 80, 1, "Çince ve Tamilce büyük topluluk dilleri.", AS, 0),
 "462": ("Maldivler", "dv", 98, 1, "", AS, 0),
 "496": ("Moğolistan", "mn", 95, 1, "", AS, 0),
 "512": ("Umman", "ar", 76, 1, "", AS, 0),
 "524": ("Nepal", "ne", 65, 1, "Ana dil olarak ~%45; 120'den fazla dil konuşuluyor.", AS, 0),
 "586": ("Pakistan", "ur", 77, 1, "Ana dil olarak ~%8; ortak dil olarak çoğunluk konuşuyor. Pencapça en büyük ana dil (~%38).", AS, 0),
 "608": ("Filipinler", "fil", 82, 1, "Ana dil olarak ~%28; ortak dil olarak yaygın. 170'ten fazla dil var.", AS, 0),
 "626": ("Doğu Timor", "tet", 60, 1, "Portekizce de resmî dil.", AS, 0),
 "634": ("Katar", "ar", 56, 1, "Nüfusun büyük çoğunluğu yabancı; İngilizce iş dili.", AS, 0),
 "682": ("Suudi Arabistan", "ar", 90, 1, "", AS, 0),
 "702": ("Singapur", "en", 48, 0, "Evde en çok konuşulan dil; Mandarin ~%30. Dört resmî dil var.", AS, 0),
 "704": ("Vietnam", "vi", 86, 1, "", AS, 0),
 "760": ("Suriye", "ar", 90, 1, "Kürtçe en büyük azınlık dili.", AS, 0),
 "762": ("Tacikistan", "tg", 84, 1, "Farsçanın bir kolu.", AS, 0),
 "764": ("Tayland", "th", 88, 1, "", AS, 0),
 "784": ("Birleşik Arap Emirlikleri", "ar", 42, 0, "Nüfusun ~%88'i yabancı; Arapça resmî dil, İngilizce fiilî ortak dil.", AS, 0),
 "795": ("Türkmenistan", "tk", 77, 1, "", AS, 0),
 "860": ("Özbekistan", "uz", 85, 1, "", AS, 0),
 "887": ("Yemen", "ar", 99, 1, "", AS, 0),
 "086": ("Britanya Hint Okyanusu Toprakları", "en", 100, 1, "", AF, 1),
 # --- Afrika
 "012": ("Cezayir", "ar", 81, 1, "Berberi dilleri (Tamazight) resmî ve yaygın (~%27).", AF, 0),
 "024": ("Angola", "pt", 71, 1, "Umbundu ve Kimbundu büyük ana diller.", AF, 0),
 "072": ("Botsvana", "tn", 78, 1, "İngilizce resmî dil.", AF, 0),
 "108": ("Burundi", "rn", 98, 1, "", AF, 0),
 "120": ("Kamerun", "fr", 70, 1, "İngilizce de resmî; 250'den fazla yerel dil var.", AF, 0),
 "132": ("Cabo Verde", "kea", 95, 1, "Portekizce resmî dil.", AF, 0),
 "140": ("Orta Afrika Cumhuriyeti", "sg", 92, 1, "Fransızca da resmî dil.", AF, 0),
 "148": ("Çad", "ar", 60, 1, "Çad Arapçası ortak dil; Fransızca da resmî. 120'den fazla dil var.", AF, 0),
 "174": ("Komorlar", "zdj", 97, 1, "Arapça ve Fransızca da resmî.", AF, 0),
 "178": ("Kongo Cumhuriyeti", "fr", 78, 1, "Lingala ve Kituba ulusal ortak diller.", AF, 0),
 "180": ("Demokratik Kongo Cumhuriyeti", "fr", 51, 0, "Çoğunluk dili yok; Lingala, Svahili, Kikongo ve Tshiluba ulusal diller.", AF, 0),
 "204": ("Benin", "fon", 25, 0, "Çoğunluk dili yok; Fransızca resmî ve ortak dil.", AF, 0),
 "226": ("Ekvator Ginesi", "es", 88, 1, "Fransızca ve Portekizce de resmî.", AF, 0),
 "231": ("Etiyopya", "am", 62, 0, "Ana dil olarak Oromoca daha yaygın (~%34); Amharca ortak dil.", AF, 0),
 "232": ("Eritre", "ti", 57, 1, "Dokuz ulusal dil var; Arapça ve İngilizce çalışma dilleri.", AF, 0),
 "262": ("Cibuti", "so", 60, 1, "Afarca ikinci büyük dil; Arapça ve Fransızca resmî.", AF, 0),
 "266": ("Gabon", "fr", 80, 1, "", AF, 0),
 "270": ("Gambiya", "mnk", 38, 0, "Çoğunluk dili yok; Volofça başkentte ortak dil, İngilizce resmî.", AF, 0),
 "288": ("Gana", "ak", 58, 1, "İngilizce resmî dil; 80'den fazla dil konuşuluyor.", AF, 0),
 "324": ("Gine", "ff", 32, 0, "Çoğunluk dili yok; Maninka ve Susu de büyük diller.", AF, 0),
 "384": ("Fildişi Sahili", "fr", 70, 1, "Diyula ticaret dili olarak yaygın.", AF, 0),
 "404": ("Kenya", "sw", 90, 1, "İngilizce de resmî; Kikuyu en büyük ana dil.", AF, 0),
 "426": ("Lesotho", "st", 98, 1, "", AF, 0),
 "430": ("Liberya", "en", 85, 1, "Günlük dil büyük ölçüde Liberya İngilizcesi ve Kpelle gibi yerel diller.", AF, 0),
 "434": ("Libya", "ar", 95, 1, "", AF, 0),
 "450": ("Madagaskar", "mg", 98, 1, "Fransızca da resmî.", AF, 0),
 "454": ("Malavi", "ny", 70, 1, "İngilizce resmî dil.", AF, 0),
 "466": ("Mali", "bm", 80, 1, "Ana dil olarak ~%46; ortak dil olarak daha yaygın.", AF, 0),
 "478": ("Moritanya", "ar", 80, 1, "Hassaniye Arapçası; Pulaar, Soninke ve Volofça ulusal diller.", AF, 0),
 "480": ("Mauritius", "mfe", 86, 1, "İngilizce ve Fransızca yönetim ve eğitim dilleri.", AF, 0),
 "504": ("Fas", "ar", 92, 1, "Berberi dilleri (Tamazight) resmî ve yaygın (~%26).", AF, 0),
 "508": ("Mozambik", "pt", 50, 0, "Ana dil olarak ~%17; Makhuwa en büyük yerel dil.", AF, 0),
 "516": ("Namibya", "kj", 49, 0, "Çoğunluk dili yok; İngilizce resmî, Afrikaanca yaygın ortak dil.", AF, 0),
 "562": ("Nijer", "ha", 60, 1, "Zarma ikinci büyük dil; Fransızca resmî.", AF, 0),
 "566": ("Nijerya", "pcm", 60, 0, "Çoğunluk dili yok; Hausa, Yorubaca ve İgboca en büyük ana diller, İngilizce resmî.", AF, 0),
 "624": ("Gine-Bissau", "pov", 90, 1, "Portekizce resmî dil.", AF, 0),
 "646": ("Ruanda", "rw", 99, 1, "", AF, 0),
 "654": ("Saint Helena", "en", 100, 1, "", AF, 1),
 "678": ("São Tomé ve Príncipe", "pt", 98, 1, "", AF, 0),
 "686": ("Senegal", "wo", 80, 1, "Ana dil olarak ~%40; ortak dil olarak daha yaygın. Fransızca resmî.", AF, 0),
 "690": ("Seyşeller", "crs", 95, 1, "İngilizce ve Fransızca da resmî.", AF, 0),
 "694": ("Sierra Leone", "kri", 90, 1, "Ortak dil olarak yaygın; Mende ve Temne büyük ana diller.", AF, 0),
 "706": ("Somali", "so", 95, 1, "Arapça da resmî.", AF, 0),
 "710": ("Güney Afrika", "zu", 25, 0, "Çoğunluk dili yok; 12 resmî dil var, İngilizce ortak dil.", AF, 0),
 "716": ("Zimbabve", "sn", 70, 1, "16 resmî dil; Ndebele ikinci büyük dil.", AF, 0),
 "728": ("Güney Sudan", "ar_jb", 50, 0, "Çoğunluk dili yok; Dinka en büyük ana dil, İngilizce resmî.", AF, 0),
 "729": ("Sudan", "ar", 70, 1, "", AF, 0),
 "732": ("Batı Sahra", "ar", 90, 1, "Hassaniye Arapçası.", AF, 0),
 "748": ("Esvatini", "ss", 90, 1, "İngilizce de resmî.", AF, 0),
 "768": ("Togo", "ee", 40, 0, "Çoğunluk dili yok; kuzeyde Kabiye yaygın, Fransızca resmî.", AF, 0),
 "788": ("Tunus", "ar", 98, 1, "Fransızca ikinci dil olarak yaygın.", AF, 0),
 "800": ("Uganda", "lg", 40, 0, "Çoğunluk dili yok; İngilizce ve Svahili resmî diller.", AF, 0),
 "818": ("Mısır", "ar", 99, 1, "", AF, 0),
 "834": ("Tanzanya", "sw", 95, 1, "Ana dil olarak azınlık; ulusal ortak dil olarak neredeyse herkes konuşuyor.", AF, 0),
 "854": ("Burkina Faso", "mos", 52, 1, "Fransızca resmî; 60'tan fazla dil var.", AF, 0),
 "894": ("Zambiya", "bem", 35, 0, "Çoğunluk dili yok; Nyanja ve İngilizce de yaygın.", AF, 0),
 "902": ("Somaliland", "so", 95, 1, "", AF, 0),
 # --- Amerika
 "028": ("Antigua ve Barbuda", "en", 95, 1, "", KA, 0),
 "032": ("Arjantin", "es", 98, 1, "", GA, 0),
 "044": ("Bahamalar", "en", 95, 1, "Bahama Kreolcesi günlük konuşma dili.", KA, 0),
 "052": ("Barbados", "en", 95, 1, "Bajan Kreolcesi günlük konuşma dili.", KA, 0),
 "060": ("Bermuda", "en", 98, 1, "", KA, 1),
 "068": ("Bolivya", "es", 87, 1, "Keçuva ve Aymara resmî ve yaygın.", GA, 0),
 "076": ("Brezilya", "pt", 99, 1, "", GA, 0),
 "084": ("Belize", "en", 63, 1, "İspanyolca ve Belize Kriolcesi de çok yaygın.", KA, 0),
 "092": ("Britanya Virjin Adaları", "en", 95, 1, "", KA, 1),
 "124": ("Kanada", "en", 87, 1, "Fransızca ikinci resmî dil; Quebec'te baskın (~%22 ana dil).", KA, 0),
 "136": ("Cayman Adaları", "en", 95, 1, "", KA, 1),
 "152": ("Şili", "es", 99, 1, "", GA, 0),
 "170": ("Kolombiya", "es", 99, 1, "", GA, 0),
 "188": ("Kosta Rika", "es", 97, 1, "", KA, 0),
 "192": ("Küba", "es", 100, 1, "", KA, 0),
 "212": ("Dominika", "en", 95, 1, "Fransız temelli Kwéyòl de konuşuluyor.", KA, 0),
 "214": ("Dominik Cumhuriyeti", "es", 98, 1, "", KA, 0),
 "218": ("Ekvador", "es", 95, 1, "Keçuva resmî statülü.", GA, 0),
 "222": ("El Salvador", "es", 99, 1, "", KA, 0),
 "238": ("Falkland Adaları", "en", 100, 1, "", GA, 1),
 "308": ("Grenada", "en", 95, 1, "", KA, 0),
 "320": ("Guatemala", "es", 78, 1, "20'den fazla Maya dili konuşuluyor (~%40).", KA, 0),
 "328": ("Guyana", "en", 90, 1, "Guyana Kreolcesi günlük konuşma dili.", GA, 0),
 "332": ("Haiti", "ht", 95, 1, "Fransızca da resmî; nüfusun küçük bir bölümü akıcı konuşuyor.", KA, 0),
 "340": ("Honduras", "es", 98, 1, "", KA, 0),
 "388": ("Jamaika", "jam", 90, 1, "İngilizce resmî dil; günlük konuşma dili Patois.", KA, 0),
 "484": ("Meksika", "es", 98, 1, "68 yerli dil ulusal dil statüsünde.", KA, 0),
 "531": ("Curaçao", "pap", 80, 1, "Felemenkçe ve İngilizce de resmî.", KA, 1),
 "533": ("Aruba", "pap", 70, 1, "Felemenkçe de resmî.", KA, 1),
 "534": ("Sint Maarten", "en", 85, 1, "Felemenkçe de resmî.", KA, 1),
 "558": ("Nikaragua", "es", 97, 1, "", KA, 0),
 "591": ("Panama", "es", 93, 1, "", KA, 0),
 "600": ("Paraguay", "gn", 77, 1, "İspanyolca da resmî; nüfusun büyük bölümü iki dilli.", GA, 0),
 "604": ("Peru", "es", 83, 1, "Keçuva ve Aymara resmî statülü.", GA, 0),
 "630": ("Porto Riko", "es", 95, 1, "İngilizce de resmî.", KA, 1),
 "652": ("Saint-Barthélemy", "fr", 95, 1, "", KA, 1),
 "659": ("Saint Kitts ve Nevis", "en", 95, 1, "", KA, 0),
 "660": ("Anguilla", "en", 95, 1, "", KA, 1),
 "662": ("Saint Lucia", "en", 90, 1, "Fransız temelli Kwéyòl yaygın.", KA, 0),
 "663": ("Saint-Martin", "fr", 90, 1, "", KA, 1),
 "666": ("Saint-Pierre ve Miquelon", "fr", 100, 1, "", KA, 1),
 "670": ("Saint Vincent ve Grenadinler", "en", 95, 1, "", KA, 0),
 "740": ("Surinam", "nl", 60, 1, "Sranan Tongo ülke genelinde ortak dil.", GA, 0),
 "780": ("Trinidad ve Tobago", "en", 95, 1, "", KA, 0),
 "796": ("Turks ve Caicos Adaları", "en", 95, 1, "", KA, 1),
 "840": ("Amerika Birleşik Devletleri", "en", 91, 1, "İspanyolca ana dil olarak ~%13.", KA, 0),
 "850": ("ABD Virjin Adaları", "en", 90, 1, "", KA, 1),
 "858": ("Uruguay", "es", 98, 1, "", GA, 0),
 "862": ("Venezuela", "es", 97, 1, "", GA, 0),
 # --- Okyanusya
 "016": ("Amerikan Samoası", "sm", 88, 1, "İngilizce de resmî.", OK, 1),
 "036": ("Avustralya", "en", 92, 1, "Evde 300'den fazla dil konuşuluyor.", OK, 0),
 "090": ("Solomon Adaları", "pis", 85, 1, "İngilizce resmî; 70'ten fazla yerel dil var.", OK, 0),
 "184": ("Cook Adaları", "rar", 70, 1, "İngilizce de resmî.", OK, 1),
 "242": ("Fiji", "fj", 54, 1, "Fiji Hintçesi ve İngilizce de resmî.", OK, 0),
 "258": ("Fransız Polinezyası", "fr", 95, 1, "Tahiti dili yaygın olarak konuşuluyor.", OK, 1),
 "296": ("Kiribati", "gil", 97, 1, "", OK, 0),
 "316": ("Guam", "en", 70, 1, "Çamorroca resmî dil; konuşan sayısı azalıyor.", OK, 1),
 "520": ("Nauru", "na", 95, 1, "", OK, 0),
 "540": ("Yeni Kaledonya", "fr", 97, 1, "30'dan fazla Kanak dili var.", OK, 1),
 "548": ("Vanuatu", "bi", 80, 1, "110'dan fazla yerel dil; İngilizce ve Fransızca da resmî.", OK, 0),
 "554": ("Yeni Zelanda", "en", 95, 1, "Maorice ve NZ işaret dili de resmî.", OK, 0),
 "570": ("Niue", "niu", 70, 1, "İngilizce de resmî.", OK, 1),
 "574": ("Norfolk Adası", "en", 95, 1, "Norfuk dili de resmî.", OK, 1),
 "580": ("Kuzey Mariana Adaları", "fil", 35, 0, "Çoğunluk dili yok; Çamorroca ve İngilizce de resmî.", OK, 1),
 "583": ("Mikronezya", "chk", 45, 0, "Çoğunluk dili yok; İngilizce ortak dil.", OK, 0),
 "584": ("Marshall Adaları", "mh", 98, 1, "", OK, 0),
 "585": ("Palau", "pau", 65, 1, "İngilizce de resmî.", OK, 0),
 "598": ("Papua Yeni Gine", "tpi", 70, 1, "840'tan fazla dille dünyanın en çok dilli ülkesi.", OK, 0),
 "612": ("Pitcairn Adaları", "en", 100, 1, "", OK, 1),
 "776": ("Tonga", "to", 98, 1, "", OK, 0),
 "882": ("Samoa", "sm", 99, 1, "", OK, 0),
 "876": ("Wallis ve Futuna", "fr", 80, 1, "Wallis ve Futuna dilleri günlük hayatta baskın.", OK, 1),
}

# ---------------------------------------------------------------- birleştir
mp = json.load(open("map_paths.json"))
feat = mp["f"]

missing = sorted(set(feat) - set(C))
extra = sorted(set(C) - set(feat))
if missing:
    print("HARİTADA VAR, VERİDE YOK:", [(k, feat[k]["n"]) for k in missing])
if extra:
    print("VERİDE VAR, HARİTADA YOK:", [(k, C[k][0]) for k in extra])
bad = sorted({c[1] for c in C.values()} - set(L))
if bad:
    print("TANIMSIZ DİL:", bad)
if missing or extra or bad:
    sys.exit(1)

bad_ids = sorted((set(MIX) | set(L2)) - set(C))
if bad_ids:
    print("MIX/L2'DE TANIMSIZ ÜLKE:", bad_ids)
    sys.exit(1)

# diaspora katmanını MIX'e karıştır: MIX'te olan dil dokunulmaz, kalanlar eklenir
added = 0
for cid, rows in DIASPORA.items():
    if cid not in C:
        print("DIASPORA'DA TANIMSIZ ÜLKE:", cid)
        sys.exit(1)
    cur = list(MIX.get(cid, []))
    have = {n for n, _ in cur}
    for name, pct in rows:
        if name not in have:
            cur.append((name, pct))
            have.add(name)
            added += 1
    MIX[cid] = sorted(cur, key=lambda r: -r[1])

no_pop = sorted(set(C) - set(POP))
if no_pop:
    print("NÜFUSU EKSİK ÜLKE:", [(i, C[i][0]) for i in no_pop])
    sys.exit(1)

countries = {}
for cid, (tr, lang, pct, maj, note, region, terr) in C.items():
    f = feat[cid]
    countries[cid] = {"n": tr, "en": f["n"], "l": lang, "p": pct, "m": maj,
                      "r": region, "t": terr, "pop": POP[cid],
                      "d": f["d"], "c": f["c"], "a": f["a"]}
    countries[cid]["re"] = i18n.REGION_EN.get(region, region)
    if note:
        countries[cid]["note"] = note
        if cid in i18n.NOTE_EN:
            countries[cid]["note_en"] = i18n.NOTE_EN[cid]
    if cid in MIX:
        countries[cid]["mix"] = [[n, p] for n, p in MIX[cid]]
    if cid in L2:
        countries[cid]["l2"] = [[n, p] for n, p in L2[cid]]

# --- konuşan sayıları: ülke nüfusu × dil payı (bin kişi)
#     MIX ana dil paylarını, L2 ikinci dil paylarını verir. Diller MIX içinde
#     Türkçe adlarıyla geçtiği için eşleştirme ada göre yapılır.
by_name = {}
for slug, (tr, *_rest) in L.items():
    by_name.setdefault(tr, slug)

speakers = {s: 0.0 for s in L}        # ana dil olarak
second = {s: 0.0 for s in L}          # ikinci dil olarak
where = {s: [] for s in L}            # [(cid, pay), …] — azınlık olduğu yerler dâhil

for cid, rows in MIX.items():
    pop = POP[cid]
    for name, pct in rows:
        slug = by_name.get(name)
        if slug is None:
            continue                   # 121 dilin dışında kalan yerel diller
        speakers[slug] += pop * pct / 100.0
        where[slug].append((cid, pct))
for cid, rows in L2.items():
    pop = POP[cid]
    for name, pct in rows:
        slug = by_name.get(name)
        if slug is not None:
            second[slug] += pop * pct / 100.0

# çoğunluk dili MIX satırında geçmiyorsa ülke indekste kaybolmasın
for cid, c in C.items():
    slug = c[1]
    if not any(i == cid for i, _ in where[slug]):
        where[slug].append((cid, c[2]))
        speakers[slug] += POP[cid] * c[2] / 100.0

langs = {}
for slug, (tr, endo, fam, grp) in L.items():
    ids = [cid for cid, c in C.items() if c[1] == slug]
    if not ids and slug not in REGIONAL:
        print("KULLANILMAYAN DİL:", slug, tr)
        continue
    rows = sorted(where[slug], key=lambda r: -POP[r[0]] * r[1])
    langs[slug] = {"n": tr, "e": endo, "f": fam, "g": grp,
                   **({"x": 1} if fam in LEXIFIER else {}),
                   "ne": i18n.LANG_EN.get(slug, tr),
                   "fe": i18n.FAM_EN.get(fam, fam),
                   "c": sum(1 for i in ids if not C[i][6]),
                   "t": sum(1 for i in ids if C[i][6]),
                   "s": round(speakers[slug]),
                   "s2": round(second[slug]),
                   "in": [[cid, pct] for cid, pct in rows]}

# ---------------------------------------------------------------- alt bölgeler
subs = {}
try:
    sp = json.load(open("sub_paths.json"))["s"]
except FileNotFoundError:
    sp = {}
    print("UYARI: sub_paths.json yok, alt bölge katmanı atlandı")

if sp:
    from subdiv import SUB, NAME, SUBPOP, US_FALLBACK
    unknown = sorted(set(SUB) - set(sp))
    if unknown:
        print("SUBDIV'DE TANIMSIZ BÖLGE:", unknown[:12], f"({len(unknown)} adet)")
        sys.exit(1)
    for sid, g in sp.items():
        cid = g["p"]
        rows = SUB.get(sid)
        if rows is None:
            rows = US_FALLBACK if cid == "840" else MIX.get(cid, [])
        mix = sorted(rows, key=lambda r: -r[1])
        # bölgenin baskın dili: 121 dil listesinde karşılığı olan ilk satır
        top = next((by_name[n] for n, _ in mix if n in by_name), C[cid][1])
        tr_name = NAME.get(sid, g["n"])
        subs[sid] = {"n": tr_name, "ne": i18n.SUB_EN.get(f"{cid}-{tr_name}", tr_name),
                     "p": cid, "l": top, "d": g["d"],
                     "c": g["c"], "a": g["a"],
                     "mix": [[n, p] for n, p in mix]}
        if sid in SUBPOP:
            subs[sid]["pop"] = SUBPOP[sid]

    # dil -> alt bölge indeksi (süzgeçte bölgeleri de vurgulamak için)
    for slug, tr in ((s, v[0]) for s, v in L.items()):
        hits = [[sid, p] for sid, s in subs.items()
                for n, p in s["mix"] if n == tr]
        if hits and slug in langs:
            langs[slug]["sub"] = sorted(hits, key=lambda r: -r[1])

out = {"w": mp["w"], "h": mp["h"], "grat": mp["grat"], "eq": mp["eq"], "frame": mp["frame"],
       "countries": countries, "langs": langs, "subs": subs,
       "groups": {k: {"n": v[0], "d": v[1],
                      "ne": i18n.GROUP_EN[k][0], "de": i18n.GROUP_EN[k][1]}
                  for k, v in GROUPS.items()},
       "tx": i18n.name_map({v[0]: i18n.LANG_EN.get(k, v[0]) for k, v in L.items()})}
json.dump(out, open("data.json", "w"), separators=(",", ":"), ensure_ascii=False)

print(f"ülke/bölge: {len(countries)}  dil: {len(langs)}  "
      f"boyut: {len(json.dumps(out, ensure_ascii=False))/1024:.0f} KB")
from collections import Counter
cnt = Counter(L[c[1]][3] for c in C.values())
for g, (name, _) in GROUPS.items():
    print(f"  {g} {name}: {cnt[g]}")
top = sorted(langs.items(), key=lambda kv: -(kv[1]["c"] + kv[1]["t"]))[:12]
print("  en yaygın:", ", ".join(f"{v['n']} {v['c']}+{v['t']}" for _, v in top))
tops = sorted(langs.items(), key=lambda kv: -kv[1]["s"])[:12]
print("  en çok konuşan:", ", ".join(f"{v['n']} {v['s']/1000:.0f}mn" for _, v in tops))
print(f"  toplam nüfus: {sum(POP.values())/1e6:.2f} milyar  ·  "
      f"ana dili sayılan: {sum(v['s'] for v in langs.values())/1e6:.2f} milyar")
print("  çoğunluk dili olmayan:", sum(1 for c in C.values() if not c[3]))
print(f"  dil dağılımı olan: {len(MIX)}/{len(C)}  ·  ikinci dil verisi olan: {len(L2)}/{len(C)}")
print(f"  diaspora katmanı: {len(DIASPORA)} ülkeye {added} satır eklendi  ·  "
      f"toplam MIX satırı: {sum(len(v) for v in MIX.values())}")
tr_in = langs["tr"]["in"]
print("  Türkçe:", ", ".join(f"{countries[i]['n']} %{p}" for i, p in tr_in))
eksik = sorted(set(C) - set(MIX))
if eksik:
    print("  dağılımı olmayan:", ", ".join(C[i][0] for i in eksik))
