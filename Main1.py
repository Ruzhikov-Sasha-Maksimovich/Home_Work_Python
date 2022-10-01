day_of_week = int(input("Введите номер дня недели: "))
if day_of_week > 7:
    print("Такого дня нет!!!")
elif day_of_week > 0 and day_of_week < 6:
    print("Рабочий день")
elif day_of_week > 5 and day_of_week < 8:
    print("Выходной день")