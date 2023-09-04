#liste uygulamaları

renkler = ["Siyah", "Beyaz", "Sarı", "Kırmızı", "Yeşil"]
renkler2 = ["Turuncu","Pembe"]
print("Başlangıçtaki listemiz : {} ".format(renkler))

#Liste nasıl parçalanır ?

print("Parçalanmış listemiz : {}".format(renkler[1::2])) # Baştaki rakam kaçıncı indexten başlanacağını, ortadaki rakam hangi indexe kadar süreceğini, sondaki rakam kaçar kaçar yazıldığını belirtir.

#append metodu
#insert metodu
#remove metodu
#extend metodu
#pop metodu
#reverse metodu
#sort ve sorted metotları

renkler.append("Gri") # "Gri" stringini listeye ekler
print("Listemize append metodu ile gri eklendi : {}".format(renkler))

renkler.insert(3,"Mavi") # insert metodu, girilen ilk parametrede aldığı rakama karşılık gelen indexin konumuna; ikinci parametrede aldığı stringi yazar.
print("Listemize insert metodu ile belirtilen indexe istenilen string yazıldı : {}".format(renkler))

renkler.remove("Sarı") # remove metodu, girilen stringi listeden siler.
print("remove metodu ile girilen string listeden silindi : {}".format(renkler))

renkler.extend(renkler2) # Renkler Listesine birden fazla karakter eklenmek istendiğinde extend metodu kullanılır.
print("extend metodu ile listemize renkler2 listesinin karakterlerini ekledik : {} ".format(renkler))

print(renkler.pop()) # renkler listesinin son elemanını siler ve geri döndürür
print("renkler listesinin son elemanı, pop metodu ile silindi : {} ".format(renkler))

renkler.reverse() # renkler listesinin elemanlarının sırasını tersine çevirir.
print("reverse metodu ile listemizin elemanları tersine çevrildi : {}".format(renkler))

renkler.sort() # listedeki stringleri alfabetik, sayıları ise küçükten büyüğe şekilde sıralar. Eğer metodun "reverse" parametresini true girerseniz tam tersi şekilde sıralar.
print("sıralanmış listemiz : {} ".format(renkler))

print("sıralanmış liste (sorted) : {} ".format(sorted(renkler))) # sorted metodu listenin sıralanmış halini geri döndürür (listeyi sıralamaz yani değiştirmez)

#min, max ve in kullanımı
#sum kullanımı
#for döngüsü ile listeyi yazdırmak
#enumerate
#listeyi stringe çevirmek ve join metodu
#stringi listeye çevirmek ve split metodu
print("--------")

sodalar = ["Beypazarı","Sırma","Kızılay","Avşar","Kızılcık"]
sayilar = [12,76,98,34,90]

print(min(sodalar)) #alfabetik önceliği olan stringi döndürecek
print(min(sayilar)) #en küçük sayıyı döndürecek

print(max(sodalar)) #alfabetik önceliği olmayan stringi döndürecek
print(max(sayilar)) #en büyük sayıyı döndürecek

#print(sum(sodalar)) # TypeError: unsupported operand type(s) for +: 'int' and 'str' hatası alınır.
print(sum(sayilar)) #sayıların toplamını döndürecek

for i in sodalar : # sodaların tamamını yazdıran döngü
    print(i)

print(list(enumerate(sodalar,start=1))) #listeyi numaralandırır
print("Beypazarı" in sodalar) # "Beypazarı" sodalar listesinde var mı ?

stringSodalar = " ".join(sodalar) # sodalar listesini bir stringe çevirir
print(stringSodalar)

sodalar2 = stringSodalar.split(" ") #stringSodalar listesini " " karakteri olan noktalardan böldü ve yeni bir liste halinde döndürdü

print(sodalar2)
