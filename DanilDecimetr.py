# region Домашка: ******************************************************************


# https://stepik.org/lesson/1309431/step/11?unit=1324547
'''
n = int(input())
b = [int(i) for i in str(n)]
b1 = sum(b)
j = 1
for i1 in b:
    j = i1*j
print(f"Произведение цифр: {j}")
print(f"Сумма цифр: {b1}")


from math import prod
n = int(input())
b = [int(i) for i in str(n)]
b1 = sum(b)
j = prod(b)  # Функция, которая возвращает произведение элементов списка
print(f"Произведение цифр: {j}")
print(f"Сумма цифр: {b1}")


num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
e = num % 10
pro = a * b * c * e
summa = a + b + c + e
print(f'Произведение цифр: {pro}')
print(f'Сумма цифр: {summa}')
'''


# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
n = int(input())
b = n + int((str(n)) + (str(n))) + int((str(n) + str(n) + str(n)))
print(f"Сумма чисел: {b}")


n = int(input())
n = str(n)
print(f"Сумма чисел: {int(n) + int(n * 2) + int(n * 3)}")
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# По сути библиотека - это просто .py файл
'''
import math
print(math.sqrt(16))

# Сочетание клавиш ctrl + B показывает содержимое библиотеки

print(help(math.sqrt)) # возвращает документацию к функции
# sqrt(x, /)
#     Return the square root of x.
'''

# Способы подключения библиотек в Python
'''
import math  # Это самое классическое подключение библиотеки
print(math.sqrt(16))

import math as m  # Подключили библиотеку с коротким именем m
print(m.sqrt(16))

from math import sqrt, factorial  # Подключили конкретные функции из библиотеки
print(sqrt(16))

from math import *  # Подключение сразу всего содержимого библиотеки
print(sqrt(16))
print(factorial(5))
'''

# При подключении библиотеки через * может возникнуть конфликт имен
# Пример конфликта имен
'''
count = 0
from itertools import permutations
for p in permutations('abcd'):
    count += 1
    print(count, p)
print(count)

count = 0
from itertools import *
for p in permutations('abcd'):
    count += 1
    print(count, p)
print(count)
'''


# 📌 Список полезных библиотек для успешной сдачи ЕГЭ по информатике! #tpy #useful


# 1⃣ Библиотека черепашки для решения 6 номера кодом:
'''
import turtle as t

t.tracer(0)

t.fd(10)  # t.bk(10)
t.rt(90)  # t.lt(90)

t.up()
t.down()

x, y = 0, 0
t.goto(x, y)
t.dot(2, 'red')

t.done()
'''


# 2⃣ Библиотека itertools для решения 1, 8, 9, 12, 24 номеров кодом:
'''
from itertools import permutations, product

combinations = list(product([1, 2, 3], repeat=2))
for combination in combinations:
    print(combination)
    # (1, 1)
    # (1, 2)
    # (1, 3)
    # (2, 1)
    # (2, 2)
    # (2, 3)
    # (3, 1)
    # (3, 2)
    # (3, 3)

perms = list(permutations("abc"))
for perm in perms:
    print(''.join(perm))
    # abc
    # acb
    # bac
    # bca
    # cab
    # cba
'''


# 3⃣ Библиотека ipaddress для решения нового 13 номера:
'''
from ipaddress import *
net = ip_network('адрес узла/маска', 0)
print(net, net.netmask, net.num_addresses)
'''

# 4⃣ Две библиотеки для решения 16 номера:
'''
# Одна увеличивает глубину рекурсии:
import sys
sys.setrecursionlimit(10000)


# Вторая ускоряет вычисления через использование кэширования:
from functools import *
@lru_cache(None)
def F(n):
'''

# 5⃣ Библиотека fnmatch и библиотека re для решения 25 номера с масками и вторая для решения 24 номера:
'''
from fnmatch import *
for x in range(169, 10**9, 169):
    if fnmatch(str(x), '123*567?'):
        print(x, x // 169)

from re import *
for x in range(169, 10**9, 169):
    if fullmatch('123[0-9]*567[0-9]', str(x)):
        print(x, x // 169)
'''

# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[^_`{|}~
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
# Функции для 19-21 номера 
from math import ceil, floor

print(4 / 3)  # 1.333333
print(ceil(4 / 3))  # 2 - округление вверх
print(floor(4 / 3))  # 1 - округление вниз

# Функция для 27 номера
from math import dist
# Возвращает расстояние между двумя точками
print(dist([4, 5], [6, 7]))  # 2.8284271
'''


# Условные операторы: if, elif, else
'''
# x = int(input('x: '))
# y = int(input('y: '))

x, y = -5, 6
if x > 0 and y > 0:  # if - если
    print('Первая четверть')
elif x < 0 and y > 0:  # elif - иначе если 
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else - иначе
    print('Лежит на осях')
print('Продолжение программы')
'''


# Логические связки: and, or, not и ^
'''
flag = True
print(not flag)  # False
print(not (not flag))  # True


a, b, c = -4, 5, -6
if a > 0 and b > 0 and c > 0:
    print('and - все условия выполняются ')
if a > 0 or b > 0 or c > 0:
    print('or - выполняется хотя бы одно условие')
if (a > 0) ^ (b > 0):
    print('^ - Только одно из условий выполняется, но только для пары')


if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия выполняются')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух выполняется')
'''


# Поговорим про 27 номер
'''
from math import dist
clustersB = [[], [], []]

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 5:
        clustersB[0].append([x, y])
    elif y < -5:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5], [5, 6]))
# print(dist([4, 5], [5, 6]))
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