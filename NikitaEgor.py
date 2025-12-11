# region Домашка: ******************************************************************


# № 48389 (Уровень: Базовый)
# Операнды арифметического выражения записаны в системах счисления с основаниями 7 и 9:
# yx320_7 + 1x3y3_9
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 181.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 181
# и укажите его в ответе в десятичной системе счисления.
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:7]:
    for y in alp[:7]:
        A = int(f'{y}{x}320', 7)
        B = int(f'1{x}3{y}3', 9)
        if (A + B) % 181 == 0:
            RES.append((A + B) // 181)
print(min(RES))
'''

# endregion Домашка: ******************************************************************


# region Урок: *************************************************************

# № 21902 Открытый вариант 2025 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:  # F(n)=n при n≥2025;
        return n
    if n < 2025:  # F(n)=n×2+F(n+2), если n<2025.
        return n * 2 + F(n + 2)

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

#   [Previous line repeated 996 more times]
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
        return  n * F(n - 1)

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
    return 2 * (G(n - 3)+8)

def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

print(F(15548))
'''


# № 14338 (Уровень: Средний)
'''
import sys
sys.setrecursionlimit(10**8)
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

print(F(4952)+2 * F(4958)+F(4964))
'''


# https://education.yandex.ru/ege/inf/task/9f0329d0-79f3-4461-a610-7f6516b217a0
# Алгоритм вычисления значения функции F(n)F(n), где nn — натуральное число, задан такими соотношениями:
# F(n)=1 при n<3n<3
# F(n)=F(n−1)+n−1  при n>2 и при этом чётно
# F(n)=F(n−2)+2n−2, если n>2 и при этом нечётно
# Чему равно значение выражения F(3048)−F(3045)F(3048)−F(3045)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n - 1) + n - 1
    if n > 2 and n % 2 != 0:
        return F(n - 2) + 2*n - 2

print(F(3048) - F(3045))
'''


# # Никита https://education.yandex.ru/ege/inf/task/de7e46c5-5861-4b77-83dc-a338a0e9d421
# F(n)=G(n)=n при n≤2;
# F(n)=G(n)+F(n−2)при n>2;
# G(n)=F(n−1)−G(n−2)при n>2.
# Определите значение, полученное при вызове G(15).
'''
def F(n):
    if n <= 2:
        return n
    if n > 2:
        return G(n) + F(n - 2)

def G(n):
    if n <= 2:
        return n
    if n > 2:
        return F(n - 1) - G(n - 2)

print(G(15))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5, 14, 16]
# КЕГЭ = []
# на следующем уроке: 23, 19-21, 15, 2
