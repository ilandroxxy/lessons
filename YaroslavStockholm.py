# region Домашка: ******************************************************************
from functools import lru_cache
from lib2to3.pgen2.grammar import opmap_raw

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/c21fb755-a462-4ee3-97b3-4c3be812dd68
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201', 1)
            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                print(z)
'''


# https://education.yandex.ru/ege/task/b5ea1e82-76f7-4781-8ef4-5f462fdc7638
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        print(mask, 32 - mask)  # 32
'''


# № 19882 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 4:
        return 1
    if n >= 4:
        return F(n - 1) + n * 2

print(F(2025))

# F(2025) = F(2024) + 2025 * 2
# F(2024) = F(2023) + 2024 * 2  + 2025 * 2
#  1 + .... + 2024 * 2  + 2025 * 2
'''
# RecursionError: maximum recursion depth exceeded in comparison


# № 19597 (Уровень: Базовый)
'''
def F(n):
    if n < 15:
        return 4
    if n >= 15 and n % 3 == 0:
        return F(2 * n/3) + n - 1
    if n >= 15 and n % 3 != 0:
        return F(n - 1) + 3


for n in range(1, 1000):
    if F(n) == 251:
        print(n)
'''


# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache()
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n/2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)

for n in range(5000):
    F(n)

print(F(4952) + 2 * F(4958) + F(4964))
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

# Просто поменять / на //
'''
# print((F(2024) / 7 - F(2023)) / F(2022))
# OverflowError: integer division result too large for a float


# № 14338 (Уровень: Средний)
# F(n) = G(n) = n, если n<10;
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 10:
        return n
    if n > 9:
        return 3 * n + G(n - 2)


def G(n):
    if n < 10:
        return n
    if n > 9:
        return n - 2 + F(n - 1)


print(F(2204) - G(2200))
'''

'''
from functools import *
import sys
sys.setrecursionlimit(10000)
@lru_cache()
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2*F(n-2)-F(n-1)+2
    if n > 2 and n % 2 !=0:
        return 2*F(n-1)+F(n-2)-2

for n in range(5000):
    F(n)

print(F(170))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 15, 16, 25]
# КЕГЭ  = []
# на следующем уроке: 23


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]
