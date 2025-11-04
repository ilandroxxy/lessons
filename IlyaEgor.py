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
        return n*2 + F(n+2)

print(F(82) - F(81))
'''
from codecs import replace_errors

# № 21415 Досрочная волна 2025 (Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – целое число, задан следующими соотношениями:
# F(n)=1 при n≤5;
# F(n)=n+F(n–2), если n>5.
# Чему равно значение выражения F(2126)–F(2122)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + F(n - 2)

print(F(2126) - F(2122))  # 4250
# RecursionError: maximum recursion depth exceeded

# F(2126) = 2126 + F(2124)
# F(2124) = 2124 + F(2122) - F(2122)
print(2126 + 2124)  # 4250
'''


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
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

print((F(2024) // 4 + F(2023)) // F(2022))
# RecursionError: maximum recursion depth exceeded
'''
# print((F(2024) / 4 + F(2023)) / F(2022))
#            ~~~~^~~
# OverflowError: integer division result too large for a float


#
# № 23756 Демоверсия 2026 (Уровень: Базовый)
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


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
# (М. Попков) Снежная Королева создала волшебную функцию
# F(n), которая помогает ей вычислять силу зимы.
# Эта функция определяется следующим образом:
# F(n)=n−1, при n⩽3;
# F(n)=F(n−2)+n/2−F(n−4), если n>3 и n чётно;
# F(n)=F(n−1)×n+F(n−2), если n>3 и n нечётно, где n – целое неотрицательное число.
# Для этого вычислите значение выражения: F(4952)+2×F(4958)+F(4964).
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

# https://education.yandex.ru/ege/inf/task/0a886190-44eb-4653-b64a-80dafc2a73d1
'''
from functools import *

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)

for n in range(3000):
    F(n)

print((F(2024) + 2 * F(2023)) // F(2022))
'''


'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n-1) + n
    if n > 2 and n % 2 == 0:
        return F(n-3) + 2 * n
for n in range(3000):
    F(n)
print(F(2048)-F(2041))
'''

from functools import *

@lru_cache(None)
def F(n):
    if n <= 10:
        return n*2

    if n % 2 == 0 and n > 10:
        return F(n-3) - F(n-9)*2

    if n % 2 != 0 and n > 10:
        return F(n-2) *2 -F(n-7)

for n in range(3500):
    F(n)

m = F(3063)
print(sum(map(int, str(m))))
print(sum([int(x) for x in str(m)]))


'''
from sys import setrecursionlimit
from functools import *
setrecursionlimit(10**8)

@lru_cache(None)
def F(n):
    if n >= 3210:
        return 1
    if n < 3210:
        return F(n+3)+7

def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n-3)+5

for n in range(4000):
    F(n)

for n in range(4000):
    G(n)

print(F(15)-G(3000))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16, 25]
# КЕГЭ = []
# на следующем уроке: 23, 19-21
