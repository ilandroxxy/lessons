# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# F(12 345) × (F(10)−F(12))/F(11) + F(10 101)?

# F(10) = F(11) + F(12)
# F(12 345) × (F(11) + F(12)−F(12))/F(11) + F(10 101)?
# F(12 345) × 1 + F(10 101)?


'''
from fnmatch import *
for x in range(9117, 10**9, 9117):
    if fnmatch(str(x), '4*64*9?7'):
        print(x)
'''

# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
'''
from fnmatch import *

def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

for x in range(10**7):
    if fnmatch(str(x), '3?1111*'):
        if is_prime(x):
            print(x)
'''


'''
import time
start = time.time()
# def divisors(x):
#     div = []
#     for j in range(1, x+1):
#         if x % j == 0:
#             div.append(j)
#     return div

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


print(divisors(100_000_000))

print(time.time() - start)  # 2.85726022  -> 0.0003621
'''


'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


cnt = 0
for x in range(460_000_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 5:
        M = d[-5]
        if M > 0:
            print(M)
            cnt += 1
            if cnt == 5:
                break
'''

# Тип 25 №35483
# Найдите все натуральные числа, принадлежащие отрезку
# [35000000; 40000000], у которых ровно пять
# различных нечётных делителей (количество чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(35_000_000, 40_000_000+1):
    d = [j for j in divisors(x) if j % 2 != 0]
    if len(d) == 5:
        print(x)
'''


# Тип 25 №33104
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(289123456, 389123456+1):
    # if (x ** 0.5) == int(x ** 0.5):
    if (x ** 0.5).is_integer():
        d = divisors(x)
        if len(d) == 3:
            print(x, max(d))

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Решить и поправить Степик № 11953 (Уровень: Средний) +++

from functools import lru_cache


@lru_cache(None)
def F(a, b):

    if a >= b or a == 100:
        return a == b

    count = 0

    x = a % 10  # Команда A: Прибавить последнюю цифру
    if x != 0:
        count += F(a + x, b)

    x = a % 68   # Команда B: Добавить остаток от деления на 68
    if x != 0:
        count += F(a + x, b)

    x = a ** 2   # Команда C: Возвести в квадрат
    if x != a:
        count += F(x, b)

    return count


print(F(2, 68) * F(68, 680))

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14, 15, 16, 17, 19-21?, 23, 25]
# КЕГЭ = []
# на следующем уроке:
