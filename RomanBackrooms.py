# region Домашка: ******************************************************************

# Кубические вычисления: объем и площадь
'''
a = int(input())
print(a ** 3)
print(a ** 2 * 6)
'''


# Произведение и сумма цифр пятизначного числа
'''
a = int(input())
a1 = a // 10000
a2 = (a // 1000) % 10
a3 = (a // 100) % 10
a4 = (a // 10) % 10
a5 = a % 10
print(a1 * a2 * a3 * a4 * a5)
print(a1 + a2 + a3 + a4 + a5)
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Подключение и использование библиотек в Python
'''
M = [1, 2, 3, 4, 5]
import math
print(math.prod(M))  # 120

import math as m  # Подключили библиотеку с коротким именем m
print(m.prod(M))  # 120

# ctrl + B - показать описание библиотеки или функции 

from math import prod, sqrt, pow  # Подключили выборочные функции из math
print(prod(M))  # 120

from math import *  # Подключаем сразу все содержимое
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
from itertools import permutations, product

combinations = list(product("abc", repeat=2))
for combination in combinations:
    print(''.join(combination))
    # aa
    # ab
    # ac
    # ba
    # bb
    # bc
    # ca
    # cb
    # cc

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
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print('Попали на ось')

print('Продолжение')
'''

# Логические связки: and, or, not, ^, !=
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = 5, -6, 7
if a > 0 and b > 0:  # and - гарантирует, что все условия выполняются
    print(1)
if a > 0 or b > 0:  # or - говорят о том, что хотя бы одно условие выполняется
    print(2)
if (a > 0) ^ (b > 0):  # ^. != - гарантирует, что только одно условие выполняется 
    print(3)
if (a > 0) != (b > 0):
    print(3)


print(True + True + False)  # 

# 
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
