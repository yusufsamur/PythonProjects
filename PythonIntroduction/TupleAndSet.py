#Tuple (demet), liste ile aynıdır ancak bir eleman eklenemez, değiştirilemez veya silinemez

demet = ("Sarı","Mavi","Kırmızı","Yeşil","Turuncu")
print(type(demet))
#Set (kümeler)
#Kümeler sırasızdır, yani elemanlarının indexleri yoktur. Kümelerde aynı eleman birden fazla kez yer alamaz.
print("-------")

kume = {"Sarı","Mavi","Kırmızı","Yeşil","Turuncu"}
print(type(kume))
print(len(kume))
print(kume)

kume.add("Pembe") # kümelere eleman ekleme metodu
print(kume)
kume.remove("Pembe") # kümelerden eleman silme metodu. Eğer eleman kümede yoksa hata verir ve program çalışmayı durdurur.
print(kume)
kume.discard("Pembe") # remove metodunun aynısı ancak hata vermez

#Kümelerde birleşim ve kesişim işlemleri
print("-----")
kume1 = {"a", "b", "c", "d", "e", "f", "g"}
kume2 = {"a", "b", "c", "u", "v", "y", "z"}

print(kume1.intersection(kume2)) # kesişim elemanlarını döndürür
print(kume1.union(kume2)) # birleşim elemanlarını döndürür

print(kume1.difference(kume2)) # Fark metodu. küme 1'de olan, kume 2'de olmayan elemanlar.

print("a" in kume1) # "a", küme 1'de var mı ?

#------------------------------

bosliste = []
bosliste2 = list()

bostuple = ()
bostuple2 = tuple()

boskume = {} # BU BİR KÜME (SET) DEĞİL, BİR DİCT'DİR (SÖZLÜKTÜR).
boskume2 = set()

print(type(boskume))



