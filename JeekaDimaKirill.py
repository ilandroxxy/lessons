# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 25354 ЕГКР 13.12.25 (Уровень: Средний)
'''
def F(x, y, A):
    return (78125 != y + 4*x) or (A > x) and (A > y)

for A in range(0, 100000):
    if all(F(x, 78125 - 4*x, A) for x in range(1, 20000)):
        print(A)
        break
'''


# № 19255 ЕГКР 21.12.24 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# 1) символ «?» означает ровно одну произвольную цифру;
# 2) символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**10, найдите все числа,
# соответствующие маске 54?1?3*7, делящиеся на 18579 без остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – соответствующие им результаты деления этих чисел на 18579.
'''
from fnmatch import *
for x in range(18579, 10**10, 18579):
    if fnmatch(str(x), '54?1?3*7'):
        print(x, x // 18579)

from re import *
for x in range(18579, 10**10, 18579):
    if fullmatch('54[0-9]1[0-9]3[0-9]+7', str(x)):
        print(x, x // 18579)
'''


'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

# [1, 2, 3, 4 | 24 // 4, 24 // 3, 24 // 2, 24 // 1]
print(divisors(24))
'''


# № 25362 ЕГКР 13.12.25 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            d += [j, x//j]
    return sorted(set(d))

cnt = 0
for x in range(1350050+1, 10**10):
    d = [j for j in divisors(x) if j % 100 == 11 and j != x and j != 11]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# № 26556 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5) + 1):  #  не считая самого числа
        if x % j == 0:
            d += [j, x//j]
    return sorted(set(d))

cnt = 0
for x in range(5_700_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        M = min(d) + max(d)
        if M > 70_000 and (M ** 0.5) == int(M ** 0.5):
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 23763 Демоверсия 2026 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5) + 1):  #  не считая самого числа
        if x % j == 0:
            d += [j, x//j]
    return sorted(set(d))

cnt = 0
for x in range(800_000+1, 10**10):
    d = divisors(x)
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 21980 (Уровень: Средний)

def divisors(x):
    d = []
    for j in range(2, int(x**0.5) + 1):  #  не считая самого числа
        if x % j == 0:
            d += [j, x//j]
    return sorted(set(d))

cnt = 0
for x in range(750_000-1, -1, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0 and j % 10 == 7]
    if len(d) > 0:
        F = int(sum(d) / len(d))
        if F % 111 == 0:
            print(x, F)
            cnt += 1
            if cnt == 5:
                break


# endregion Урок: *************************************************************
#
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 12, 27
