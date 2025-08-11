# region Домашка: ******************************************************************

# Реформат кода - сочетание клавиш: ctrl + alt + L


# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
k = input()
summa = int(k) + int(k * 2) + int(k * 3)
print(f'Сумма чисел: {summa}')


k = int(input())
summa = k + k * 11 + k * 111
print(f'Сумма чисел: {summa}')
'''
from runpy import run_path

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
# Сочетание клавиш: ctrl + B (открыть содержимое библиотеки)

print(help(len))
# len(obj, /)
#     Return the number of items in a container.


import math
print(math.factorial(5))  # 120
print(math.sqrt(16))  # 4.0
'''

# Способы подключения библиотек в Python
'''
import math  # Самый простой способ подключения библиотеки
print(math.sqrt(16))


import math as m  # Подключили библиотеку через короткое имя
print(m.sqrt(16))


from math import sqrt, factorial  # Подключаем конкретные функции/константы из библиотеки
print(sqrt(16))


from math import *  # Подключение сразу всего содержимого библиотеки
print(sqrt(16))
print(factorial(5))
'''


# Пример ошибки с конфликтом имен
'''
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
from itertools import product, permutations

combinations = list(product([1, 2, 3], repeat=3))
for combination in combinations:
    print(combination)
    # (1, 1, 1)
    # (1, 1, 2)
    # (1, 1, 3)
    # (1, 2, 1)
    # (1, 2, 2)
    # (1, 2, 3)
    # (1, 3, 1)
    # (1, 3, 2)
    # (1, 3, 3)
    # (2, 1, 1)
    # (2, 1, 2)
    # (2, 1, 3)
    # (2, 2, 1)
    # (2, 2, 2)
    # (2, 2, 3)
    # (2, 3, 1)
    # (2, 3, 2)
    # (2, 3, 3)
    # (3, 1, 1)
    # (3, 1, 2)
    # (3, 1, 3)
    # (3, 2, 1)
    # (3, 2, 2)
    # (3, 2, 3)
    # (3, 3, 1)
    # (3, 3, 2)
    # (3, 3, 3)

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


# 5⃣ Библиотеки fnmatch и re для решения 25 номера с масками и 24 номера на регулярные выражения:
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '1*2322?2'):
        print(x)
        
        
from re import *
for x in range(2024, 10**10, 2024):
    if fullmatch('1[0-9]*2322[0-9]2', str(x)):
        print(x)
'''


# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@_`{|}~
'''


# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist

print(4 / 3)  # 1.333
print(ceil(4 / 3))  # 2 - округление вверх
print(floor(4 / 3))  # 1 - округление вниз

print(round(4 / 3))  # 1 - округление по правилам математики (вне библиотеки)
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
x, y = 5, 0

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

M = [1, 2, 4, 5, 6, 6]
print(3 in M)  # False - лежит ли 3 в списке М
print(4 not in M)  # False
print(4 in M)  # True

a, b, c = 4, 5, 6
if a > 0 and b > 0 and c > 0:
    print('and - все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие верное')
    
    
print(True + True + True)  # 3

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все условия выполняются')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия выполняются')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
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
