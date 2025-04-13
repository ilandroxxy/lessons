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
num = r'([1-B][0-B]*[02468A]|[0-B])'
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
reg = rf'{num}([-*]{num})+'
M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)

print(max([len(x.group()) for x in finditer(reg, s)]))
'''

# № 19970 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()

num = r'([1-9][0-9]*[05]|[0])'
reg = rf'{num}([+*]{num})+'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 19968 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()

num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([+*]{num})+'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 19967 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()

num = r'([1-9][0-9]*|[0])'
reg = rf'AFD{num}([+*]{num})+'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''

# № 19887 (Уровень: Базовый)
# Во входном файле в строчку записаны арабские цифры от 0 до 9 включительно.
#
# Требуется найти самую длинную последовательность,
# в которой чётные и нечётные цифры чередуются.
'''
from re import *
s = open('0. files/24.txt').readline()

pattern = r'(([13579][02468])+[13579]?|([2468][13579])+[02468]?)'

M = [x.group() for x in finditer(pattern, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 19719 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()

num = r'([12349][012349]*|[0])'
reg = rf'{num}([-*]{num})+'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 18619 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()

pattern = r'(([13579][02468])+[13579]?|([2468][13579])+[02468]?)'

M = [x.group() for x in finditer(pattern, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
print(maxi)
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
