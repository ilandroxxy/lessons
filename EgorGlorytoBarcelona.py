# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 2387 (Уровень: Базовый)
'''
def F(n):
    if n <= 2:  # F(n)=1 при n≤2
        return 1
    if n > 2:
        return F(n - 1) + 2 * F(n - 2)

print(F(17))
'''


# № 2248 (Уровень: Сложный)
'''
def F(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + F(n / 3)
    if n > 1 and n % 3 != 0:
        return n + F(n + 3)


for n in range(1, 100):
    try:
        if F(n) > 100:
            print(n)
            break
    except RecursionError:
        continue
'''


# № 2237 (Уровень: Средний)
'''
def F(n):
    if n == 0:  # F(0)=0
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

cnt = 0
for n in range(1, 500+1):
    if F(n) == 8:
        cnt += 1
print(cnt)
'''


# № 4704 Демоверсия 2023 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print(F(2023) / F(2020))
# RecursionError: maximum recursion depth exceeded


# Решаем номер письменно:
# F(2023) = 2023 * F(2022)
# F(2022) = 2022 * F(2021)
# F(2021) = 2021 * F(2020) / F(2020)

print(2023 * 2022 * 2021)
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
        return F(n+1) + F(n+2)


print(F(12345) * ((F(10) - F(12)) / F(11)) + F(10101))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 6, 8, 12, 13, 14, 16]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# 7/10 -> 43 вторичных баллов +[1, 4, 5, 10, 12, 13, 14] -[2, 6, 8]
