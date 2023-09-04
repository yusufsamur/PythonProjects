# 10000'den küçük olan asal sayılardan kaç tanesi 3 ile başlayıp 7 ile bitiyor ?
# asal_liste = list()
#
# for i in range(2,10000):
#     for k in range(2,i):
#         if i % k == 0:
#             break
#         elif k == (i-1):
#             asal_liste.append(i)
#             break
#
# print (type(asal_liste))
# print(asal_liste)
# count = 0
# liste2 = list()
# for i in asal_liste:
#     if len(str(i)) == 2:
#         if i % 10 == 7 and i // 10 == 3:
#             liste2.append(i)
#             count +=1
#     elif len(str(i)) == 3:
#         if i % 10 == 7 and i // 100 == 3:
#             liste2.append(i)
#             count += 1
#     elif len(str(i)) == 4:
#         if i % 10 == 7 and i // 1000 == 3:
#             liste2.append(i)
#             count += 1
#
# print(count)
# print(liste2)

# 3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir ?
# count = 0
#
# for i in range(100,1000):
#     if i == (i % 10)**3 + ((i // 10)%10)**3 + (i // 100)**3:
#         print(i)
#         count +=1
#
# print(f"kaç tanesi : {count} ")

# İlk 100 Fibonacci terimi

# i = 0
# k = 2
# l = 1
# count = 0
# while True:
#     if count == 100:
#         break
#     print(l)
#     count += 1
#     yedek = k
#     i = k+l
#     k = i
#     l = yedek


# 100 basamaklı ilk fibonacci sayısı nedir ?
#
# fibonacci_list = [1,1]
# i = 2
# while True:
#     fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
#     i+=1
#     print(fibonacci_list[i-1])
#     if len(str(fibonacci_list[i-1])) == 100:
#         print(fibonacci_list[i-1])
#         break













