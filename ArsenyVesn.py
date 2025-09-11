# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Сочетание клавиш ctrl + B - открывает документацию по функции/методу/библиотеке


# Способы подключения библиотек
'''
import math  # Самый стандартный способ подключения библиотеки
print(math.sqrt(16))
print(math.factorial(5))


import math as m  # Подключение библиотеки через короткое имя
print(m.sqrt(16))
print(m.factorial(5))


from math import sqrt, factorial, ceil  # Подключаем конкретные функции
print(sqrt(16))
print(factorial(5))


from math import *  # Подключаем сразу все содержимое из функции
print(sqrt(16))
print(factorial(5))
print(ceil(7/2))
'''


# Пример конфликта имен:
'''
count = 0
from itertools import permutations  # По сути эта функция просто перемешивает содержимое последовательности
for p in permutations(['a', 'b', 'c']):
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
for p in permutations(['a', 'b', 'c']):
    count += 1
    print(count, p)
# TypeError: unsupported operand type(s) for +=: 'type' and 'int'



cnt = 0
from itertools import *
for p in permutations(['a', 'b', 'c']):
    cnt += 1
    print(cnt, p)
    # 1 ('a', 'b', 'c')
    # 2 ('a', 'c', 'b')
    # 3 ('b', 'a', 'c')
    # 4 ('b', 'c', 'a')
    # 5 ('c', 'a', 'b')
    # 6 ('c', 'b', 'a')
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


# 2⃣ Библиотека itertools для решения 1, 8, 9, 12, 17, 24 номеров кодом:
'''
from itertools import permutations, product

combinations = list(product(['a', 'b', 'c'], repeat=2))
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
    print(' '.join(perm))
    # a b c
    # a c b
    # b a c
    # b c a
    # c a b
    # c b a
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

# 5⃣ Библиотека fnmatch для решения 25 номера с масками и библиотека re для решения 25/24 номера:
'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x)


from re import *
for x in range(1917, 10**10, 1917):
    if fullmatch(r'3[0-9]12[02468]14[0-9]*5', str(x)):
        print(x)
'''


# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@]^_`{|}~
'''


# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist, prod

print(4 / 3)  # 1.3333333
print(ceil(4 / 3))  # 2 - округление вверх
print(floor(4 / 3))  # 1 - округление вниз
print(round(4 / 3))  # 1 - округление по математике

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([3, 4], [5, 6]))  # 2.82842

print(dist([3, 4], [5, 6]))  # 2.82842


M = [1, 2, 3, 4, 5]
print(prod(M))  # 120 - произведение элементов списка 

print(sum(M))  # 15
'''


# Условные операторы if, elif, else
'''
n = int(input('n: '))
if n > 0:  # if - если
    print('Положительное число')
elif n == 0:  # elif - иначе если 
    print('Равно нулю')
else:  # else - иначе 
    print('Отрицательное число')
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
'''


# Условные связки: and, or, not, in, not in, ^
'''
a, b, c = 4, -5, 6

if a > 0 and b > 0 and c > 0:
    print('and - все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие верное')

if (a > 0) ^ (b > 0):
    print(' ^ - Только одно выполняется')

if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Выполняется только два условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Выполняется хотя бы одно условие')

print(True + True + True + False)  # 3


flag = True
print(not flag)  # False
print(not(not flag))  # True

M = [2, 3, 4, 3, 2, 4, 2, 3, 4, 2, 3, 2, 3, 5, 2, 3, 5, 2]
for x in M:
    if x in (0, 2, 4, 6, 8):
        print(x, end=' ')

print()

for x in M:
    if x not in (0, 2, 4, 6, 8):
        print(x, end=' ')  # 3 3 3 3 3 5 3 5 
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
