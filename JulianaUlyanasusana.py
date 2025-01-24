# region Домашка: ******************************************************************

# № 2588 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))



for x in range(190201, 190260):
    d = [j for j in divisors(x) if j % 2 == 0]
    if len(d) == 4:
        print(d[-1], d[-2])
'''


# № 8511 Апробация 17.05 (Уровень: Базовый)
'''
from fnmatch import fnmatch

for x in range(253, 10 ** 8, 253):
    if fnmatch(str(x), '12??15*6'):
        print(x, x // 253)
'''

'''
# Факториал числа:
# 5! = 1 * 2 * 3 * 4 * 5 = 120

import math  # Самое базовое импортирование библиотеки
print(math.factorial(5))  # 120

import math as m  # Подключаем с коротким именем
print(m.factorial(5))  # 120

from math import factorial, sqrt, fabs  # Подключаем конкретные библиотеки
print(factorial(5))  # 120

from math import *  # Подключаем сразу все содержимое
print(factorial(5))  # 120
print(sqrt(16))  # 4


def my_factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

print(my_factorial(5))  # 120
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19709 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1  # F(n)=1 при n=1;
    if n > 1:
        return n**3 + F(n - 1)  # F(n)=n**3+F(n−1) при n>1.


print(F(2025) - F(2022))
# RecursionError: maximum recursion depth exceeded
'''


# № 19248 ЕГКР 21.12.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2*n * F(n-4)


print((F(13766) - 9 * F(13762)) / F(13758))
'''


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n-2) + n/2 - F(n-4)
    if n > 3 and n % 2 != 0:
        return F(n-1) * n + F(n - 2)

for i in range(5000):
    F(i)

print(F(4952) + 2*F(4958) + F(4964))
'''


# № 18140 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x - y >= 39) or (y <= x) or (y >= A - 20)

for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
'''


# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 18266(Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 16332 Открытый вариант 2024 (Уровень: Базовый)

# У исполнителя есть три команды, которые обозначены латинскими буквами:
# A. Прибавить 1
# B. Прибавить 2
# C. Умножить на 2

# Сколько существует программ, которые преобразуют исходное число 4 в число 15,
# и при этом траектория вычислений программы содержит числа 11 и 13?

def F(a, b):   # F(4, 15)
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*2, b)


print(F(4, 11) * F(11, 13) * F(13, 15))

# Ответ: 100

#
# № 17534 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    else:
        return F(a - 1, b) + F(a // 2, b)

print(F(30, 8) * F(8, 1))
'''
# Ответ: 288


# А. Вычесть 2
# В. Вычесть 5
# С. Найти целую часть от деления на 3

# Сколько существует программ, для которых при исходном числе 46 результатом является число 7,
# при этом траектория вычислений не содержит числа 32 и содержит 19?

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 14 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]
