"""Alt bölge (eyalet / il / kanton / bölge) dil dağılımları.

Anahtar: "<ülke kodu>-<Natural Earth bölge adı>" — build_subs.py ile aynı.
Değer: [(dil, yüzde), …] — bölge nüfusunun o dili evde/ana dil olarak
konuşan payı. Toplam %100'ü aşabilir (çok dillilik).

Kaynaklar: Kanada 2021 sayımı (ana dil), ABD ACS 2019-2023 "evde konuşulan
dil", İsviçre yapısal anketi (ana diller, çoklu yanıt), Belçika bölge dil
rejimleri + Brüksel anketleri, İspanya özerk topluluk dil anketleri,
Hindistan 2011 sayımı, Ukrayna 2001 sayımı (2022 sonrası kayma dikkate
alınarak), Finlandiya nüfus kütüğü, Bolivya 2012 sayımı, İtalya ISTAT
azınlık dilleri, Türkiye için KONDA/TÜİK temelli ana dil tahminleri.
Türkiye rakamları resmî sayım olmadığı için tahmindir.
"""

SUB = {}


def put(cid, rows, *names):
    for n in names:
        SUB[f"{cid}-{n}"] = rows


# ------------------------------------------------------------------ Kanada
put("124", [("Fransızca", 78), ("İngilizce", 8), ("Arapça", 2.5),
            ("İspanyolca", 1.7), ("İtalyanca", 1), ("Haiti Kreolcesi", 0.8)], "Québec")
put("124", [("İngilizce", 68), ("Mandarin Çincesi", 3), ("Fransızca", 3.4),
            ("Pencapça", 2), ("Arapça", 1.7), ("Urduca", 1.3), ("İtalyanca", 1),
            ("Kantonca", 1.6), ("Tamilce", 1.1)], "Ontario")
put("124", [("İngilizce", 70), ("Pencapça", 5), ("Mandarin Çincesi", 4.2),
            ("Kantonca", 3.6), ("Filipince", 1.6), ("Korece", 1.2),
            ("Fransızca", 1.1), ("Hintçe", 0.9)], "British Columbia")
put("124", [("İngilizce", 78), ("Pencapça", 2.6), ("Filipince", 2.2),
            ("Mandarin Çincesi", 2), ("Fransızca", 1.6), ("Arapça", 1.4),
            ("Almanca", 1)], "Alberta")
put("124", [("İngilizce", 74), ("Filipince", 5), ("Almanca", 3.2),
            ("Fransızca", 3), ("Pencapça", 2), ("Ukraynaca", 0.9),
            ("Kri dilleri", 2)], "Manitoba")
put("124", [("İngilizce", 84), ("Filipince", 2.5), ("Almanca", 1.6),
            ("Fransızca", 1.4), ("Kri dilleri", 1.2), ("Ukraynaca", 0.8)], "Saskatchewan")
put("124", [("İngilizce", 65), ("Fransızca", 31), ("Arapça", 0.8)], "New Brunswick")
put("124", [("İngilizce", 90), ("Fransızca", 3.2), ("Arapça", 1.2),
            ("Mikmakça", 0.6)], "Nova Scotia")
put("124", [("İngilizce", 89), ("Fransızca", 3.5), ("Mandarin Çincesi", 2)], "Prince Edward Island")
put("124", [("İngilizce", 96), ("Fransızca", 0.5)], "Newfoundland and Labrador")
put("124", [("İngilizce", 84), ("Fransızca", 4), ("Filipince", 1.5)], "Yukon")
put("124", [("İngilizce", 78), ("Dene dilleri", 8), ("Fransızca", 2.9),
            ("İnuktitut", 3)], "Northwest Territories")
put("124", [("İnuktitut", 65), ("İngilizce", 32), ("Fransızca", 1.4)], "Nunavut")

# ------------------------------------------------------------------ ABD
US_DEFAULT = [("İngilizce", 91), ("İspanyolca", 5)]
put("840", [("İngilizce", 56), ("İspanyolca", 28), ("Mandarin Çincesi", 2),
            ("Filipince", 2), ("Vietnamca", 1.5), ("Korece", 1),
            ("Ermenice", 0.6), ("Farsça", 0.5)], "California")
put("840", [("İngilizce", 64), ("İspanyolca", 30), ("Vietnamca", 1),
            ("Mandarin Çincesi", 0.6)], "Texas")
put("840", [("İngilizce", 63), ("İspanyolca", 27), ("Navaho", 3.5)], "New Mexico")
put("840", [("İngilizce", 70), ("İspanyolca", 22), ("Haiti Kreolcesi", 2.3),
            ("Portekizce", 0.8)], "Florida")
put("840", [("İngilizce", 68), ("İspanyolca", 15), ("Mandarin Çincesi", 3),
            ("Rusça", 1.5), ("Kantonca", 1.2), ("Bengalce", 0.7)], "New York")
put("840", [("İngilizce", 68), ("İspanyolca", 16), ("Hintçe", 1.6),
            ("Mandarin Çincesi", 1.5), ("Korece", 1), ("Portekizce", 1)], "New Jersey")
put("840", [("İngilizce", 72), ("İspanyolca", 20), ("Navaho", 1.5)], "Arizona")
put("840", [("İngilizce", 69), ("İspanyolca", 21), ("Filipino", 3)], "Nevada")
put("840", [("İngilizce", 76), ("İspanyolca", 14), ("Lehçe", 1.5),
            ("Mandarin Çincesi", 0.8), ("Arapça", 0.7)], "Illinois")
put("840", [("İngilizce", 76), ("İspanyolca", 10), ("Portekizce", 3),
            ("Mandarin Çincesi", 1.5), ("Haiti Kreolcesi", 1)], "Massachusetts")
put("840", [("İngilizce", 73), ("Filipince", 6), ("Japonca", 4),
            ("Mandarin Çincesi", 1.5), ("Hawaii dili", 1.5), ("İspanyolca", 2)], "Hawaii")
put("840", [("İngilizce", 83), ("İspanyolca", 4), ("Filipince", 3),
            ("Yupikçe", 2), ("İnuitçe", 1)], "Alaska")
put("840", [("İngilizce", 91), ("İspanyolca", 5), ("Fransızca", 1.3)], "Louisiana")
put("840", [("İngilizce", 93), ("Fransızca", 3.5)], "Maine")
put("840", [("İngilizce", 94), ("Fransızca", 1.5)], "Vermont")
put("840", [("İngilizce", 88), ("İspanyolca", 4), ("Somalice", 1.3),
            ("Hmong", 1), ("Vietnamca", 0.5)], "Minnesota")
put("840", [("İngilizce", 79), ("İspanyolca", 9), ("Mandarin Çincesi", 1.5),
            ("Vietnamca", 1.3), ("Rusça", 1.2), ("Korece", 0.8)], "Washington")
put("840", [("İngilizce", 90), ("İspanyolca", 3), ("Arapça", 2)], "Michigan")
put("840", [("İngilizce", 78), ("İspanyolca", 13), ("Portekizce", 3)], "Rhode Island")
put("840", [("İngilizce", 83), ("İspanyolca", 9), ("Fransızca", 1.5),
            ("Amharca", 1)], "District of Columbia")
put("840", [("İngilizce", 74), ("İspanyolca", 12), ("Mandarin Çincesi", 1.4),
            ("Korece", 1.3), ("Vietnamca", 1.2), ("Amharca", 0.9)], "Virginia")
put("840", [("İngilizce", 81), ("İspanyolca", 8), ("Mandarin Çincesi", 1.2),
            ("Korece", 1), ("Fransızca", 1), ("Amharca", 0.8)], "Maryland")
put("840", [("İngilizce", 78), ("İspanyolca", 12), ("Portekizce", 1.5),
            ("Lehçe", 1), ("İtalyanca", 0.8)], "Connecticut")
put("840", [("İngilizce", 85), ("İspanyolca", 10), ("Vietnamca", 0.6)], "Georgia")
put("840", [("İngilizce", 82), ("İspanyolca", 12), ("Vietnamca", 0.6)], "North Carolina")
put("840", [("İngilizce", 82), ("İspanyolca", 12), ("Vietnamca", 0.7),
            ("Mandarin Çincesi", 0.7)], "Colorado")
put("840", [("İngilizce", 85), ("İspanyolca", 10)], "Utah")
put("840", [("İngilizce", 85), ("İspanyolca", 9), ("Mandarin Çincesi", 0.7)], "Oregon")

# ------------------------------------------------------------------ İsviçre
CH_DE = [("Almanca", 86), ("İngilizce", 6), ("İtalyanca", 3), ("Fransızca", 3)]
put("756", CH_DE, "Zürich", "Lucerne", "Uri", "Schwyz", "Obwalden", "Nidwalden",
    "Glarus", "Zug", "Solothurn", "Basel-Landschaft", "Schaffhausen",
    "Appenzell Ausserrhoden", "Appenzell Innerrhoden", "Sankt Gallen",
    "Aargau", "Thurgau")
put("756", [("Almanca", 78), ("İngilizce", 8), ("İtalyanca", 4),
            ("Portekizce", 3), ("Sırp-Hırvatça", 3)], "Basel-Stadt")
put("756", [("Almanca", 84), ("Fransızca", 11), ("İngilizce", 5)], "Bern")
put("756", [("Fransızca", 68), ("Almanca", 21), ("İngilizce", 4),
            ("Portekizce", 3)], "Fribourg")
put("756", [("Fransızca", 67), ("Almanca", 23), ("Portekizce", 5),
            ("İtalyanca", 2)], "Valais")
put("756", [("Fransızca", 80), ("İngilizce", 6), ("Portekizce", 4),
            ("İspanyolca", 2), ("İtalyanca", 2)], "Vaud")
put("756", [("Fransızca", 74), ("İngilizce", 11), ("Portekizce", 5),
            ("İspanyolca", 4), ("İtalyanca", 4), ("Arapça", 2)], "Genève")
put("756", [("Fransızca", 84), ("İngilizce", 4), ("İtalyanca", 3),
            ("Portekizce", 3)], "Neuchâtel")
put("756", [("Fransızca", 90), ("Almanca", 4), ("İngilizce", 2)], "Jura")
put("756", [("İtalyanca", 82), ("Almanca", 8), ("Fransızca", 4),
            ("İngilizce", 4)], "Ticino")
put("756", [("Almanca", 74), ("Romanşça", 14), ("İtalyanca", 11),
            ("İngilizce", 3)], "Graubünden")

# ------------------------------------------------------------------ Belçika
BE_VL = [("Felemenkçe", 88), ("Fransızca", 5), ("İngilizce", 4), ("Arapça", 2)]
put("056", BE_VL, "Antwerp", "East Flanders", "West Flanders", "Flemish Brabant")
put("056", [("Felemenkçe", 86), ("Fransızca", 5), ("Türkçe", 3),
            ("İngilizce", 3), ("İtalyanca", 2)], "Limburg")
BE_WA = [("Fransızca", 91), ("İtalyanca", 3), ("Arapça", 3), ("İngilizce", 2)]
put("056", BE_WA, "Hainaut", "Namur", "Walloon Brabant")
put("056", [("Fransızca", 89), ("Almanca", 2), ("İtalyanca", 3),
            ("Arapça", 3), ("Türkçe", 1.5)], "Liege")
put("056", [("Fransızca", 88), ("Lüksemburgca", 3), ("Almanca", 2),
            ("Portekizce", 2)], "Luxembourg")
put("056", [("Fransızca", 68), ("Felemenkçe", 12), ("Arapça", 8),
            ("İngilizce", 6), ("Türkçe", 3), ("İspanyolca", 2),
            ("Berberice", 4)], "Brussels")

# ------------------------------------------------------------------ İspanya
put("724", [("İspanyolca", 55), ("Katalanca", 36), ("Arapça", 2),
            ("Romence", 1)], "Cataluña")
put("724", [("İspanyolca", 68), ("Katalanca", 25), ("Romence", 2)], "Valenciana")
put("724", [("İspanyolca", 51), ("Katalanca", 37), ("Almanca", 2),
            ("İngilizce", 2)], "Islas Baleares")
put("724", [("Galiçyaca", 51), ("İspanyolca", 48)], "Galicia")
put("724", [("İspanyolca", 68), ("Baskça", 30)], "País Vasco")
put("724", [("İspanyolca", 88), ("Baskça", 11)], "Foral de Navarra")
put("724", [("İspanyolca", 85), ("Arapça", 40)], "Ceuta")
put("724", [("İspanyolca", 82), ("Berberice", 30), ("Arapça", 10)], "Melilla")
put("724", [("İspanyolca", 96), ("Arapça", 2), ("Romence", 1)], "Andalucía")
put("724", [("İspanyolca", 93), ("İngilizce", 3), ("Almanca", 2)], "Canary Is.")
put("724", [("İspanyolca", 94), ("Romence", 2), ("Arapça", 1)], "Madrid")
put("724", [("İspanyolca", 96), ("Asturyasça", 20)], "Asturias")
ES_REST = [("İspanyolca", 97), ("Romence", 1)]
put("724", ES_REST, "Aragón", "Castilla y León", "Castilla-La Mancha",
    "Extremadura", "La Rioja", "Murcia", "Cantabria")

# ------------------------------------------------------------------ B. Krallık
put("826", [("İngilizce", 92), ("Lehçe", 1), ("Romence", 1), ("Urduca", 1),
            ("Bengalce", 0.9), ("Pencapça", 0.5), ("Arapça", 0.5)], "İngiltere")
put("826", [("İngilizce", 96), ("Lehçe", 1.1), ("İskoç Gaelcesi", 1),
            ("Urduca", 0.5), ("İskoçça", 30)], "İskoçya")
put("826", [("İngilizce", 82), ("Galce", 18), ("Lehçe", 0.5)], "Galler")
put("826", [("İngilizce", 96), ("İrlandaca", 6), ("Ulster İskoççası", 2),
            ("Lehçe", 1)], "Kuzey İrlanda")

# ------------------------------------------------------------------ Hindistan
put("356", [("Hintçe", 70), ("Bhojpuri", 10), ("Urduca", 5)], "Uttar Pradesh")
put("356", [("Marathi", 69), ("Hintçe", 13), ("Urduca", 7), ("Gucaratça", 2)], "Maharashtra")
put("356", [("Hintçe", 60), ("Bhojpuri", 20), ("Maithili", 12), ("Urduca", 9)], "Bihar")
put("356", [("Bengalce", 86), ("Hintçe", 7), ("Santali", 3), ("Urduca", 2)], "West Bengal")
put("356", [("Hintçe", 88), ("Bhili", 4), ("Urduca", 2)], "Madhya Pradesh")
put("356", [("Tamilce", 89), ("Telugu", 5), ("Kannada", 2), ("Urduca", 2)], "Tamil Nadu")
put("356", [("Hintçe", 91), ("Bhili", 4), ("Urduca", 2)], "Rajasthan")
put("356", [("Kannada", 66), ("Urduca", 11), ("Telugu", 6), ("Tamilce", 4),
            ("Marathi", 3)], "Karnataka")
put("356", [("Gucaratça", 86), ("Hintçe", 5), ("Bhili", 3), ("Urduca", 2)], "Gujarat")
put("356", [("Telugu", 84), ("Urduca", 8)], "Andhra Pradesh")
put("356", [("Telugu", 76), ("Urduca", 12), ("Hintçe", 5), ("Marathi", 2)], "Telangana")
put("356", [("Oriya", 82), ("Hintçe", 3), ("Santali", 3)], "Odisha")
put("356", [("Malayalam", 97), ("Tamilce", 1)], "Kerala")
put("356", [("Hintçe", 62), ("Santali", 10), ("Bengalce", 9), ("Urduca", 6)], "Jharkhand")
put("356", [("Assamca", 48), ("Bengalce", 30), ("Hintçe", 7), ("Bodo", 5)], "Assam")
put("356", [("Pencapça", 90), ("Hintçe", 8)], "Punjab")
put("356", [("Hintçe", 84), ("Oriya", 1), ("Gondi", 2)], "Chhattisgarh")
put("356", [("Hintçe", 88), ("Pencapça", 8), ("Urduca", 2)], "Haryana")
put("356", [("Hintçe", 80), ("Urduca", 6), ("Pencapça", 4), ("Bengalce", 2)], "Delhi")
put("356", [("Keşmirce", 53), ("Dogri", 20), ("Pahari", 8), ("Urduca", 2),
            ("Hintçe", 2)], "Jammu and Kashmir")
put("356", [("Hintçe", 88), ("Urduca", 5), ("Nepalce", 1)], "Uttarakhand")
put("356", [("Hintçe", 86), ("Pencapça", 4), ("Kinnauri", 1)], "Himachal Pradesh")
put("356", [("Bengalce", 65), ("Kokborok", 25)], "Tripura")
put("356", [("Kasi", 47), ("Garo", 32), ("Bengalce", 6), ("Nepalce", 2)], "Meghalaya")
put("356", [("Meitei", 60), ("Tangkhul", 6), ("Nepalce", 2), ("Hintçe", 2)], "Manipur")
put("356", [("Nagamese", 30), ("Konyak", 12), ("Ao", 11), ("İngilizce", 3)], "Nagaland")
put("356", [("Konkani", 57), ("Marathi", 19), ("Hintçe", 8), ("Kannada", 5)], "Goa")
put("356", [("Nisi", 20), ("Adi", 17), ("Hintçe", 9), ("Bengalce", 7)], "Arunachal Pradesh")
put("356", [("Mizo", 73), ("Bengalce", 8), ("Hintçe", 2)], "Mizoram")
put("356", [("Nepalce", 62), ("Sikkimce", 7), ("Limbu", 6), ("Hintçe", 6)], "Sikkim")
put("356", [("Tamilce", 88), ("Telugu", 4), ("Malayalam", 3), ("Fransızca", 0.3)], "Puducherry")
put("356", [("Hintçe", 73), ("Pencapça", 22)], "Chandigarh")
put("356", [("Bengalce", 26), ("Hintçe", 19), ("Tamilce", 19), ("Telugu", 13)],
    "Andaman and Nicobar")
put("356", [("Malayalam", 84), ("Divehi", 12)], "Lakshadweep")
put("356", [("Ladakhça", 65), ("Balti", 10), ("Urduca", 5)], "Ladakh")
put("356", [("Gucaratça", 55), ("Hintçe", 20), ("Bhili", 12), ("Marathi", 10)],
    "Dadra and Nagar Haveli and Daman and Diu")

# ------------------------------------------------------------------ Ukrayna
put("804", [("Rusça", 70), ("Ukraynaca", 28)], "Donets'k")
put("804", [("Rusça", 66), ("Ukraynaca", 32)], "Luhans'k")
put("804", [("Ukraynaca", 53), ("Rusça", 44)], "Kharkiv")
put("804", [("Ukraynaca", 47), ("Rusça", 42), ("Bulgarca", 3), ("Romence", 2)], "Odessa")
put("804", [("Ukraynaca", 50), ("Rusça", 48)], "Zaporizhzhya")
put("804", [("Ukraynaca", 67), ("Rusça", 32)], "Dnipropetrovs'k")
put("804", [("Ukraynaca", 69), ("Rusça", 29)], "Mykolayiv")
put("804", [("Ukraynaca", 73), ("Rusça", 25)], "Kherson")
put("804", [("Ukraynaca", 72), ("Rusça", 25), ("İngilizce", 2)], "Kiev City")
put("804", [("Ukraynaca", 81), ("Macarca", 12), ("Rusça", 3), ("Romence", 2)],
    "Transcarpathia")
put("804", [("Ukraynaca", 75), ("Romence", 19), ("Rusça", 4)], "Chernivtsi")
UA_W = [("Ukraynaca", 98), ("Rusça", 1)]
put("804", UA_W, "L'viv", "Ternopil'", "Ivano-Frankivs'k", "Volyn", "Rivne")
UA_C = [("Ukraynaca", 91), ("Rusça", 8)]
put("804", UA_C, "Kiev", "Cherkasy", "Chernihiv", "Khmel'nyts'kyy", "Kirovohrad",
    "Poltava", "Sumy", "Vinnytsya", "Zhytomyr")

# ------------------------------------------------------------------ Finlandiya
put("246", [("Fince", 78), ("İsveççe", 8), ("Rusça", 2), ("Estonca", 2),
            ("İngilizce", 2), ("Somalice", 1)], "Uusimaa")
put("246", [("İsveççe", 50), ("Fince", 45), ("İngilizce", 1)], "Ostrobothnia")
put("246", [("Fince", 88), ("İsveççe", 9)], "Central Ostrobothnia")
put("246", [("Fince", 91), ("İsveççe", 5.6), ("Estonca", 1)], "Finland Proper")
put("246", [("Fince", 95), ("Sami dilleri", 1.5), ("İsveççe", 0.4)], "Lapland")
FI_REST = [("Fince", 96), ("Rusça", 1), ("Estonca", 0.7)]
put("246", FI_REST, "Kainuu", "Kymenlaakso", "North Karelia", "Northern Ostrobothnia",
    "Northern Savonia", "Pirkanmaa", "Päijät-Häme", "Satakunta", "South Karelia",
    "Southern Ostrobothnia", "Southern Savonia", "Tavastia Proper", "Central Finland")

# ------------------------------------------------------------------ Bolivya
put("068", [("İspanyolca", 70), ("Aymara", 27), ("Keçuva", 5)], "La Paz")
put("068", [("İspanyolca", 62), ("Aymara", 30), ("Keçuva", 12)], "Oruro")
put("068", [("İspanyolca", 60), ("Keçuva", 45), ("Aymara", 8)], "Potosí")
put("068", [("İspanyolca", 72), ("Keçuva", 33)], "Cochabamba")
put("068", [("İspanyolca", 75), ("Keçuva", 30)], "Chuquisaca")
put("068", [("İspanyolca", 92), ("Keçuva", 4), ("Guaraní", 1)], "Santa Cruz")
put("068", [("İspanyolca", 93), ("Keçuva", 3), ("Guaraní", 2)], "Tarija")
put("068", [("İspanyolca", 95), ("Keçuva", 1)], "El Beni", "Pando")

# ------------------------------------------------------------------ İtalya
put("380", [("Almanca", 52), ("İtalyanca", 45), ("Ladince", 4)], "Trentino-Alto Adige")
put("380", [("İtalyanca", 88), ("Fransızca", 15)], "Valle d'Aosta")
put("380", [("İtalyanca", 88), ("Friulice", 25), ("Slovence", 3)], "Friuli-Venezia Giulia")
put("380", [("İtalyanca", 90), ("Sardunyaca", 45)], "Sardegna")
put("380", [("İtalyanca", 92), ("Sicilyaca", 55)], "Sicily")
put("380", [("İtalyanca", 95), ("Napolice", 40), ("Arnavutça", 1)], "Calabria")
put("380", [("İtalyanca", 95), ("Napolice", 45)], "Campania", "Apulia", "Basilicata",
    "Molise", "Abruzzo")
IT_REST = [("İtalyanca", 96), ("Romence", 2), ("Arapça", 1)]
put("380", IT_REST, "Emilia-Romagna", "Lazio", "Liguria", "Lombardia", "Marche",
    "Piemonte", "Toscana", "Umbria", "Veneto")

# ------------------------------------------------------------------ Türkiye
TR_KURT_HIGH = [("Kürtçe", 82), ("Türkçe", 25), ("Arapça", 2)]
put("792", TR_KURT_HIGH, "Sirnak", "Hakkari", "Mardin", "Batman", "Siirt", "Agri", "Mus")
put("792", [("Kürtçe", 72), ("Türkçe", 32), ("Zazaca", 3)], "Diyarbakir", "Bitlis", "Van")
put("792", [("Kürtçe", 55), ("Türkçe", 45), ("Arapça", 6)], "Sanliurfa")
put("792", [("Kürtçe", 40), ("Türkçe", 62), ("Zazaca", 8)], "Bingöl", "Adiyaman")
put("792", [("Kürtçe", 25), ("Türkçe", 78), ("Zazaca", 12)], "Elazig")
put("792", [("Zazaca", 32), ("Kürtçe", 24), ("Türkçe", 56)], "Tunceli")
put("792", [("Kürtçe", 22), ("Türkçe", 82)], "Kars", "Iğdir", "Ardahan", "Erzurum")
put("792", [("Kürtçe", 18), ("Türkçe", 86), ("Arapça", 4)], "Gaziantep", "Malatya", "K. Maras")
put("792", [("Arapça", 25), ("Türkçe", 78), ("Kürtçe", 5)], "Hatay")
put("792", [("Arapça", 12), ("Türkçe", 88), ("Kürtçe", 12)], "Kilis")
put("792", [("Türkçe", 88), ("Kürtçe", 12), ("Arapça", 4)], "Mersin", "Adana", "Osmaniye")
put("792", [("Türkçe", 88), ("Kürtçe", 8), ("Arapça", 3), ("Zazaca", 1)], "Istanbul")
put("792", [("Türkçe", 92), ("Kürtçe", 6), ("Arapça", 1)], "Ankara", "Izmir", "Bursa",
    "Kocaeli", "Konya", "Antalya", "Mugla", "Aydin", "Manisa", "Denizli", "Balikesir",
    "Tekirdag", "Sakarya", "Eskisehir", "Kayseri", "Samsun", "Trabzon", "Erzincan")
TR_REST = [("Türkçe", 96), ("Kürtçe", 3)]
put("792", TR_REST, "Afyonkarahisar", "Aksaray", "Amasya", "Artvin", "Bartın",
    "Bayburt", "Bilecik", "Bolu", "Burdur", "Düzce", "Edirne", "Giresun", "Gümüshane",
    "Isparta", "Karabük", "Karaman", "Kastamonu", "Kinkkale", "Kirklareli", "Kirsehir",
    "Kütahya", "Nevsehir", "Nigde", "Ordu", "Rize", "Sinop", "Sivas", "Tokat", "Usak",
    "Yalova", "Yozgat", "Zinguldak", "Çanakkale", "Çankiri", "Çorum")

# ---------------------------------------------------------------- Türkçe adlar
NAME = {
    "124-Québec": "Québec", "124-British Columbia": "British Columbia",
    "124-Northwest Territories": "Kuzey Batı Toprakları",
    "124-Newfoundland and Labrador": "Newfoundland ve Labrador",
    "124-Prince Edward Island": "Prince Edward Adası",
    "124-New Brunswick": "New Brunswick", "124-Nova Scotia": "Nova Scotia",
    "840-District of Columbia": "Washington DC", "840-New Mexico": "New Mexico",
    "840-New York": "New York", "840-California": "Kaliforniya",
    "840-Texas": "Teksas", "840-Florida": "Florida", "840-Hawaii": "Hawaii",
    "840-Alaska": "Alaska", "840-Washington": "Washington",
    "756-Genève": "Cenevre", "756-Bern": "Bern", "756-Zürich": "Zürih",
    "756-Ticino": "Ticino", "756-Graubünden": "Graubünden", "756-Valais": "Valais",
    "756-Vaud": "Vaud", "756-Lucerne": "Luzern", "756-Basel-Stadt": "Basel-Şehir",
    "756-Basel-Landschaft": "Basel-Kırsal", "756-Sankt Gallen": "Sankt Gallen",
    "056-Brussels": "Brüksel", "056-Antwerp": "Anvers", "056-East Flanders": "Doğu Flandre",
    "056-West Flanders": "Batı Flandre", "056-Flemish Brabant": "Flaman Brabant",
    "056-Walloon Brabant": "Valon Brabant", "056-Liege": "Liège", "056-Limburg": "Limburg",
    "056-Hainaut": "Hainaut", "056-Namur": "Namur", "056-Luxembourg": "Lüksemburg (il)",
    "724-Cataluña": "Katalonya", "724-País Vasco": "Bask Ülkesi",
    "724-Galicia": "Galiçya", "724-Islas Baleares": "Balear Adaları",
    "724-Canary Is.": "Kanarya Adaları", "724-Foral de Navarra": "Navarra",
    "724-Valenciana": "Valensiya", "724-Andalucía": "Endülüs", "724-Madrid": "Madrid",
    "724-Castilla y León": "Castilla y León", "724-Asturias": "Asturias",
    "380-Sicily": "Sicilya", "380-Sardegna": "Sardinya", "380-Piemonte": "Piyemonte",
    "380-Lombardia": "Lombardiya", "380-Toscana": "Toskana", "380-Apulia": "Puglia",
    "380-Trentino-Alto Adige": "Trentino-Güney Tirol", "380-Valle d'Aosta": "Aosta Vadisi",
    "380-Veneto": "Veneto", "380-Lazio": "Lazio",
    "804-Kiev City": "Kiev (şehir)", "804-Kiev": "Kiev (oblast)",
    "804-Donets'k": "Donetsk", "804-Luhans'k": "Luhansk", "804-L'viv": "Lviv",
    "804-Kharkiv": "Harkiv", "804-Odessa": "Odesa", "804-Kherson": "Herson",
    "804-Zaporizhzhya": "Zaporijya", "804-Dnipropetrovs'k": "Dnipropetrovsk",
    "804-Transcarpathia": "Zakarpatya", "804-Chernivtsi": "Çernivtsi",
    "804-Ivano-Frankivs'k": "İvano-Frankivsk", "804-Ternopil'": "Ternopil",
    "804-Mykolayiv": "Mikolayiv", "804-Khmel'nyts'kyy": "Hmelnitski",
    "246-Ostrobothnia": "Pohjanmaa (İsveççe bölgesi)", "246-Uusimaa": "Uusimaa",
    "246-Lapland": "Lapland", "246-Finland Proper": "Varsinais-Suomi",
    "356-West Bengal": "Batı Bengal", "356-Tamil Nadu": "Tamil Nadu",
    "356-Jammu and Kashmir": "Cammu ve Keşmir", "356-Delhi": "Delhi",
    "356-Andaman and Nicobar": "Andaman ve Nikobar",
    "356-Dadra and Nagar Haveli and Daman and Diu": "Dadra, Daman ve Diu",
    "068-La Paz": "La Paz", "068-El Beni": "Beni", "068-Potosí": "Potosí",
    "792-Sirnak": "Şırnak", "792-Hakkari": "Hakkâri", "792-Mardin": "Mardin",
    "792-Batman": "Batman", "792-Siirt": "Siirt", "792-Agri": "Ağrı", "792-Mus": "Muş",
    "792-Diyarbakir": "Diyarbakır", "792-Bitlis": "Bitlis", "792-Van": "Van",
    "792-Sanliurfa": "Şanlıurfa", "792-Bingöl": "Bingöl", "792-Adiyaman": "Adıyaman",
    "792-Elazig": "Elazığ", "792-Tunceli": "Tunceli", "792-Kars": "Kars",
    "792-Iğdir": "Iğdır", "792-Ardahan": "Ardahan", "792-Erzurum": "Erzurum",
    "792-Gaziantep": "Gaziantep", "792-Malatya": "Malatya", "792-K. Maras": "Kahramanmaraş",
    "792-Hatay": "Hatay", "792-Kilis": "Kilis", "792-Mersin": "Mersin",
    "792-Adana": "Adana", "792-Osmaniye": "Osmaniye", "792-Istanbul": "İstanbul",
    "792-Izmir": "İzmir", "792-Ankara": "Ankara", "792-Bursa": "Bursa",
    "792-Kocaeli": "Kocaeli", "792-Konya": "Konya", "792-Antalya": "Antalya",
    "792-Mugla": "Muğla", "792-Aydin": "Aydın", "792-Manisa": "Manisa",
    "792-Denizli": "Denizli", "792-Balikesir": "Balıkesir", "792-Tekirdag": "Tekirdağ",
    "792-Sakarya": "Sakarya", "792-Eskisehir": "Eskişehir", "792-Kayseri": "Kayseri",
    "792-Samsun": "Samsun", "792-Trabzon": "Trabzon", "792-Erzincan": "Erzincan",
    "792-Afyonkarahisar": "Afyonkarahisar", "792-Aksaray": "Aksaray",
    "792-Amasya": "Amasya", "792-Artvin": "Artvin", "792-Bartın": "Bartın",
    "792-Bayburt": "Bayburt", "792-Bilecik": "Bilecik", "792-Bolu": "Bolu",
    "792-Burdur": "Burdur", "792-Düzce": "Düzce", "792-Edirne": "Edirne",
    "792-Giresun": "Giresun", "792-Gümüshane": "Gümüşhane", "792-Isparta": "Isparta",
    "792-Karabük": "Karabük", "792-Karaman": "Karaman", "792-Kastamonu": "Kastamonu",
    "792-Kinkkale": "Kırıkkale", "792-Kirklareli": "Kırklareli",
    "792-Kirsehir": "Kırşehir", "792-Kütahya": "Kütahya", "792-Nevsehir": "Nevşehir",
    "792-Nigde": "Niğde", "792-Ordu": "Ordu", "792-Rize": "Rize", "792-Sinop": "Sinop",
    "792-Sivas": "Sivas", "792-Tokat": "Tokat", "792-Usak": "Uşak",
    "792-Yalova": "Yalova", "792-Yozgat": "Yozgat", "792-Zinguldak": "Zonguldak",
    "792-Çanakkale": "Çanakkale", "792-Çankiri": "Çankırı", "792-Çorum": "Çorum",
}

# veri girilmemiş ABD eyaletleri ülke ortalamasına düşsün
US_FALLBACK = US_DEFAULT

# ------------------------------------------------- bölge nüfusları (bin kişi)
SUBPOP = {}


def pop(cid, **kw):
    for name, v in kw.items():
        SUBPOP[f"{cid}-{name.replace('_', ' ')}"] = v


SUBPOP.update({
    # Kanada (2023)
    "124-Ontario": 15600, "124-Québec": 9000, "124-British Columbia": 5600,
    "124-Alberta": 4800, "124-Manitoba": 1450, "124-Saskatchewan": 1220,
    "124-Nova Scotia": 1070, "124-New Brunswick": 830,
    "124-Newfoundland and Labrador": 540, "124-Prince Edward Island": 180,
    "124-Northwest Territories": 45, "124-Yukon": 45, "124-Nunavut": 40,
    # ABD (2023)
    "840-California": 39000, "840-Texas": 30500, "840-Florida": 22600,
    "840-New York": 19600, "840-Pennsylvania": 13000, "840-Illinois": 12600,
    "840-Ohio": 11800, "840-Georgia": 11000, "840-North Carolina": 10800,
    "840-Michigan": 10000, "840-New Jersey": 9300, "840-Virginia": 8700,
    "840-Washington": 7800, "840-Arizona": 7400, "840-Tennessee": 7100,
    "840-Massachusetts": 7000, "840-Indiana": 6900, "840-Missouri": 6200,
    "840-Maryland": 6200, "840-Wisconsin": 5900, "840-Colorado": 5900,
    "840-Minnesota": 5700, "840-South Carolina": 5400, "840-Alabama": 5100,
    "840-Louisiana": 4600, "840-Kentucky": 4500, "840-Oregon": 4200,
    "840-Oklahoma": 4100, "840-Connecticut": 3600, "840-Utah": 3400,
    "840-Iowa": 3200, "840-Nevada": 3200, "840-Arkansas": 3100,
    "840-Mississippi": 2900, "840-Kansas": 2900, "840-New Mexico": 2100,
    "840-Nebraska": 2000, "840-Idaho": 1960, "840-West Virginia": 1770,
    "840-Hawaii": 1440, "840-New Hampshire": 1400, "840-Maine": 1390,
    "840-Montana": 1130, "840-Rhode Island": 1100, "840-Delaware": 1030,
    "840-South Dakota": 920, "840-North Dakota": 780, "840-Alaska": 730,
    "840-District of Columbia": 680, "840-Vermont": 650, "840-Wyoming": 580,
    # İsviçre
    "756-Zürich": 1580, "756-Bern": 1050, "756-Vaud": 830, "756-Aargau": 710,
    "756-Sankt Gallen": 520, "756-Genève": 520, "756-Lucerne": 420,
    "756-Valais": 360, "756-Ticino": 350, "756-Fribourg": 335,
    "756-Basel-Landschaft": 295, "756-Thurgau": 290, "756-Solothurn": 285,
    "756-Graubünden": 205, "756-Basel-Stadt": 200, "756-Neuchâtel": 175,
    "756-Schwyz": 165, "756-Zug": 130, "756-Schaffhausen": 85, "756-Jura": 74,
    "756-Appenzell Ausserrhoden": 55, "756-Nidwalden": 44, "756-Glarus": 41,
    "756-Obwalden": 39, "756-Uri": 37, "756-Appenzell Innerrhoden": 16,
    # Belçika
    "056-Antwerp": 1900, "056-East Flanders": 1560, "056-Hainaut": 1350,
    "056-Brussels": 1240, "056-West Flanders": 1210, "056-Flemish Brabant": 1170,
    "056-Liege": 1110, "056-Limburg": 890, "056-Namur": 500,
    "056-Walloon Brabant": 410, "056-Luxembourg": 290,
    # İspanya
    "724-Andalucía": 8600, "724-Cataluña": 8000, "724-Madrid": 7000,
    "724-Valenciana": 5300, "724-Galicia": 2700, "724-Castilla y León": 2380,
    "724-Canary Is.": 2240, "724-País Vasco": 2220, "724-Castilla-La Mancha": 2100,
    "724-Murcia": 1560, "724-Aragón": 1350, "724-Islas Baleares": 1230,
    "724-Extremadura": 1050, "724-Asturias": 1000, "724-Foral de Navarra": 670,
    "724-Cantabria": 590, "724-La Rioja": 320, "724-Melilla": 86, "724-Ceuta": 84,
    # Birleşik Krallık
    "826-İngiltere": 57100, "826-İskoçya": 5470, "826-Galler": 3130,
    "826-Kuzey İrlanda": 1910,
    # Hindistan (2023 tahmini)
    "356-Uttar Pradesh": 235000, "356-Bihar": 128000, "356-Maharashtra": 126000,
    "356-West Bengal": 100000, "356-Madhya Pradesh": 87000, "356-Rajasthan": 82000,
    "356-Tamil Nadu": 77000, "356-Gujarat": 72000, "356-Karnataka": 69000,
    "356-Andhra Pradesh": 53000, "356-Odisha": 47000, "356-Telangana": 39000,
    "356-Jharkhand": 40000, "356-Assam": 36000, "356-Kerala": 36000,
    "356-Punjab": 31000, "356-Chhattisgarh": 30000, "356-Haryana": 30000,
    "356-Delhi": 21000, "356-Jammu and Kashmir": 14000, "356-Uttarakhand": 12000,
    "356-Himachal Pradesh": 7500, "356-Tripura": 4200, "356-Meghalaya": 3500,
    "356-Manipur": 3300, "356-Nagaland": 2300, "356-Goa": 1600,
    "356-Arunachal Pradesh": 1600, "356-Puducherry": 1600, "356-Mizoram": 1300,
    "356-Chandigarh": 1200, "356-Sikkim": 700,
    "356-Dadra and Nagar Haveli and Daman and Diu": 600,
    "356-Andaman and Nicobar": 400, "356-Ladakh": 300, "356-Lakshadweep": 70,
    # Ukrayna (savaş öncesi kayıtlı nüfus)
    "804-Donets'k": 4000, "804-Dnipropetrovs'k": 3100, "804-Kiev City": 3000,
    "804-Kharkiv": 2500, "804-L'viv": 2500, "804-Odessa": 2350,
    "804-Luhans'k": 2100, "804-Kiev": 1800, "804-Zaporizhzhya": 1650,
    "804-Vinnytsya": 1500, "804-Poltava": 1350, "804-Ivano-Frankivs'k": 1350,
    "804-Transcarpathia": 1240, "804-Khmel'nyts'kyy": 1230, "804-Zhytomyr": 1180,
    "804-Cherkasy": 1150, "804-Rivne": 1140, "804-Mykolayiv": 1090,
    "804-Sumy": 1030, "804-Ternopil'": 1030, "804-Volyn": 1020,
    "804-Kherson": 1000, "804-Chernihiv": 970, "804-Kirovohrad": 910,
    "804-Chernivtsi": 890,
    # Finlandiya
    "246-Uusimaa": 1740, "246-Pirkanmaa": 530, "246-Finland Proper": 490,
    "246-Northern Ostrobothnia": 415, "246-Central Finland": 275,
    "246-Northern Savonia": 245, "246-Satakunta": 215, "246-Päijät-Häme": 200,
    "246-Southern Ostrobothnia": 190, "246-Lapland": 176, "246-Ostrobothnia": 176,
    "246-Tavastia Proper": 170, "246-Kymenlaakso": 165, "246-North Karelia": 162,
    "246-Southern Savonia": 130, "246-South Karelia": 125, "246-Kainuu": 71,
    "246-Central Ostrobothnia": 68,
    # Bolivya
    "068-Santa Cruz": 3400, "068-La Paz": 3000, "068-Cochabamba": 2100,
    "068-Potosí": 900, "068-Chuquisaca": 640, "068-Tarija": 610,
    "068-Oruro": 570, "068-El Beni": 500, "068-Pando": 160,
    # İtalya
    "380-Lombardia": 9900, "380-Veneto": 4850, "380-Campania": 5600,
    "380-Lazio": 5700, "380-Sicily": 4800, "380-Emilia-Romagna": 4450,
    "380-Piemonte": 4250, "380-Apulia": 3900, "380-Toscana": 3660,
    "380-Calabria": 1850, "380-Sardegna": 1580, "380-Liguria": 1500,
    "380-Marche": 1480, "380-Abruzzo": 1270, "380-Friuli-Venezia Giulia": 1200,
    "380-Trentino-Alto Adige": 1080, "380-Umbria": 860, "380-Basilicata": 540,
    "380-Molise": 290, "380-Valle d'Aosta": 123,
})

# Türkiye illeri (TÜİK 2023, bin kişi)
SUBPOP.update({f"792-{k}": v for k, v in {
    "Istanbul": 15650, "Ankara": 5800, "Izmir": 4460, "Bursa": 3230,
    "Antalya": 2700, "Konya": 2300, "Adana": 2270, "Sanliurfa": 2200,
    "Gaziantep": 2160, "Kocaeli": 2130, "Mersin": 1930, "Diyarbakir": 1810,
    "Hatay": 1690, "Manisa": 1470, "Kayseri": 1450, "Samsun": 1370,
    "Balikesir": 1260, "K. Maras": 1180, "Aydin": 1160, "Tekirdag": 1140,
    "Van": 1130, "Sakarya": 1090, "Denizli": 1060, "Mugla": 1050,
    "Eskisehir": 910, "Mardin": 870, "Trabzon": 820, "Malatya": 810,
    "Ordu": 760, "Erzurum": 750, "Afyonkarahisar": 750, "Adiyaman": 640,
    "Sivas": 640, "Batman": 640, "Elazig": 600, "Tokat": 600,
    "Zinguldak": 590, "Kütahya": 580, "Sirnak": 570, "Çanakkale": 570,
    "Osmaniye": 550, "Çorum": 520, "Agri": 510, "Isparta": 450,
    "Giresun": 450, "Aksaray": 440, "Yozgat": 420, "Edirne": 410,
    "Düzce": 410, "Mus": 400, "Kastamonu": 390, "Kirklareli": 380,
    "Nigde": 380, "Usak": 380, "Rize": 350, "Bitlis": 350, "Siirt": 340,
    "Amasya": 340, "Bolu": 320, "Nevsehir": 310, "Yalova": 300,
    "Hakkari": 280, "Bingöl": 280, "Kars": 280, "Kinkkale": 280,
    "Burdur": 270, "Karaman": 260, "Karabük": 250, "Kirsehir": 240,
    "Erzincan": 240, "Bilecik": 230, "Sinop": 220, "Iğdir": 200,
    "Çankiri": 200, "Bartın": 200, "Artvin": 170, "Kilis": 150,
    "Gümüshane": 150, "Ardahan": 92, "Bayburt": 85, "Tunceli": 84,
}.items()})
