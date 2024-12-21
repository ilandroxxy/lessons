# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038667/step/13?unit=1062772
'''
from itertools import *
R = []
for p in permutations('КЛАБХАУС'):
    word = ''.join(p)
    if 'АА' not in word:
        R.append(word)
print(len(set(R)))
'''


# https://stepik.org/lesson/1038667/step/14?unit=1062772
'''
from itertools import *
cnt = 0
for p in product('01234567', repeat=5):
    num = ''.join(p)
    a, b, c, d, e = num
    if a != '0':
        if a not in '1357':
            if e not in '26':
                if num.count('7') <= 2:
                    cnt += 1
print(cnt)
'''

'''
from itertools import *
cnt = 0
s1 = '1357'
s2 = '2468'  # в записи которых не встречается цифра 0
for p in product(s1, s2, s1, s2, s1, s2, s1, s2, s1):
    num = ''.join(p)
    if num[0] != '0':
        if all(num.count(x) <= 3 for x in num):
            cnt += 1
print(cnt * 2)
'''

'''
from itertools import *
cnt = 0
s1 = '1357'
s2 = '2468'  # в записи которых не встречается цифра 0
for p in product(s1, s2, s1, s2, s1, s2, s1, s2, s1):
    num = ''.join(p)
    if all(num.count(x) <= 3 for x in num):
        cnt += 1
for p in product(s2, s1, s2, s1, s2, s1, s2, s1, s2):
    num = ''.join(p)
    if num[0] != '0':
        if all(num.count(x) <= 3 for x in num):
            cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 1199 Апробация 27.04 (Уровень: Базовый)
'''
def F(n):
    if n <= 1:  # F(n)=1 при n≤1
        return 1
    if n > 1 and n % 2 == 0:
        return 3 * n * F(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * F(n - 2)

print(F(31))
'''


# № 1131 (Уровень: Средний)
'''
def F(n):
    if n == 1:  # F(1)=1
        return 1
    if n >= 2 and n % 2 == 0:
        return F(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return F(n - 1) + n


for n in range(1, 1000):
    if F(n) == 19:
        print(n)
        break
'''


#
# № 2709 Пробный 02.2022 /dev/inf Middle level (Уровень: Сложный)
'''
from functools import *


@lru_cache(None)
def F(n):
    if n <= 2:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n - 1) - n
    if n > 2 and n % 2 == 0:
        return F(n - 2) + G(n - 1) + 2

def G(n):
    if n <= 0:
        return 2
    if n > 0 and n % 2 != 0:
        return F(n - 1) - 2 * G(n - 2)
    if n > 0 and n % 2 == 0:
        return 2 * F(n - 2) - 2 * G(n - 1)

print(F(96))
'''


# № 15331 Досрочная волна 2024 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

from sys import *
setrecursionlimit(10000)

def F(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + F(n - 1)

print(F(2024) - F(2020))
# RecursionError: maximum recursion depth exceeded

# Решение руками:
# F(2024) = 2024 + 2 + F(2023)
# F(2023) = 2023 + 2 + F(2022)
# F(2022) = 2022 + 2 + F(2021)
# F(2021) = 2021 + 2 + F(2020) - F(2020)

print(2024 + 2023 + 2022 + 2021 + 8)
'''


# № 17679 Пересдача 04.07.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)


print((F(2024) // 7 - F(2023)) // F(2022))
# print((F(2024) / 7 - F(2023)) / F(2022))
#        ~~~~~~~~^~~
# OverflowError: integer division result too large for a float
'''

import sys
sys.setrecursionlimit(100000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)


print((F(2024) + 2 * F(2023)) // F(2022))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 16]
# КЕГЭ  = []
# на следующем уроке:
