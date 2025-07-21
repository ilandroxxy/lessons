# region Домашка: ******************************************************************

# k = int(input())
# kk = int(str(k)*2)
# kkk = int(str(k)*3)
# summ = k+kk+kkk
# print(f'Сумма чисел: {summ}')
'''
k = input()  # '3'
# summ = k+kk+kkk
summ = int(k) + int(k * 2) + int(k * 3)
print(f'Сумма чисел: {summ}')
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Способов подлючения библиотек
'''
# ctrl + B - посмотреть содержимое библиотеки
print(help(len))  #   Return the number of items in a container.

# Функция help() - возвращает документацию пайтон 

n = 16

import math  # самое стандартное подключение библиотеки
print(math.sqrt(16))

import math as m  # подключение библиотеки с коротким именем
print(m.sqrt(16))

from math import sqrt, fabs, factorial  # подключаем конкретные элементы из библиотеки
print(sqrt(16))

from math import *  # подключение сразу всего содержимого библиотеки
print(sqrt(16))
print(factorial(5))


# Пример почему не стоит подключаться через *
"""
count = 0
from itertools import *

for p in permutations('1234'):
    print(p)
    count += 1
print(count)
"""
'''


# Список библиотек, который мы будем использовать на ЕГЭ

# 1.
'''
from math import ceil, floor, dist

# Будем использовать их в 19-21 номерах и 27 номере

print(4/3)  # 1.3333333333

# ceil - округление вверх
print(ceil(4/3))  # 2

# floor - округление вниз
print(floor(4/3))  # 1

# Функция дист ищет расстояние между двумя точками
print(dist([3, 4], [5, 6]))  # 2.828427
'''

# 2.
'''
import turtle as t
t.forward(100)
t.done()

# Конкретно для решения только 6 номера с черепашкой 
'''


# 3.
'''
from itertools import product, permutations

for p in permutations('abc'):
    print(p)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')

# Функции перемешивания (комбинаторики) помогают решать 8, 1 номера кодом и иногда встречаются в 12, 9, 17, 24 номерах
'''

# 4.
'''
from ipaddress import *

# Библиотека только для решения 13 номера с айпи адресами 
'''

# 5.
'''
from string import digits, ascii_uppercase
print(digits)
print(ascii_uppercase)
alp = digits + ascii_uppercase
print(alp)
'''

# 6.
'''
# № 19723 (Уровень: Базовый)

from fnmatch import *
for x in range(451, 10**9, 451):
    if fnmatch(str(x), '10?451*3'):
        print(x, x // 451)
'''
# Для решения 25 номера с масками


# 7.

# # № 19723 (Уровень: Базовый)
'''
from re import *
for x in range(451, 10**9, 451):
    if fullmatch('10[0-9]451[0-9]*3', str(x)):
        print(x, x // 451)
'''

# Для решения 24 на регулярные выражения и 25 номера с масками

# № 20288 (Уровень: Средний)
'''
from re import *
for x in range(9231, 10**10, 9231):
    if fullmatch('[02468]*12[13579]4[13579]', str(x)):
        print(x, x // 9231)
'''


# 8.
'''
# Для оптимизации 16 номера

# № 21711 ЕГКР 19.04.25 (Уровень: Базовый)

from functools import *
import sys
sys.setrecursionlimit(10**6)

@lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)

print((F(47872) - 290 * F(47865)) / F(47858))
'''


# Условные операторы: if, elif, else
'''
x = int(input('x: '))  # 5
y = int(input('y: '))  # -6

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
'''

# Логические связки
'''
a, b, c = 7, -2, -5

if a > 0 and b > 0 and c > 0:
    print('and - все условия должны выполняться')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие выполняется')


if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно из них выполняется')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два из них выполняется')
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все выполняются')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы один выполняется')


flag = True
print(not flag)  # False
print(not(not flag))  # True
'''


# Пример, где if, elif, else встречаются в 27 номере 
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


# for x, y in clustersB[2]:
#     print(x, y)

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([4, 5], [5, 6]))  # 1.4142
print(dist([4, 5], [5, 6]))  # 1.4142
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
# на следующем уроке: Циклы
