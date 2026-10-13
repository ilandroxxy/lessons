




# Условные операторы if, elif, else (ветвление)
'''
n = int(input('n: '))
if n > 0:  # если
    print('Число положительное')
elif n < 0:  # иначе если
    print('Число отрицательное')
else:  # иначе
    print('Число равно 0')

n = int(input('n: '))
if n > 0:  # если
    print('Число положительное')
if n < 0:  # иначе если
    print('Число отрицательное')
if n == 0:  # иначе
    print('Число равно 0')
'''


'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, 0
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
print('Конец условия')
'''


# Логические связки: and, or, not, in, not in, ==, !=
"""
a, b, c = 4, 5, 4

print(a == c)  # True
print(a == b)  # False

print(a != c)  # False

if a > 0 and b > 0 and c > 0:
    print('and - Все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - Хотя бы одно условие верное')

print(True + True + False + True)  # 3

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все условия верные')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух выполняются')


flag = True
print(not flag)  # False
print(not(not flag))  # True

s = '3kj45h3kjh5'
for x in s:
    print(x, end=' ')  # 3 k j 4 5 h 3 k j h 5
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 3 4 5 3 5
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # k j h k j h
print()


summa = 0
s = '34535'
for x in s:
    summa += int(x)
print(summa)  # 20

'''
summa = 0
s = '3kj45h3kjh5'
for x in s:
    summa += int(x)  # ValueError: invalid literal for int() with base 10: 'k'
print(summa)  # 20
'''

summa = 0
s = '3kj45h3kjh5'
for x in s:
    if x in '0123456789':
        summa += int(x)  
print(summa)  # 20
"""

'''
n = int(input())
# n = 53489
a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10
print(a + b + c + d + e)
print(a * b * c * d * e)
'''


# Способы подключения библиотек

import math  # - классический способ, но неудобный так как везде нужно таскать с собой имя math

print(16 ** (1/2))  # 4.0
print(math.sqrt(16))  # 4.0
print(math.factorial(5))

import math as m  # - подключение библиотеки через короткое имя (любое)
print(m.sqrt(16))
print(m.factorial(5))

from math import sqrt, factorial, fabs  # - подключение конкретных функций из библиотеки
print(sqrt(16))
print(factorial(5))


from math import *  # - подключение всего содержимого библиотеки
print(sqrt(16))
print(factorial(5))
print(fabs(5))



count = 0
from itertools import product, permutations
for p in permutations('abc'):
    count += 1
    print(p)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
print(count)

count = 0
from itertools import *
for p in permutations('abc'):
    count += 1
    print(p)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
print(count)
# TypeError: unsupported operand type(s) for +=: 'type' and 'int'











# todo На следующем уроке: проговорить типы данных коллекций












