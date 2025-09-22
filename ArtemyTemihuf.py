# region Домашка: ******************************************************************

# Сочетание клавиш ctrl + alt + L - приводит код в соответствие PEP8
'''
a = int(input())
b = int(input())
print(a // b)
print(a % b)
'''
from runpy import run_path

# https://stepik.org/lesson/1309430/step/8?unit=1324546
'''
print(123 // 10)  # 12
print(123 % 10)  # 3

n = int(input())  # 48395
a = n // 10000  # 4
b = (n // 1000) % 10
c = (n % 1000) // 100
d = (n % 100) // 10
e = n % 10  # 5
print(a * b * c * d * e)
print(a + b + c + d + e)
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Пример использования библиотек
'''
def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2  +(y2 - y1) ** 2) ** 0.5

print(d([4, 5], [6, 7]))  # 2.82842

from math import dist
print(dist([4, 5], [6, 7]))  # 2.82842
'''
#  Сочетание клавиш ctrl + B - выводим документацию


# Способы подключения библиотек в Пайтон
'''
import math  # Самый простой способ подключения библиотеки
print(math.sqrt(16))

import math as m  # Подключение через свое короткое имя
print(m.sqrt(16))

from math import sqrt, factorial  # Подключаем конкретные две функции
print(sqrt(16))

from math import *  # Подключение сразу всего содержимого 
print(sqrt(16))
print(factorial(5))
'''

# Пример ошибки конфликта имен
'''
count = 0
from itertools import permutations
for p in permutations('abc'):
    count += 1
    print(count, p)
    # 1 ('a', 'b', 'c')
    # 2 ('a', 'c', 'b')
    # 3 ('b', 'a', 'c')
    # 4 ('b', 'c', 'a')
    # 5 ('c', 'a', 'b')
    # 6 ('c', 'b', 'a')

count = 0
from itertools import *
for p in permutations('abc'):
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


# 2⃣ Библиотека itertools для решения 1, 8, 9, 12, 24 номеров кодом:
'''
from itertools import permutations, product

combinations = list(product('abc', repeat=2))
for combination in combinations:
    print(combination)
    # ('a', 'a')
    # ('a', 'b')
    # ('a', 'c')
    # ('b', 'a')
    # ('b', 'b')
    # ('b', 'c')
    # ('c', 'a')
    # ('c', 'b')
    # ('c', 'c')

perms = list(permutations("abc", r=3))
for perm in perms:
    print(perm)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
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

# 5⃣ Библиотеки fnmatch и re для решения 25 номера с масками (и 24 номера на регулярные выражения):
'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x)


from re import *
for x in range(1917, 10**10, 1917):
    if fullmatch('3[0-9]12[0-9]14[0-9]*5', str(x)):
        print(x)
'''


# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?]^_`{|}~

alp36 = string.digits + string.ascii_uppercase
print(alp36)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import dist, floor, ceil

print(4 / 3)  # 1.33333
print(round(4 / 3))  # 1 - округление по правилам математики 
print(ceil(4 / 3))  # 2 - округление вверх 
print(floor(4 / 3))  # 1 - округление вниз
'''


# Условные операторы: if, elif, else
'''
n = int(input('n: '))
if n > 0:  # if - если 
    print('Положительное')
elif n < 0:  # elif - иначе если 
    print('Отрицательное')
else:  # else - иначе 
    print('Равно нулю')
'''

'''
x = int(input('x: '))
y = int(input('y: '))
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
'''


# Логические связки: and, or, not, in, not in


flag = True
print(not flag)  # False
print(not(not flag))  # True

s = '1473289473298'

for x in s:
    print(x, end=' ')  # 1 4 7 3 2 8 9 4 7 3 2 9 8
print()

for x in s:
    if x in '02468':
        print(x, end=' ')  # 4 2 8 4 2 8
print()

for x in s:
    if x not in '02468':
        print(x, end=' ')  # 1 7 3 9 7 3 9
print()


a, b, c = 5, 6, 7
if a > 0 and b > 0 and c > 0:
    print('and - Все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - Хотя бы одно условие верное')

print(True + True + True)  # 3

if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие верное')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия верные')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие верное')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух условий верны')




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
