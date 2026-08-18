"""Ülke nüfusları — bin kişi cinsinden, 2024 civarı tahminler.

Kaynak: BM Nüfus Bölümü (World Population Prospects 2024) ve bağımlı bölgeler
için ulusal istatistik kurumları. Değerler yuvarlanmıştır; konuşan sayısı
hesapları bu yüzden kesin değil, büyüklük mertebesi olarak okunmalıdır.
"""

POP = {
    "004": 42650,   # Afganistan
    "008": 2750,    # Arnavutluk
    "012": 46800,   # Cezayir
    "016": 47,      # Amerikan Samoası
    "020": 81,      # Andorra
    "024": 37900,   # Angola
    "028": 94,      # Antigua ve Barbuda
    "031": 10200,   # Azerbaycan
    "032": 46000,   # Arjantin
    "036": 27200,   # Avustralya
    "040": 9150,    # Avusturya
    "044": 412,     # Bahamalar
    "048": 1500,    # Bahreyn
    "050": 173000,  # Bangladeş
    "051": 3000,    # Ermenistan
    "052": 282,     # Barbados
    "056": 11800,   # Belçika
    "060": 64,      # Bermuda
    "064": 790,     # Butan
    "068": 12400,   # Bolivya
    "070": 3200,    # Bosna-Hersek
    "072": 2700,    # Botsvana
    "076": 212000,  # Brezilya
    "084": 420,     # Belize
    "086": 3,       # Britanya Hint Okyanusu Toprakları
    "090": 820,     # Solomon Adaları
    "092": 39,      # Britanya Virjin Adaları
    "096": 460,     # Brunei
    "100": 6400,    # Bulgaristan
    "104": 54500,   # Myanmar
    "108": 13200,   # Burundi
    "112": 9100,    # Belarus
    "116": 17400,   # Kamboçya
    "120": 29100,   # Kamerun
    "124": 41300,   # Kanada
    "132": 525,     # Cabo Verde
    "136": 74,      # Cayman Adaları
    "140": 5700,    # Orta Afrika Cumhuriyeti
    "144": 22200,   # Sri Lanka
    "148": 19300,   # Çad
    "152": 19800,   # Şili
    "156": 1410000, # Çin
    "158": 23400,   # Tayvan
    "170": 52300,   # Kolombiya
    "174": 870,     # Komorlar
    "178": 6100,    # Kongo Cumhuriyeti
    "180": 106000,  # Demokratik Kongo Cumhuriyeti
    "184": 15,      # Cook Adaları
    "188": 5100,    # Kosta Rika
    "191": 3850,    # Hırvatistan
    "192": 11000,   # Küba
    "196": 950,     # Kıbrıs
    "203": 10900,   # Çekya
    "204": 14100,   # Benin
    "208": 5950,    # Danimarka
    "212": 67,      # Dominika
    "214": 11300,   # Dominik Cumhuriyeti
    "218": 18100,   # Ekvador
    "222": 6350,    # El Salvador
    "226": 1750,    # Ekvator Ginesi
    "231": 129000,  # Etiyopya
    "232": 3700,    # Eritre
    "233": 1370,    # Estonya
    "234": 54,      # Faroe Adaları
    "238": 4,       # Falkland Adaları
    "242": 930,     # Fiji
    "246": 5600,    # Finlandiya
    "248": 30,      # Åland
    "250": 68400,   # Fransa
    "258": 280,     # Fransız Polinezyası
    "262": 1150,    # Cibuti
    "266": 2500,    # Gabon
    "268": 3700,    # Gürcistan
    "270": 2800,    # Gambiya
    "275": 5500,    # Filistin
    "276": 84500,   # Almanya
    "288": 34400,   # Gana
    "296": 133,     # Kiribati
    "300": 10400,   # Yunanistan
    "304": 57,      # Grönland
    "308": 117,     # Grenada
    "316": 172,     # Guam
    "320": 18100,   # Guatemala
    "324": 14800,   # Gine
    "328": 830,     # Guyana
    "332": 11800,   # Haiti
    "336": 1,       # Vatikan
    "340": 10600,   # Honduras
    "344": 7500,    # Hong Kong
    "348": 9600,    # Macaristan
    "352": 390,     # İzlanda
    "356": 1441000, # Hindistan
    "360": 281000,  # Endonezya
    "364": 89000,   # İran
    "368": 45500,   # Irak
    "372": 5350,    # İrlanda
    "376": 9900,    # İsrail
    "380": 58900,   # İtalya
    "384": 31900,   # Fildişi Sahili
    "388": 2830,    # Jamaika
    "392": 123500,  # Japonya
    "398": 20300,   # Kazakistan
    "400": 11400,   # Ürdün
    "404": 55100,   # Kenya
    "408": 26500,   # Kuzey Kore
    "410": 51700,   # Güney Kore
    "414": 4850,    # Kuveyt
    "417": 7100,    # Kırgızistan
    "418": 7800,    # Laos
    "422": 5800,    # Lübnan
    "426": 2340,    # Lesotho
    "428": 1870,    # Letonya
    "430": 5600,    # Liberya
    "434": 7400,    # Libya
    "438": 40,      # Liechtenstein
    "440": 2880,    # Litvanya
    "442": 670,     # Lüksemburg
    "446": 720,     # Makao
    "450": 31000,   # Madagaskar
    "454": 21400,   # Malavi
    "458": 34600,   # Malezya
    "462": 530,     # Maldivler
    "466": 23800,   # Mali
    "470": 550,     # Malta
    "478": 5000,    # Moritanya
    "480": 1270,    # Mauritius
    "484": 130000,  # Meksika
    "492": 39,      # Monako
    "496": 3500,    # Moğolistan
    "498": 2470,    # Moldova
    "499": 620,     # Karadağ
    "500": 4,       # Montserrat
    "504": 37800,   # Fas
    "508": 34600,   # Mozambik
    "512": 5300,    # Umman
    "516": 3050,    # Namibya
    "520": 12,      # Nauru
    "524": 30900,   # Nepal
    "528": 18100,   # Hollanda
    "531": 155,     # Curaçao
    "533": 108,     # Aruba
    "534": 44,      # Sint Maarten
    "540": 273,     # Yeni Kaledonya
    "548": 335,     # Vanuatu
    "554": 5340,    # Yeni Zelanda
    "558": 7050,    # Nikaragua
    "562": 27200,   # Nijer
    "566": 229000,  # Nijerya
    "570": 2,       # Niue
    "574": 2,       # Norfolk Adası
    "578": 5570,    # Norveç
    "580": 47,      # Kuzey Mariana Adaları
    "583": 115,     # Mikronezya
    "584": 42,      # Marshall Adaları
    "585": 18,      # Palau
    "586": 245000,  # Pakistan
    "591": 4500,    # Panama
    "598": 10900,   # Papua Yeni Gine
    "600": 6900,    # Paraguay
    "604": 34200,   # Peru
    "608": 115000,  # Filipinler
    "612": 0.05,    # Pitcairn Adaları
    "616": 36600,   # Polonya
    "620": 10600,   # Portekiz
    "624": 2200,    # Gine-Bissau
    "626": 1400,    # Doğu Timor
    "630": 3200,    # Porto Riko
    "634": 3050,    # Katar
    "642": 19000,   # Romanya
    "643": 144000,  # Rusya
    "646": 14300,   # Ruanda
    "652": 11,      # Saint-Barthélemy
    "654": 5,       # Saint Helena
    "659": 47,      # Saint Kitts ve Nevis
    "660": 16,      # Anguilla
    "662": 180,     # Saint Lucia
    "663": 32,      # Saint-Martin
    "666": 6,       # Saint-Pierre ve Miquelon
    "670": 100,     # Saint Vincent ve Grenadinler
    "674": 34,      # San Marino
    "678": 235,     # São Tomé ve Príncipe
    "682": 33300,   # Suudi Arabistan
    "686": 18400,   # Senegal
    "688": 6600,    # Sırbistan
    "690": 107,     # Seyşeller
    "694": 8800,    # Sierra Leone
    "702": 6000,    # Singapur
    "703": 5400,    # Slovakya
    "704": 100300,  # Vietnam
    "705": 2120,    # Slovenya
    "706": 18100,   # Somali
    "710": 63000,   # Güney Afrika
    "716": 16700,   # Zimbabve
    "724": 48800,   # İspanya
    "728": 11500,   # Güney Sudan
    "729": 48000,   # Sudan
    "732": 590,     # Batı Sahra
    "740": 620,     # Surinam
    "748": 1230,    # Esvatini
    "752": 10600,   # İsveç
    "756": 8900,    # İsviçre
    "760": 24000,   # Suriye
    "762": 10400,   # Tacikistan
    "764": 71700,   # Tayland
    "768": 9300,    # Togo
    "776": 105,     # Tonga
    "780": 1370,    # Trinidad ve Tobago
    "784": 10500,   # Birleşik Arap Emirlikleri
    "788": 12100,   # Tunus
    "792": 85700,   # Türkiye
    "795": 7200,    # Türkmenistan
    "796": 47,      # Turks ve Caicos Adaları
    "800": 49000,   # Uganda
    "804": 37000,   # Ukrayna
    "807": 1830,    # Kuzey Makedonya
    "818": 114000,  # Mısır
    "826": 69000,   # Birleşik Krallık
    "831": 64,      # Guernsey
    "832": 103,     # Jersey
    "833": 85,      # Man Adası
    "834": 68500,   # Tanzanya
    "840": 342000,  # Amerika Birleşik Devletleri
    "850": 85,      # ABD Virjin Adaları
    "854": 23500,   # Burkina Faso
    "858": 3400,    # Uruguay
    "860": 37000,   # Özbekistan
    "862": 28800,   # Venezuela
    "876": 11,      # Wallis ve Futuna
    "882": 220,     # Samoa
    "887": 35000,   # Yemen
    "894": 21300,   # Zambiya
    "900": 1600,    # Kosova
    "901": 390,     # Kuzey Kıbrıs
    "902": 5700,    # Somaliland
}
