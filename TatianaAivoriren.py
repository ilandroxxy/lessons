# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# ctrl + B - открыть содержимое библиотеки или документацию к фуункции
# print(help(len))  # - вывести документацию к функции

# len(obj, /)
#     Return the number of items in a container.

# Какие есть способы подключения библиотек в Пайтон
'''
import math  # самый обычный способ подключения библиотеки
print(math.sqrt(16))

import math as m  # подключение с новым именем (поменяли имя на m)
print(m.sqrt(16))

from math import sqrt, factorial  # подключаем сразу несколько конкретных функций
print(sqrt(16))

from math import *  # подключаем сразу все функции
print(sqrt(16))

count = 0
from itertools import permutations
for p in permutations('1234'):
    count += 1
    print(count, p)


count = 0
from itertools import *
for p in permutations('1234'):
    count += 1
    print(count, p)
'''


# Список библиотек, которые пригодятся на ЕГЭ
'''
from itertools import product, permutations
# 1. Камбиноторика для 8 номера, а так же для решения 1 номера
# и может пригодиться в номерах: 9, 12, 17, 24


import turtle as t
# 2. Для решения 6 номера


from ipaddress import *
# 3. Для решения 13 номера с айпи адресами


from fnmatch import *
# 4. Для решения 25 номера с масками


from re import fullmatch
# 5. Для решения 25 номера и для решения 24


from functools import *
from sys import setrecursionlimit
setrecursionlimit(100000)
# 6. Для оптимизации 16 номера 

@lru_cache(None)
def F(n):
    return G(n - 1) + G(n - 3)

def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 4) + 2

print(F(42999))


from math import ceil, floor, dist
# 7. Библиотека математики и функции из математики 
# ceil - округление вверх
# floor - округление вниз
# dist - поиск расстояния между двумя точками 
'''


# Условные операторы if, elif, else
'''
x = int(input('x: '))
y = int(input('y: '))

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


# Логические связки and, or, not

flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = -4, -5, -6
if a > 0 and b > 0 and c > 0:
    print('and - все условия верные ')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно из условий выполняется')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия выполняются')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')


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
