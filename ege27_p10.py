# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20906 Апробация 05.03.25(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=1 при n=1;
# F(n)=n×F(n−1), если n>1.
# Чему равно значение выражения (F(2024)/4+F(2023))/F(2022)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print( (F(2024) // 4 + F(2023)) // F(2022) )
'''
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

#     print( (F(2024) / 4 + F(2023)) / F(2022) )
#             ~~~~~~~~^~~
# OverflowError: integer division result too large for a float
'''
from sys import setrecursionlimit
from fractions import Fraction

setrecursionlimit(10**8)

def F(n):
    if n < 2:
        return 1
    if n > 1 and n % 2 == 0:
        return Fraction(n, 3) * F(n - 1)
    if n > 1 and n % 2 != 0:
        return 6 * F(n - 1)

print( F(2027) // F(2025))
'''



# № 23275 Основная волна 11.06.25(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n) и G(n), где n – целое число, задан следующими соотношениями:
# F(n)=2×(G(n−3)+8);
# G(n)=2×n, если n<10.
# G(n)=G(n−2)+1, если n≥10.
# Чему равно значение выражения F(15548)?
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

# Вариант 2
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
# Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−4)+3580, если n≥19;
# F(n)=6×(G(n−7)−36), если n<19;

# G(n)=n/20+28, если n≥248045;
# G(n)=G(n+9)−4, если n<248045.
# Чему равно значение функции F(673)?
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

for n in range(0, 700, 1):
    F(n)

print(F(673))
'''

# № 25398 (Уровень: Средний)
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
    if n > 30:
        return f(n - 6) + 2048
    if n <= 30:
        return 3 * (g(n - 5) + 13)

@lru_cache(None)
def g(n):
    if n >= 221337:
        return 2 * n + 50
    if n < 221337:
        return g(n + 11) - 48

for n in range(222000 - 1, -1, -1):
    g(n)
for n in range(5500):
    f(n)
print(f(5078))
'''

# № 25397 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций F(n) и G(n), где
# n - целое число, задан следующими соотношениями:
# F(n)=F(n−4)+3020, если n>40;
# F(n)=3×(G(n−2)−15), если n≤40;
# G(n)=10×n+50, если n≥301208;
# G(n)=G(n+7)−21, если n<301208.
# Чему равно значение функции F(2026)?
'''
from functools import *

@lru_cache
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    if n <= 40:
        return 3 * (G(n - 2) - 15)

@lru_cache
def G(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return G(n + 7) - 21


for n in range(310000 - 1, -1, -1):
    G(n)
for n in range(2100):
    F(n)
print(F(2026))
'''

# № 27076 (Уровень: Средний)
# (В. Лашин) Алгоритм вычисления функций F(n), G(n) и Q(n), где n – целое число, задан следующими соотношениями:
# F(n)=G(n+4), если n<43;
# F(n)=2∗F(n−2)−F(n−4)+2, если n≥43;
# G(n)=G(n+3)+2 при n<11240;

# G(n)=Q(n), если n ≥11240.
# Q(n)=n+4, если n<21;
# Q(n)=Q(n−4)+2, если n≥21;
# Чему равно значение функции F(2026)?
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

for n in range(12000):
    Q(n)
for n in range(12000 - 1, -1, -1):
    G(n)
for n in range(2500):
    F(n)

print(F(2026))
'''


# № 25399 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−5)+1092, если n≥128;
# F(n)=5×G(n−7)+29,, если n<128;
# G(n)=n−15, если n>303728;
# G(n)=G(n+8)/2−109, если n≤303728.
# Чему равно значение функции F(2049)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 128:
        return F(n - 5) + 1092
    if n < 128:
        return 5 * G(n - 7) + 29

@lru_cache(None)
def G(n):
    if n > 303728:
        return n - 15
    if n <= 303728:
        return G(n + 8) / 2 - 109

for n in range(310000-1, -1, -1):
    G(n)

for n in range(2100):
    F(n)

print(F(2049))
'''

# № 25397 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций F(n) и G(n), где
# n - целое число, задан следующими соотношениями:
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
        return 3 * (G(n - 2) - 15)

@lru_cache(None)
def G(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return G(n + 7) - 21


for n in range(302_000 - 1, -1, -1):
    G(n)
for n in range(2500):
    F(n)
print(F(2026))
'''

# № 25398 (Уровень: Средний)
# (Р. Косов) Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−6)+2048, если n>30;
# F(n)=3×(G(n−5)+13), если n≤30;
# G(n)=2×n+50, если n≥221337;
# G(n)=G(n+11)−48, если n<221337.
# Чему равно значение функции F(5078)?

from functools import *


@lru_cache(None)
def F(n):
    if n > 30:
        return F(n - 6) + 2048
    if n <= 30:
        return 3 * (G(n - 5) + 13)


@lru_cache(None)
def G(n):
    if n >= 221337:
        return 2 * n + 50
    if n < 221337:
        return G(n + 11) - 48


for n in range(230000 - 1, -1, -1):
    G(n)
for n in range(5100):
    F(n)

print(F(5078))

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [8, 15]
# КЕГЭ = []
# todo на следующем уроке: 13, 19-21, 10

# 2, 5, 18