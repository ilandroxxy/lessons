# region Домашка: ******************************************************************

# № 10774 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('217.19.128.131/255.255.192.0', 0)
print(net)  # 217.19.128.0/18
'''
# Ответ: HCEA

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18490 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n > 3000:
        return n
    if n <= 3000:
        return (2 * n + 4) * F(n + 2)

print(F(20) / F(28))
'''
# RecursionError: maximum recursion depth exceeded


# № 18297 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 10:
        return n - 1
    if n >= 10 and n % 2 == 0:
        return 3 * n - 1 + F(n - 3)
    if n >= 10 and n % 2 != 0:
        return 5 * n + 2 + F(n - 4)

print(F(4445) - F(4444))
'''



# № 18931 Новогодний вариант 2025 (Уровень: Базовый)
'''
from functools import *
import sys
sys.setrecursionlimit(100000)

@lru_cache(None)
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


#
# № 17557 Основная волна 08.06.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)

print((F(2024) // 16 - F(2023)) / F(2022))
'''
#      ~~~~~~~~^~~~
# OverflowError: integer division result too large for a float

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 13, 14, 16]
# КЕГЭ  = []
# на следующем уроке: Разбираем пробный вариант. Будет 1.5 часовое занятие


# Первый пробник 21.12.24:

