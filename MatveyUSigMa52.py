# region Домашка: ******************************************************************

'''
a = int(input())
summa = 0
proiz = 1
p1 = a // 10000
p2 = (a // 1000) % 10
p3 = (a // 100) % 10
p4 = (a // 10) % 10
p5 = a % 10
summa = p1 + p2 + p3 + p4 + p5
proiz = p1 * p2 * p3 * p4 * p5
print(proiz)
print(summa)
'''

'''
import math

a = int(input())
p1 = a // 10000
p2 = (a // 1000) % 10
p3 = (a // 100) % 10
p4 = (a // 10) % 10
p5 = a % 10
# Из библиотеки math импортировали функцию prod,
# которая ищет произведение элементов последовательности
print(math.prod([p1, p2, p3, p4, p5]))
print(sum([p1, p2, p3, p4, p5]))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Способы подключения библиотек Python
'''
M = [1, 2, 3, 4, 5]

import math
print(math.prod(M))  # 120

import math as m  # Подключили библиотеку с коротким названием m
print(m.prod(M))  # 120

from math import prod, sqrt, pow  # Подключаем конкретные функции из библиотеки
print(prod(M))  # 120

from math import *  # Подключаем сразу все функции
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

combinations = list(product('abc', repeat=3))
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

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -6, 7

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
print('Конец')
'''


# Логические связки: and, or, not, ^, !=, ==, =
'''
flag = True
print(not flag)  # False: not - инверсия (отрицание)
print(not(not flag))  # True

a, b, c = 5, -6, -7
if a > 0 and b > 0:  # and - гарантирует, что все условия выполняются
    print('YES 1')
if a > 0 or b > 0:  # or - говорит о том, что хотя бы одно выполняется
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^, != - гарантируют, что только одно выполняется
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 3')
    
print(True + True + False)  # 2
# Только два условия выполняются 
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('YES 4')
# Хотя бы два выполняются
if (a > 0) + (b > 0) + (c > 0) >= 2:
    print('YES 5')
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
