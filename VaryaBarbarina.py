# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № КЕГЭ № 4335 (Уровень: Базовый)
'''
from fnmatch import *

def divisors(x):
    res = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            res += [j, x // j]
    return sorted(set(res))


def prime(x):
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


k = 0
for x in range(960_000+1, 10**10):
    div = [j for j in divisors(x) if fnmatch(str(j), '*3?') and prime(j)]
    if len(div) >= 3:
        print(x, sum(div))
        k += 1
        if k == 5:
            break
'''


# КЕГЭ № 9710 (Уровень: Средний)
'''
from fnmatch import *
R = []
for x in range(10**9 + 1268, 10**10, 2023):
    if fnmatch(str(x), '1*1'):
        # R.append(sum([int(i) for i in str(x)]))
        R.append([sum(map(int, str(x))), x // 2023])

R = sorted(R)
M = sorted([x[1] for x in R[-5:]])
for x in M:
    print(x)
'''

# КЕГЭ № 9170 (Уровень: Средний)
'''
def divisors(x):
    res = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            if str(j)[0] == '4':
                res.append(j)
            if str(x // j)[0] == '4':
                res.append(x // j)
    return sorted(set(res))


for x in range(1, 10**6+1):
    div = divisors(x)
    if len(div) == 24:
        print(x, max(div))
'''

# endregion Урок: ******************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ= [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 14, 17]
# на следующем уроке: 22 и 24 с новых вариантов и 25 номер на отрезки.
