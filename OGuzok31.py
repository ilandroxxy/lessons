# region Домашка: ******************************************************************
from pprint import pformat
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


# № 20813 Апробация 05.03.25 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*|[0])'
reg = rf'{num}([-*]{num})*'
M = [x.group() for x in finditer(reg, s)]
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
    print(x)
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
# ФИПИ = [1, 2? сопоставление, 3, 4, 5, 7, 8, 9-, 11-, 12-, 13, 14, 15, 16, 18, 19-21-, 22, 23]
# КЕГЭ = []
# на следующем уроке:


# Второй пробник 28.02.25:
# Селим 18/29 -> 72 вторичных баллов +[1-5, 8, 10-16, 19-21, 23, 25] -[6, 7, 9, 17, 22, 24]
