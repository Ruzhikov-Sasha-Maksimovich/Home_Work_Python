#Типы переменных

a3 = int(input())
print(type(a3))

b3 = float(input())
print(type(b3))

s = str(input())
print(type(s))
#Арифметические действия с переменными
a = 3
b = 4

c = a + b
print(c)

c = a * b
print(c)

c = a % b
print(c)

c = a - b
print(c)

c = a / b
print(c)

c = a ** b
print(c)
#Операторы вывода и ввода
int(input())
float(input())
str(input())

print()
print("{1} - {2} - {0}".format(a, b, s))
print("qwe \n rty")


#Списки и их использование


text = "Съешь ещё этих мягких французких булок"

print(text[0])  #с
print(text[1])  #ъ
print(text[len(text)-1])    # к
print(text[-5])     # б
print(text[:])      # print(text)
print(text[:])      # съ
print(text[len(text)-2:])   # ок
print(text[2:9])    # ешь ещё
print(text[6: -18])    # ещё этих мягких
print(text[0:len(text):6])  #сеикакл
print(text[0::6])  #сеикакл
text = text[2:9]+ text[-5] #...

print(len(text))    #39
print('ещё' in text)    #True
print(text.isdigit())   #False
print(text.islower())   #True
print(text.replace("ещё", 'ЕЩЁ'))

number = [1,2,3,4,5]
print(number)
ran = range(1, 6)
number = list(ran)
print(type(number))

print(number)
number[0] = 10
print(f'{len(number)} len')
print(number)
for i in number:
    i *= 2
    print(i)


color = list["one"]
print(color)
color.append('gray')
print(color)
color.remove('gray')
print(color)
#Логические операции

a = 1 < 4 and 5 < 6
print(a)

a = 1 > 4 and 5 > 6
print(a)

a = [1, 2]
b = [1, 2]

print(a == b)

func = 1
T = 4
x = 123

print(func<T>(x))

f = 1 > 2 or 4 < 6

print(f)

f = [1,2,3,4]
print(2 in f)

f = [1,2,3,4]
print(not 4 in f)

is_add = f[0] % 2 == 0
print(is_add)

is_add = not f[0] % 2
print(is_add)


#оператор If
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)


a = int(input(('a = ')))
b = int(input(('b = ')))
if a > b:
    print(a)
else:
    print(b)


username = input('Введите имя: ')
if username == 'Маша':
    print("Привет, Маша")
elif username == 'Саша':
    print("Привет, Санёк")
elif username == 'Лиза':
    print("Привет, Лиза")
else:
    print("Привет, " + username)

#оператор While
original = 23
inverted = 0
while original !=0:
    inverted = inverted  * 10 + (original % 10)
    original //= 10
else:
    print("Пожалуй Хватит")
print(inverted)


#оператор For
for i in 1,2,3,4,5:
    print(i ** 2)


list = [1, 2, 3, 4, 5, 6, 10]
for i in list:
    print(list)


for i in range(1, 10, 2):
    print(i)


for i in range(15):
    print(i)


list = range(10)
for i in list:
    print(i)


for i in 'qwe - rty':
    print(i)


#Функции и их использование
def f(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))


#Команды
help(text.istitle())