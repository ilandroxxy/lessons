# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309431/step/10?unit=1324547
'''
a=int(input())
b=int(input())
P=2*(a+b)
S=a*b
print(f'Периметр прямоугольника: {P}')
print(f'Площадь прямоугольника: {S}')
'''


# https://stepik.org/lesson/1309431/step/12?unit=1324547
'''
a = int(input())
b = int(input())
S = (a + b) ** 3
V = (a - b) ** 3
print('Куб суммы: ', S)
print('Куб разности: ',V)
'''

# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
k = int(input())  # 3
summa = k + k * 11 + k * 111
print(f'Сумма чисел: {summa}')
'''

# https://stepik.org/lesson/1309432/step/4?unit=1324548
'''
a = int(input())
if a % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
'''


# https://stepik.org/lesson/1309432/step/6?unit=1324548
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or (a % 40 == 0):
    summa += a
if (b % 7 == 0 and b % 49 != 0) or (b % 40 == 0):
    summa += b
if (c % 7 == 0 and c % 49 != 0) or (c % 40 == 0):
    summa += c
print(summa)
'''


'''
n = 123
print(n // 10)  # 12
print(n % 10)  # 3

print(n)  # 123

n = n // 10
print(n)  # 12


m = int(input())
if m % 2 == 0:
    print('Кратно 2 | Делится на 2 | Четное')
'''


'''
a = int(input())
if a > 80:
    print ('Почва пересыщена')
elif 60 < a <= 80:
    print ('Уровень влажности оптимален')
elif 30 < a <= 60:
    print ('Уровень влажности умеренный')
else:
    print ('Почва слишком сухая')
'''

'''
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print('Равносторонний')
elif a==b or a==c or b==c:
    print('Равнобедренный')
else:
    print('Разносторонний')
'''

# https://stepik.org/lesson/1309432/step/9?unit=1324548
'''
a=int(input())
b=int(input())
if max(a, b) % min(a, b) == 0:
    print("Делится")
else:
    print("Не делится")
    

a=int(input())
b=int(input())
if a > b:
    if a % b == 0:
        print("Делится")
    else:
        print("Не делится")
else:
    if b % a == 0:
        print("Делится")
    else:
        print("Не делится")
'''

'''
a=int(input())
if a % 4 == 0 and a % 100 != 0:
    print('Високосный')
elif a % 400 == 0:
    print('Обычный')
else:
    print('Обычный')
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "Повтори N раз", "Пробеги от А до В"

# Работа цикла for с функцией range()
'''
# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(i, end=' ')
print()

for i in range(2, 10):  # 2 3 4 5 6 7 8 9
    print(i, end=' ')
print()

for i in range(2, 10, 2):  # 2 4 6 8
    print(i, end=' ')
print()

for i in range(3, 10, 3):  # 3 6 9
    print(i, end=' ')
print()

for i in range(2, 10+1, 2):  # 2 4 6 8 10
    print(i, end=' ')
print()

for i in range(10, 0, -1):  # 10 9 8 7 6 5 4 3 2 1
    print(i, end=' ')
print()
'''

# Работа цикла for через последовательности
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']

for x in L:
    print(x, end=' ')  # a b c d e
print()

for x in L:
    if x in 'ae':
        print(x, end=' ')  # a e
print()

print(len(L))  # 5 - Кол-во элементов в списке

for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()

for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "пока условие верное - делаем действие", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # 2 4 6 8 10
    print(i, end=' ')
print()


i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()


n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n = n // b
print(r)


alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n = n // b
    return r

print(convert(1000, 2))  # 1111101000
print(convert(1000, 8))  # 1750
print(convert(1000, 3))  # 1101001
print(convert(1000, 5))  # 13000
print(convert(1000, 16))  # 3E8
print(convert(1000, 36))  # RS
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает шаг (итерацию) цикла
    if k == 100_000:
        break  # Прерывает выполнение цикла в котором лежит
    if k == 50_000:
        exit()  # Прерывала полностью выполнение программы
    print(k)

print('Продолжение программы')
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
