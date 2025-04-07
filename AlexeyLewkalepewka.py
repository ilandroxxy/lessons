# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20813 Апробация 05.03.25 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*|0)'
reg = rf'{num}([-*]{num})*'

"""
m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
"""

print(max([len(x.group()) for x in finditer(reg, s)]))
'''


# № 17563 Основная волна 08.06.24 (Уровень: Сложный)
# натуральные числа без незначащих нулей.
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*)'
reg = rf'{num}([-*]{num})*'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 17641 Основная волна 19.06.24 (Уровень: Гроб)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|0)'
reg = rf'{num}([+*]{num})*'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    if eval(x) == 0:
        maxi = max(maxi, len(x))
print(maxi)
'''


# 17756 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|0)'
reg = rf'[+*]{num}([+*]{num})*[+*]'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 17878 Демоверсия 2025 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([6789][06789]*|0)'
reg = rf'{num}([-*]{num})*'

m = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in m:
    maxi = max(maxi, len(x))
print(maxi)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [8, 14, 15, 23]
# на следующем уроке:

# Первый пробник 21.12.24:
# 24/25 -> 88 вторичных баллов +[1, 3-25] -[2]

# Второй пробник 10.02.25:
# 23/25 -> 86 вторичных баллов +[1-9, 11-23, 25] -[10, 24]
