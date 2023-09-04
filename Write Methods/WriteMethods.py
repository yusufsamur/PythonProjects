list_methods = []
set_methods = []
string_methods = []
tuple_methods = []
dict_methods = []
for metot in dir(list):
    if metot.startswith("_"):
        continue
    else:
        list_methods.append(metot)

for metot in dir(set):
    if metot.startswith("_"):
        continue
    else:
        set_methods.append(metot)
for metot in dir(str):
    if metot.startswith("_"):
        continue
    else:
        string_methods.append(metot)
for metot in dir(tuple):
    if metot.startswith("_"):
        continue
    else:
        tuple_methods.append(metot)

for metot in dir(dict):
    if metot.startswith("_"):
        continue
    else:
        dict_methods.append(metot)

titles = ["List Methods", "Set Methods", "String Methods", "Tuple Methods", "Dict Methods"]
classes = [list_methods, set_methods, string_methods, tuple_methods, dict_methods]

maxLen = 0
for class_ in classes:
    if maxLen < len(class_):
        maxLen = len(class_)
with open("methods.txt", "w") as f:
    for i in titles:
        print(i, end=" " * (30 - len(i)))
        f.write(i)
        f.write(" " * (30 - len(i)))
    print("\n")
    f.write("\n\n")
    for i in range(maxLen):
        for class_ in classes:
            if i >= len(class_):
                print("-------", end="")
                print(" " * 23, end="")
                f.write("-------")
                f.write(" " * 23)
            else:
                print(class_[i], end="")
                print(" " * (30 - len(class_[i])), end="")
                f.write(class_[i])
                f.write(" " * (30 - len(class_[i])))
        print()
        f.write("\n")
