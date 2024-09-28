# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import math
print(f'Возведем число 7 в степень 2: {7 ** 2}')  # 49
print(f'Взять квадратный корень от числа 16: {math.sqrt(16)}')  # 4.0
print(f'Взять квадратный корень от числа 16: {16**(1/2)}')  # 4.0
print(f'Взять кубический корень от числа 27: {27**(1/3)}')  # 3.0
'''

# ctrl + B - открыть содержимое библиотеки (или документацию к функции)

# Способы взаимодействия с библиотеками:
'''
M = [1, 2, 3, 4, 5]

import math  # Самый базовый способ импортирования библиотеки
print(math.sqrt(16))

import math as m  # Подключаем библиотеку с коротким именем m
print(m.sqrt(16))

from math import sqrt, prod  # Подключаем конкретные функции/константы
print(sqrt(16))

from math import *  # Подключение всего содержимого из библиотеки 
print(sqrt(16))
print(prod(M))
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


# Условные операторы (ветвление):  if, elif, else

# if - если
# elif - иначе если
# else - иначе
'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -6, 5

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

print('Продолжение программы')
'''


# Каскадные условные операторы:
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0, y > 0
        print('Первая')
    else:  # x > 0, y <= 0
        print('Четвертая')
else:
    if y > 0:  # x <= 0, y > 0
        print('Вторая')
    else:  # x <= 0, y <= 0
        print('Третья')
'''


# Логические связки: and, or, not, in, ^, ==, !=
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

n = 4
if n % 2 == 0:
    print('Четное')
elif n % 2 != 0:
    print('Нечетное')


M = [1, 2, 3, 2, 3, 5, 6, 7, 8, 9]
for x in M:
    if x % 2 == 0:
        print(x, end=' ')  # 2 2 6 8
print()


s = '1232356789'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 2 6 8
print()



a, b, c = 4, -5, 6
if a > 0 and b > 0:
    print('and')  # Гарантирует, что все условия выполняются
if a > 0 or b > 0:
    print('or')  # Говорит о том, что хотя бы одно выполняется
if (a > 0) ^ (b > 0):
    print('^')  # Гарантирует, что только одно выполняется
if (a > 0) ^ (b > 0):
    print('!=')  # Гарантирует, что только одно выполняется


print(True + False + True)  # 2

if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Гарантирует, что только два выполняется ')

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
