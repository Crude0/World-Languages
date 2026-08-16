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


# --- 0.7.0'da eklenen ülkelerin Türkçe adları. Natural Earth Rusya'yı
# İngilizce transliterasyonla yazıyor ("Bashkortostan", "Yevrey"); Çin'de
# de yerel değil pinyin adlar var ("Xizang" = Tibet).
NAME.update({
    # Rusya — cumhuriyetler ve özerk okruglar
    "643-Bashkortostan": "Başkurdistan", "643-Tatarstan": "Tataristan",
    "643-Chuvash": "Çuvaşistan", "643-Sakha (Yakutia)": "Saha (Yakutistan)",
    "643-Tuva": "Tuva", "643-Gorno-Altay": "Altay Cumhuriyeti",
    "643-Altay": "Altay Krayı", "643-Khakass": "Hakasya",
    "643-Chechnya": "Çeçenistan", "643-Ingush": "İnguşetya",
    "643-Dagestan": "Dağıstan", "643-North Ossetia": "Kuzey Osetya",
    "643-Kabardin-Balkar": "Kabardey-Balkar", "643-Karachay-Cherkess": "Karaçay-Çerkes",
    "643-Adygey": "Adigey", "643-Mariy-El": "Mari El", "643-Mordovia": "Mordovya",
    "643-Udmurt": "Udmurtya", "643-Komi": "Komi", "643-Karelia": "Karelya",
    "643-Buryat": "Buryatya", "643-Kalmyk": "Kalmukya",
    "643-Chukchi Autonomous Okrug": "Çukotka", "643-Nenets": "Nenets ÖO",
    "643-Yamal-Nenets": "Yamalo-Nenets", "643-Khanty-Mansiy": "Hantı-Mansi",
    "643-Yevrey": "Yahudi Özerk Oblastı", "643-Chita": "Zabaykalye",
    "643-Maga Buryatdan": "Magadan", "643-Primor'ye": "Primorye",
    "643-Moskva": "Moskova", "643-Moskovskaya": "Moskova Oblastı",
    "643-City of St. Petersburg": "Sankt-Peterburg",
    "643-Arkhangel'sk": "Arhangelsk", "643-Astrakhan'": "Astrahan",
    "643-Chelyabinsk": "Çelyabinsk", "643-Khabarovsk": "Habarovsk",
    "643-Kamchatka": "Kamçatka", "643-Krasnoyarsk": "Krasnoyarsk",
    "643-Nizhegorod": "Nijni Novgorod", "643-Perm'": "Perm",
    "643-Ryazan'": "Ryazan", "643-Sakhalin": "Sahalin",
    "643-Stavropol'": "Stavropol", "643-Tver'": "Tver",
    "643-Tyumen'": "Tümen", "643-Ul'yanovsk": "Ulyanovsk",
    "643-Voronezh": "Voronej", "643-Yaroslavl'": "Yaroslavl",
    "643-Orel": "Oryol", "643-Irkutsk": "İrkutsk", "643-Ivanovo": "İvanovo",
    # Çin
    "156-Xizang": "Tibet", "156-Inner Mongol": "İç Moğolistan",
    "156-Xinjiang": "Sincan (Doğu Türkistan)", "156-Beijing": "Pekin",
    "156-Shanghai": "Şanghay", "156-Guangdong": "Guangdong",
    "156-Heilongjiang": "Heilongjiang", "156-Shaanxi": "Şaanksi",
    "156-Shanxi": "Şanksi", "156-Shandong": "Şandong", "156-Sichuan": "Siçuan",
    "156-Chongqing": "Çongçing", "156-Zhejiang": "Zhejiang",
    "156-Tianjin": "Tiencin", "156-Qinghai": "Çinghay",
    # Güney Afrika
    "710-Western Cape": "Batı Cape", "710-Eastern Cape": "Doğu Cape",
    "710-Northern Cape": "Kuzey Cape", "710-Free State": "Özgür Devlet",
    "710-North West": "Kuzey Batı", "710-KwaZulu-Natal": "KwaZulu-Natal",
    # Fransa
    "250-Guyane française": "Fransız Guyanası", "250-Corse": "Korsika",
    "250-Bretagne": "Bretanya", "250-Normandie": "Normandiya",
    "250-Réunion": "Réunion", "250-Île-de-France": "Île-de-France",
    # Almanya
    "276-Bayern": "Bavyera", "276-Sachsen": "Saksonya",
    "276-Sachsen-Anhalt": "Saksonya-Anhalt", "276-Niedersachsen": "Aşağı Saksonya",
    "276-Nordrhein-Westfalen": "Kuzey Ren-Vestfalya", "276-Hessen": "Hessen",
    "276-Thüringen": "Türingiya", "276-Rheinland-Pfalz": "Renanya-Pfalz",
    "276-Mecklenburg-Vorpommern": "Mecklenburg-Ön Pomeranya",
    "276-Baden-Württemberg": "Baden-Württemberg",
})

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


# ================================================================== Rusya
# Kaynak: 2021 Rusya nüfus sayımı (Всероссийская перепись населения 2021),
# "ana dil" ve "evde konuşulan dil" soruları. Sayımın dil bölümü 2010'a göre
# daha çok cevapsız içeriyor; oranlar cevap verenlere göre normalleştirildi.
# Rusya'da 30'dan fazla dil cumhuriyet düzeyinde resmî statülüdür; harita
# bunu ilk kez gösteriyor.
#
# Kırım ve Sivastopol bilerek yok: Natural Earth bu iki birimi Rusya'ya
# bağlıyor, depo ise sınırlarda taraf tutmuyor (bkz. build_subs.py SKIP).

RU = "Rusça"

# çoğunluğu Rusça olan oblast/kray'lar — tek satırlık kısayol
for _n, _p in {
    "Altay": 97, "Amur": 98, "Arkhangel'sk": 98, "Belgorod": 97, "Bryansk": 97,
    "City of St. Petersburg": 98, "Ivanovo": 98, "Kaliningrad": 96, "Kaluga": 97,
    "Kamchatka": 96, "Kemerovo": 97, "Khabarovsk": 97, "Kostroma": 98,
    "Krasnoyarsk": 97, "Kursk": 97, "Leningrad": 97, "Lipetsk": 98,
    "Maga Buryatdan": 97, "Moskovskaya": 96, "Moskva": 95, "Murmansk": 97,
    "Novgorod": 98, "Novosibirsk": 97, "Orel": 98, "Primor'ye": 98,
    "Pskov": 98, "Ryazan'": 98, "Smolensk": 98, "Tambov": 98, "Tomsk": 96,
    "Tula": 98, "Vladimir": 98, "Vologda": 98, "Voronezh": 98,
    "Yaroslavl'": 98, "Yevrey": 99, "Irkutsk": 97,
}.items():
    put("643", [(RU, _p)], _n)

# Türk dilli cumhuriyetler
put("643", [("Tatarca", 52), (RU, 44), ("Çuvaşça", 3)], "Tatarstan")
put("643", [("Tatarca", 30), ("Başkurtça", 26), (RU, 40)], "Bashkortostan")
put("643", [("Çuvaşça", 52), (RU, 45), ("Tatarca", 2)], "Chuvash")
put("643", [("Sahaca", 49), (RU, 45), ("Evenkice", 1)], "Sakha (Yakutia)")
put("643", [("Tuvaca", 82), (RU, 16)], "Tuva")
put("643", [("Altayca", 34), (RU, 63)], "Gorno-Altay")
put("643", [("Hakasça", 11), (RU, 87)], "Khakass")

# Kafkasya
put("643", [("Çeçence", 95), (RU, 4)], "Chechnya")
put("643", [("İnguşça", 94), ("Çeçence", 4), (RU, 2)], "Ingush")
put("643", [("Avarca", 29), ("Dargice", 17), ("Kumukça", 15), ("Lezgice", 13),
            ("Lakça", 5), ("Tabasaranca", 4), ("Azerbaycanca", 4),
            ("Çeçence", 3), (RU, 4)], "Dagestan")
put("643", [("Osetçe", 62), (RU, 29), ("İnguşça", 3)], "North Ossetia")
put("643", [("Kabardeyce", 53), (RU, 32), ("Karaçay-Balkarca", 11)], "Kabardin-Balkar")
put("643", [("Karaçay-Balkarca", 39), (RU, 32), ("Kabardeyce", 11), ("Abazaca", 7),
            ("Nogayca", 3)], "Karachay-Cherkess")
put("643", [("Adigece", 24), (RU, 74)], "Adygey")

# Ural ve Moğol dilli cumhuriyetler
put("643", [("Marice", 42), (RU, 53), ("Tatarca", 4)], "Mariy-El")
put("643", [("Mordvaca", 33), (RU, 62), ("Tatarca", 5)], "Mordovia")
put("643", [("Udmurtça", 24), (RU, 72), ("Tatarca", 7)], "Udmurt")
put("643", [("Komice", 19), (RU, 78)], "Komi")
put("643", [("Karelce", 2), (RU, 93), ("Fince", 1)], "Karelia")
put("643", [("Buryatça", 29), (RU, 68)], "Buryat")
put("643", [("Kalmukça", 40), (RU, 55)], "Kalmyk")
put("643", [("Buryatça", 5), (RU, 94)], "Chita")

# Kuzey: yerli diller küçük ama bölgenin adını veriyor
put("643", [("Nenetsçe", 13), (RU, 85)], "Nenets")
put("643", [("Nenetsçe", 6), ("Hantıca", 2), ("Tatarca", 3), (RU, 86)], "Yamal-Nenets")
put("643", [("Tatarca", 3), ("Başkurtça", 2), (RU, 90)], "Khanty-Mansiy")
put("643", [("Çukçice", 7), (RU, 89)], "Chukchi Autonomous Okrug")

# İdil-Ural ve güney: Rusça çoğunlukta ama azınlık dilleri kayda değer
put("643", [(RU, 88), ("Tatarca", 6), ("Kazakça", 3), ("Başkurtça", 2.5)], "Orenburg")
put("643", [(RU, 89), ("Tatarca", 6), ("Çuvaşça", 6)], "Ul'yanovsk")
put("643", [(RU, 89), ("Tatarca", 4), ("Çuvaşça", 3), ("Mordvaca", 2)], "Samara")
put("643", [(RU, 91), ("Tatarca", 5), ("Mordvaca", 3)], "Penza")
put("643", [(RU, 92), ("Tatarca", 4.5), ("Komice", 2), ("Başkurtça", 1.5)], "Perm'")
put("643", [(RU, 92), ("Tatarca", 4), ("Çuvaşça", 1)], "Tyumen'")
put("643", [(RU, 93), ("Tatarca", 3.5), ("Başkurtça", 1)], "Sverdlovsk")
put("643", [(RU, 92), ("Tatarca", 4), ("Başkurtça", 2)], "Chelyabinsk")
put("643", [(RU, 96), ("Başkurtça", 2), ("Tatarca", 2)], "Kurgan")
put("643", [(RU, 96), ("Tatarca", 1.5), ("Mordvaca", 1)], "Nizhegorod")
put("643", [(RU, 96), ("Marice", 2), ("Tatarca", 2)], "Kirov")
put("643", [(RU, 93), ("Kazakça", 3), ("Tatarca", 2)], "Saratov")
put("643", [(RU, 94), ("Kazakça", 1.5)], "Volgograd")
put("643", [(RU, 88), ("Kazakça", 7), ("Tatarca", 4)], "Astrakhan'")
put("643", [(RU, 95), ("Kazakça", 2), ("Almanca", 1.5)], "Omsk")
put("643", [(RU, 94), ("Ermenice", 5)], "Krasnodar")
put("643", [(RU, 95), ("Ermenice", 2.5)], "Rostov")
put("643", [(RU, 88), ("Ermenice", 5), ("Dargice", 2)], "Stavropol'")
put("643", [(RU, 96), ("Korece", 5)], "Sakhalin")
put("643", [(RU, 97), ("Karelce", 0.5)], "Tver'")


# =========================================================== Güney Afrika
# Kaynak: Census 2022, "evde en çok konuşulan dil". Ülkenin 12 resmî dili
# var ve hiçbiri ülke genelinde çoğunluk değil; asıl dağılım il düzeyinde.
put("710", [("Afrikaanca", 41), ("Xhosa", 32), ("İngilizce", 21)], "Western Cape")
put("710", [("Xhosa", 77), ("Afrikaanca", 10), ("İngilizce", 6)], "Eastern Cape")
put("710", [("Afrikaanca", 66), ("Setsvana", 21), ("Xhosa", 6)], "Northern Cape")
put("710", [("Sesotho", 62), ("Afrikaanca", 11), ("Xhosa", 8), ("Setsvana", 5)], "Free State")
put("710", [("Zuluca", 78), ("İngilizce", 12), ("Xhosa", 5)], "KwaZulu-Natal")
put("710", [("Setsvana", 60), ("Afrikaanca", 8), ("Sesotho", 6), ("Xhosa", 5)], "North West")
put("710", [("Zuluca", 20), ("İngilizce", 15), ("Sesotho", 12), ("Afrikaanca", 11),
            ("Sepedi", 10), ("Setsvana", 9), ("Tsonga", 7), ("Xhosa", 6)], "Gauteng")
put("710", [("Sisvati", 27), ("Zuluca", 24), ("Tsonga", 10), ("Ndebele", 10),
            ("Sepedi", 9)], "Mpumalanga")
put("710", [("Sepedi", 52), ("Tsonga", 17), ("Venda", 17)], "Limpopo")

# ================================================================ Nijerya
# Kaynak: Ethnologue ve ulusal etnik dağılım tahminleri; Nijerya'da dil
# sorusu soran bir sayım yok. Nijerya Pidgini her yerde ortak dil olarak
# konuşuluyor, güneyde ana dile en yakın konumda.
put("566", [("Hausa", 92), ("Fulaca", 6)], "Kano", "Katsina", "Jigawa", "Zamfara")
put("566", [("Hausa", 85), ("Fulaca", 10)], "Kebbi", "Sokoto")
put("566", [("Hausa", 68), ("Fulaca", 12), ("Nijerya Pidgini", 25)], "Kaduna")
put("566", [("Hausa", 75), ("Fulaca", 15), ("Nijerya Pidgini", 20)], "Bauchi", "Gombe")
put("566", [("Kanuri", 55), ("Hausa", 30), ("Fulaca", 8)], "Borno", "Yobe")
put("566", [("Fulaca", 35), ("Hausa", 25), ("Nijerya Pidgini", 30)], "Adamawa", "Taraba")
put("566", [("Hausa", 45), ("Nupe", 20), ("Nijerya Pidgini", 35)], "Niger")
put("566", [("Yorubaca", 75), ("Hausa", 10), ("Nijerya Pidgini", 25)], "Kwara")
put("566", [("İgboca", 30), ("Yorubaca", 20), ("Hausa", 15),
            ("Nijerya Pidgini", 45)], "Kogi")
put("566", [("Tiv", 60), ("İgboca", 10), ("Nijerya Pidgini", 40)], "Benue")
put("566", [("Hausa", 30), ("Nijerya Pidgini", 55)], "Plateau", "Nassarawa")
put("566", [("Hausa", 25), ("Yorubaca", 15), ("İgboca", 12),
            ("Nijerya Pidgini", 60)], "Federal Capital Territory")
put("566", [("Yorubaca", 90), ("Nijerya Pidgini", 30)], "Ogun", "Oyo", "Osun",
    "Ondo", "Ekiti")
put("566", [("Yorubaca", 70), ("İgboca", 8), ("Nijerya Pidgini", 55),
            ("İngilizce", 10)], "Lagos")
put("566", [("İgboca", 92), ("Nijerya Pidgini", 45)], "Abia", "Anambra",
    "Ebonyi", "Enugu", "Imo")
put("566", [("Edo", 55), ("İgboca", 12), ("Nijerya Pidgini", 75)], "Edo")
put("566", [("Urhobo", 30), ("İgboca", 20), ("İjo dilleri", 12),
            ("Nijerya Pidgini", 80)], "Delta")
put("566", [("İjo dilleri", 70), ("Nijerya Pidgini", 85)], "Bayelsa")
put("566", [("İjo dilleri", 25), ("İgboca", 25), ("Nijerya Pidgini", 85)], "Rivers")
put("566", [("İbibioca", 75), ("Nijerya Pidgini", 70)], "Akwa Ibom")
put("566", [("Efikçe", 40), ("İbibioca", 20), ("Nijerya Pidgini", 75)], "Cross River")


# =================================================================== Çin
# Kaynak: Çin dil atlası (中国语言地图集) lehçe/dil bölgeleri ve 2020 nüfus
# sayımının etnik dağılımı. "Çince" tek bir dil değil: Mandarin, Kantonca,
# Wu, Min, Hakka, Xiang ve Gan karşılıklı anlaşılmaz; harita bunları ayırıyor.
# Mandarin her yerde okul ve devlet dili olduğu için oranlar %100'ü aşar.
MAN = "Mandarin Çincesi"
for _n in ("Beijing", "Tianjin", "Hebei", "Shanxi", "Shandong", "Henan",
           "Shaanxi", "Gansu", "Ningxia", "Jilin", "Liaoning", "Heilongjiang"):
    put("156", [(MAN, 97)], _n)
put("156", [(MAN, 82), ("Moğolca", 17)], "Inner Mongol")
put("156", [("Uygurca", 45), (MAN, 42), ("Kazakça", 7), ("Kırgızca", 1)], "Xinjiang")
put("156", [("Tibetçe", 90), (MAN, 9)], "Xizang")
put("156", [(MAN, 74), ("Tibetçe", 22)], "Qinghai")
put("156", [(MAN, 95), ("Yice", 3)], "Sichuan")
put("156", [(MAN, 97)], "Chongqing")
put("156", [(MAN, 85), ("Miao dilleri", 8), ("Buyice", 5)], "Guizhou")
put("156", [(MAN, 70), ("Yice", 11), ("Miao dilleri", 3), ("Tayca", 3)], "Yunnan")
put("156", [("Kantonca", 60), (MAN, 22), ("Hakka", 9), ("Min Çincesi", 9)], "Guangdong")
put("156", [(MAN, 40), ("Zhuangca", 30), ("Kantonca", 25)], "Guangxi")
put("156", [("Min Çincesi", 65), (MAN, 30)], "Hainan")
put("156", [("Min Çincesi", 70), (MAN, 22), ("Hakka", 6)], "Fujian")
put("156", [("Wu Çincesi", 78), (MAN, 20)], "Zhejiang")
put("156", [("Wu Çincesi", 70), (MAN, 28)], "Shanghai")
put("156", [(MAN, 55), ("Wu Çincesi", 42)], "Jiangsu")
put("156", [(MAN, 75), ("Wu Çincesi", 12), ("Gan Çincesi", 5)], "Anhui")
put("156", [("Gan Çincesi", 65), (MAN, 18), ("Hakka", 15)], "Jiangxi")
put("156", [("Xiang Çincesi", 65), (MAN, 20), ("Gan Çincesi", 5),
            ("Miao dilleri", 3)], "Hunan")
put("156", [(MAN, 92), ("Gan Çincesi", 5)], "Hubei")

# ================================================================ Fransa
# Ölçüt evde konuşulan dil. Denizaşırı bölgelerde Fransızcayı
# *konuşabilenler* çok daha yüksek (Réunion'da ~%90) ama evin dili
# kreol. Fransa'da sayım dil sormaz. Bölgesel diller için kaynak: INED/INSEE
# "Étude de l'histoire familiale" (1999) ve DGLFLF raporları; göçmen
# dilleri için "Trajectoires et Origines" (2019-20). Hepsi tahmindir.
FR = "Fransızca"
put("250", [(FR, 96), ("Korsikaca", 45)], "Corse")
put("250", [(FR, 99), ("Bretonca", 5)], "Bretagne")
put("250", [(FR, 98), ("Almanca", 12), ("Arapça", 3), ("Türkçe", 2)], "Grand Est")
put("250", [(FR, 99), ("Oksitanca", 4), ("Arapça", 3), ("Katalanca", 1)], "Occitanie")
put("250", [(FR, 99), ("Oksitanca", 3), ("Baskça", 2), ("Portekizce", 1)], "Nouvelle-Aquitaine")
put("250", [(FR, 96), ("Arapça", 5), ("Portekizce", 2), ("Türkçe", 1),
            ("Mandarin Çincesi", 1)], "Île-de-France")
put("250", [(FR, 98), ("Oksitanca", 2), ("Arapça", 4), ("İtalyanca", 1)],
    "Provence-Alpes-Côte-d'Azur")
put("250", [(FR, 98), ("Oksitanca", 2), ("Arapça", 3), ("Portekizce", 1)],
    "Auvergne-Rhône-Alpes")
put("250", [(FR, 99), ("Arapça", 2), ("Portekizce", 1)], "Hauts-de-France",
    "Normandie", "Centre-Val de Loire", "Pays de la Loire", "Bourgogne-Franche-Comté")
put("250", [("Antil Kreolcesi", 85), (FR, 45)], "Guadeloupe", "Martinique")
put("250", [("Guyana Kreolcesi", 40), (FR, 35), ("Portekizce", 10)], "Guyane française")
put("250", [("Réunion Kreolcesi", 85), (FR, 40)], "Réunion")
put("250", [("Komorca", 60), ("Kibushi", 25), (FR, 40)], "Mayotte")

# =============================================================== Almanya
# Kaynak: Zensus 2022, hanede ağırlıklı olarak konuşulan dil. Almanya'da
# uzun süre dil sorusu sorulmamıştı; 2022 sayımı ilk kez sordu.
DE = "Almanca"
put("276", [(DE, 78), ("Türkçe", 5), ("Rusça", 3.5), ("Arapça", 3),
            ("Lehçe", 2), ("İngilizce", 2)], "Berlin")
put("276", [(DE, 85), ("Türkçe", 4), ("Arapça", 2), ("Lehçe", 2),
            ("Rusça", 1.5)], "Nordrhein-Westfalen")
put("276", [(DE, 87), ("Türkçe", 2), ("Romence", 1.5), ("Rusça", 1.5),
            ("Arapça", 1)], "Bayern")
put("276", [(DE, 85), ("Türkçe", 3), ("Romence", 1.5), ("İtalyanca", 1.5),
            ("Rusça", 1.5)], "Baden-Württemberg")
put("276", [(DE, 84), ("Türkçe", 3.5), ("Arapça", 2), ("Lehçe", 1.5)], "Hessen")
put("276", [(DE, 82), ("Türkçe", 3.5), ("Arapça", 2), ("Lehçe", 2),
            ("Rusça", 2)], "Hamburg")
put("276", [(DE, 81), ("Türkçe", 5), ("Arapça", 3), ("Lehçe", 2)], "Bremen")
put("276", [(DE, 89), ("Türkçe", 2.5), ("Arapça", 1.5), ("Lehçe", 1.5),
            ("Rusça", 1.5)], "Niedersachsen")
put("276", [(DE, 88), ("Türkçe", 2), ("Arapça", 1.5), ("Lehçe", 1.5)], "Rheinland-Pfalz")
put("276", [(DE, 89), ("Türkçe", 2), ("Arapça", 2), ("İtalyanca", 1.5)], "Saarland")
put("276", [(DE, 92), ("Türkçe", 1.5), ("Danca", 1), ("Arapça", 1)], "Schleswig-Holstein")
put("276", [(DE, 95), ("Rusça", 1.5), ("Ukraynaca", 1), ("Sorbca", 0.3)], "Sachsen")
put("276", [(DE, 95), ("Rusça", 1.5), ("Ukraynaca", 1), ("Sorbca", 0.1)], "Brandenburg")
put("276", [(DE, 96), ("Rusça", 1.5), ("Ukraynaca", 1)], "Sachsen-Anhalt",
    "Thüringen", "Mecklenburg-Vorpommern")

# --- 0.7.0'da eklenen bölgelerin nüfusları (bin kişi)
# Rusya: Rosstat 2024 tahmini · Çin: 2020 sayımı · Nijerya: 2022 tahmini
# Güney Afrika: Census 2022 · Fransa: INSEE 2023 · Almanya: Destatis 2023
SUBPOP.update({
    # Rusya
    "643-Moskva": 13100, "643-Moskovskaya": 8600, "643-Krasnodar": 5900,
    "643-City of St. Petersburg": 5600, "643-Sverdlovsk": 4200,
    "643-Rostov": 4150, "643-Bashkortostan": 4050, "643-Tatarstan": 4000,
    "643-Chelyabinsk": 3400, "643-Nizhegorod": 3100, "643-Samara": 3100,
    "643-Dagestan": 3200, "643-Krasnoyarsk": 2850, "643-Novosibirsk": 2800,
    "643-Kemerovo": 2560, "643-Perm'": 2500, "643-Stavropol'": 2900,
    "643-Saratov": 2350, "643-Voronezh": 2270, "643-Volgograd": 2450,
    "643-Tyumen'": 3900, "643-Irkutsk": 2350, "643-Altay": 2100,
    "643-Omsk": 1830, "643-Leningrad": 2000, "643-Belgorod": 1500,
    "643-Primor'ye": 1830, "643-Khabarovsk": 1280, "643-Vladimir": 1320,
    "643-Tula": 1450, "643-Yaroslavl'": 1200, "643-Ul'yanovsk": 1200,
    "643-Udmurt": 1450, "643-Chuvash": 1180, "643-Penza": 1230,
    "643-Kirov": 1130, "643-Bryansk": 1150, "643-Ryazan'": 1080,
    "643-Lipetsk": 1120, "643-Tver'": 1230, "643-Khanty-Mansiy": 1730,
    "643-Chechnya": 1550, "643-Kursk": 1080, "643-Kaliningrad": 1030,
    "643-Kaluga": 1070, "643-Tambov": 950, "643-Arkhangel'sk": 1000,
    "643-Vologda": 1130, "643-Smolensk": 900, "643-Astrakhan'": 950,
    "643-Kurgan": 800, "643-Orenburg": 1900, "643-Mordovia": 780,
    "643-Ivanovo": 970, "643-Mariy-El": 670, "643-Sakha (Yakutia)": 1000,
    "643-Buryat": 980, "643-Komi": 720, "643-Kabardin-Balkar": 900,
    "643-North Ossetia": 690, "643-Karelia": 520, "643-Novgorod": 580,
    "643-Pskov": 590, "643-Orel": 700, "643-Kostroma": 570,
    "643-Murmansk": 660, "643-Yamal-Nenets": 510, "643-Ingush": 520,
    "643-Karachay-Cherkess": 460, "643-Adygey": 500, "643-Tomsk": 1050,
    "643-Amur": 750, "643-Zabaykalye": 990, "643-Chita": 990,
    "643-Khakass": 530, "643-Sakhalin": 460, "643-Kalmyk": 260,
    "643-Kamchatka": 290, "643-Maga Buryatdan": 135, "643-Gorno-Altay": 210,
    "643-Tuva": 340, "643-Yevrey": 145, "643-Nenets": 41,
    "643-Chukchi Autonomous Okrug": 48,
    # Çin
    "156-Guangdong": 126000, "156-Shandong": 101500, "156-Henan": 99400,
    "156-Jiangsu": 84700, "156-Sichuan": 83700, "156-Hebei": 74600,
    "156-Hunan": 66400, "156-Zhejiang": 64600, "156-Anhui": 61000,
    "156-Hubei": 57800, "156-Guangxi": 50100, "156-Yunnan": 47200,
    "156-Jiangxi": 45200, "156-Liaoning": 42600, "156-Fujian": 41500,
    "156-Shaanxi": 39500, "156-Heilongjiang": 31900, "156-Shanxi": 34900,
    "156-Guizhou": 38600, "156-Chongqing": 32100, "156-Jilin": 24100,
    "156-Gansu": 25000, "156-Inner Mongol": 24000, "156-Shanghai": 24900,
    "156-Xinjiang": 25900, "156-Beijing": 21900, "156-Tianjin": 13900,
    "156-Hainan": 10100, "156-Ningxia": 7200, "156-Qinghai": 5900,
    "156-Xizang": 3650,
    # Nijerya
    "566-Lagos": 13500, "566-Kano": 15100, "566-Kaduna": 8900,
    "566-Katsina": 9300, "566-Oyo": 7900, "566-Rivers": 7300,
    "566-Bauchi": 6900, "566-Jigawa": 6100, "566-Benue": 6100,
    "566-Anambra": 5900, "566-Borno": 5900, "566-Delta": 5600,
    "566-Imo": 5400, "566-Niger": 6100, "566-Akwa Ibom": 5500,
    "566-Ogun": 5900, "566-Sokoto": 5700, "566-Ondo": 4900,
    "566-Osun": 4700, "566-Kogi": 4500, "566-Zamfara": 5300,
    "566-Enugu": 4400, "566-Kebbi": 4900, "566-Edo": 4500,
    "566-Plateau": 4400, "566-Adamawa": 4500, "566-Cross River": 4200,
    "566-Abia": 4000, "566-Ekiti": 3400, "566-Kwara": 3400,
    "566-Gombe": 3600, "566-Yobe": 3600, "566-Taraba": 3300,
    "566-Ebonyi": 3000, "566-Nassarawa": 2700, "566-Bayelsa": 2400,
    "566-Federal Capital Territory": 3800,
    # Güney Afrika
    "710-Gauteng": 15100, "710-KwaZulu-Natal": 12400, "710-Western Cape": 7400,
    "710-Eastern Cape": 7200, "710-Limpopo": 6600, "710-Mpumalanga": 5100,
    "710-North West": 4100, "710-Free State": 2900, "710-Northern Cape": 1350,
    # Fransa
    "250-Île-de-France": 12300, "250-Auvergne-Rhône-Alpes": 8200,
    "250-Nouvelle-Aquitaine": 6100, "250-Occitanie": 6100,
    "250-Hauts-de-France": 6000, "250-Grand Est": 5550,
    "250-Provence-Alpes-Côte-d'Azur": 5150, "250-Pays de la Loire": 3900,
    "250-Normandie": 3300, "250-Bretagne": 3450, "250-Bourgogne-Franche-Comté": 2800,
    "250-Centre-Val de Loire": 2570, "250-Réunion": 880, "250-Guadeloupe": 380,
    "250-Martinique": 350, "250-Guyane française": 290, "250-Mayotte": 320,
    "250-Corse": 350,
    # Almanya
    "276-Nordrhein-Westfalen": 18100, "276-Bayern": 13400,
    "276-Baden-Württemberg": 11300, "276-Niedersachsen": 8100,
    "276-Hessen": 6400, "276-Rheinland-Pfalz": 4200, "276-Sachsen": 4050,
    "276-Berlin": 3800, "276-Schleswig-Holstein": 2950,
    "276-Brandenburg": 2570, "276-Sachsen-Anhalt": 2160, "276-Thüringen": 2110,
    "276-Hamburg": 1900, "276-Mecklenburg-Vorpommern": 1630,
    "276-Saarland": 995, "276-Bremen": 690,
})
