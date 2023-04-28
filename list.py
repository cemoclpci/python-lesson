
# 34 => İstanbul
# 35 => İzmir

# sehirler = ["İstanbul","İzmir"]
# plakalar = [34,35]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])


# print(plakalar[sehirler.index("İstanbul")])

# key - value

# plakalar = {"İzmir": 35, "İstanbul": 34}

# plakalar["Bursa"] = 16
# plakalar["Eskişehir"] = 26

# print(plakalar)

urunler = {
    100: {
        "urunAdi" : "Monitör",
        "urunAcikmalasi" : "16 inç",
        "garantiSuresi" : 3,
        "fiyati" : [1500,2500],

    },
    101: {
        "urunAdi" : "SSD",
        "urunAcikmalasi" : "250 GB",
        "garantiSuresi" : 2,
        "fiyati" : [1200,1700],

    }
}

sonuc = urunler[100]["fiyati"]

tutar = urunler[100]["fiyati"][1] + urunler[101]["fiyati"][1]

print(tutar)

