# region Домашка: ******************************************************************

'''
cnt = 0
for x in range(320400+1, 10**9):
    if all(x % p == 0 for p in [10, 12, 14, 16, 18]):
        print(x, x // 18)
        cnt += 1
        if cnt == 5:
            break
'''

'''
from fnmatch import *
R = []
for x in range(0, 10**10, 11071):
    if fnmatch(str(x), '?136*1'):
        if str(x)[0] in '13579' and str(x)[-2] in '02468':
            R.append([x, x//11071])

print(*R[-5])
print(*R[-4])
print(*R[-3])
print(*R[-2])
print(*R[-1])
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 16 №5362
'''
def F(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return 2 * F(n - 1) + F(n - 2)

print(F(4))
'''


# Тип 16 №59841
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 7:
        return 7
    if n >= 7:
        return 2*n + F(n - 1)

print(F(2024) - F(2022))  # 8094
'''
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# Тип 16 №38591
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


# Тип 16 №39245
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)


cnt = 0
for n in range(1, 900+1):
    if F(n) == 9:
        cnt += 1
print(cnt)
'''


# КЕГЭ № 8474 (Уровень: Базовый)
#
# (В. Рыбальченко) Алгоритм вычисления функции F(n), где n – целое число, задан следующими соотношениями:
#
# F(n) = n + 1, при n > 3456;
# F(n) = F(n + 1) + F(n + 2), при n ≤ 3456 и кратном трем;
# F(n) = F(n + n mod 3) + 2, при n ≤ 3456 и не кратном трем;
#
# Определите значение выражения F(12) – F(17).
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n > 3456:
        return n + 1
    if n <= 3456 and n % 3 == 0:
        return F(n + 1) + F(n + 2)
    if n <= 3456 and n % 3 != 0:
        return F(n + n % 3) + 2

print(F(12) - F(17))
'''


# № 7655 Вариант от ChatGPT (Уровень: Средний)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 2025:
        return n**2
    if 2025 <= n < 2050:
        return 2 * F(n - 1) - F(n - 2) + n
    if 2050 <= n <= 2100:
        return F(n - 1) + 2 * F(n - 2) + 3 * F(n - 3)
    if n > 2100:
        return 2 * F(n - 1) + F(n - 2) + n

print(str(F(2020) + F(2200))[-7:])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 25]
# КЕГЭ  = []
# на следующем уроке:
