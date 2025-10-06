# region Домашка: ******************************************************************


# https://stepik.org/lesson/1038816/step/5?unit=1062780
# Программа перебирает числа больше 10**9 и
# выбирает из них числа-палиндромы, у которых наибольший
# делитель (отличный от 1 и самого числа) кратен 7.
#
# Выведите первые 5 чисел, которые выберет
# программа, и для каждого числа выведите наибольший делитель.
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # (отличный от 1 и самого числа)
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(10**9, 10**10):
    if str(x) == str(x)[::-1]:
        d = divisors(x)
        if len(d) > 0:
            if max(d) % 7 == 0:
                print(x, max(d))
                cnt += 1
                if cnt == 5:
                    break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21902 Открытый вариант 2025 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:
        return n  # F(n)=n при n≥2025;
    if n < 2025:
        return n * 2 + F(n + 2)  # F(n)=n×2+F(n+2), если n<2025.

print(F(82) - F(81))  # 1945
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
# RecursionError: maximum recursion depth exceeded


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


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print((F(2024) // 4+F(2023)) // F(2022))

# print((F(2024) / 4+F(2023)) / F(2022))
#         ~~~~~~~^~
# OverflowError: integer division result too large for a float
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
    if n > 3 and n % 2 != 0 :
        return F(n - 1) * n + F(n - 2)

for n in range(5000):
    F(n)

print(F(4952)+2 * F(4958) + F(4964))
'''

# № 23562 Пересдача 03.07.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(100000)

def F(n):
    return G(n - 1)


def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 2) + 1


print(F(47995))
'''


# 23375
'''
import sys

sys.setrecursionlimit(10 ** 8)


def F(n):
    return G(n - 1) + G(n - 3)


def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 4) + 2


print(F(42999))
'''

# 23200
'''
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n < 10:
        return n
    if n >= 10:
        return 3*n + F(n-3)
print((F(6250) + 2 * F(6244)) // F(6238))
'''


# № 18297 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n < 10:
        return n - 1
    if n >= 10 and n % 2 == 0:
        return 3 * n - 1 + F(n-3)
    if n >= 10 and n % 2 != 0:
        return 5 * n + 2 + F(n - 4)
print(F(4445) - F(4444))
'''

# 21711

import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)

print((F(47872) - 290 * F(47865)) // F(47858))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 16, 25]
# КЕГЭ = []
# на следующем уроке: В идеале на выходные взять повторение всех номером
