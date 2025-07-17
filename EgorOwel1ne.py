# region Домашка: ******************************************************************
from runpy import run_path

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Способы подключения библиотек
"""
# Сочетание клавиш ctrl + B - открывает документацию по функции
# Или функция help()
print(help(len))
# len(obj, /)
#     Return the number of items in a container.


# Взятие квадратного корня
print(16 ** (1/2))  # 4.0

import math  # самый стандартный способ подключения библиотеки
print(math.sqrt(16))  # 4.0

import math as m  # подключаем библиотеку с коротким именем
print(m.sqrt(16))  # 4.0

from math import sqrt, factorial  # подключаем определенные функции из библиотеки
print(sqrt(16))  # 4.0

from math import *  # подключаем сразу все функции из библиотеки
print(sqrt(4.0))

# Пример почему не стоит подключать библиотеку через *
'''
count = 0
for i in range(10):
      count += 1
print(count)

count = 0
from itertools import *
for p in permutations('123'):
      count += 1
print(count)
'''
"""

# Перечислим библиотеки, которые мы будем использовать на ЕГЭ
'''
# 1.
from itertools import product, permutations
# Используется в первую очередь для решения 8 и 1 номера через код, так же может помогать решать 2, 9, 17, 24 номера

for p in permutations('123', 2):
      print(p)

for p in product('123', repeat=2):
      print(p)

# 2.
from ipaddress import *
# Этот номер нужен для решения 13 номера и только его.

# 3.
from fnmatch import *
# Библиотека для решения 25 номера с масками и только его

# № 21718 ЕГКР 19.04.25 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10,
# найдите все числа, соответствующие маске 4*4736*1,
# которые делятся на 7993 без остатка.

from fnmatch import *
for x in range(7993, 10**10, 7993):
      if fnmatch(str(x), '4*4736*1'):
            print(x, x // 7993)

from re import *
for x in range(7993, 10**10, 7993):
      if fullmatch('4[0-9]*4736[0-9]*1', str(x)):
            print(x, x // 7993)

# 4.
from re import *
# Библиотека для решения 24 номера и 25 номера с масками


# 5.
from math import ceil, floor, dist
# ceil - округление вверх
# floor - округление вниз
# dist - поиск расстояния между двумя точками (для 27 номера)


# 6.
import turtle as t
# Для решения 6 номера с черепашкой

# 7.
from string import *
alp = digits + ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Удобная штука для переводов в различные системы счисления 14, 5 номера

# 8.
from functools import *
from sys import setrecursionlimit

# RecursionError: maximum recursion depth exceeded
setrecursionlimit(10**6)

@lru_cache(None)
def F(n):
      if n <= 3:
            return n - 1
      if n > 3 and n % 2 == 0:
            return F(n - 2) + n/2 - F(n - 4)
      if n > 3 and n % 2 != 0:
            return F(n - 1) * n + F(n - 2)

for n in range(5000):
      F(n)

print(F(4952) + 2 * F(4958) + F(4964))
'''


# Условные операторы: if, elif, else

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -5, 4

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на какой-то Оси')
'''

# Логические связки и функции all, any
'''
a, b, c = -5, 6, 7
if a > 0 and b > 0 and c > 0:
    print('and - все условия выполняются')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие выполняется')

print(True + True + True)  # 3
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Выполняется только два условия')
elif (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')

flag = True
print(not flag)  # False
print(not(not flag))  # True

M = [1, 1, 1]
if all(x % 2 == 0 for x in M):
    print('Все четные')
elif any(x % 2 == 0 for x in M):
    print('Хотя бы кто-то четный')
else:
    print('Никто не четный')
'''


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)

def F(x, y, A):
    return (x < A) and (y < 3*A) or (2*x + y > 128)

for A in range(1, 10000):
    if all(F(x, y, A) == True for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break

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


