# region Домашка: ******************************************************************

# № 2356 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 10 <= x <= 45
    Q = 35 <= x <= 78
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)


R = []  # сюда будем складывать длины отрезков
M = [x / 4 for x in range(5 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) == False for x in M):
            R.append(a2 - a1)
print(round(min(R)))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/4c423ac1-ef41-4eba-b73c-f8f714df7cd5
'''
from fnmatch import *
for x in range(96437, 10**10, 96437):  # [0, 10**10)
    if fnmatch(str(x), '7?2*4??9?'):
        print(x, x // 96437)
'''


# https://education.yandex.ru/ege/task/83b21e05-822c-44b1-b785-f14418c83449
'''
from fnmatch import *
for x in range(42, 2*10**8, 42):
    if fnmatch(str(x), '?2*4*0'):
        if not fnmatch(str(x), '1*7*'):
            print(x, x // 42)
'''


# https://education.yandex.ru/ege/task/2135bad3-5844-4cbd-8a72-93751f24130f
'''
from fnmatch import *
for x in range(124, 10**10, 124):
    if fnmatch(str(x), '1*28?64'):
        divisors = [x % j == 0 for j in (14, 24, 34, 44, 54, 64, 74, 84, 94)]
        if sum(divisors) == 5:
            print(x, x // 124)
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


print(divisors(24))
print(divisors(100_000_000))

print(time.time() - start)  # 2.8512 -> 0.00033
'''


# https://education.yandex.ru/ege/task/26295a68-9546-4dd9-87ca-c8f32bd7a755
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(114578, 114616+1):
    d = [j for j in divisors(x) if j % 10 == 8]
    if len(d) > 0:
        R = sum(d)
        if R % 10 == 6:
            print(x, R)
'''


# https://education.yandex.ru/ege/task/ad067f91-26ed-4058-b28a-cb9fc3d92ac0
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(625681, 758641+1):
    d = [j for j in divisors(x) if j > 10]
    if len(d) == 7:
        print(x, d)
'''


# https://education.yandex.ru/ege/task/dc4c312e-1acd-406e-83a6-d4aac88cf80e
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


k = 0
for x in range(800_001, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            k += 1
            if k == 5:
                break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]
