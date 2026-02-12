# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# todo глянуть новый 15 номер статград январь
'''
def F(x, y, A):
    return (y < A) and (x < A) or (89_241 - 5*y)

for A in range(0, 10000):
    if all(F(89_241 - 5*y, y, A) for y in range(100000)):
        print(A)
        break
'''



# Статград вариант 1 (27.01.26) номер 16
'''
F = [0] * 1000
G = [0] * 400_000

for n in range(400_000-1, -1, -1):
    if n >= 384_242:
        G[n] = n / 4 + 18
    if n < 384_242:
        G[n] = 12 + G[n + 41]

for n in range(0, 1000):  # 0, 999
    if n >= 20:
        F[n] = F[n - 4] + 4620
    if n < 20:
        F[n] = 8 * (G[n - 12] - 21)

print(F[913])
'''

'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 20:
        return F(n - 4) + 4620
    if n < 20:
        return 8 * (G(n - 12) - 21)

@lru_cache(None)
def G(n):
    if n >= 384_242:
        return n / 4 + 18
    if n < 384_242:
        return 12 + G(n + 41)

for n in range(400_000-1, -1, -1):
    G(n)

for n in range(1, 1000):
    F(n)

print(F(913))
'''

# G(n + 41)
# G(100) -> G(141) -> G(182)
# for n in range(400_000-1, -1, -1):

# G(n - 40)
# G(100) -> G(60) -> G(20)
# for n in range(1, 400_000):



# № 9846 Основная волна 27.06.23 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**8, найдите все числа, соответствующие маске 12*34?5,
# делящиеся на 2025 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им результаты деления этих чисел на 2025.
# Количество строк в таблице для ответа избыточно.
'''
from fnmatch import *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)

from re import *
for x in range(2025, 10**8, 2025):
    if fullmatch('12[0-9]*34[0-9]5', str(x)):
        print(x, x // 2025)
'''


# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

# print([x for x in range(100) if is_prime(x)])
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

from fnmatch import *
for x in range(1, 10**7):
    if fnmatch(str(x), '3?1111*'):
        if is_prime(x):
            print(x)
'''


# № 11814 (Уровень: Средний)
'''
from re import *
for x in range(1777, 10**10, 1777):
    if fullmatch('21[0-9][0-9][0-9]68[0-9]79', str(x)):
        print(x, x // 1777)
'''

# № 11955 (Уровень: Средний)
'''
from re import *
for x in range(133, 10**10, 133):
    if fullmatch('1[02468]2157[13579]*4', str(x)):
        print(x, x // 133)
'''

# № 13832 (Уровень: Средний)
'''
from re import *
for x in range(7777, 10**9, 7777):
    if fullmatch('[02468][13579][02468][02468][13579][02468][13579]77', str(x)):
        print(x, x // 7777)
'''


# № 14437 (Уровень: Средний)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(700_000-1, -1, -1):
    d = divisors(x)
    if len(d) > 0:
        M = int(sum(d) / len(d))
        if M % 1000 == 313:
            print(x, M)
            cnt += 1
            if cnt == 7:
                break
'''


# № 21980 (Уровень: Средний)
'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(750_000-1, -1, -1):
    d = [j for j in divisors(x) if is_prime(j) and j % 10 == 7]
    if len(d) > 0:
        F = int(sum(d) / len(d))
        if F != 0 and F % 111 == 0:
            print(x, F)
            cnt += 1
            if cnt == 5:
                break
'''

# Вариант 2
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(750_000-1, -1, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0 and j % 10 == 7]
    if len(d) > 0:
        F = int(sum(d) / len(d))
        if F != 0 and F % 111 == 0:
            print(x, F)
            cnt += 1
            if cnt == 5:
                break
'''


# № 23569 Пересдача 03.07.25 (Уровень: Средний)

def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            if is_prime(j) and is_prime(x // j):
                if str(j).count('6') == 1 and str(x//j).count('6') == 1:
                    d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(6_086_055+1, 10**10):
    d = divisors(x)
    if len(d) > 0:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [7, 11, 25]
# на следующем уроке:
# Разбирать задачи 24 номера по типу арифметика и символ X 80 раз (как 51993 решу егэ)
