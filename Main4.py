#Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in ["1", "0"]:
    for y in ["1", "0"]:
        for z in ["1", "0"]:
            print(x or y or z == x and not y and not z)
            print(x, y, z)
            print("")
print("")
print("0 это False, 1 это True")