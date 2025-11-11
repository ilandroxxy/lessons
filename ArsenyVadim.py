# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 21718 ЕГКР 19.04.25 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(7993, 10**10, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x, x // 7993)

from re import *
for x in range(7993, 10**10, 7993):
    if fullmatch('4[0-9]*4736[0-9]*1', str(x)):
        print(x, x // 7993)
'''


# Универсальная функция поиска делителей числа
'''
import time
start = time.time()

def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(1_000_000_000))

end = time.time()
print(end - start)  # 19.590 -> 0.0007
'''


# Поиск простых чисел
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

print([x for x in range(1, 100) if len(divisors(x)) == 2])
print([x for x in range(1, 100) if len(divisors(x)) > 2])

def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

print([x for x in range(1, 100) if is_prime(x)])
print([x for x in range(1, 100) if not is_prime(x)])
'''

# № 21909 Открытый вариант 2025 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):  
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(500_000+1, 10**10):
    d = divisors(x)
    R = sum(d)
    if R % 10 == 6:
        print(x, R)
        cnt += 1
        if cnt == 5:
            break
'''


# № 21422 Досрочная волна 2025 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(1_125_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 7 and j != 7 and j != x]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# № 20814 Апробация 05.03.25 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(500_000+1, 10**10):
    d = divisors(x)
    R = sum(d)
    if R % 10 == 9:
        print(x, R)
        cnt += 1
        if cnt == 5:
            break
'''


# № 23569 Пересдача 03.07.25 (Уровень: Средний)
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
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            if is_prime(j) and is_prime(x // j):
                if str(j).count('6') == 1 and str(x // j).count('6') == 1:
                    d += [j, x // j]
    return sorted(d)

cnt = 0
for x in range(6_086_055+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break
'''


# № Демоверсия 2025 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(800_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 19778(Уровень: Средний)
'''
def divisors(x):
    d = []
    for j in range(1, int(x ** 0.5) + 1):  # не считая единицы и самого числа.
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

cnt = 0
for i in range(9_500_000+1, 10**8):
    p = [i for i in divisors(i) if prime(i)]
    if len(p) > 0:
        f = sum(p) // len(p)
        if f != 0 and f % 813 == 0:
            print(i, f)
            cnt += 1
            if cnt == 5:
                break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
