# region Домашка: ******************************************************************

# Монетный размен: количество и остаток
'''
rubles = int(input())  # 105
nominal = int(input())  # 10
print(rubles // nominal)  # 10
print(rubles % nominal)  # 5
'''


# Произведение и сумма цифр пятизначного числа
'''
n = int(input())
a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10
print(a * b * c * d * e)
print(a + b + c + d + e)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Условные операторы (ветвление): if, elif, else

# if - если
# elif - иначе если
# else - иначе
'''
n = int(input('n: '))
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
    

n = int(input('n: '))
if n > 0:
    print('Положительное')
elif n < 0:
    print('Отрицательное')
else:
    print('Равно нулю')

n = int(input('n: '))
if n > 0:
    print('Положительное')
if n < 0:
    print('Отрицательное')
if n == 0:
    print('Равно нулю')
'''

# К какой четверти принадлежит точка x, y?
# x = int(input('x: '))
# y = int(input('y: '))
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
    print('Лежит на осях')
    
print('Продолжение программы')
'''


# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

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


# Логические связки: or, and, not, in, ==, !=, ^
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True

M = [1, 2, 3, 1, 4]
for x in M:
    if x % 2 == 0:  # == - сравнение равно ли?
        print(x, end=' ')  # 2 4
print()

for x in M:
    if x % 2 != 0:  # != - сравнение не равно ли?
        print(x, end=' ')  # 1 3 1
print()

s = '12314'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 4 
print()

for x in s:
    if x not in '02468':  # 
        print(x, end=' ')  # 1 3 1 
print()
'''

'''
a, b, c = 4, -5, 6

if a > 0 and b > 0:
    print('and')  # and - "и" Гарантирует, что все условия выполняются
if a > 0 or b > 0:
    print('or')  # or - "или" Говорит о том, что хотя бы одно условие выполняется
if (a > 0) ^ (b > 0):
    print('^')  # ^, != - Гарантируют, что только одно условие выполняется
if (a > 0) != (b > 0):
    print('!=')

print(True + False + True)  # 2
#   True      False     True
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('В данном случае выполняется только два условия')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('В данном случае выполняется не более двух условий')
'''


# Библиотеки в Python
# ctrl + B
'''
import math  # Самый простой способ подключения библиотеки
print(math.sqrt(16))

import math as m  # Переименовываем библиотеку в короткое имя m
print(m.sqrt(16))

from math import sqrt, pow, prod  # Подключаю конкретные функции из библиотеки
print(sqrt(16))

from math import *  # Подключаем сразу все функции из библиотеки
print(sqrt(16))
print(pow(4, 2))
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
