# region Домашка: ******************************************************************

# Сочетание клавиш ctrl + alt + L приводит код в соответствие с PEP8
'''
a = int(input())
b = a // 10000
c = a // 1000 % 10
d = a // 100 % 10
e = a // 10 % 10
f = a % 10
g = b * c * d * e * f
h = b + c + d + e + f
print(g)
print(h)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Сочетние клавиш ctrl + B - показывает содержимое библиотеки или документацию функции

# Четыре способа взаимодействия с библиотекой
'''
import math
print(math.sqrt(16))

import math as m  # Подключение библиотеки с коротким именем m
print(m.sqrt(16))

from math import sqrt, pow, prod  # Подключаю конкретные функции из библиотеки
print(sqrt(16))

from math import *  # Подключаем сразу все содержимое библиотеки
print(sqrt(16))
print(prod([1, 2, 3, 4, 5]))  # Произведение элементов списка 
'''

# 📌 Список полезных библиотек для успешной сдачи ЕГЭ по информатике!

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

print('Продолжение программы')
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


# Логические связки и функции: and, or, not, in, ==, !=
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

for x in '128943721':
    if x in '02468':  # in - лежит ли
        print(x, end=' ')  # 2 8 4 2
print()

for x in '128943721':
    if x not in '02468':  # не лежит в четных
        print(x, end=' ')  # 1 9 3 7 1
print()

M = [1, 2, 8, 9, 4, 3, 7, 2, 1]
for x in M:
    if x % 2 == 0:  # == - сравнение равны ли элементы
        print(x, end=' ')  # 2 8 4 2
print()

for x in M:
    if x % 2 != 0:  # == - сравнение не равны ли элементы
        print(x, end=' ')  # 1 9 3 7 1 
print()
'''

'''
a, b = 4, -5
if a > 0 and b > 0:
    print('and')  # and - Гарантирует, что все условия выполняются
if a > 0 or b > 0:
    print('or')  # or - Говорит о том, что хотя бы одно условие выполняется
if (a > 0) ^ (b > 0):
    print('^')  # ^, != - Гарантируют, что только одно условие выполняется
if (a > 0) != (b > 0):
    print('!=')
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
