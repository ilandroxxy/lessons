# region Домашка: ******************************************************************

# № 7011 (Уровень: Средний) 🌶
'''
def f(a, b, c):
    if a >= b or a == 28:
        # print(a == b, 'BACA' not in c, c)
        return a == b and 'BACA' not in c
    return f(a + 2, b, c+'A') + f(a + 3, b, c+'B') + f(a * 2, b, c+'C')


print(f(2, 40, ''))
'''


# № 13099 (Уровень: Средний) 🌶
'''
def f(a, b, c):
    if a > b+1 or 'AA' in c:
        return 0  # 15 -> +1 -> 16 -> -1 -> 15
    elif a == b:
        return 1
    return f(a - 1, b, c+'A') + f(a * 2, b, c+'B') + f(a * 3, b, c+'C')


print(f(3, 15, ''))
'''


# № 11953 (Уровень: Средний)
'''
from functools import lru_cache

@lru_cache(None)
def F(a, b):
    if a >= b or a == 100:
        return a == b
    summa = 0
    if a % 10 != 0:
        summa += F(a + a % 10, b)
    if a % 68 != 0:
        summa += F(a + a % 68, b)
    if a ** 2 != a:
        summa += F(a ** 2, b)
    return summa


print(F(2, 68) * F(68, 680))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 12779 (Уровень: Средний)
'''
def F(n, x):
    if n >= 3000:
        return n
    if n < 3000:
        return n + x + F(n+2, x)


for x in range(-100, 100):
    if F(2984, x) - F(2988, x) == 5916:
        print(x)
'''


# № 11948 (Уровень: Средний)
'''
def F(n):
    return G(n - 1)

def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n - 2) + 1

cnt = 0
for n in range(1, 100+1):
    r = F(n)
    if r > 0:
        if (r ** 0.5).is_integer():
            cnt += 1
print(cnt)
'''


# 5! = 5 * 4 * 3 * 2 * 1
'''
from math import factorial
import sys
sys.setrecursionlimit(100000)

# def factorial(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res



def F(n):
    if n >= 5000:
        return factorial(n)
    if 1 <= n < 5000:
        return 2 * F(n + 1) // (n + 1)


print(1000 * F(7) // F(4))
'''

# № 928 Джобс 08.02.2021 (Уровень: Средний)
'''
def F(n):
    if n <= 3:
        return n + 3
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n
    if n > 3 and n % 2 != 0:
        return F(n - 2) + 2 * n


summa = 0
for n in range(40, 50+1):
    summa += F(n)
print(summa)
'''

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 14, 16, 23]
# на следующем уроке: Повторяем/разбираем 22


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
