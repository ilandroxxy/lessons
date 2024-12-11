# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

"""
import time
start = time.time()

'''
def divisors(x):
    div = []
    for j in range(1, x+1):
        if x % j == 0:
            div.append(j)
    return div
'''

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
            # div.append(j)
            # div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)  # 3.48028 -> 0.00048
"""


# Задание 25 https://education.yandex.ru/ege/task/d8b3bd78-66b1-48d6-9cd3-f34b0182e601
'''
def divisors(x):
    div = []
    # В качестве делителей не рассматривать числа 1 и исследуемое число.
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(135_790, 163_228+1):
    d = divisors(x)
    if sum(d) > 460_000:
        print(len(d), sum(d))
'''


# Задание 25 https://education.yandex.ru/ege/task/2f0244ec-e26c-4ebe-a8dd-7b32e94d30e4
# Поиск чисел с полными квадратами
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(10**7+1, 10**10):
    # d = [j for j in divisors(x) if (j**0.5) == int(j**0.5)]
    d = [j for j in divisors(x) if (j**0.5).is_integer()]
    if len(d) == 3:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Задание 25 https://education.yandex.ru/ege/task/2d62d9fd-a99a-4bef-a747-57a6ad2539d7
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(177000, 177300+1):
    if len(divisors(x)) == 0:
        summa = sum([int(i) for i in str(x)])
        if len(divisors(summa)) == 0:
            print(x, summa)
'''


# Задание 25 https://education.yandex.ru/ege/task/f057cfef-606b-4010-8258-037b3517a524
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(424_242+1, 10**10):  # большие 424 242
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 2024 == 42:
            print(x, M)
            cnt += 1
            if cnt == 8:
                break
'''


# Задание 25 https://education.yandex.ru/ege/task/d02f4351-acc7-4b66-9ca1-83d0d1887db7
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(700_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 7 and j != 7]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Тип 25 №29673
# Найдите все натуральные числа, принадлежащие отрезку [123_456_789; 223_456_789]
# и имеющие ровно три нетривиальных делителя. Для каждого найденного
# числа запишите в ответе его наибольший нетривиальный делитель.
# Ответы расположите в порядке возрастания.
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(123_456_789, 223_456_789+1):
    if (x**0.5).is_integer():
        d = divisors(x)
        if len(d) == 3:
            print(x, max(d))
'''


# Задание 25 https://education.yandex.ru/ege/task/2135bad3-5844-4cbd-8a72-93751f24130f
'''
from fnmatch import *
d = [14, 24, 34, 44, 54, 64, 74, 84, 94]
for x in range(124, 10**10, 124):
    if fnmatch(str(x), '1*28?64'):
        D = [j for j in d if x % j == 0]
        if len(D) == 5:
            print(x, x // 124)
'''


# https://education.yandex.ru/ege/task/08b93dc7-c401-48a3-9078-75af3fa2e240
'''
from fnmatch import *
for x in range(0, 10**8, 13):
    if fnmatch(str(x), '123*678'):
        print(x, x // 13)
'''


# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
'''
import time
start = time.time()

from fnmatch import *


def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(10**7):
    if fnmatch(str(x), '3?1111*'):
        if len(divisors(x)) == 0:
                print(x)


print(time.time() - start)  # 3.99135804
'''


# № 10725 (Уровень: Средний)
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(65_000+1, 10**10):
    if fnmatch(str(x), '6*97*5?'):
        d = [j for j in divisors(x) if j % 2 == 0]
        if len(d) >= 4:
            print(x, sum(d))
            cnt += 1
            if cnt == 7:
                break
'''


# № 7724 (Уровень: Базовый)
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(1018, 10**9, 1018):
    if x % 18 == 0:
        if fnmatch(str(x), '*18??18'):
            print(x, len(divisors(x)))
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
# ФИПИ = [5, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
