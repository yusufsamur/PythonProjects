# Dictionaries (Sözlükler)

kisi = {"isim" : "ali", "yas" : 20, "cinsiyet" : "m", "hobiler" : ["Sinema", "Konser", "Yazılım"] }
# Sözlüklerde anahtar kelime (Key) mutlaka int veya str olmalıdır ancak değer (Value) herhangi bir tip olabilir.
print(kisi)
print(kisi["isim"])
print(kisi["hobiler"]) # Sözlüklerde index yoktur, anahtar kelimeler vardır.

kisi["isim"] = "Ahmet"
print(kisi)

kisi.update({"isim" : "Yusuf", "yas" : 19})
print(kisi)

kisi["id"] = 123214
print(kisi)

del kisi["id"]
print(kisi)

for x in kisi :
    print(x) # Key elemanları yazdırır

print("------")
for x in kisi :
    print(kisi[x]) # Value elemanları yazdırır

print("-------")
for x in kisi :
    print(str(x) + ": " + str(kisi[x])) # Dict'i for ile yazdırır

print(kisi.keys())
print(kisi.values())
print(kisi.items())

for k in kisi.items():
    print(k)

print(kisi.get("id","Şibididom"))#Eğer aranan Key, sözlükte yoksa program hata vermez ve çalışmaya devam eder. 2. Parametreyi girerseniz,eleman bulunamadığında onu döndürür.



