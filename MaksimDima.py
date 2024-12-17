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
        return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))


# Вариант 2
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))
'''


# № 18047 (Уровень: Базовый)
# А. Вычесть 2
# В. Вычесть 3
# С. Найти целую часть от деления на 4
# Сколько существует программ, для которых при исходном
# числе 36 результатом является число 13,
# при этом траектория вычислений не содержит числа 24?
'''
def F(a, b):
    if a <= b or a == 24:
        return a == b
    return F(a-2, b) + F(a-3, b) + F(a//4, b)


print(F(36, 13))
'''

#
# № 18267 (Уровень: Средний)
# А. Прибавить 2
# В. Прибавить 5
# С. Возвести в квадрат
# Сколько существует программ, для которых при исходном числе 4
# результатом является число 36, при этом последняя в них команда — не C?
'''
def F(a, b, c):
    if a >= b:
        # return a == b and c != 'C'
        return a == b and c in 'AB'
    return F(a+2, b, 'A') + F(a+5, b, 'B') + F(a**2, b, 'C')


print(F(4, 36, ''))

# Вариант 2
def F(a, b, c):
    if a >= b:
        return a == b and c[-1] != 'C'
    return F(a+2, b, c+'A') + F(a+5, b, c+'B') + F(a**2, b, c+'C')


print(F(4, 36, ''))
'''

# Задача статград 12.03.2024
'''
def F(a, b, c):
    if a >= b:
        M = [x for x in c if x in '02468']
        return a == b and len(M) <= 4
    return F(a+1, b, c+str(a)) + F(a*2, b, c+str(a))


print(F(1, 17, ''))  # 8


def F(a, b, c):
    if a >= b:
        M = [int(x) for x in c.split() if int(x) % 2 == 0]
        return a == b and len(M) <= 4
    return F(a+1, b, c+' '+str(a)) + F(a*2, b, c+' '+str(a))


print(F(1, 17, ''))  # 8
'''


# № 610 (Уровень: Базовый)
'''
def F(n):
    if n < 5:
        return 1 + 2*n
    if n >= 5 and n % 3 == 0:
        return 2 * (n+1) * F(n-2)
    if n >= 5 and n % 3 != 0:
        return 2*n + 1 + F(n-1) + 2*F(n-2)


print(F(15))
'''


# № 1021
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

# F(2023) = 2023 * F(2022)
# F(2022) = 2022 * F(2021)
# F(2021) = 2021 * F(2020) / F(2020)
print(2023 * 2022 * 2021)
'''


# № 4739 (Уровень: Средний)
'''
from functools import *
import sys
sys.setrecursionlimit(1000000)

@lru_cache(None)
def F(n):
    if n > 10_000:
        return n - 10_000
    if 1 <= n <= 10_000:
        return F(n + 1) + F(n + 2)


print(F(12345 * ((F(10) - F(12)) / F(11))) + F(10101))
print(F(12345) + F(10101))
'''


# № 12470 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 3:
        return n
    if n > 2 and n % 2 != 0:
        return F(n - 1) + F(n - 2) + 1
    if n > 2 and n % 2 == 0:
        return sum(F(i) for i in range(1, n))

print(F(38))  # 9182657279
'''


# № 17529 Основная волна 07.06.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print((2 * F(2024) + F(2023)) / F(2022))
'''


# № 17557 Основная волна 08.06.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)


print((F(2024) // 16 - F(2023)) / F(2022))
# print((F(2024) / 16 - F(2023)) / F(2022))
#        ~~~~~~~~^~~~
# OverflowError: integer division result too large for a float
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 12, 13, 14, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
