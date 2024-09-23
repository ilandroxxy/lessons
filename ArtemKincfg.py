# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# from math import sqrt
# print(f'Возьмите квадратный корень от числа 16: {sqrt(16)}')
# print(f'Возьмите квадратный корень от числа 16: {16 ** (1/2)}')
# print(f'Возьмите кубический корень от числа 27: {27 ** (1/3)}')

# ctrl + B - посмотреть содержимое библиотеки или документацию к функции

# Работа с библиотеками Python и способы их подключения
'''
M = [1, 2, 3, 4, 5]

import math
print(math.sqrt(16))

import math as m   # Переименовали функцию math в короткое имя
print(m.sqrt(16))

from math import sqrt, prod, pow  # Подключаем конкретные функции из библиотеки
print(sqrt(16))

from math import *  # Подключаем сразу все содержимое библиотеки
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


# Условные операторы (ветвление): if, elif, else

# if - если
# elif - иначе если
# else - иначе


'''
n = int(input('n: '))
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''

'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, 6

if x > 0 and y > 0:
    print('Первая')
elif x < 0 and y > 0:
    print('Вторая')
elif x < 0 and y < 0:
    print('Третья')
elif x > 0 and y < 0:
    print('Четвертая')
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

# Логические связки: anf, or, not, in, ^, !=, ==
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

M = [2, 3, 4, 3, 4, 5, 6, 7, 8]
for x in M:
    if x % 2 == 0:
        print(x, end=' ')  # 2 4 4 6 8
print()

s = '234345678'
for x in s:
    if int(x) % 2 == 0:  # 2 4 4 6 8
        print(x, end=' ')
print()

s = '234345678'
for x in s:
    if x in '02468':  # 2 4 4 6 8
        print(x, end=' ')
print()


a, b, c = 3, -4, 5
if a > 0 and b > 0:
    print('and')  # and - гарантирует, что все условия выполняются
if a > 0 or b > 0:
    print('or')  # or - хотя бы одно из условий выполняется
if (a > 0) ^ (b > 0):
    print('^')  # () ^ () - гарантирует, что только одно условие выполняется
if (a > 0) != (b > 0):
    print('!=')  # () != () - гарантирует, что только одно условие выполняется

print(True + False + True)  # 2

if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Гарантирует, что только два условия выполняются ')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Говорим, что не более двух условий выполняется ')
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
