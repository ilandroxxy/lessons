# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20196 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 110:
        return n
    if n >= 110:
        return n + F(n - 1)

print(F(2025) - F(2021))
'''
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# № 14338 (Уровень: Средний)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 10:
        return n
    if n > 9:
        return 3 * n + G(n - 2)

def G(n):
    if n < 10:
        return n
    if n > 9:
        return n - 2 + F(n - 1)

print(F(2204) - G(2200))
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
        return F(n - 2) + n/2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)

for n in range(5000):
    F(n)

print(F(4952) + 2 *F(4958) + F(4964))
'''


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print((F(2024) // 4 + F(2023)) / F(2022))
# print((F(2024) / 4 + F(2023)) / F(2022))
#             ~~~^~~
# OverflowError: integer division result too large for a float
'''


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))


def F(a, b):
    if a >= b:
        return a == b  # True/False
    return F(a+1, b) + F(a+2, b) + F(a+3, b)


# print(True + True + False)  # 2

print(F(5, 7) * F(7, 11))
'''


# № 6756 Апробация 10.03.23 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a-2, b) + F(a//2, b)

print(F(40, 10) * F(10, 2))
'''


# № 7011 (Уровень: Средний)
'''
def F(a, b, c):
    if a >= b or a == 28:
        return a == b and 'BACA' not in c
    return F(a+2, b, c+'A') + F(a+3, b, c+'B')  +F(a*2, b, c+'C')

print(F(2, 40, ''))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [15, 16, 23]
# КЕГЭ  = []
# на следующем уроке: 5, 7, 8, 9, 13, 19-21 (2 кучи + убывание), 25

# Первый пробник 21.12.24:
# Анастасия 9/29 -> 48 вторичных баллов +[1, 2, 4, 12, 16, 14, 15, 23, 20-21] -[3, 8, 10, 11, 18, 19]
