# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 15 Демоверсия 2021(Уровень: Базовый)
'''
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * F(n - 2)

print(F(26))
'''


# № 4704 Демоверсия 2023(Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

from sys import *
setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print(F(2023) / F(2020))
'''
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded



# № 17557 Основная волна 08.06.24(Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)

print( (F(2024) // 16 - F(2023)) // F(2022)   )
#     print( (F(2024) / 16 - F(2023)) / F(2022)   )
#             ~~~~~~~~^~~~
# OverflowError: integer division result too large for a float
'''


# № 18931 Новогодний вариант 2025(Уровень: Базовый)
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

for n in range(0, 5000):
    F(n)

print(F(4952) + 2 * F(4958) + F(4964))
'''


# № 23756 Демоверсия 2026(Уровень: Базовый)
'''
from functools import *

def F(n):
    return 2 * (G(n - 3) + 8)

@lru_cache(None)
def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

for n in range(16000):
    G(n)

print(F(15548))
'''


# № 25355 ЕГКР 13.12.25(Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4

for n in range(250_000-1, -1, -1):
    G(n)

for n in range(0, 700):
    F(n)

print(F(673))
'''


# № 27076 (Уровень: Средний)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 43:
        return G(n + 4)
    if n >= 43:
        return 2 * F(n - 2) - F(n - 4) + 2

@lru_cache(None)
def G(n):
    if n < 11240:
        return G(n + 3) + 2
    if n >= 11240:
        return Q(n)

@lru_cache(None)
def Q(n):
    if n < 21:
        return n + 4
    if n >= 21:
        return Q(n - 4) + 2

for n in range(0, 11250):
    Q(n)

for n in range(11250-1, -1, -1):
    G(n)

for n in range(0, 2030):
    F(n)

print(F(2026))
'''



# № 28937 ЕГКР 18.04.26(Уровень: Базовый)
# Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−8)+1095, если n≥21;
# F(n)=10×(G(n−7)−36), если n<21;

# G(n)=n/23+33, если n≥22560;
# G(n)=G(n+11)−4, если n<22560.
# Чему равно значение функции F(548)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 21:
        return F(n - 8) + 1095
    if n < 21:
        return 10 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 22560:
        return n / 23 + 33
    if n < 22560:
        return G(n + 11) - 4

for n in range(22600 - 1, -1, -1):
    G(n)

for n in range(0, 600):
    F(n)

print(F(548))
'''


# № 25397 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−4)+3020, если n>40;
# F(n)=3×(G(n−2)−15), если n≤40;

# G(n)=10×n+50, если n≥301208;
# G(n)=G(n+7)−21, если n<301208.
# Чему равно значение функции F(2026)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    if n <= 40:
        return 3 * (G(n - 2) -15)

@lru_cache(None)
def G(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return G(n + 7) - 21

for n in range(302000 - 1, -1, -1):
    G(n)

for n in range(2030):
    F(n)

print(F(2026))
'''


# № 25398 (Уровень: Средний
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−6)+2048, если n>30;
# F(n)=3×(G(n−5)+13), если n≤30;

# G(n)=2×n+50, если n≥221337;
# G(n)=G(n+11)−48, если n<221337.
# Чему равно значение функции F(5078)?
'''
from functools import *

@lru_cache(None)
def f(n):
    if n <= 30:
        return 3 * (g(n - 5) + 13)
    return f(n - 6) + 2048

@lru_cache(None)
def g(n):
    if n < 221337:
        return g(n + 11) - 48
    return 2 * n + 50

for n in range(230000 - 1, -1, -1):
    g(n)

for n in range(6000):
    f(n)

print(f(5078))
'''


# № 25399 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−5)+1092, если n≥128;
# F(n)=5×G(n−7)+29,, если n<128;

# G(n)=n−15, если n>303728;
# G(n)=G(n+8)/2−109, если n≤303728.
# Чему равно значение функции F(2049)?

from functools import *

@lru_cache(None)
def f(n):
    if n < 128:
        return 5 * g(n - 7) + 29
    return f(n - 5) + 1092

@lru_cache(None)
def g(n):
    if n <= 303728:
        return g(n + 8) / 2 - 109
    return n - 15

for n in range(310000-1, -1, -1):
    g(n)

for n in range(3000):
    f(n)

print(f(2049))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 13, 16]
# КЕГЭ = []
# todo на следующем уроке:
