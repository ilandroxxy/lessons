# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def divisors(x):  # 24
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)  # 4
            div.append(x // j)  # 24 // 4 = 6
    return sorted(set(div))
'''

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))
'''


# № 19755 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))

# print([x for x in range(1, 100) if len(divisors(x)) == 0])

cnt = 0
for x in range(1_200_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) >= 2:
        M = min(d) + max(d)
        if M > 2000 and M % 10 == 8:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 19778 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


cnt = 0
for x in range(9_500_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        F = sum(d) // len(d)
        if F != 0 and F % 813 == 0:
            print(x, F)
            cnt += 1
            if cnt == 5:
                break
'''


# Тип 25 №29673
# https://inf-ege.sdamgia.ru/problem?id=29673
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))

for x in range(123456789, 223456789+1):
    # число является полным квадратом
    # if (x ** 0.5) == int(x ** 0.5):
    if (x ** 0.5).is_integer():
        d = divisors(x)
        if len(d) == 3:
            print(x, max(d))
'''


# № 20288 (Уровень: Средний)

# print(help(set))
'''
from fnmatch import *
for x in range(9231, 10**10, 9231):
    if fnmatch(str(x), '*12?4?'):
        s = str(x)
        if s[-1] in '13579' and s[-3] in '13579':
            if all(p in '02468' for p in s[:-5]):
                print(x, x // 9231)
'''

# № 19720 (Уровень: Средний)
'''
from fnmatch import *
for x in range(153, 10**8, 153):
    if fnmatch(str(x), '1*2?3*45'):
        s = str(x)
        if s[s.index('2')+1] in '02468':
            if all(p in '13579' for p in s[1:s.index('2')]):
                if all(p in '13579' for p in s[(s.index('2')+2):s.index('45')]):
                    print(x, x//153)
'''


# № 18962 (Уровень: Базовый)
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))

cnt = 0
for x in range(500_000+1, 10**10):
    d = [j for j in divisors(x) if fnmatch(str(j), '2*3?')]
    if len(d) >= 1:
        print(x, min(d))
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
# ФИПИ = [25]
# КЕГЭ  = []
# на следующем уроке: 8, 9, 11, 13, 17, 18, 11, 22

# Первый пробник 5.02.25:
# Ангелина 11/29 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/29 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]

# Второй пробник 28.02.25:
# Ангелина /29 -> _ вторичных баллов +[] -[]
# Сергей 16/29 -> 67 вторичных баллов +[1, 2, 5, 6, 8, 11, 13-18, 19-21, 23, 25] -[3, 4, 7, 9, 10, 12, 22, 24]
