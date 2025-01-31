# region Домашка: ******************************************************************

# № 7897 (Уровень: Базовый) 🌶
'''
from fnmatch import *

R = []
for x in range(11071, 10 ** 10, 11071):
    if fnmatch(str(x), '?136*1'):
        if str(x)[0] in '13579' and str(x)[-2] in '02468':
            R.append([x, x // 11071])

print(*R[-5])
print(*R[-4])
print(*R[-3])
print(*R[-2])
print(*R[-1])
'''


# № 3376 (Уровень: Базовый)
'''
from fnmatch import *

for x in range(21, 10 ** 8, 21):
    if fnmatch(str(x), '1*5*9'):
        s = str(x)
        if sorted(s) == list(s):
            if len(set(s)) == len(s):
                print(x, x // 21)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

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


print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(24))  # [1, 24, 2, 12, 3, 8, 4, 6]
print(divisors(100_000_000))  # 2.896  -> 0.00036

print(time.time() - start)
'''


# https://education.yandex.ru/ege/task/2d62d9fd-a99a-4bef-a747-57a6ad2539d7
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(177000, 177300+1):
    d = divisors(x)
    if len(d) == 2:
        summa = sum([int(x) for x in str(x)])
        if len(divisors(summa)) == 2:
            print(x, summa)
'''


# https://education.yandex.ru/ege/task/e9239096-46bf-4dab-a19b-ad07eed75bb4
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(106732567, 152673836+1):
    if (x**0.5).is_integer():
        d = divisors(x)
        if len(d) == 3:
            print(x, max(d))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]
