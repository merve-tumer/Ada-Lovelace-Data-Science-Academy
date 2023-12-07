def karakter_sayisi(dizi):
    karakter_sozlugu = {}
    for karakter in dizi:
        if karakter in karakter_sozlugu:
            karakter_sozlugu[karakter] += 1
        else:
            karakter_sozlugu[karakter] = 1
    return karakter_sozlugu

kullanicidan_alinan_dizi = input("Lütfen bir dize girin: ")

sonuc = karakter_sayisi(kullanicidan_alinan_dizi)
print(sonuc)
