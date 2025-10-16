# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80  # (x ∈ B)
    return (x % A == 0) or (B <= (x % 22 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 23755 Демоверсия 2026 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

RES = []
M = [x / 4 for x in range(15 * 4, 130 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''


# № 20961 (Уровень: Базовый)
# (М. Попков) На числовой прямой даны два отрезка: P=[15;142] и Q=[38;167].
# Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
# ¬((x∈Q)→((¬(x∈A)∧(x∈P))→¬(x∈Q)))
# ложно (т.е. принимает значение 0) при любом значении переменной x.

'''
def F(x, a1, a2):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2
    return P <= not((Q <= (A and P)) <= not(Q))

RES = []
M = [x / 4 for x in range(5 * 4, 175 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) == False for x in M):
            RES.append(a2 - a1)
print(min(RES))

'''


# № 21902 Открытый вариант 2025 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + F(n + 2)

print(F(82) - F(81))
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
# RecursionError: maximum recursion depth exceeded
'''


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print((F(2024) // 4 + F(2023)) // F(2022))

# print((F(2024) / 4 + F(2023)) / F(2022))
#           ~~~~~^~~
# OverflowError: integer division result too large for a float
'''


# № 23756 Демоверсия 2026 (Уровень: Базовый)
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

# 23562
'''
import sys

sys.setrecursionlimit(10 ** 8)

def F(n):
    return G(n - 1)

def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 2) + 1


print(F(47995))
'''


# 23375
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return G(n - 1) + G(n - 3)

def G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return G(n - 4) + 2

print(F(42999))
'''

# 21979
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 110:
        return n
    if n >= 110:
        return (n - 7) * F(n - 8)
print((F(74914) - F(74898)) / (16 * F(74890)))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15]
# КЕГЭ = []
# на следующем уроке: 16, 23, 19-21
