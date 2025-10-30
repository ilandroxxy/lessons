# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Сочетание клавиш: ctrl + B - открывает содержимое библиотеки


# Способы подключения библиотек
'''
import math  # Самый базовый способ подключения библиотеки через имя
print(math.sqrt(16))

import math as m  # Подключение библиотеки через короткое имя
print(m.sqrt(16))

from math import sqrt, factorial, pi  # Подключаем конкретные функции и константы
print(sqrt(16))

from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(factorial(5))
'''
from resource import struct_rusage

# Пример конфликта имен
'''
count = 0
from itertools import permutations, product
for p in permutations('ABC'):
    count += 1
    print(count, p)
    # 1 ('A', 'B', 'C')
    # 2 ('A', 'C', 'B')
    # 3 ('B', 'A', 'C')
    # 4 ('B', 'C', 'A')
    # 5 ('C', 'A', 'B')
    # 6 ('C', 'B', 'A')

count = 0
from itertools import *
for p in permutations('ABC'):
    count += 1
    print(count, p)
    # TypeError: unsupported operand type(s) for +=: 'type' and 'int'
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


# 2⃣ Библиотека itertools для решения 1, 8, 9, 17, 24 номеров кодом:
'''
from itertools import permutations, product

combinations = list(product('ABC', repeat=2))
for combination in combinations:
    print(combination)
    # ('A', 'A')
    # ('A', 'B')
    # ('A', 'C')
    # ('B', 'A')
    # ('B', 'B')
    # ('B', 'C')
    # ('C', 'A')
    # ('C', 'B')
    # ('C', 'C')

perms = list(permutations('ABC'))
for perm in perms:
    print(perm)
    # ('A', 'B', 'C')
    # ('A', 'C', 'B')
    # ('B', 'A', 'C')
    # ('B', 'C', 'A')
    # ('C', 'A', 'B')
    # ('C', 'B', 'A')
'''


# 3⃣ Библиотека ipaddress для решения нового 13 номера:
'''
from ipaddress import *
net = ip_network('адрес узла/маска', 0)
print(net, net.netmask, net.num_addresses)
'''

# 4⃣ Две библиотеки для решения 16 номера:
# Одна увеличивает глубину рекурсии:
'''
import sys
sys.setrecursionlimit(10000)
'''

# Вторая ускоряет вычисления через использование кэширования:
'''
from functools import *
@lru_cache(None)
def F(n):
'''


# 5⃣ Библиотеки fnmatch и re для решения 25 номера с масками и регулярных выражений в 24 номере:
'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)

from re import *
for x in range(1917, 10**10, 1917):
    if fullmatch('3[0-9]12[0-9]14[0-9]*5', str(x)):
        print(x, x // 1917)
'''


# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@]^_`{|}~

alp36 = string.digits + string.ascii_uppercase
print(alp36)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(alp36[:2])  # 01
print(alp36[:8])  # 01234567
print(alp36[:16])  # 0123456789ABCDEF
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist

print(4 / 3)  # 1.33333 - Вещественное деление (дроби)
print(int(4 / 3))  # 1 - Взять только целую часть
print(int(4 // 3))  # 1 - Взять только целую часть
print(round(4 / 3))  # 1 - Базовое математическое округление

print(ceil(4 / 3))  # 2 - Округление строго вверх
print(floor(4 / 3))  # 1 - Округление строго вниз

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([3, 4], [6, 7]))  # 4.24264
print(dist([3, 4], [6, 7]))  # 4.24264
'''

# Условные операторы if, elif, else (ветвление)
'''
n = int(input('n: '))
if n > 0:  # if - если
    print('Положительное')
elif n < 0:  # elif - иначе если
    print('Отрицательное')
else:  # else - иначе
    print('Равно нулю')
'''

# Логические связки: and, or, not, in, not in

flag = True
print(not flag)  # False
print(not(not flag))  # True

s = '3612536752136125'

for x in s:
    if x in '02468':
        print(x, end=' ')
print()

for x in s:
    if x not in '02468':
        print(x, end=' ')
print()


a, b, c = 4, 5, 6

if a > 0 and b > 0 and c > 0:
    print('and - Все условия выполняются')
if a > 0 or b > 0 or c > 0:
    print('or - Хотя бы одно условие выполняется')


if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все условия выполняются')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполняется')

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
