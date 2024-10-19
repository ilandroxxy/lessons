# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 16 №45250
'''
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return F(n - 2) + F(n - 1) - n
    if n > 2 and n % 2 != 0:
        return F(n - 1) - F(n - 2) + 2 * n

print(F(32))
'''


# Тип 16 №33486
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return n + F(n - 3)
    if n % 3 > 0:
        return n + F(n - (n % 3))


print(F(26))
'''


# Тип 16 №59721
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
# F(n)=n, если n=1;
# F(n)=n−1+F(n−1), если n>1.
#
# Чему равно значение выражения F(2024)−F(2022)?
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return n
    if n > 1:
        return n - 1 + F(n - 1)


print(F(2024) - F(2022))  # 4045
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2024) = 2023 + F(2023)
# F(2023) = 2022 + F(2022) - F(2022)
print(2023 + 2022)  # 4045
'''


# Тип 16 №4657
# https://inf-ege.sdamgia.ru/problem?id=4657
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * G(n-1) + 5*n

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) + 2*n


print(F(4) + G(4))
'''


# Тип 16 №36871
'''
def F(n):
    if n== 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

cnt = 0
for n in range(1, 1000+1):
    if F(n) == 3:
        cnt += 1
print(cnt)
'''


# № 17679 Пересдача 04.07.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)


print((F(2024) // 7 - F(2023)) / F(2022))

# print((F(2024) / 7 - F(2023)) / F(2022))
#        ~~~~~~~~^~~
# OverflowError: integer division result too large for a float
'''


# № 13297 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
def F(n):
    if n == 3:
        return 1
    if n > 3:
        return 5 * F(n - 1) + 6*G(n - 1) - 3*n + 8

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

print(F(170))
'''


# Тип 23 №18598
# У исполнителя есть три команды, которым присвоены номера.
# 1. Прибавить 1.
# 2. Умножить на 2.
# 3. Умножить на 3.
#
# Сколько существует программ, которые преобразуют исходное число 1 в число 40
# и при этом траектория вычислений содержит число 12 и не содержит числа 14?
'''
def F(a, b):
    if a >= b or a == 14:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a*3, b)


print(F(1, 12) * F(12, 40))
'''

'''
def F(a, b):
    if a > b or a == 14:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a*3, b)

print(F(1, 12) * F(12, 40))
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
