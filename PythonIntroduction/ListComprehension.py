numbers = [1,2,3,4,5,6,7,8,9]
#Verilen listedeki rakamlardan oluşan bir liste oluşturalım
# list2 = []
# for number in numbers:
#     list2.append(number)


# list3 = [number for number in numbers]
# print(list3)

#Verilen listedeki rakamların karelerinden oluşan bir liste oluşturalım
#
# list3 = []
# for number in numbers:
#     list3.append(number*number)
# print(list3)

# list3 = [number*number for number in numbers]
# print(list3)

#Verilen listedeki çift rakamların karelerinden oluşan bir liste oluşturalım

# list3 = []
# for number in numbers:
#     if number %2 == 0:
#         list3.append(number*number)
#
#list3 = [number*number for number in numbers if number %2 == 0]

#Verilen listedeki 4'ten büyük çift rakamların karelerinden oluşan bir liste oluşturalım
# list3 = []
#
# for number in numbers:
#     if number %2 == 0 and number >4:
#         list3.append(number*number)

#list3 = [number*number for number in numbers if number %2 == 0 and number > 4 ]

# [(1,a),(1,b),(1,c),(1,d),(2,a) .... ,(4,d)] biçiminde ikililerden oluşan bir liste oluşturalım

numbers = [1,2,3,4]
letters = "abcd"
# list3 = []
# for number in numbers:
#     for letter in letters:
#         list3.append((number,letter))

#list3 = [(number,letter) for number in numbers for letter in letters ]

# Birinci listede bulunup ikinci listede bulunmayan rakamların karesinden oluşan bir liste oluşturalım

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,6,9,5]

# list3 = []
# for i in list1:
#     if not i in list2:
#         list3.append(i*i)
# print(list3)

# list3 = [i*i for i in list1 if i not in list2 ]
# print(list3)

#Verilen listeden elemanları tek tek alan [1,2,3,4,5,6,7,8,9,10,11,12] biçiminde bir liste oluşturalım.
list_ = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
# list3 = []
# for i in list_:
#     for number in i:
#         list3.append(number)

# list3 = [j for i in list_ for j in i]
# print(list3)

# list_methods = []
# for method in dir(list):
#     if not method.startswith("_"):
#         list_methods.append(method)

# list_methods = [method for method in dir(list) if not method.startswith("_")]
# print(list_methods)

