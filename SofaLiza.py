# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038794/step/8?unit=1062789
# n = 1: Петя 1
# n = 2: Ваня 1
# n = 3: Петя 2
# n = 4: Ваня 2
# n = 5: Петя 3

def F(s, n):
    if s >= 21:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)


print(19, [s for s in range(1, 20+1) if F(s, n=3) and not F(s, n=1)])
print(20, [s for s in range(1, 20+1) if F(s, n=4) and not F(s, n=2)])
print(21, [s for s in range(1, 20+1) if F(s, n=5) and not F(s, n=3) and not F(s, n=1)])



# https://stepik.org/lesson/1038794/step/15?unit=1062789
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-8, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print(19, [s for s in range(16, 1000) if F(s, n=2)])
print(20, [s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# https://stepik.org/lesson/1038794/step/16?unit=1062789
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 69:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(floor(a/2), s, n-1), F(a, floor(s/2), n-1), F(a-5, s+2, n-1), F(a+2, s-5, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print(19, [s for s in range(51, 1000) if F(35, s, n=2)])
print(20, [s for s in range(51, 1000) if F(35, s, n=3) and not F(35, s, n=1)])
print(21, [s for s in range(51, 1000) if F(35, s, n=4) and not F(35, s, n=2)])
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
        return n*2 + F(n + 2)

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
'''
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


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

# print((F(2024) / 4 + F(2023)) / F(2022))
#          ~~~~~~^~~
# OverflowError: integer division result too large for a float
'''


# № 23562 Пересдача 03.07.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return G(n - 1)

def G(n):
    if n <= 9:
        return 3*n
    if n > 9:
        return G(n - 2) + 1

print(F(47995))
'''


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *

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

print(F(4952) + 2 * F(4958) + F(4964))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 13, 14, 15, 16, 19-21, 23]
# КЕГЭ = []
# на следующем уроке:
