# region Домашка: ******************************************************************

# Произведение и сумма цифр пятизначного числа
'''
n = int(input())  # 74382
a = n // 10000
b = (n // 1000) % 10
c = 0
d = 0
e = n % 10
print(a, b, c, d, e)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Условные операторы (ветвление): if, elif, else
'''
n = int(input('n: '))
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''


# x, y = int(input('x: ')), int(input('y: '))
'''
x, y = -4, -7

if x > 0 and y > 0:  # if - если
    print('Первая четверть')
elif x < 0 and y > 0:  # elif - иначе если
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else - иначе
    print('Лежит на осях')
print('КОНЕЦ')
'''


# Каскадные условные операторы
'''
x, y = int(input('x: ')), int(input('y: '))
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


# Логические связки: not, and, or, ^, !=, ==
'''
flag = True
print(not flag)  # False
print(not(not flag))  # True


a, b = 7, -2
if a > 0 and b > 0:  # and - гарантирует, что оба (все) выполнимы
    print('YES 1')
if a > 0 or b > 0:  # or - говорит, что хотя бы одно выполнимо
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^, != - гарантирует, что только один выполняется
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 3')

print(True + True + False)  # 2

# = - присваивание значения 
# == - сравнение значения (равны ли они)
# != - сравнение значения (не равны ли они)

a, b, c = 7, -2, 6
# Только два элемента должны быть положительные
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два элемента должны быть положительные ')
# Хотя бы два элемента положительные 
if (a > 0) + (b > 0) + (c > 0) >= 2:
    print('Только два элемента должны быть положительные ')
'''

# Работа с библиотеками в python
'''
import useful  # Самый топорный способ подключения, необходимо таскать с собой useful
print(useful.divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(useful.ALPHABET)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ


import useful as u  # Подключили библиотеку два ей короткое имя
print(u.divisors(24))
print(u.ALPHABET)

from useful import divisors, ALPHABET, orel_or_reshka  # Подключаем конкретные функции
print(divisors(24))
print(ALPHABET)

from useful import *  # Подключаем сразу все функции
print(divisors(24))
print(ALPHABET)


# CTRL + B

print(divisors.__doc__)
#     Функция поиска делителей числа num
#     :param num: Принимает целое (int) число.
#     :return: Возвращает список делителей от 1 до числа num

print(help(divisors))
#     Функция поиска делителей числа num
#     :param num: Принимает целое (int) число.
#     :return: Возвращает список делителей от 1 до числа num
'''

# Список библиотек необходимых нам на экзамене

# Для 6 номера
'''
import turtle as t
t.forward(100)
t.done()
'''

from fnmatch import *
# Помогает нам решать 25 номер с масками


from itertools import product, permutations
# Помогает решать 1, 8 и не будет лишний в номерах: 9, 12, 24


from ipaddress import *
'''
import sys
from functools import *
@lru_cache(None)
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
