# region Домашка: ******************************************************************


# № 4465 Джобс 15.06.2022 (Уровень: Базовый)
'''
RES = []
from itertools import product
n = 0
for p in product(sorted('ПЯТЬДНЕЙ'), repeat=4):
    word = ''.join(p)
    n += 1
    if len(word) == len(set(word)):
        if ('Я' not in word) and ('И' not in word):
            RES.append(n)
print(max(RES))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21902 Открытый вариант 2025 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + F(n + 2)

print(F(82) - F(81))
'''


# № 21415 Досрочная волна 2025 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + F(n - 2)

print(F(2126) - F(2122))
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# F(2126) = 2126 + F(2124)
# F(2124) = 2124 + F(2122) - F(2122)
print(2126 + 2124)
'''


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print((F(2024) // 4 + F(2023)) // F(2022))
'''
# print((F(2024) / 4 + F(2023)) / F(2022))
#            ~~~~^~~
# OverflowError: integer division result too large for a float



# № 23756 Демоверсия 2026 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return 2 * (G(n - 3) + 8)

def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

print(F(15548))
'''



# № 13297 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
def F(n):
    if n == 3:
        return 1
    if n > 3:
        return 5 * F(n-1)+6 * G(n-1) - 3*n+8

def G(n):
    if n == 3:
        return 1
    if n > 3:
        return 6 * F(n - 1) + 5 * G(n - 1) + 3

print(F(9) + G(9))
'''


# № 10718 (Уровень: Средний)
'''
from functools import *
@lru_cache(None)
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * F(n - 2) - F(n - 1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * F(n - 1) + F(n - 2) - 2

for n in range(200):
    F(n)

print(F(170))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16]
# КЕГЭ = []
# на следующем уроке: 23, 19-21
