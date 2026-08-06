"""Göçmen ve azınlık toplulukları — ana MIX tablosunun altındaki ince kuyruk.

MIX tablosu ülkelerin baskın dillerini verir ve pratikte ~%1'in altındaki
toplulukları dışarıda bırakır. Oysa Belçika'daki ya da İsveç'teki Türkçe gibi
pek çok topluluk tam da o eşiğin altında kalır. Bu tablo onları ekler.

Değerler: dili evde konuşan kişilerin ülke nüfusuna oranı (yüzde). Köken/soy
sayısı değil — ikinci kuşakta dil kaybı olduğu için ikisi farklıdır. Kaynak:
ulusal nüfus sayımlarının dil soruları (Kanada, Avustralya, ABD ACS, İsviçre,
Yeni Zelanda), Eurostat göç istatistikleri ve ülke bazlı topluluk tahminleri.
MIX'te zaten bulunan bir dil buradan tekrar eklenmez.
"""

DIASPORA = {
    # ---------------------------------------------------------- Batı Avrupa
    "276": [  # Almanya
        ("Ukraynaca", 1.4), ("Kürtçe", 1.2), ("Arapça", 1.2), ("Romence", 1),
        ("İtalyanca", 0.8), ("Sırp-Hırvatça", 0.8), ("İngilizce", 0.5),
        ("Bulgarca", 0.4), ("Yunanca", 0.4), ("Farsça", 0.3), ("İspanyolca", 0.3),
        ("Hırvatça", 0.3), ("Fransızca", 0.2), ("Vietnamca", 0.2),
        ("Mandarin Çincesi", 0.2), ("Filipince", 0.1),
    ],
    "250": [  # Fransa
        ("Berberice", 1.5), ("Almanca", 0.6), ("İspanyolca", 0.6),
        ("Türkçe", 0.6), ("İtalyanca", 0.5), ("Mandarin Çincesi", 0.4),
        ("Romence", 0.3), ("Vietnamca", 0.3), ("Ermenice", 0.3), ("İngilizce", 0.3),
        ("Lehçe", 0.2), ("Rusça", 0.2), ("Tamilce", 0.2), ("Volofça", 0.2),
        ("Lingala", 0.2), ("Haiti Kreolcesi", 0.2),
    ],
    "056": [  # Belçika
        ("Arapça", 4), ("İtalyanca", 1.5), ("Berberice", 1.5),
        ("Türkçe", 1.3), ("Lehçe", 0.7), ("Romence", 0.6), ("İngilizce", 0.5),
        ("İspanyolca", 0.5), ("Portekizce", 0.3), ("Lingala", 0.3),
        ("Rusça", 0.3), ("Yunanca", 0.2),
    ],
    "528": [  # Hollanda
        ("Arapça", 1.5), ("Berberice", 1.2), ("İngilizce", 1),
        ("Lehçe", 0.7), ("Ukraynaca", 0.5), ("Sranan Tongo", 0.5),
        ("Almanca", 0.4), ("Papiamentu", 0.3), ("Mandarin Çincesi", 0.2),
        ("Endonezce", 0.2), ("Somalice", 0.1),
    ],
    "756": [  # İsviçre
        ("İngilizce", 5.4), ("Portekizce", 3.5), ("Arnavutça", 3.1),
        ("Sırp-Hırvatça", 2.5), ("İspanyolca", 2.4), ("Türkçe", 0.9),
        ("Tamilce", 0.5), ("Arapça", 0.4), ("Rusça", 0.3), ("Kürtçe", 0.2),
    ],
    "040": [  # Avusturya
        ("Romence", 1.2), ("Macarca", 1), ("Ukraynaca", 0.9), ("Lehçe", 0.7),
        ("Arapça", 0.6), ("İngilizce", 0.5), ("Slovakça", 0.5), ("Bulgarca", 0.4),
        ("Farsça", 0.3), ("Kürtçe", 0.3), ("Slovence", 0.2), ("Çekçe", 0.2),
    ],
    "826": [  # Birleşik Krallık
        ("Bengalce", 0.8), ("Romence", 0.8), ("Pencapça", 0.5), ("Arapça", 0.5),
        ("Portekizce", 0.4), ("İspanyolca", 0.4), ("Türkçe", 0.4),
        ("Mandarin Çincesi", 0.3), ("Fransızca", 0.3), ("Tamilce", 0.3),
        ("Gucaratça", 0.3), ("İtalyanca", 0.2), ("Litvanca", 0.2),
        ("Somalice", 0.2), ("Farsça", 0.2),
    ],
    "372": [  # İrlanda
        ("Ukraynaca", 1.3), ("Romence", 0.9), ("Litvanca", 0.6),
        ("Portekizce", 0.5), ("İspanyolca", 0.5), ("Letonca", 0.4),
        ("Fransızca", 0.4), ("Hintçe", 0.3), ("Arapça", 0.3),
        ("Mandarin Çincesi", 0.2), ("İtalyanca", 0.2),
    ],
    "442": [  # Lüksemburg
        ("İngilizce", 8), ("İtalyanca", 3), ("Sırp-Hırvatça", 1.5),
        ("İspanyolca", 1), ("Romence", 1), ("Lehçe", 0.8),
    ],
    # ---------------------------------------------------------- Kuzey Avrupa
    "752": [  # İsveç
        ("Sırp-Hırvatça", 1), ("Kürtçe", 0.9), ("Türkçe", 0.9), ("Lehçe", 0.9),
        ("Farsça", 0.8), ("Somalice", 0.7), ("Süryanice", 0.6),
        ("İspanyolca", 0.6), ("İngilizce", 0.5), ("Tigrinya", 0.4),
        ("Ukraynaca", 0.4), ("Romence", 0.3), ("Darice", 0.3), ("Arnavutça", 0.3),
    ],
    "208": [  # Danimarka
        ("Lehçe", 0.9), ("Romence", 0.7), ("İngilizce", 0.6), ("Ukraynaca", 0.5),
        ("Almanca", 0.4), ("Somalice", 0.3), ("Farsça", 0.3),
        ("Sırp-Hırvatça", 0.3), ("Litvanca", 0.2), ("Urduca", 0.2),
    ],
    "578": [  # Norveç
        ("Ukraynaca", 1.2), ("İngilizce", 0.9), ("Litvanca", 0.8), ("Arapça", 0.8),
        ("İsveççe", 0.7), ("Somalice", 0.5), ("Farsça", 0.4), ("Tigrinya", 0.4),
        ("Urduca", 0.4), ("Rusça", 0.3), ("Vietnamca", 0.3), ("Türkçe", 0.2),
    ],
    "246": [  # Finlandiya
        ("Estonca", 0.9), ("Ukraynaca", 0.7), ("İngilizce", 0.5),
        ("Somalice", 0.5), ("Kürtçe", 0.3), ("Farsça", 0.3),
        ("Mandarin Çincesi", 0.2), ("Vietnamca", 0.2), ("Türkçe", 0.1),
    ],
    "352": [("Lehçe", 5.5), ("Litvanca", 0.8), ("İngilizce", 2), ("Filipince", 0.5)],  # İzlanda
    # ---------------------------------------------------------- Güney Avrupa
    "380": [  # İtalya
        ("Arnavutça", 0.7), ("Almanca", 0.6), ("Ukraynaca", 0.4),
        ("Mandarin Çincesi", 0.4), ("İspanyolca", 0.4), ("Bengalce", 0.3),
        ("Filipince", 0.3), ("Sırp-Hırvatça", 0.2), ("Fransızca", 0.2),
        ("Rusça", 0.2), ("Pencapça", 0.2), ("Türkçe", 0.05),
    ],
    "724": [  # İspanya
        ("Arapça", 1.8), ("Romence", 1.2), ("İngilizce", 0.8), ("Berberice", 0.5),
        ("Fransızca", 0.5), ("İtalyanca", 0.5), ("Ukraynaca", 0.5),
        ("Mandarin Çincesi", 0.4), ("Almanca", 0.3), ("Portekizce", 0.3),
        ("Bulgarca", 0.3), ("Rusça", 0.3),
    ],
    "620": [  # Portekiz
        ("Ukraynaca", 0.6), ("İngilizce", 0.5), ("Fransızca", 0.3),
        ("Romence", 0.3), ("Nepalce", 0.3), ("Hintçe", 0.2), ("Bengalce", 0.2),
        ("Mandarin Çincesi", 0.2), ("Cabo Verde Kreolcesi", 0.4),
    ],
    "300": [  # Yunanistan
        ("Romanca", 1.5), ("Türkçe", 1), ("Rusça", 0.4), ("Romence", 0.4),
        ("Bulgarca", 0.3), ("Gürcüce", 0.3), ("Urduca", 0.3), ("Arapça", 0.3),
        ("Makedonca", 0.2), ("İngilizce", 0.3),
    ],
    "196": [("İngilizce", 5), ("Romence", 3), ("Rusça", 3), ("Filipince", 1.5), ("Bulgarca", 1.5)],  # Kıbrıs
    "470": [("İngilizce", 60), ("İtalyanca", 20), ("Arapça", 1), ("Filipince", 0.6)],  # Malta
    # ---------------------------------------------------------- Orta/Doğu Avrupa
    "203": [  # Çekya
        ("Vietnamca", 0.7), ("Rusça", 0.5), ("Lehçe", 0.4), ("Romence", 0.3),
        ("Bulgarca", 0.3), ("Almanca", 0.2), ("Moğolca", 0.1),
    ],
    "616": [("Belarusça", 0.3), ("Rusça", 0.3), ("Almanca", 0.3), ("Kaşubca", 0.3)],  # Polonya
    "348": [("Romence", 1.3), ("Almanca", 1), ("Romanca", 2), ("Slovakça", 0.3)],  # Macaristan
    "703": [("Macarca", 8), ("Romanca", 2), ("Çekçe", 0.6), ("Ukraynaca", 0.5)],  # Slovakya
    "642": [("Macarca", 6), ("Romanca", 3), ("Almanca", 0.2), ("Türkçe", 0.1)],  # Romanya
    "100": [("Romanca", 5), ("Rusça", 0.3), ("Ukraynaca", 0.3)],  # Bulgaristan
    # ---------------------------------------------------------- Kuzey Amerika
    "840": [  # ABD
        ("Hintçe", 0.35), ("Vietnamca", 0.5), ("Arapça", 0.4), ("Fransızca", 0.4),
        ("Korece", 0.35), ("Rusça", 0.35), ("Portekizce", 0.3), ("Almanca", 0.3),
        ("Urduca", 0.25), ("İtalyanca", 0.2), ("Lehçe", 0.15), ("Japonca", 0.15),
        ("Farsça", 0.15), ("Kantonca", 0.3), ("Amharca", 0.1), ("Ermenice", 0.1),
        ("Yunanca", 0.1), ("Bengalce", 0.1), ("Pencapça", 0.1), ("Ukraynaca", 0.1),
        ("Türkçe", 0.06), ("Somalice", 0.06), ("Navaho", 0.05),
    ],
    "124": [  # Kanada
        ("Filipince", 1.6), ("Kantonca", 1.5), ("Arapça", 1.3), ("İspanyolca", 1.3),
        ("Hintçe", 0.7), ("Urduca", 0.5), ("İtalyanca", 0.8), ("Almanca", 0.6),
        ("Portekizce", 0.6), ("Farsça", 0.6), ("Tamilce", 0.5), ("Rusça", 0.5),
        ("Vietnamca", 0.4), ("Korece", 0.4), ("Lehçe", 0.4), ("Ukraynaca", 0.3),
        ("Yunanca", 0.2), ("Haiti Kreolcesi", 0.2), ("Türkçe", 0.1),
    ],
    # ---------------------------------------------------------- Okyanusya
    "036": [  # Avustralya
        ("Pencapça", 1), ("Yunanca", 0.9), ("İtalyanca", 0.9), ("Filipince", 0.8),
        ("Hintçe", 0.8), ("İspanyolca", 0.6), ("Nepalce", 0.5), ("Farsça", 0.4),
        ("Tamilce", 0.4), ("Korece", 0.4), ("Sırp-Hırvatça", 0.4), ("Almanca", 0.3),
        ("Urduca", 0.3), ("Makedonca", 0.3), ("Türkçe", 0.2), ("Endonezce", 0.2),
        ("Japonca", 0.2), ("Rusça", 0.2), ("Lehçe", 0.15), ("Portekizce", 0.15),
    ],
    "554": [  # Yeni Zelanda
        ("Hintçe", 1.7), ("Fransızca", 1.2), ("Filipince", 1.1), ("Tongaca", 0.7),
        ("Afrikaanca", 0.7), ("Pencapça", 0.7), ("Almanca", 0.7), ("Korece", 0.6),
        ("İspanyolca", 0.5), ("Japonca", 0.5), ("Kantonca", 0.5), ("Arapça", 0.2),
    ],
    # ---------------------------------------------------------- Körfez ve Ortadoğu
    "784": [  # BAE
        ("Bengalce", 7), ("İngilizce", 5), ("Telugu", 2), ("Tamilce", 2),
        ("Farsça", 1.5), ("Nepalce", 1), ("Peştuca", 1), ("Sinhalca", 1),
        ("Mandarin Çincesi", 0.5),
    ],
    "634": [("Bengalce", 8), ("Malayalam", 5), ("İngilizce", 4), ("Tamilce", 2), ("Sinhalca", 1)],  # Katar
    "414": [("Malayalam", 5), ("İngilizce", 3), ("Tamilce", 2), ("Farsça", 1), ("Nepalce", 1), ("Sinhalca", 1)],  # Kuveyt
    "048": [("Bengalce", 5), ("Malayalam", 3), ("İngilizce", 3), ("Tamilce", 2), ("Nepalce", 1)],  # Bahreyn
    "512": [("Bengalce", 5), ("Malayalam", 3), ("İngilizce", 3), ("Hintçe", 2), ("Filipince", 1)],  # Umman
    "682": [("Bengalce", 4), ("Hintçe", 3), ("İngilizce", 3), ("Malayalam", 2), ("Endonezce", 1), ("Amharca", 1), ("Nepalce", 1)],  # Suudi Arabistan
    "376": [("Fransızca", 2), ("İngilizce", 2), ("Amharca", 1.3), ("İspanyolca", 1), ("Romence", 0.5), ("Ukraynaca", 0.5), ("Gürcüce", 0.5), ("Türkçe", 0.1)],  # İsrail
    "792": [  # Türkiye — Suriyeliler MIX'teki Arapça payında; aşağısı diğer topluluklar
        ("Zazaca", 1), ("Çerkesçe", 0.5), ("Boşnakça", 0.3), ("Farsça", 0.3),
        ("Rusça", 0.25), ("Darice", 0.25), ("Gürcüce", 0.2), ("Lazca", 0.2),
        ("Ukraynaca", 0.15), ("Azerbaycanca", 0.15), ("Türkmence", 0.1),
        ("Özbekçe", 0.1), ("Ermenice", 0.1), ("Peştuca", 0.05), ("Rumca", 0.02),
    ],
    # 2022 sonrası Rus/Ukrayna göçünün belirgin olduğu ülkeler
    "268": [("Rusça", 2.5), ("Ukraynaca", 0.3), ("Osetçe", 0.3), ("Abhazca", 0.2)],  # Gürcistan
    "688": [("Arnavutça", 1), ("Rusça", 0.7), ("Slovakça", 0.7), ("Hırvatça", 0.5), ("Romence", 0.4)],  # Sırbistan
    "499": [("Rusça", 1.5), ("Ukraynaca", 0.5), ("Romanca", 1)],  # Karadağ
    "191": [("Ukraynaca", 0.3), ("Romanca", 0.4), ("Boşnakça", 0.5)],  # Hırvatistan
    "233": [("Ukraynaca", 2.5), ("İngilizce", 1), ("Fince", 0.5)],  # Estonya
    "428": [("Ukraynaca", 2), ("Belarusça", 1.5), ("Lehçe", 1.5)],  # Letonya
    "440": [("Ukraynaca", 2.5), ("Belarusça", 1.5), ("İngilizce", 0.6)],  # Litvanya
    "498": [("Romanca", 1), ("Bulgarca", 1.5), ("İngilizce", 0.4)],  # Moldova
    "051": [("Yezidice", 1), ("Ukraynaca", 0.2), ("Farsça", 0.1)],  # Ermenistan
    # ---------------------------------------------------------- Avrasya / Asya
    "643": [  # Rusya
        ("Ukraynaca", 1), ("Çuvaşça", 0.7), ("Özbekçe", 0.7), ("Tacikçe", 0.6),
        ("Avarca", 0.5), ("Ermenice", 0.5), ("Azerbaycanca", 0.5), ("Yakutça", 0.3),
        ("Kırgızca", 0.3), ("Almanca", 0.1), ("Korece", 0.05), ("Türkçe", 0.05),
    ],
    "398": [("Ukraynaca", 0.7), ("Uygurca", 0.7), ("Korece", 0.5), ("Tatarca", 0.5), ("Azerbaycanca", 0.5), ("Almanca", 0.4), ("Türkçe", 0.1)],  # Kazakistan
    "392": [("Vietnamca", 0.4), ("İngilizce", 0.2), ("Portekizce", 0.2), ("Filipince", 0.2), ("Nepalce", 0.1), ("Endonezce", 0.1)],  # Japonya
    "410": [("Mandarin Çincesi", 1), ("Vietnamca", 0.5), ("Tayca", 0.3), ("İngilizce", 0.3), ("Özbekçe", 0.1), ("Filipince", 0.1)],  # Güney Kore
    "702": [("Hintçe", 1), ("Filipince", 3), ("Bengalce", 3), ("Endonezce", 1), ("Japonca", 0.6), ("Korece", 0.4)],  # Singapur
    "344": [("İngilizce", 4), ("Filipince", 2), ("Endonezce", 2), ("Nepalce", 0.3)],  # Hong Kong
    # ---------------------------------------------------------- Afrika
    "710": [("Sesotho", 8), ("Sitsonga", 4), ("Sivenda", 2), ("Portekizce", 0.6), ("Şonaca", 1.5), ("Fransızca", 0.2)],  # Güney Afrika
    "504": [("Berberice", 26), ("Fransızca", 1), ("İspanyolca", 0.3)],  # Fas
    "012": [("Berberice", 15), ("Fransızca", 1)],  # Cezayir
}
