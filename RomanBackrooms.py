# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19882 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(2025)

def F(n):
    if n < 4:
        return 1
    if n >= 4:
        return F(n - 1) + n * 2


print(F(2025))
'''
# Ответ: 4102639


# № 19708 (Уровень: Базовый)
'''
from sys import *
setrecursionlimit(10000)

def F(n):
    if n < 13:
        return 13
    if n >= 13 and n % 5 != 0:
        return 13 - F(n - 1)
    if n >= 13 and n % 5 == 0:
        return 13 + F(n - 1)

print(F(3013))
'''
# Ответ: -7800


# № 19597 (Уровень: Базовый)
'''
def F(n):
    if n < 15:
        return 4
    if n >= 15 and n % 3 == 0:
        return F(2 * n/3) + n - 1
    if n >= 15 and n % 3 != 0:
        return F(n - 1) + 3


for n in range(1, 10000):
    if F(n) == 251:
        print(n)
'''


# A. Вычти 2
# B. Найди целую часть от деления на 2
# Сколько существует программ, для которых при исходном
# числе 38 результатом является число 2 и при этом траектория
# вычислений содержит число 16?

def F(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    else:
        return F(a-2, b) + F(a//2, b)


print(F(38, 16) * F(16, 2))



# № 9752 Основная волна 19.06.23 (Уровень: Базовый)
#
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 2
# B. Прибавить 3
# C. Умножить на 2
# Сколько существует программ, для которых при исходном числе 3
# результатом является число 25, и при этом
# траектория вычислений содержит число 10 и не содержит 17?
'''
def F(a, b):
    if a > b or a == 17:
        return 0
    if a == b:
        return 1
    else:
        return F(a + 2, b) + F(a + 3, b) + F(a * 2, b)


print(F(3, 10) * F(10, 25))
'''


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


# Первый пробник 21.12.24:
# Роман 2/5 -> 14 вторичных баллов +[2, 12] -[5, 6, 8]
