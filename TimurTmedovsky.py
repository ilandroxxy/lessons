# region Домашка: ******************************************************************

# Проверка соотношения для пятизначного числа
'''
n = int(input())
a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10
print(a, b, c, d, e)

if a * c == b + d + e:
    print("Да")
else:
    print("Нет")
'''


# Вычисление суммы чисел по определенным условиям
# которые кратны 7, но не кратны 49 или являются кратными 40.
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    summa += a
if (b % 7 == 0 and b % 49 != 0) or b % 40 == 0:
    summa += b
if (c % 7 == 0 and c % 49 != 0) or c % 40 == 0:
    summa += c
print(summa)
'''


# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы - это некоторое повторяющееся действие

# Цикл for отвечающий на запросы: "повтори n раз", "пробеги от А до В"

# Цикл for с функцией range():
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(10+1):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9 10
print()

for i in range(2, 10+1):  # range(START=2, STOP=11-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9 10
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-11)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# i  0  1  2  3  4  5  6  7  8  9
M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(M))  # Возвращает длину списка М (кол-во его элементов)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
    print(M[i], end=' ')  # 1 2 3 4 5 6 7 8 9 10
print()

for i in range(len(M)):
    M[i] = M[i] ** 2
print(M)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

# Цикл for с последовательностями:
'''
M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in M:
    print(x, end=' ')  # 1 2 3 4 5 6 7 8 9 10
print()

A = []
for x in M:
    A.append(x ** 2)
print(A)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

A = []
for x in M:
    if x % 2 == 0:
        A.append(x ** 2)
print(A)  # [4, 16, 36, 64, 100]
'''

# Цикл while отвечающий на запросы: "Пока условие верно - выполняй действие", "Бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    if i % 2 == 0:
        print(i, end=' ')  # 2 4 6 8 10
    i += 1
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

# Напишем свою функцию перевода в различные системы счисления
'''
n = 8
b = 2
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()
print(M)  # [1, 0, 0, 0]

print(int('1000', 2))  # 8 -> Перевод из 2-ой в 10-ную

n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)  # '1000'

print(int(r, 2))  # 8 -> Перевод из 2-ой в 10-ную


from string import *
alphabet = digits + ascii_uppercase
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r

r = convert(8, 2)  # Перевод из 10-ой в 2-ую
print(r)  # '1000'

print(int(r, 2))  # 8 -> Перевод из 2-ой в 10-ную
'''


# Бесконечные циклы и операторы break, continue, exit():
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию цикла
    if k == 3_000_000:
        break  # прерывает выполнение цикла в котором он лежит
    if k == 2_000_000:
        exit()  # прерывает выполнение нашей программы
    print(k)

print('Продолжение программы')
'''


from string import *


alphabet = digits + ascii_uppercase


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


while True:
    case = int(input('\n'
                     'case 1: Перевод из 10-й в n-ую систему \n'
                     'case 2: Перевод из n-й в 10-ую систему \n'
                     'case 3: Перевод из n-й в k-ую систему \n'
                     'case 0: exit '
                     '\n'))

    if case == 1:
        n = int(input('n: '))
        b = int(input('b: '))
        r = convert(n, b)
        print(f'Результат перевода: {r}')

    elif case == 2:
        pass

    elif case == 3:
        pass

    elif case == 0:
        print('Спасибо, что пользовались нашей программой!')
        exit()


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
