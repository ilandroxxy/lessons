# region Домашка: ******************************************************************


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
print(2126 + 2124)  # 4250
'''

# № 4739 (Уровень: Средний)
'''
def F(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return F(n + 1) + F(n + 2)

print(F(12345) + F(10101))
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
#           ~~~~~^~~
# OverflowError: integer division result too large for a float


# № 23375 Резервный день 19.06.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return G(n - 1) + G(n - 3)

def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 4) + 2

print(F(42999))
'''


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *

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

from functools import *
import sys

sys.setrecursionlimit(10 ** 8)


@lru_cache(None)
def F(n):
    if n <= 10:
        return n * 2
    if n > 10 and n % 2 == 0:
        return F(n - 3) - F(n - 9) * 2
    if n > 10 and n % 2 != 0:
        return F(n - 2) * 2 - F(n - 7)


for i in range(4000):
    F(i)

n = F(3063)
print(sum([int(x) for x in str(n)]))

z = list(str(F(3063)))
for i in range(len(z)):
    z[i] = int(z[i])
print(sum(z))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14, 15, 16, 25]
# КЕГЭ = []
# на следующем уроке:
