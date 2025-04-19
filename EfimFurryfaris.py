# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 21421 Досрочная волна 2025 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-B][0-B]*[02468A]|[0])'
M = [x.group() for x in finditer(num, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 20813 Апробация 05.03.25 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*|[0])'
reg = rf'{num}([-*]{num})*'
M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 20968 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*[02468]|[02468])'
reg = rf'{num}([+*]{num})*'
M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''

# № 18619 (Уровень: Сложный
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-6]+)'
reg = rf'B{num}([-*]{num})*'
M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 21597 (Уровень: Сложный)

from re import *
s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([*]{num})*([-]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi=0
for x in M:
    if len(x) == 46:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)


# 51 3021*1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1
# 46 1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1
#


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = [9, 13, 19-21, 22, 24, 25]
# на следующем уроке:


# Первый пробник 21.12.24:
# Ефим 12/25 -> 56 вторичных баллов +[1-4, 7, 8, 11, 14-18] -[5, 6, 9, 10, 12, 19-21, 22, 23, 24, 25]
