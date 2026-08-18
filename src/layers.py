#!/usr/bin/env python3
"""İki yeni harita katmanının verisi: yazı sistemi ve resmî dil.

Ana harita "evde hangi dil konuşuluyor" sorusunu yanıtlıyor. Buradaki iki
katman aynı ülkelere başka iki soru soruyor:

  yazı  — o dil hangi alfabeyle yazılıyor? Aile haritasının söylemediği bir
          şey söylüyor: Türkçe, Vietnamca ve Endonezce akraba değil ama üçü
          de Latin; Sırpça ile Hırvatça aynı dil sayılabilecek kadar yakın
          ama biri Kiril biri Latin.
  resmî — devletin dili ile evin dili aynı mı? Afrika'nın yarısında değil.

Yazı verisi elle yazılmıyor: dilin kendi adındaki (endonim) harflerin Unicode
bloğundan çıkarılıyor, aşağıda yalnız istisnalar duruyor. Resmî dil tablosu
elle derlendi; kaynaklar ve sınırları DATA.md'de.
"""

# --------------------------------------------------------------- yazı sistemi
# Unicode blok adı -> (anahtar, Türkçe ad, renk grubu). Anahtar data.json'a
# gider, ad ayrıntı kartında görünür, grup haritayı boyar.
#
# Renk grupları mevcut sekiz aile renginin ta kendisi. Katman değişince
# gösterge de değiştiği için çakışma olmuyor; karşılığında koda yeni bir
# palet araması girmiyor (palet OKLCH'te aranıp renk körlüğü modeliyle
# doğrulanmıştı, ikinci bir sekizliyi aynı kalitede üretmek ayrı bir iş).
LAT, CYR, ARA, BRH, SEA, CJK, ALP, GEZ, OTH = (
    "lat", "cyr", "ara", "brh", "sea", "cjk", "alp", "gez", "oth")

SCRIPTS = {
    "latn": ("Latin", LAT),
    "cyrl": ("Kiril", CYR),
    "arab": ("Arap", ARA),
    "deva": ("Devanagari", BRH),
    "beng": ("Bengal", BRH),
    "gujr": ("Gucarat", BRH),
    "guru": ("Gurmukhi", BRH),
    "orya": ("Odia", BRH),
    "taml": ("Tamil", BRH),
    "telu": ("Telugu", BRH),
    "knda": ("Kannada", BRH),
    "mlym": ("Malayalam", BRH),
    "sinh": ("Sinhala", BRH),
    "mtei": ("Meetei Mayek", BRH),
    "thai": ("Tay", SEA),
    "laoo": ("Lao", SEA),
    "khmr": ("Khmer", SEA),
    "mymr": ("Myanmar", SEA),
    "tibt": ("Tibet", SEA),
    "hani": ("Han (Çin yazısı)", CJK),
    "jpan": ("Kanji + kana", CJK),
    "hang": ("Hangıl", CJK),
    "grek": ("Yunan", ALP),
    "armn": ("Ermeni", ALP),
    "geor": ("Gürcü", ALP),
    "hebr": ("İbrani", ALP),
    "ethi": ("Ge'ez", GEZ),
    "thaa": ("Thaana", OTH),
    "cans": ("Kanada hece yazısı", OTH),
    "tfng": ("Tifinagh", OTH),
    "yiii": ("Yi hece yazısı", OTH),
    "olck": ("Ol Chiki", OTH),
}

SCRIPT_GROUPS = {
    LAT: ("Latin", "Avrupa'nın batısı, Amerika, Afrika'nın çoğu, Güneydoğu Asya"),
    CYR: ("Kiril", "Rusya, Balkanlar'ın doğusu, Orta Asya'nın bir bölümü"),
    ARA: ("Arap", "Kuzey Afrika, Ortadoğu, İran, Pakistan"),
    BRH: ("Brahmi kökenli · Güney Asya", "Devanagari, Bengal, Tamil, Telugu, Sinhala…"),
    SEA: ("Brahmi kökenli · Güneydoğu Asya", "Tay, Lao, Khmer, Myanmar, Tibet"),
    CJK: ("Doğu Asya", "Han yazısı, Japon kana'sı, Kore hangıl'ı"),
    ALP: ("Diğer alfabe ve ebcedler", "Yunan, Ermeni, Gürcü, İbrani"),
    GEZ: ("Ge'ez", "Amharca ve Tigrinya — Afrika'nın kendi yazısı"),
    OTH: ("Diğer", "Thaana, Kanada hece yazısı, Tifinagh, Yi, Ol Chiki"),
}

# Endonimden çıkarım yanlış ya da eksik kalıyorsa buradan düzeltiliyor.
SCRIPT_FIX = {
    "ja": "jpan",     # 日本語 sadece kanji görünüyor; yazı kanji + hiragana + katakana
    "kok": "deva",    # Goa'da Devanagari resmî; Latin ve Kannada da kullanılıyor
    "mni": "mtei",    # Unicode adı "MEETEI MAYEK"
    "iu": "cans",     # Unicode adı "CANADIAN ABORIGINAL SYLLABICS"
    "zh": "hani",
    "yue": "hani",
}

# İki yazılı diller (digrafya). Harita ana yazıyı boyar, ikincisi kartta
# yazar. Bu liste katmanın asıl anlattığı şey: yazı dilin değil devletin
# ve tarihin seçimi.
SCRIPT2 = {
    "sr":  ("latn", "Kiril resmî yazı; Latin de her yerde kullanılıyor"),
    "bs":  ("cyrl", "Anayasada iki yazı da eşit; günlük kullanım Latin"),
    "uz":  ("cyrl", "1993'te Latin'e geçildi; Kiril hâlâ yaygın"),
    "kk":  ("latn", "2023–2031 arası kademeli Latin'e geçiş sürüyor"),
    "ku":  ("arab", "Türkiye ve Suriye'de Latin, Irak ve İran'da Arap yazısı"),
    "pa":  ("arab", "Hindistan'da Gurmukhi, Pakistan'da Şahmukhi (Arap yazısı)"),
    "ms":  ("arab", "Latin (Rumi) esas; Brunei'de Cavi (Arap yazısı) da resmî"),
    "mn":  ("latn", "Moğolistan'da Kiril; geleneksel Moğol yazısı geri getiriliyor"),
    "ha":  ("arab", "Latin (Boko) esas; Acemî (Arap yazısı) dinî metinlerde"),
    "ko":  ("hani", "Hangıl esas; Hanca (Çin karakterleri) sınırlı kullanımda"),
    "iu":  ("latn", "Nunavut'ta hece yazısı, batıda Latin"),
    "az":  ("arab", "Azerbaycan'da Latin, İran'da Arap yazısı"),
    "tzm": ("arab", "Fas'ta Tifinagh resmî; Cezayir'de Latin de kullanılıyor"),
}

# --------------------------------------------------------------- resmî diller
# Yalnız resmî dil olarak geçen, hiçbir ülkede/bölgede çoğunluk olmayan
# diller. L tablosuna eklenirler; dizinde "yalnız resmî" olarak işaretlenir.
OFFICIAL_ONLY = {
    "ga":  ("İrlandaca", "Gaeilge", "Hint-Avrupa · Kelt", "ine"),
    "ps":  ("Peştuca", "پښتو", "Hint-Avrupa · Hint-İran", "ine"),
    "tzm": ("Berberi (Tamazight)", "ⵜⴰⵎⴰⵣⵉⵖⵜ", "Afro-Asyatik · Berberi", "afa"),
    "af":  ("Afrikaanca", "Afrikaans", "Hint-Avrupa · Cermen", "ger"),
    "be":  ("Belarusça", "Беларуская", "Hint-Avrupa · Slav", "ine"),
    "nd":  ("Ndebele", "isiNdebele", "Nijer-Kongo · Bantu", "nkg"),
    "mi":  ("Maorice", "Te Reo Māori", "Avustronezya · Okyanusya", "aus"),
    "rm":  ("Romanşça", "Rumantsch", "Hint-Avrupa · Roman", "rom"),
    "la":  ("Latince", "Latina", "Hint-Avrupa · İtalik", "rom"),
    "ho":  ("Hiri Motu", "Hiri Motu", "Avustronezya · Okyanusya", "aus"),
    "hif": ("Fiji Hintçesi", "फ़िजी हिंदी", "Hint-Avrupa · Hint-Aryan", "ine"),
    "ch":  ("Çamorroca", "Chamoru", "Avustronezya · Malayo-Polinezya", "aus"),
    "xh":  ("Xhosa", "isiXhosa", "Nijer-Kongo · Bantu", "nkg"),
}

# ülke -> hukuken (de jure) resmî diller, yasal öncelik sırasıyla.
# Sıra önemli: harita ilk sıradaki dile göre boyanıyor. İrlanda'da Anayasa
# İrlandacayı "birinci resmî dil" sayar, günlük hayatın dili İngilizcedir —
# katmanın göstermek istediği tam olarak bu fark.
OFFICIAL = {
    # --- Avrupa
    "008": ("sq",),
    "020": ("ca",),
    "040": ("de",),
    "056": ("nl", "fr", "de"),
    "070": ("bs", "hr", "sr"),
    "100": ("bg",),
    "112": ("be", "ru"),
    "191": ("hr",),
    "196": ("el", "tr"),
    "203": ("cs",),
    "208": (),
    "233": ("et",),
    "234": ("fo", "da"),
    "246": ("fi", "sv"),
    "248": ("sv",),
    "250": ("fr",),
    "268": ("ka",),
    "276": ("de",),
    "300": ("el",),
    "304": ("kl",),
    "336": ("it", "la"),
    "348": ("hu",),
    "352": ("is",),
    "372": ("ga", "en"),
    "376": ("he",),
    "380": ("it",),
    "428": ("lv",),
    "438": ("de",),
    "440": ("lt",),
    "442": ("lb", "fr", "de"),
    "470": ("mt", "en"),
    "492": ("fr",),
    "498": ("ro",),
    "499": ("cnr",),
    "500": ("en",),
    "528": ("nl",),
    "578": ("no",),
    "616": ("pl",),
    "620": ("pt",),
    "642": ("ro",),
    "643": ("ru",),
    "688": ("sr",),
    "703": ("sk",),
    "705": ("sl",),
    "724": ("es",),
    "752": ("sv",),
    "756": ("de", "fr", "it", "rm"),
    "792": ("tr",),
    "804": ("uk",),
    "807": ("mk", "sq"),
    "900": ("sq", "sr"),
    "901": ("tr",),
    # --- Asya
    "004": ("ps", "prs"),
    "031": ("az",),
    "048": ("ar",),
    "050": ("bn",),
    "051": ("hy",),
    "064": ("dz",),
    "096": ("ms",),
    "104": ("my",),
    "116": ("km",),
    "144": ("si", "ta"),
    "156": ("zh",),
    "275": ("ar",),
    "344": ("yue", "en"),
    "356": ("hi", "en"),
    "360": ("id",),
    "364": ("fa",),
    "368": ("ar", "ku"),
    "392": (),
    "398": ("kk", "ru"),
    "400": ("ar",),
    "408": ("ko",),
    "410": ("ko",),
    "414": ("ar",),
    "417": ("ky", "ru"),
    "418": ("lo",),
    "422": ("ar",),
    "446": ("yue", "pt"),
    "458": ("ms",),
    "462": ("dv",),
    "496": ("mn",),
    "512": ("ar",),
    "524": ("ne",),
    "586": ("ur", "en"),
    "608": ("fil", "en"),
    "626": ("tet", "pt"),
    "634": ("ar",),
    "682": ("ar",),
    "702": ("ms", "en", "zh", "ta"),
    "704": ("vi",),
    "760": ("ar",),
    "762": ("tg",),
    "764": ("th",),
    "784": ("ar",),
    "795": ("tk",),
    "860": ("uz",),
    "887": ("ar",),
    # --- Afrika
    "012": ("ar", "tzm"),
    "024": ("pt",),
    "072": ("en",),
    "086": ("en",),
    "108": ("rn", "en", "fr"),
    "120": ("fr", "en"),
    "132": ("pt",),
    "140": ("sg", "fr"),
    "148": ("ar", "fr"),
    "174": ("zdj", "ar", "fr"),
    "178": ("fr",),
    "180": ("fr",),
    "204": ("fr",),
    "226": ("es", "fr", "pt"),
    "231": ("am", "so", "ti"),
    "232": (),
    "262": ("ar", "fr"),
    "266": ("fr",),
    "270": ("en",),
    "288": ("en",),
    "324": ("fr",),
    "384": ("fr",),
    "404": ("sw", "en"),
    "426": ("st", "en"),
    "430": ("en",),
    "434": ("ar",),
    "450": ("mg", "fr"),
    "454": ("en",),
    "466": ("bm",),
    "478": ("ar",),
    "480": (),
    "504": ("ar", "tzm"),
    "508": ("pt",),
    "516": ("en",),
    "562": ("ha",),
    "566": ("en",),
    "624": ("pt",),
    "646": ("rw", "en", "fr", "sw"),
    "654": ("en",),
    "678": ("pt",),
    "686": ("fr",),
    "690": ("crs", "en", "fr"),
    "694": ("en",),
    "706": ("so", "ar"),
    "710": ("zu", "xh", "af", "en"),
    "716": ("sn", "nd", "en"),
    "728": ("en",),
    "729": ("ar", "en"),
    "732": ("ar", "es"),
    "748": ("ss", "en"),
    "768": ("fr",),
    "788": ("ar",),
    "800": ("en", "sw"),
    "818": ("ar",),
    "834": ("sw", "en"),
    "854": ("mos", "bm", "ff"),
    "894": ("en",),
    "902": ("so", "ar"),
    # --- Kuzey Amerika
    "028": ("en",),
    "044": ("en",),
    "052": ("en",),
    "060": ("en",),
    "084": ("en",),
    "092": ("en",),
    "124": ("en", "fr"),
    "136": ("en",),
    "188": ("es",),
    "192": ("es",),
    "212": ("en",),
    "214": ("es",),
    "222": ("es",),
    "308": ("en",),
    "320": ("es",),
    "332": ("fr", "ht"),
    "340": ("es",),
    "388": (),
    "484": (),
    "531": ("nl", "pap", "en"),
    "533": ("nl", "pap"),
    "534": ("nl", "en"),
    "558": ("es",),
    "591": ("es",),
    "630": ("es", "en"),
    "652": ("fr",),
    "659": ("en",),
    "660": ("en",),
    "662": ("en",),
    "663": ("fr",),
    "666": ("fr",),
    "670": ("en",),
    "780": ("en",),
    "796": ("en",),
    "840": ("en",),
    "850": ("en",),
    # --- Güney Amerika
    "032": (),
    "068": ("es", "qu", "ay", "gn"),
    "076": ("pt",),
    "152": (),
    "170": ("es",),
    "218": ("es", "qu"),
    "238": ("en",),
    "328": ("en",),
    "600": ("es", "gn"),
    "604": ("es", "qu", "ay"),
    "740": ("nl",),
    "858": (),
    "862": ("es",),
    # --- Okyanusya
    "016": ("en", "sm"),
    "036": (),
    "090": ("en",),
    "184": ("en", "rar"),
    "242": ("en", "fj", "hif"),
    "258": ("fr",),
    "296": ("gil", "en"),
    "316": ("en", "ch"),
    "520": ("na", "en"),
    "540": ("fr",),
    "548": ("bi", "en", "fr"),
    "554": ("mi",),
    "570": ("niu", "en"),
    "574": ("en",),
    "580": ("en", "ch"),
    "583": ("en",),
    "584": ("mh", "en"),
    "585": ("pau", "en"),
    "598": ("en", "tpi", "ho"),
    "612": ("en",),
    "776": ("to", "en"),
    "876": ("fr",),
    "882": ("sm", "en"),
    # --- kalan bağımlı topraklar (İngiliz tacı / deniz aşırı)
    "826": (),
    "831": (),
    "832": (),
    "833": (),
    "158": (),
    "674": (),
}

# Hukuken resmî olmadığı hâlde devletin fiilen kullandığı dil. Yukarıdaki
# tabloda boş demet duran ülkeler burada karşılığını bulur; ayrıca resmî
# dilin yanında ayrı bir fiilî dil varsa (Yeni Zelanda) yine burada durur.
DE_FACTO = {
    "032": ("es",),
    "036": ("en",),
    "152": ("es",),
    "158": ("zh",),
    "208": ("da",),
    "232": ("ti", "ar", "en"),
    "388": ("en",),
    "392": ("ja",),
    "480": ("en", "fr"),
    "484": ("es",),
    "554": ("en",),
    "674": ("it",),
    "826": ("en",),
    "831": ("en",),
    "832": ("en",),
    "833": ("en",),
    "858": ("es",),
}

# Katmanın anlattığı ayrıntılar. Ülke kartında resmî dil satırının altına
# düşer; hepsi ya bir uyumsuzluğu ya da hukukla hayatın ayrıldığı bir yeri
# anlatıyor.
OFF_NOTE = {
    "032": "Anayasada resmî dil yok; İspanyolca fiilî devlet dili.",
    "036": "Anayasada resmî dil yok; İngilizce fiilî devlet dili.",
    "090": "İngilizce resmî; sokakta ve mecliste ortak dil Solomon Pijini.",
    "112": "Belarusça anayasal olarak birinci dil; günlük hayatta Rusça baskın.",
    "152": "Anayasada resmî dil yok; İspanyolca fiilî devlet dili.",
    "158": "1949'dan beri fiilî devlet dili Mandarin; 2018 yasası bütün "
           "yerli dilleri \"ulusal dil\" saydı.",
    "204": "Fransızca tek resmî dil; evde en yaygın diller Fon ve Yoruba.",
    "208": "Anayasada resmî dil yok; Danca fiilî devlet dili. Komşusu İsveç "
           "2009'da İsveççeyi yasayla resmî yapmıştı.",
    "262": "Arapça ve Fransızca resmî; halkın çoğunluğu Somalice konuşuyor.",
    "324": "Fransızca tek resmî dil; en büyük ana dil Fulaca.",
    "232": "Resmî dil ilan edilmedi; Tigrinya, Arapça ve İngilizce çalışma dili.",
    "072": "İngilizce tek resmî dil; Setsvana ulusal dil ve halkın dili.",
    "132": "Portekizce resmî; anayasa Kriolu'nun resmîleştirilmesini öngörür "
           "ama adım henüz atılmadı.",
    "270": "İngilizce resmî; halkın çoğunluğu evde Mandinka konuşuyor.",
    "344": "Yasa yalnız \"Çince\" der; konuşulan resmî çeşit Kantonca, "
           "yazı geleneksel Çin karakterleri.",
    "288": "İngilizce resmî; evde en yaygın dil Akanca.",
    "356": "Birlik düzeyinde Hintçe ve İngilizce; anayasa listesinde 22 dil var.",
    "372": "Anayasa İrlandacayı birinci resmî dil sayar; günlük dil İngilizce.",
    "388": "Resmî dil ilan edilmedi; İngilizce yönetim dili, evde Patois.",
    "392": "Resmî dil ilan edilmedi; Japonca fiilî devlet dili.",
    "446": "Yasa yalnız \"Çince\" der; konuşulan resmî çeşit Kantonca.",
    "454": "İngilizce tek resmî dil; Çeva ulusal dil ve halkın dili.",
    "466": "2023 anayasası Fransızcanın resmî statüsünü kaldırdı; 13 ulusal "
           "dil resmî oldu.",
    "480": "Anayasada resmî dil yok; meclisin dili İngilizce, evde Kreol.",
    "484": "Anayasada resmî dil yok; 68 yerli dil İspanyolcayla eşit \"ulusal dil\".",
    "516": "Tek resmî dil İngilizce; evde en yaygın diller Oşivambo ve Afrikaanca.",
    "554": "İngilizce hiç resmî ilan edilmedi; hukuken resmî diller Maorice "
           "(1987) ve Yeni Zelanda İşaret Dili (2006).",
    "562": "2025'te Hausa ulusal dil, Fransızca ve İngilizce çalışma dili oldu.",
    "566": "İngilizce resmî; sokakta ortak dil Nijerya Pidgini.",
    "580": "Resmî diller İngilizce, Çamorroca ve Karolince; evde en yaygın "
           "dil ise göçle gelen Filipince.",
    "583": "Federal resmî dil İngilizce; Çuukça gibi ada dilleri eyalet "
           "düzeyinde tanınıyor.",
    "624": "Portekizce resmî; sokakta ortak dil Gine-Bissau Kreolcesi.",
    "643": "Federasyon genelinde 30'dan fazla dil cumhuriyet düzeyinde resmî.",
    "674": "Anayasada resmî dil yok; İtalyanca fiilî devlet dili.",
    "686": "Fransızca resmî; halkın çoğunluğu Volofça konuşuyor.",
    "694": "İngilizce resmî; evde ortak dil Krio.",
    "702": "Dört resmî dil; Malayca ulusal dil, yönetim dili İngilizce.",
    "710": "12 resmî dil (2023'ten beri işaret dili dâhil).",
    "716": "16 resmî dil — dünyanın en uzun listesi.",
    "728": "İngilizce tek resmî dil; sokakta ortak dil Cuba Arapçası.",
    "768": "Fransızca tek resmî dil; Eve ve Kabiye ulusal dil sayılıyor.",
    "800": "Resmî diller İngilizce ve Svahili; başkentin ve güneyin dili "
           "Ganda hiç resmî olmadı.",
    "826": "Anayasal düzeyde resmî dil yok; Galce Galler'de, Gaelce "
           "İskoçya'da yasayla korunuyor.",
    "840": "2025 başkanlık kararnamesiyle İngilizce resmî dil ilan edildi; "
           "federal yasada resmî dil hükmü yok.",
    "854": "2024 anayasası Mòoré, Diula ve Fulfulde'yi resmî yaptı; "
           "Fransızca çalışma diline indi.",
    "858": "Anayasada resmî dil yok; İspanyolca fiilî devlet dili.",
    "894": "İngilizce tek resmî dil; yedi dil bölgesel olarak tanınıyor, "
           "en büyüğü Bemba.",
    "902": "Tanınmamış devlet; Somalice ve Arapça resmî.",
}
