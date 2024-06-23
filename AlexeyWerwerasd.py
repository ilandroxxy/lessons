# region Домашка: ************************************************************


# i  0123
s = '5346'

'''
n = input()  # str()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
e = int(n[4])
sum = a + b + c + d + e
print(sum)
prod = a * b * c * d * e
print(prod)
'''

'''
n = int(input())
a = n // 10000
b = (n % 10000) // 1000
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10
print(a * b * c * d * e)
print(a + b + c + d + e)
'''

# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# Условные операторы (ветвление): if, elif, else

'''
x = int(input('x: '))
if x % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''

'''
x = int(input('x: '))
if x > 0:
    print('Больше нуля')
else:
    print('Меньше или равно нулю')
'''

'''
x = int(input('x: '))
if x > 0:  # if - если
    print('Больше нуля')
elif x < 0:  # elif - иначе если
    print('Меньше нуля')
else:  # else - иначе
    print('Равно нулю')
'''

'''
x = 7
y = 8

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
print('КОНЕЦ')
'''

# Каскадные условные операторы
'''
x = 7
y = 8

if x > 0:
    if y > 0:  # x > 0, y > 0
        print('Первая четверть')
    else:  # x > 0, y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <=, y > 0
        print('Вторая четверть')
    else:  # x <= 0, y <= 0
        print('Третья четверть')
'''

# Логические связки: not, and, or, ^, ==, !=
'''
flag = True  # bool
print(not flag)  # False
print(not(not flag))  # True
'''

'''
= - присваивание нового значения для переменной
== - сравнение значения переменных (равно)
!= - сравнение значения переменных (не равно)
'''

'''
a, b, c = 5, -8, 6

if a > 0 and b > 0:  # and - гарантирует, что оба (все) выполняются
    print('YES 1')
if a > 0 or b > 0:  # or - говорит о том, что хотя бы одно условие выполняется
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^ - гарантирует, что только одно условие выполняется
    print('YES 3')
if (a > 0) != (b > 0):  # != - гарантирует, что только одно условие выполняется
    print('YES 4')
if (a > 0) + (b > 0) + (c > 0) == 2:  # "Только два значения истинны"
    print('YES 5')

print(True + False + True)
'''


# Логические функции all(), any()
'''
M = [2, 4, 6, 8, 10]
print(all(x % 2 == 0 for x in M))  # True - "Все элементы списка четные"
print(any(x % 2 == 0 for x in M))  # True - "Хотя бы один элемент списка четный"

M = [2, 4, 6, 7, 10]
print(all(x % 2 == 0 for x in M))  # False
print(any(x % 2 == 0 for x in M))  # True


M = [2, 4, 6, 7, 10]
print(all(x % 2 != 0 for x in M))  # False
print(any(x % 2 != 0 for x in M))  # True
'''

# Подключение библиотек в Python
'''
import useful
print(useful.ALPHABET)
print(useful.orel_or_reshka())

import useful as u
print(u.ALPHABET)
print(u.orel_or_reshka())

from useful import ALPHABET, orel_or_reshka, who_is_name
print(ALPHABET)
print(orel_or_reshka())

from useful import *
print(ALPHABET)
print(orel_or_reshka())
'''

import sys
import turtle as t
from itertools import product, permutations
from ipaddress import *

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
