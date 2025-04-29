# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 21421 Досрочная волна 2025 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-B][0-B]*[02468A])'
M = [x.group() for x in finditer(num, s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, len(x))
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
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 17641 Основная волна 19.06.24 (Уровень: Гроб)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|[0])'
reg = rf'{num}([+*]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    if eval(x) == 0:
        print(x)
        maxi = max(maxi, len(x))
print(maxi)
'''

'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|[0])'
reg = rf'{num}([+*]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 21597 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([*]{num})*([-]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    if len(x) == 51:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''

# 46      1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1
# 51 3021*1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21.2, 22, 23, 24.2, 25, 26.1]
# КЕГЭ = [19-21, 24, 25]
# на следующем уроке:

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


