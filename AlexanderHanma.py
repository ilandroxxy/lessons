# region Домашка: ******************************************************************
'''
s = sorted('ФОКУС')
R = []
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if 'Ф' not in slovo and slovo.count('У') == 2:
                        R.append(num)
print(max(R))
'''

'''
from itertools import *

num = 0
R = []
for x in product(sorted('МАРКСЛ'), repeat=6):
    sl = ''.join(x)
    num += 1
    if len(set(sl)) == 4 and any(sl.count(s) == 3 for s in sl):
        if 'КС' not in sl and 'СК' not in sl:
            R.append(num)

print(max(R))
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from fnmatch import *
for x in range(4173, 10**10, 4173):
    if fnmatch(str(x), '1?2655*8'):
        print(x)

        # 1026558
        # 1226553198
        # 1526550168
'''


# № 13868 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '112?57*4'):
        summa = sum([int(i) for i in str(x)])
        if summa % 2 != 0:
            print(x, x // 2024)
'''


# № 12741 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(1234, 10**10, 1234):
    if fnmatch(str(x), '4*5*6') and fnmatch(str(x), '?74*68?'):
        print(x, x // 1234)
'''


'''
import time
start = time.time()

# def divisors(x):
#     div = []
#     for j in range(1, x + 1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
            # div.append(j)
            # div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)  # 3.05926704 -> 0.00036311

print(3.05926704 / 0.00036311)  # 8425.179
'''

# № 17879 Демоверсия 2025 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(800_000+1, 10**10):
    div = divisors(x)
    if len(div) >= 2:
        M = div[0] + div[-1]
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 17686 Пересдача 04.07.24 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(700_000+2, 20**20):
    d = [j for j in divisors(x) if j % 10 == 7 and j != 7]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Тип 25 №27422
# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [174457;174505], числа, имеющие ровно
# два различных натуральных делителя,
# не считая единицы и самого числа.
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(174457, 174505+1):
    d = divisors(x)
    if len(d) == 2:
        print(*d)
'''


# Тип 25 №27855
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [95632; 95700], числа, имеющие ровно шесть различных чётных
# натуральных делителей
# (при этом количество нечётных делителей может быть любым).

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(95632, 95700+1):
    d = [j for j in divisors(x) if j % 2 == 0]
    if len(d) == 6:
        print(*d)
'''

# Тип 25 №29673
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(123456789, 223456789+1):
    # Проверка есть ли у числа x целый квадратный корень
    if x ** 0.5 == int(x ** 0.5):  
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
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
