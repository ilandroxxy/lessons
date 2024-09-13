# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Способы взаимодействия с библиотеками
'''
import math
print(f'Возьмите квадратный корень от числа 16: {math.sqrt(16)}')  # 4.0
print(f'Возьмите квадратный корень от числа 16: {16**(1/2)}')  # 4.0

import math as m  # Переименовали библиотеку math в переменную m
print(m.sqrt(16))  # 4.0

from math import sqrt, gcd, fabs  # Из библиотеки math импортируем конкретные функции
print(sqrt(16))  # 4.0

from math import *  # Подключаем сразу все функции из библиотеки
print(sqrt(16))  # 4.0
print(gcd(4, 24))  # 4
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
from itertools import product
from itertools import permutations

combinations = list(product([1, 2, 3], repeat=2))
for combination in combinations:
    print(combination)

perms = list(permutations("abc"))
for perm in perms:
    print(''.join(perm))
    
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 2)
# (2, 3)
# (3, 1)
# (3, 2)
# (3, 3)
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
'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, 6
if x > 0 and y > 0:
    print('Первую четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
print('Конец программы.')
'''

# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))
if x > 0:
    if y > 0:  # x > 0, y > 0
        print('Первую четверть')
    else:  # x > 0, y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0, y > 0
        print('Вторая четверть')
    else:  # x <= 0, y <= 0
        print('Третья четверть')
'''


# Логические связки: and, or, not, ^, !=
'''
flag = True
print(not flag)  # False, not - операция инверсии, то есть меняем значение на противоположное
print(not(not flag))  # True

a, b, c = 5, 6, -7
if a > 0 and b > 0:  # and - гарантирует, что все условия выполняются
    print('YES 1')
if a > 0 or b > 0:  # or - говорит о том, что хотя одно из условий должно выполняться
    print('YES 2')
if (a > 0) ^ (b > 0):  # () ^ () - гарантирует, что только одно условие выполняется
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 3')

# Пусть выполняют ровно два условия (ровно два из a, b, c должны быть положительны)

print((a > 0) + (b > 0) + (c > 0))  # 2
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('YES 4')
'''


# Принадлежит ли число числовому отрезку
'''
# P = [14; 56], необходимо проверить принадлежит ли x этому отрезку
x = int(input('x: '))
if 14 <= x <= 56:
    print('Принадлежит')
else:
    print('Не принадлежит')


# P = (14; 56], необходимо проверить принадлежит ли x этому отрезку
x = int(input('x: '))
if 14 < x <= 56:
    print('Принадлежит')
else:
    print('Не принадлежит')
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
