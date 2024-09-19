# region Домашка: ******************************************************************
'''
a = int(input())
b = int(input())
c = int(input())
print(a - b)
print(a + c)
print(a % b)
'''
# PEP8 - Формат оформления кода.


# Операции с прямоугольником
'''
a = int(input())
b = int(input())
x = 2*(a+b)
print(f'Периметр прямоугольника: {x}')
print(f'Площадь прямоугольника: {(a*b)}')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Библиотеки в Python и способы их подключения
'''
M = [1, 2, 3, 4, 5]

import math
print(math.prod(M))  # 120

import math as m  # Переименовали библиотеку в m
print(m.prod(M))  # 120

from math import prod, pow, sqrt  # Подключаем определенные функции из библиотеки
print(prod(M))  # 120

from math import *  # Подключаем сразу все функции из библиотеки
print(prod(M))  # 120
print(sqrt(16))  # 4.0
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

combinations = list(product("abc", repeat=3))
for combination in combinations:
    print(''.join(combination))
    # aaa
    # aab
    # aac
    # aba
    # abb
    # abc
    # aca
    # acb
    # acc
    # baa
    # bab
    # bac
    # bba
    # bbb
    # bbc
    # bca
    # bcb
    # bcc
    # caa
    # cab
    # cac
    # cba
    # cbb
    # cbc
    # cca
    # ccb
    # ccc

perms = list(permutations("abc", r=3))
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

# 5⃣ Библиотека fnmatch для решения 25 номера с масками:
'''
from fnmatch import *
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

# if - если
# elif - иначе если
# else - иначе

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -7, 6
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print('Лежит на оси')
print('Конец программы')
'''


# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0, y > 0
        print(1)
    else:  # x > 0, y <= 0
        print(4)
else:
    if y > 0:  # x <= 0, y > 0
        print(2)
    else:  # x <= 0, y <= 0
        print(3)
'''

# Логические связки: and, or, not, ^, !=, ==, in
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

s = '128674351278'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 8 6 4 2 8
print()

M = [1, 2, 8, 6, 7, 4,  3, 5, 1, 2, 7, 8]
for x in M:
    if x % 2 == 0:  # = - присваивание, == - сравнение
        print(x, end=' ')  # 2 8 6 4 2 8
print()


a, b, c = 5, -6, 7
if a > 0 and b > 0:  # and - гарантирует, что все условия выполняются
    print(1)
if a > 0 or b > 0:  # or - говорит о том, что хотя бы одно выполняется (могут и два)
    print(2)
if (a > 0) ^ (b > 0):  # ^, != - гарантирует, что только одно условие выполняется
    print(3)
if (a > 0) != (b > 0):
    print(3)


print(True + True + False)  # 2

# Только два условия выполняются
if (a > 0) + (b > 0) + (c > 0) == 2:
    print(4)
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
