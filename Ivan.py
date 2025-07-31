# region Домашка: ******************************************************************


'''
a = int(input())
b = 0
c = 1
while a > 0:
    b += a%10
    c *= a%10
    a //= 10
print(c)
print(b)
'''
from xml.sax.handler import property_xml_string

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Условные операторы: if, elif, else
'''
n = int(input())
if n > 0:  # if - если
    print('Число положительное')
elif n < 0:  # elif - иначе если 
    print('Число отрицательное')
else:  # else - иначе
    print('Число равно нулю ')
'''


# Полезный пример из 27 номера
'''
# x = int(input('x: '))
# y = int(input('y: '))
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
    print('Лежит на оси')
print('Продолжение программы')
'''

# Логические связки: and, or, not и тд
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = 5, 6, 7
if a > 0 and b > 0 and c > 0:
    print('and - все условия выполнились')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие выполняется ')
    
    
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполнилось только одно условие')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Выполнилось только два условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Выполнилось хотя бы одно условие')
'''


# Через сочетание ctrl + B - можно заглянуть в документацию функции/библиотеки/константы

# Тоже самое можно сделать через функцию help()
# print(help(len))
'''
len(obj, /)
    Return the number of items in a container.
'''


# Способы подключения библиотек
'''
import math  # Самый тривиальный способ подключения
print(f'Вычислить квадратный корень от числа 16: {math.sqrt(16)}')

import math as m  # Подключение библиотеки с коротким именем
print(f'Вычислить квадратный корень от числа 16: {m.sqrt(16)}')

from math import sqrt, factorial  # Подключили конкретные функции из библиотеки
print(f'Вычислить квадратный корень от числа 16: {sqrt(16)}')

from math import *  # Подключение сразу всего содержимого библиотеки
print(f'Вычислить квадратный корень от числа 16: {sqrt(16)}')
print(f'Вычислить факториал числа 5: {factorial(5)}')
'''

# Пример почему опасно подключать библиотеки через *
'''
count = 0
from itertools import permutations
for p in permutations('abcd'):
    count += 1
    print(count, p)
print(count)

count = 0
from itertools import *
for p in permutations('abcd'):
    count += 1
    print(count, p)
print(count)
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


# 5⃣ Библиотека fnmatch, re для решения 25 номера с масками и решения 24 номеров:
'''
from fnmatch import *
if fnmatch('123', '*?3'):
    pass


from re import *
if fullmatch('[1-9]*[02468]3', '123')
    pass
'''

# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[^_`{|}~
'''


# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist

print(4 / 3)  # 1.33333
print(ceil(4 / 3))  # 2 - округление вверх
print(floor(4 / 3))  # 1 - округление вниз


# Найти расстояние между двумя точками 
print(dist([3, 4], [5, 6]))
'''

from math import dist
clustersB = [[], [], []]

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 5:
        clustersB[0].append([x, y])
    elif y < -5:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5], [5, 6]))
# print(dist([4, 5], [5, 6]))

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

cl1 = clustersB[0]
cl2 = clustersB[0]
cl3 = clustersB[0]
center1 = center(cl1)
center2 = center(cl2)
center3 = center(cl3)
print(center1)
PxB = (center1[0] + center2[0] + center3[0]) / 3
PyB = (center1[1] + center2[1] + center3[1]) / 3
print(PxB * 10000, PyB * 10000)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Говорим про циклы

