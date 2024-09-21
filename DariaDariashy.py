# region Домашка: ******************************************************************

'''
from turtle import *
screensize(-5000, 5000)
tracer(0)
lt(90)
l = 20

for i in range(3):
    fd(7 * l)
    rt(90)
    fd(12 *l)
    rt(90)
up()
fd(4 * l)
rt(90)
fd(6 * l)
lt(90)
down()
for i in range(4):
    fd(83 * l)
    rt(90)
    fd(77 * l)
    rt(90)
up()
for x in range(-100, 50):
    for y in range(-70, 50):
        goto(x * l, y * l)
        dot(3, 'red')
update()
done()
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
'''


# Тип 16 №4645
'''
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return F(n-1) * n + F(n - 2) * (n - 1)


print(F(5))
'''

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 7:
        return 7
    if n >= 7:
        return 2 * n + F(n-1)


print(F(2024) - F(2022))

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2024) = 2 * 2024 + F(2023)
# F(2023) = 2 * 2023 + F(2022) - F(2022)
print(2 * 2024 + 2 * 2023)
'''


# № 4739 (Уровень: Средний)
'''
import sys
from functools import *
sys.setrecursionlimit(20000)

@lru_cache(None)
def F(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return F(n + 1) + F(n + 2)


print(F(12345) * ((F(10) - F(12)) / F(11)) + F(10101))
'''

'''
def F(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return F(n + 1) + F(n + 2)


print(F(12345) * 1 + F(10101))
# F(10) = F(11) + F(12)
# print(F(12345) * ((F(10) - F(12)) / F(11)) + F(10101))
'''

# div - //
# mod - %


# Тип 16 №38950
'''
def F(n):
    if n == 0:
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


# Тип 16 №4656
'''
def F(n):
    if n == 1:
        return 0
    if n > 1:
        return F(n - 1)

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return G(n - 1) * n


print(F(5) + G(5))
'''


# Тип 23 №59728
# У исполнителя есть три команды, которым присвоены номера.
# 1. Прибавить 1.
# 2. Прибавить 2.
# 3. Умножить на 3.
#
# Сколько существует программ, для которых при исходном числе 3
# результатом является число 18 и при этом траектория вычислений
# содержит число 8, но не содержит число 13?

def F(a, b):   # a - start, b - stop
    if a > b or a == 13:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)


print(F(3, 8) * F(8, 18))


def F(a, b):   # a - start, b - stop
    if a >= b or a == 13:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)


print(F(3, 8) * F(8, 18))


print(True + True + False + True)  # 3


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
