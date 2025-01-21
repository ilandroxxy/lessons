# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 5! = 1 * 2 * 3 * 4 * 5 = 120
'''
import math
print(math.factorial(5))  # 120


def my_factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


print(my_factorial(5))  # 120
'''

#
# № 4107 (Уровень: Базовый)
'''
def F(n):
    if n == 1:   # F(n)=1 при n=1;
        return 1
    if n > 1 and n % 2 == 0:
        return n * F(n - 1)
    if n > 1 and n % 2 != 0:
        return 1 + F(n - 2)

print(F(84))
'''


# № 5954 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print((F(2023) - F(2022)) / F(2020))
'''
# RecursionError: maximum recursion depth exceeded


#
# № 18931 Новогодний вариант 2025 (Уровень: Базовый)


import time
start = time.time()

from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n / 2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)

for i in range(5000):
    F(i)

# 0.002565 0.00412

print(F(4952) + 2 * F(4958) + F(4964))

print(time.time() - start)
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 16]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Роман 2/5 -> 14 вторичных баллов +[2, 12] -[5, 6, 8]
