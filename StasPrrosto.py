# region Домашка: ******************************************************************
'''
def divisors(x):
    diviz = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            diviz += [j, x // j]
    return sorted(set(diviz))

cnt = 0
for x in range(10**9+1, 10**11):
    if str(x) == str(x)[::-1]:
        div = divisors(x)
        if max(div) % 7 == 0:
            print(x, max(div))
            cnt += 1
            if cnt == 5:
                break


def divisors(x):
    diviz = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            diviz += [j, x // j]
    return sorted(set(diviz))

cnt = 0
for x in range(10**9, 10**11):
    div = [i for i in divisors(x)]
    if x == int(str(x)[::-1]):
        if max(div) % 7 == 0:
            print(x, max(div))
            cnt += 1
            if cnt == 5:
                break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
print(x, y, z, ...)
range(start, stop, step)
max(x, y, z, ...)
len(x: list)
'''


a, b, c = 1, 2, 3
M = [1, 2, 3]

'''
print(max(M), max(a, b, c))  # 3 3
print(sum(M), sum(a, b, c))  # 6 ошибка
'''

'''
def my_sum(*args):
    print(type(args), args)
    return sum(args)


print(my_sum(a, b, c))
'''


# Базовые самописные функции для ЕГЭ
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


div = divisors(24)
print(div)   # [1, 2, 3, 4, 6, 8, 12, 24]

def prime(x):
    if x == 1:
        return False
    for j in range(2, int(x ** 0.5)+1):
        if x % j == 0:
            return False
    return True


print([x for x in range(1, 100) if prime(x)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res

print(convert(8, 2))  # 1000
'''


# Тип 16 №4978
'''
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return F(n - 2) * (n - 1)


print(F(8))  # 105
'''

# Тип 16 №59841
# Задан алгоритм вычисления функции F(n), где n — натуральное число:
#
# F(n)=7, при n<7;
# F(n)=2n+F(n−1), если n≥7.
#
# Чему равно значение функции F(2024)−F(2022)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 7:
        return 7
    if n >= 7:
        return 2*n + F(n-1)

print(F(2024) - F(2022))
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2024) = 4048 + F(2023)
# F(2023) = 4046 + F(2022) - F(2022)
'''
# Ответ: 8094


# Тип 16 №36871
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n > 0 and n % 2 != 0:
        return 1 + F(n - 1)


cnt = 0
for n in range(1, 1000+1):
    try:
        if F(n) == 3:
            cnt += 1
    except Exception as e:
        continue
print(cnt)
'''

'''
a = int(input())
b = int(input())
try:
    print(a / b)
except Exception as e:
    print(e)
# except ZeroDivisionError:
#     print('Деление на нуль запрещено.')
'''


# № 10718 (Уровень: Средний)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * F(n-2) - F(n-1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * F(n-1) + F(n-2) - 2

print(F(170))  # 3596910688800
'''


# todo Разобраться задачу https://stepik.org/lesson/1228671/step/9?unit=1242204

# F(n) = n, если n > 1000000;
#  F(n) = n + F(2n), если n ≤ 1000000;
#  G(n) = F(n) / n.
# Сколько существует таких натуральных чисел n (включая число 1000), для которых G(n)=G(2000)?

from sys import *
from functools import *
setrecursionlimit(100000000)
@lru_cache(None)
def F(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + F(2*n)

@lru_cache(None)
def G(n):
    return F(n)/n

cnt = 0
x = G(2000)
for n in range(10**8):
    if G(n) == x:
        cnt += 1
        print(cnt)


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
