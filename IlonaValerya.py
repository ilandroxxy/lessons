# region Домашка: ******************************************************************
from wheel.metadata import requires_to_requires_dist


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 16 №4656
'''
from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n == 1:
        return 0  # F(1) = 0
    if n > 1:
        return F(n - 1) + n

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return G(n - 1) * n

for n in range(500):
    F(n)

print(F(500) + G(5))
'''


# Тип 15 №59693
'''
def F(x, y, A):
    return (x < A) or (y < A) or (x + 2 * y > 50)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break

# Вариант 2
print(min([A for A in range(1, 1000) if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100))]))
'''

# Тип 15 №69893
'''
def F(x, A):
    return ((x % 2 == 0) <= (x % 5 != 0)) or (x + A >= 70)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

# Тип 15 №34518
'''
def F(x, A):
    return (x & A != 0) <= ((x & 36 == 0) <= (x & 6 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# Тип 15 №34542
'''
def F(x, a1, a2):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P <= (not Q)) <= (not A)


R = []
M = [x / 5 for x in range(1 * 5, 70 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))  # 15.6 -> 16
'''

# Тип 23 №18801
# 1. Прибавить 1.
# 2. Умножить на 3.
# 3. Прибавить 2.
# Сколько существует программ, которые преобразуют исходное число 2 в число 12
# и при этом траектория вычислений содержит числа 9 и 11?
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a*3, b) + F(a+2, b)


print(F(2, 9) * F(9, 11) * F(11, 12))

# Вариант 2
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a*3, b) + F(a+2, b)


print(F(2, 9) * F(9, 11) * F(11, 12))
'''


# Тип 23 №68256
'''
def F(a, b):
    if a <= b or a == 15 or a == 12:
        return a == b
    summa = 0
    summa += F(a-1, b)
    if a % 2 == 0:
        summa += F(a//2, b)
    if a % 3 == 0:
        summa += F(a//3, b)
    return summa


print(F(19, 1))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
