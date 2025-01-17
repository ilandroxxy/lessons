# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):  # a - start, b - stop
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2, b) + F(a + 3, b)


print(F(5, 7) * F(7, 11))

# Вариант 2
def F(a, b):  # a - start, b - stop
    if a >= b:
        return a == b
    return F(a + 1, b) + F(a + 2, b) + F(a + 3, b)


print(F(5, 7) * F(7, 11))
'''


# № 18146 (Уровень: Базовый)
# У исполнителя есть две команды, которые обозначены латинскими буквами:
# A. Вычти 3
# B. Найди целую часть от деления на 3
# С. Найди целую часть от деления на 2

# Сколько существует программ, для которых при исходном числе 46 результатом является число 3
# и при этом траектория вычислений содержит число 20 и не содержит числа 28?
'''
def F(a, b):
    if a <= b or a == 28:
        return a == b
    return F(a-3, b) + F(a//3, b) + F(a//2, b)


print(F(46, 20) * F(20, 3))
'''


# № 1199 Апробация 27.04 (Уровень: Базовый)
'''
def F(n):
    if n <= 1:  # F(n)=1 при n≤1
        return 1
    if n > 1 and n % 2 == 0:
        return 3*n + F(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * F(n - 2)

print(F(31))
'''

'''
def F(n):
    if n == 0:
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


# № 7595 Досрочная волна 2023 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n + 3)

print(F(23) - F(21))
'''


#
# № 7618 Досрочная волна 2023 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + F(n + 2)

print(F(2022) - F(2023))
'''

# № 15331 Досрочная волна 2024 (Уровень: Базовый)
'''
# import sys
# sys.setrecursionlimit(10000)

from sys import *
setrecursionlimit(10000)


def F(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + F(n - 1)


print(F(2024) - F(2020))
# RecursionError: maximum recursion depth exceeded
'''


#
# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
import sys
from functools import *
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n / 2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)


for i in range(5000):
    F(i)

print(F(4952) + 2 * F(4958) + F(4964))
'''

import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * F(n - 4)

print((F(13766) - 9 * F(13762)) / F(13758))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 16, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]
