# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19723 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(451, 10**9, 451):
    if fnmatch(str(x), '10?451*3'):
        print(x, x // 451)
'''


# № 20288 (Уровень: Средний)
'''
from fnmatch import *
for x in range(9231, 10**10, 9231):
    if fnmatch(str(x), '*12?4?'):
        if str(x)[-3] in '13579' and str(x)[-1] in '13579':
            r = str(x)[:-5]
            if r[-1] in '02468':
                print(x, x // 9231)
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

print(divisors(16))
print(divisors(24))
print(divisors(100_000_000))

print(time.time() - start)  # 2.059286 -> 0.00035
'''


# № 17536 Основная волна 07.06.24 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

k = 0
for x in range(800_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            k += 1
            if k == 5:
                break
'''


def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

k = 0
for x in range(800_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2? сопоставление, 3, 4, 5, 7, 8, 9-, 11-, 12-, 13, 14, 15, 16, 18, 19-21-, 22, 23]
# КЕГЭ  = []
# на следующем уроке:
