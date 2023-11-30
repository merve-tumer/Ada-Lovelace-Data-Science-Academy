def liste_uzunlugu(liste):
    if not liste:
        raise ValueError("Hata: Liste boş, en az bir eleman ekleyin.")
    return len(liste)

try:
    kullanicidan_alinan_liste = input("Lütfen bir liste girin ")
    uzunluk = liste_uzunlugu([int(eleman) for eleman in kullanicidan_alinan_liste.split(',')])
    print(f"Liste uzunluğu: {uzunluk}")
except ValueError as e:
    print(e)
