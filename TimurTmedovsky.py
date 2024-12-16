# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 16 https://education.yandex.ru/ege/task/c29d8526-670e-420f-b570-bf389148e7e4
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n + 3)


print(F(23) - F(21))
'''


# 16 https://education.yandex.ru/ege/task/e6698118-3eea-44a7-9649-652cc0eb183a
'''
# RecursionError: maximum recursion depth exceeded
import sys
sys.setrecursionlimit(1000)

def F(n):
    if n <= 1:
        return 0
    if n > 1 and n % 6 == 0:
        return n + F(n/6 - 2)
    if n > 1 and n % 6 != 0:
        return n + F(n + 6)


for n in range(1000, 10000):
    try:
        if F(n) > 4242:
            print(n)
            break
    except RecursionError:
        continue
'''


# 16 https://education.yandex.ru/ege/task/f1c6d72d-9c1f-4bc9-bece-8ff2447f219d
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n >= 10000:
        return 1
    if n < 10000 and n % 2 == 0:
        return F(n + 3) + 7
    if n < 10000 and n % 2 != 0:
        return F(n + 1) - 3


print(F(50) - F(57))
# RecursionError: maximum recursion depth exceeded
'''


# № 18931 Новогодний вариант 2025
'''
from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n/2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)


print(F(4952) + 2 * F(4958) + F(4964))
'''


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
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



#
# № 18047 (Уровень: Базовый)
# А. Вычесть 2
# В. Вычесть 3
# С. Найти целую часть от деления на 4
# Сколько существует программ, для которых при исходном числе 36
# результатом является число 13, при этом траектория
# вычислений не содержит числа 24?

'''
def F(a, b):
    if a < b or a == 24:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-2, b) + F(a-3, b) + F(a//4, b)


print(F(36, 13))

# Вариант 2
def F(a, b):
    if a <= b or a == 24:
        return a == b
    return F(a-2, b) + F(a-3, b) + F(a//4, b)


print(F(36, 13))
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
