# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Библиотека - это файл .py с функциями и константами
"""
from math import sqrt
print(sqrt(16))

# Через сочетание клавиш 'ctrl + B' можно открыть содержимое библиотеки

# Аналогично работает функция help()
print(help(sqrt))
'''
sqrt(x, /)
    Return the square root of x.
'''
"""


# Способы подключения библиотек в Python
'''
import math  # самый стандартный способ подключения библиотеки
print(math.sqrt(16))


import math as m  # подключаем библиотеку через короткое имя
print(m.sqrt(16))


from math import sqrt, factorial  # подключаем только лишь конкретные функции
print(sqrt(16))


from math import *  # подключили сразу все содержимое библиотеки
print(sqrt(16))
print(factorial(5))


count = 0
from itertools import permutations
for p in permutations('abcd'):
    count += 1
    print(count, p)

count = 0
from itertools import *
for p in permutations('abcd'):
    count += 1
    print(count, p)
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

combinations = list(product([1, 2, 3], repeat=2))
for combination in combinations:
    print(combination)

perms = list(permutations("abc"))
for perm in perms:
    print(''.join(perm))
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


# 5⃣ Библиотека fnmatch и re для решения 25 номера с масками и 24 номера с регулярными выражениями:
'''
from fnmatch import *
for x in range(7993, 10**10, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x)

from re import *
for x in range(7993, 10**10, 7993):
    if fullmatch('4[0-9]*4736[0-9]*1', str(x)):
        print(x)
'''

# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?_`{|}~
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist
print(4 / 3)
print(ceil(4 / 3))  # округление вверх 
print(floor(4 / 3))  # округление вниз 
'''


# Условные операторы: if, elif, else
'''
n = int(input('n: '))
if n > 0:  # if - если
    print('Положительное число')
elif n < 0:  # elif - иначе если
    print('Отрицательное число')
else:  # else - иначе 
    print('Равно нулю')
'''

'''
# x = int(input('x: '))
# y = int(input('y: '))
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


# Логические связки: and, or, not, in
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True


M = [1, 2, 3, 4, 5]
print(5 in M)  # True
print(6 in M)  # False

s = '12345'
print('5' in s)  # True
print('6' in s)  # False


a, b, c = 4, 5, 6
if a > 0 and b > 0 and c > 0:
    print('and - все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие верное')


print(True + True + True)  # 3

if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Выполняется только два условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Выполняется хотя бы одно условие')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Выполняется не более двух условий')
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
