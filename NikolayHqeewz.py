# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Условные операторы (ветвление): if, elif, else

'''
x = int(input('x: '))
if x % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''

'''
x = -6
y = 7

if x > 0 and y > 0:  # if - если
    print('Первая четверть')
elif x < 0 and y > 0:  # elif - иначе если 
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else - иначе
    print('Лежит на осях')
print('КОНЕЦ')
'''

# Каскадные условия:
'''
x = -6
y = 7

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


# Логические связки: not, and, or, ^, ==, !=, =
'''
# = - присваивание, когда нужно положить данные в переменную
# == - сравнение, когда спрашиваем "равны ли"
# != - сравнение, когда спрашиваем "не равны ли"

flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = 7, 8, -8
if a > 0 and b > 0:  # and - гарантирует, что оба (все) условия выполняются (истинны)
    print('YES 1')
if a > 0 or b > 0:  # or - хотя бы одно, то есть первое или второе или оба
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^, != - гарантирует, что только одно из условий истинно
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 4')
if (a > 0) + (b > 0) + (c > 0) == 1:  # только одно из трех должно выполняться
    print('YES 5')
if (a > 0) + (b > 0) + (c > 0) == 2:  # только два из трех должно выполняться
    print('YES 6')
'''


# Подключение и использование библиотек в Пайтон:
'''
import useful
print(useful.orel_or_reshka())
# print(useful.)

import useful as u  # переименовал библиотеку в отдельную короткую переменную
print(u.who_is_name())

from useful import orel_or_reshka, who_is_name, ALPHABET  # мы импортируем конкретные методы/константы
print(ALPHABET)

from useful import *  # импортируем из библиотеки сразу все содержимое
print(ALPHABET)
print(who_is_name())
'''
# Сочетание клавиш ctrl (cmd) + B

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

from itertools import product
from itertools import permutations

combinations = list(product([1, 2, 3], repeat=2))
for combination in combinations:
    print(combination)

perms = list(permutations("abc"))
for perm in perms:
    print(''.join(perm))


from ipaddress import *

# net = ip_network('адрес узла/маска', 0)
# print(net, net.netmask, net.num_addresses)


import sys

sys.setrecursionlimit(10000)


from functools import *


# @lru_cache(None)
# def F(n):



from fnmatch import fnmatch

if fnmatch('123', '*?3'):
    pass


import string

alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

import math as m

print(m.sqrt(16))
print(m.ceil(7 / 2))


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
