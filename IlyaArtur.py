# region Домашка: ******************************************************************

# № 7846 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))


R = []
M = [x / 4 for x in range(10 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(int(max(R)))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/51f79716-aac8-4ddc-b6b0-3c0c0df2aafe
'''
from fnmatch import *
for x in range(183, 10**9, 183):
    if fnmatch(str(x), '??287*139'):
        print(x, x // 183)
'''

# https://education.yandex.ru/ege/task/83afed62-b003-45be-b7f8-a004109ff15a
'''
from fnmatch import *
for x in range(11071, 10**10, 11071):
    if fnmatch(str(x), '?136*1'):
        if str(x)[0] in '13579':
            if str(x)[-2] in '02468':
                print(x, x // 11071)
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


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(100_000_000))

print(time.time() - start)  # 2.87503 -> 0.00057
'''


# https://education.yandex.ru/ege/task/f057cfef-606b-4010-8258-037b3517a524
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


k = 0
for x in range(424_242+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 2024 == 42:  # M при делении на 2024 даёт в остатке 42
            print(x, M)
            k += 1
            if k == 8:
                break
'''


# https://education.yandex.ru/ege/task/9c37aa6f-004c-432b-a955-f2a55df1f675

def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(397438, 443520+1):
    d = [j for j in divisors(x) if j % 2 == 0]
    if len(d) >= 142:
        print(len(d), max(d))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
