tag_fiyati = int(input("Tag fiyatını giriniz: "))
isminiz = input("Kullanıcı adınızı giriniz: ")
oynama_saati = int(input("Oynama saatinizi giriniz: "))

print("\nTAG SATIN ALMA SİSTEMİ")
print("=======================")

if tag_fiyati >= 3000:
    if oynama_saati >= 150:
        print("Tag almak için saatiniz ve bakiyeniz yeterli.")
        print("1. Tag satın al")
        print("2. İptal et")
        secim = input("Seçiminizi yapınız (1 veya 2): ")
        
        if secim == "1":
            print("Tag satın alındı.")
        elif secim == "2":
            print("Tag satın alma işlemi iptal edildi.")
        else:
            print("Geçersiz seçim. Tag satın alma işlemi iptal edildi.")
    else:
        print(f"{isminiz}, tag almak için oynama saatiniz yetmiyor.")
else:
    print(f"{isminiz}, tag almak için yeterli bakiyeniz bulunmuyor.")
