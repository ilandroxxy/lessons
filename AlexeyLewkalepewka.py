# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 16389 ЕГКР 27.04.24 (Уровень: Базовый)
# Среди натуральных чисел, не превышающих 10**10,
# найдите все числа, соответствующие маске 5?2*3?3?,
# делящиеся на 98591 без остатка.
'''
from fnmatch import *
for x in range(98591, 10**10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x, x // 98591)
'''

# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
# Среди натуральных чисел, не превышающих 10**7,
# найдите все простые числа, соответствующие маске 3?1111*.
'''
def prime(x):
    if x == 1:
        return False
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return False
    return True


# print([i for i in range(1, 100) if prime(i)])


from fnmatch import *
for x in range(10**7):
    if fnmatch(str(x), '3?1111*'):
        if prime(x):
            print(x)
'''


# Тип 25 №46983
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # без учёта самого числа и единицы.
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


cnt = 0
for x in range(460_000_000+1, 10**100):
    d = divisors(x)
    if len(d) >= 5:
        M = d[-5]
        print(M)
        cnt += 1
        if cnt == 5:
            break
'''

# Тип 25 №28122
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [489421; 489440],
# числа, имеющие ровно четыре различных натуральных делителя.
# Для каждого найденного числа запишите эти четыре делителя в четыре
# соседних столбца на экране с новой строки.
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1): 
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


for x in range(489421, 489440+1):
    d = divisors(x)
    if len(d) == 4:
        print(*d)
'''


# Тип 25 №37130
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # но не равное 7 и самому числу
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


cnt = 0
for x in range(600_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 7 and j != 7]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Тип 25 №27858
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [120115; 120200], число, имеющее максимальное количество
# различных натуральных делителей, если таких чисел несколько — найдите
# максимальное из них.
# Выведите на экран количество делителей такого числа и само число.
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


# maxi = 0
# for x in range(120115, 120200+1):
#     d = divisors(x)
#     if len(d) >= maxi:
#         maxi = len(d)
#         print(maxi, x)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:

