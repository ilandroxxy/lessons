# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Поговорить про библиотеки Python
'''
# ctrl + B - открывает документацию к фунциям

from math import sqrt
print(f'Взять квадратный корень от числа 16: {sqrt(16)}')

print(f'Взять квадратный корень от числа 16: {16 ** (1/2)}')

from Useful import divisors
'''


# Способы подключения библиотек
'''
import math  # Это самый простой способ подключения 
print(math.sqrt(16))

import math as m  # Переименовываем библиотеку через любое короткое имя 
print(m.sqrt(16))

from math import sqrt, factorial  # Подключаем конкретные функции 
print(sqrt(16))

from math import *  # Подключение сразу всего содержимого 
print(sqrt(16))
print(factorial(5))
'''

# Пример конфликта имен:
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


# Список полезных библиотек для успешной сдачи ЕГЭ по информатике!

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
from itertools import product, permutations

perms = list(product('abc', repeat=2))
for perm in perms:
    print(perm)
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
net = ip_network('узла/маска', 0)
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

# 5⃣ Библиотеки fnmatch и re для решения 25 номера с масками и 24 номера с регулярными выражениями:

# № 23764 Демоверсия 2026 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10, найдите все числа,
# соответствующие маске 3?12?14*5,
# делящиеся на 1917 без остатка.
'''
# Вариант 1
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)

# Вариант 2
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
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(alp36[:2])  # 01
print(alp36[:8])  # 01234567
print(alp36[:16])  # 0123456789ABCDEF
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import floor, ceil, dist

print(4 / 3)  # 1.333(3)
print(round(4 / 3))  # 1 - округление по математике
print(ceil(4 / 3))  # 2 - округление строго вверх
print(floor(4 / 3))  # 1 - округление строго вниз

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([4, 5], [6, 7]))  # 2.82842
print(dist([4, 5], [6, 7]))  # 2.82842
'''


# Условные операторы (ветвление): if, elif, else
'''
n = int(input('n: '))
if n > 0:  # if - если 
    print('Положительное')
elif n < 0:  # elif - иначе если 
    print('Отрицательное')
else:  # else - иначе 
    print('Равно нулю')
'''

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = 5, 6
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

print('Продолжение программы ')
'''


# Открытие и считывание файла для 17 номера
'''
clustersA = [[], []]
# clustersB = [[], [], []]


for s in open('0. files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]

    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in clustersA[1]:
    print(s)
'''


# Логические связки: and, or, not, in
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True


s = '1234234123213487436578345'

for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 4 2 4 2 2 4 8 4 6 8 4
print()

for x in s:
    if x not in '02468':
        print(x, end=' ')  # 1 3 3 1 3 1 3 7 3 5 7 3 5 
print()


a, b, c = 4, 5, 6

if a > 0 and b > 0 and c > 0:
    print('and - все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - Хотя бы одно условие верное ')

if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие верное')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия верные')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие верное ')
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
# на следующем уроке: Должен +10 минут
