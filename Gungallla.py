# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 21415 Досрочная волна 2025 (Уровень: Базовый)
'''
# RecursionError: maximum recursion depth exceeded

import sys
sys.setrecursionlimit(10**6)

def F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + F(n-2)

print(F(2126) - F(2122))
'''
import sys

# № 23275 Основная волна 11.06.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**6)

def F(n):
    return 2 * (G(n - 3) + 8)

def G(n):
    if n < 10:
        return 2*n
    if n >= 10:
        return G(n - 2) + 1

print(F(15548))
'''


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**6)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print((F(2024) // 4 + F(2023)) // F(2022))
'''
# print((F(2024) / 4 + F(2023)) / F(2022))
#        ~~~~~~~~^~~
# OverflowError: integer division result too large for a float


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
# F(n)=n−1, при n⩽3;
# F(n)=F(n−2)+n/2−F(n−4), если n>3 и n чётно;
# F(n)=F(n−1)×n+F(n−2), если n>3 и n нечётно,
'''
from functools import *
import sys
sys.setrecursionlimit(10**6)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n / 2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)

for n in range(5000):
    F(n)

print(F(4952) + 2 * F(4958) + F(4964))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 25]
# КЕГЭ  = []
# на следующем уроке:
