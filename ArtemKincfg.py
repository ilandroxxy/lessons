# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19255 ЕГКР 21.12.24 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(18579, 10**10, 18579):
    if fnmatch(str(x), '54?1?3*7'):
        print(x, x // 18579)
'''

# todo Разобрать № 19720 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(153, 10**8, 153):
    if fnmatch(str(x), '1*2?3*45'):
        if str(x)[-3] in '13579':
            print(x, x // 153)
'''


'''
import time
start = time.time()

# def divisors(n):
#     div = []
#     for j in range(1, n+1):
#         if n % j == 0:
#             div.append(j)
#     return div


def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


print(divisors(100_000_000))


print(time.time() - start)  # 2.8418760 -> 0.00032
'''


# № 19721 (Уровень: Базовый)
'''
def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


for n in range(178965, 178982+1):
    d = divisors(n)[::-1]
    if len(d) == 4:
        print(*d)
'''


# № 17879 Демоверсия 2025 (Уровень: Базовый)
'''
def divisors(n):
    div = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
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
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
