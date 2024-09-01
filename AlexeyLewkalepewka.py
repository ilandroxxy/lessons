# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


def prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r
'''


# Тип 16 №6459
'''
def F(n):
    if n <= 2:
        return 2
    if n > 2:
        return 3 * F(n - 1) - F(n - 2)

print(F(6))
'''

'''
def F(n):
    if n <= 1:
        return 0
    if n > 1 and n % 2 != 0:
        return F(n - 1) + 3*n**2
    if n > 1 and n % 2 == 0:
        return n / 2 + F(n - 1) + 2

print(F(49))
'''


# Тип 16 №59721
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return n
    if n > 1:
        return n - 1 + F(n - 1)


print(F(2024) - F(2022))

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2024) = 2023 + F(2023)
# F(2023) = 2022 + F(2022) - F(2022)
print(2023 + 2022)
'''


# № 4739 (Уровень: Средний)
'''
from functools import *
import sys

sys.setrecursionlimit(100000)
@lru_cache(None)
def F(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return F(n + 1) + F(n + 2)

print(F(12345) * (1) + F(10101))
'''
# F(10) = F(11) / F(11) = 1


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):  # a - начало + траектория, b - конец
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))


def F(a, b):  # a - начало + траектория, b - конец
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))
'''


# № 17877 Демоверсия 2025 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a-2, b) + F(a//2, b)

print(F(38, 16) * F(16, 2))
'''

'''
from functools import *

my_set = set()

@lru_cache(None)
def F(a, c):
    if c == 68:
        my_set.add(a)
        return 0
    else:
        return F(a+3, c+1) + F(a-2, c+1)


F(1, 0)
print(len(my_set))
'''


# № 10027 (Уровень: Базовый)
'''
def F(a, b, c: str):
    if a >= b:
        return a == b and c[0] != 'C'
    return F(a+2, b, c+'A') + F(a+3, b, c+'B') + F(a*2, b, c+'C')

print(F(5, 30, ''))
'''


#  7623 Досрочная волна 2023 (Уровень: Базовый)
# У исполнителя есть три команды, которым обозначены латинскими буквами:
# A. Прибавить 1
# B. Умножить на 2
# C. Умножить на 3
#
# Сколько существует программ, для которых при исходном числе
# 2 результатом является число 25, и при этом траектория вычислений содержит число 15, но не содержит число 11?
'''
def F(a, b):
    if a >= b or a == 11:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a*3, b)


print(F(2, 15) * F(15, 25))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:

