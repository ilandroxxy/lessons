# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


"""
'''  # - многострочный комментарий
# - однострочный комментарий
# ctrl + / - быстрый однострочный комментарий
'''
"""


# Работа с f-строками
'''
name = input('Введите имя: ')
wether = 'облачно'
temperature = int(input('Введите температуру: '))

# Привет, name! Сегодня облачно, а температура 24 градуса.

print('Привет, ', name,'! Сегодня ', wether ,', а температура ', temperature,' градуса.')
print('Привет, ' + name + '! Сегодня ' + wether +', а температура ' + str(temperature) + ' градуса.')
print('Привет, {}! Сегодня {}, а температура {} градуса.'.format(name, wether, temperature))  # - однострочный комментарий 
print(f'Привет, {name}! Сегодня {wether}, а температура {temperature} градуса.')
'''


'''
from math import sqrt
print(f'Возьмем квадратный корень от числа 16: {sqrt(16)}')
print(f'Возьмем квадратный корень от числа 16: {16 ** 0.5}')
print(f'Возьмем кубический корень от числа 27: {27 ** 1/3}')

# ctrl + B - открыть содержимое библиотеки
print(help(sqrt))
# sqrt(x, /)
#     Return the square root of x.
'''

# Очень полезные библиотеки Python для ЕГЭ по информатике #tpy

# 🐢  turtle -- для графики (№6)
'''
from turtle import *
tracer(0)
fd(100)
rt(90)
goto(50, 30)
dot(5, 'red')
done()
'''

# 🔄 itertools -- для комбинаторики (№1, 8, 9, 12, 24)
# Для этого модуля лучше импортировать только нужные функции, чтобы код оставался понятным.
'''
from itertools import product, permutations

for combo in product([1, 2, 3], repeat=2):
    print(combo)
    # (1, 1)
    # (1, 2)
    # (1, 3)
    # (2, 1)
    # (2, 2)
    # (2, 3)
    # (3, 1)
    # (3, 2)
    # (3, 3)

for perm in permutations('abc'):
    print(perm)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
'''


# 🌐  ipaddress -- для сетей (№13)
'''
from ipaddress import ip_network

net = ip_network('192.168.1.64/26', strict=False)
print(net, net.netmask, net.num_addresses)
'''


# 🤔 sys + functools -- для рекурсии (№16)
'''
from sys import setrecursionlimit
setrecursionlimit(10000)

from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 3:
        return n
    return F(n - 1) + F(n - 3)
'''

'''
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * F(n - 3)

print((F(247563) // 519 - 477 * F(247560)) // F(247557))
'''

# 🎭  fnmatch -- для поиска по маске (№25)
'''
from fnmatch import fnmatch

if fnmatch('12345', '12?45'):
    print('Подходит')
'''

# № 29355 Открытый вариант 2026 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать
# и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10, найдите все числа, соответствующие маске 89*6?7?9?,
# делящиеся на 9874 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – соответствующие им результаты деления этих чисел на 9874.
# Количество строк в таблице для ответа избыточно.
'''
from fnmatch import *
for x in range(9874, 10**10, 9874):
    if fnmatch(str(x), '89*6?7?9?'):
        print(x, x // 9874)

from re import *
for x in range(9874, 10**10, 9874):
    if fullmatch('89[0-9]*6[0-9]7[0-9]9[0-9]', str(x)):
        print(x, x // 9874)
'''


# 🔤 string -- готовые алфавиты
'''
from string import ascii_uppercase, digits, punctuation

print(ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(digits)           # 0123456789
print(punctuation)      # !"#$%&'()*+,-./:;<|}~
'''

#  🔣  math -- математические функции
'''
from math import *

print(sqrt(225))    # 15.0
print(ceil(7 / 2))  # 4
print(factorial(5)) # 120
print(gcd(36, 60))  # 12
'''

# 📎 Важно: при использовании from < . . . > import * - может произойти конфликт имен, если вы используете у себя такие же названия переменных.
#
# 🛁 На экзамене from turtle import * и from math import * помогают писать код быстрее.
# 🛁 В остальных случаях лучше использовать точечный импорт: from module import func.


# Способы подключения библиотек
'''
import math
print(f'Возьмем квадратный корень от числа 16: {math.sqrt(16)}')

import math as m  # Подключение с коротким именем
print(f'Возьмем квадратный корень от числа 16: {m.sqrt(16)}')

from math import sqrt, factorial  # Подключаем конкртеные функции
print(f'Возьмем квадратный корень от числа 16: {sqrt(16)}')

from math import *  # Подключаем сразу все содержимое
print(f'Возьмем квадратный корень от числа 16: {sqrt(16)}')
print(factorial(5))

cnt = 0
from itertools import *
for p in permutations('abc'):
    print(p)
    cnt += 1
print(cnt)
'''


# Условные операторы (ветвление if elif else)
'''
n = int(input('Ввдеите число: '))
if n > 0:  # if - если 
    print('Положительное')
elif n < 0:  # elif - иначе если 
    print('Отрицательное')
else:  # else - иначе 
    print('Равно нулю')
'''

# Пример зачем нужен elif
'''
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
    print('Лежит осях')
print('Продолжение программы')
'''


# Логические связки: or, and, not, in, +

flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = 4, -5, -6
if a > 0 and b > 0 and c > 0:
    print('AND - Все условия выполняются')
if a > 0 or b > 0 and c > 0:
    print('OR - Хотя бы одно условие выполняется')

for x in '23894572389457239':
    if x in '02468':
        print(x, end=' ')  # 2 8 4 2 8 4 2
print()

for x in '23894572389457239':
    if x not in '02468':
        print(x, end=' ')  # 3 9 5 7 3 9 5 7 3 9



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:

