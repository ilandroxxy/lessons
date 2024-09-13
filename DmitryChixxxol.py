# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
#

# import math
# print(f'Возьмем квадратный корень от числа 16: {math.sqrt(16)}')  # 4.0
# print(f'Возьмем квадратный корень от числа 16: {16 ** 0.5}')  # 4.0


# Способы подключения библиотек
'''
import math
print(math.sqrt(16))

import math as m  # Переименовали библиотеку math в m
print(m.sqrt(16))

from math import sqrt, fabs, pow  # Подключаем только выбранные функции
print(sqrt(16))

from math import *  # Подключаем сразу все функции
print(sqrt(16))
print(gcd(4, 24))
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
from itertools import product, permutations

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
sys.setrecursionlimit(1000)


# Вторая ускоряет вычисления через использование кэширования:
from functools import *
@lru_cache(None)
def F(n):
'''


# Тип 16 №59760
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + F(n - 1)

print(F(2021) - F(2019))

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
'''
# Ответ: 4041


# 5⃣ Библиотека fnmatch для решения 25 номера с масками:
'''
from fnmatch import fnmatch
if fnmatch('123', '*?3'):
    pass
'''


# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''


# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
import math as m
print(m.sqrt(16))
print(m.ceil(7/2))
'''


# Условные операторы (ветвление): if, elif, else

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -5, 6
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
print('Конец программы')
'''


# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0, y > 0
        print('Первая четверть')
    else:  # x > 0, y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0, y > 0
        print('Вторая четверть')
    else:  # x <= 0, y <= 0
        print('Третья четверть')
'''


# Логические связки: and, or, not, ^, in, !=, ==, =
'''
x = 5  # присваивание
print(x == 5)  # сравнение "равны ли они?"
print(x != 5)  # сравнение "не равны ли они?"

flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = 5, -6, 7

if a > 0 and b > 0:  # and - гарантирует, что выполняются все условия
    print('YES 1')
if a > 0 or b > 0:  # or - говорит о том, что хотя бы одно условие выполняется
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^, != - гарантируют, что только одно из условий выполняется
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 3')
'''

# Есть три значения, проверьте, что только два из них положительные

'''
a, b, c = 5, 6, 7

print(True + False + True)  # 2
print((a > 0) + (b > 0) + (c > 0))  # 2

if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Да, только две из переменных положительные.')
else:
    print(f'Положительных элементов: {(a > 0) + (b > 0) + (c > 0)}')
'''


# Как проверить, что число принадлежит списку/последовательности или отрезку
'''
x = int(input('x: '))

M = [1, 2, 3, 4, 5]
if x in M:
    print(f'Переменная {x} лежит в списке M: {M}')

s = '12345'
if str(x) in s:
    print(f'Переменная {x} лежит в строке s: {s}')

# P = [15, 30]
if 15 <= x <= 30:
    print(f'Переменная {x} лежит на отрезке P: [15, 30]')

# Q = (30, 40]
if 30 < x <= 40:
    print(f'Переменная {x} лежит на отрезке Q: (30, 40]')
'''


'''
pas1 = input()
pas2 = input()
if pas1 == pas2:
    print("Пароль принят")
else:
    print("Пароль не принят")
'''

'''
s = input()
if len(s) >= 10 or len(s) % 2 == 0:
    print("ДА")
else:
    print('НЕТ')
'''
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
