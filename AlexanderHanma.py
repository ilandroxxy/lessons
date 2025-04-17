# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 19751
'''
from re import *

s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|[0])'
reg = rf'(?=(A{num}([+]{num})*))'

M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, eval(x[1:]))
    print(x)
print(maxi)
'''


# № 21597 (Уровень: Сложный)
'''
from re import *

s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([*]{num})*([-]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(0) for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    if len(x) == 46:
        print(len(x), x)
    if len(x) == 51:
        print(len(x), x)
print(maxi)
'''
# 46 1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1


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


# № 17685 Пересдача 04.07.24 (Уровень: Гроб)
'''
from re import *

s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|[0])'
reg = rf'(?=({num}([+*]{num})*))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    if eval(x) == 0:
        print(x)
        maxi = max(maxi, len(x))
print(maxi)
'''

# Шаблон для решения номеров 24 с регулярными выражениями
'''
from re import *

s = open('0. files/24.txt').readline()
num = r'([...][...]*|[0])'
reg = rf'(?=({num}([....]{num})*))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 20288 (Уровень: Средний)
'''
from re import *
for x in range(9231, 10**10, 9231):
    if fullmatch(r'[24680]*12[13579]4[13579]', str(x)):
        print(x, x // 9231)
'''


# № 7897 (Уровень: Базовый)
'''
from re import *
for x in range(11071, 10**10, 11071):
    if fullmatch(r'[13579]136[0-9]*(24680)?1', str(x)):
        print(x, x // 11071)
'''

'''
from re import *
for x in range(1, 10**10):
    if fullmatch(r'[13579]136[0-9]*([24680])?1', str(x)):
        print(x, x // 11071)
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
