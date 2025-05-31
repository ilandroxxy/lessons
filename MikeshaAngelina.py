# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 21981
'''
from re import *

f = open('0. files/24.txt').readline()

s = r'([1-F][0-F]*)'
s = rf'(?=({s}))'
M = [x.group(1) for x in finditer(s,f)]
maxi = 0
l = 0
for x in M:
    if x.count('B') == 10:
        if maxi < int(x, 16):
            maxi = int(x, 16)
            l = len(x)
print(l, maxi)
'''
# 5*5-5-5-5-5-3454645*5*5*5*5-5-5-5-5
# 5*5-5-5-5-5-3454645   5*5*5*5-5-5-5-5
# 5*5-5-5-5-5-3454645   3454645*5*5*5*5-5-5-5-5


# № 17685 Пересдача 04.07.24 (Уровень: Гроб)
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
s = open('0. files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 12931 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
s = open('0. files/24.txt').readline()
s = s.replace('T', ' ').replace('U', ' ').split()
for x in s:
    if len(x) > 5:
        print(x, len(x))
'''

# XYZVWXYZVWXYZV
'''
s = open('0. files/24.txt').readline()
cnt = 4  # считаем промежуточные последовательности
maxi = 0  # считаем максимальную последовательность
for i in range(len(s)-4):
    if s[i:i+5] in ('VWXYZ', 'WXYZV', 'XYZVW', 'YZVWX', 'ZVWXY'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 4
print(maxi)
'''

s = open('0. files/24.txt').readline()
cnt = 2  # считаем промежуточные последовательности
maxi = 0  # считаем максимальную последовательность
for i in range(len(s)-2):
    if s[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)


# № 12931 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)

from re import *
s = open('0. files/24.txt').readline()
num = r'(VWXYZ)+'
reg = rf'((Z)|(YZ)|(XYZ)|(WXYZ))*{num}((VWXY)|(VWX)|(VW)|(V))*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    if len(x) == 40:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [8, 9, 11, 13, 17, 19-21, 22, 24.2, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 5.02.25:
# Ангелина 11/29 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/29 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]

# Второй пробник 28.02.25:
# Ангелина 10/29 -> 51 вторичных баллов +[2, 3, 4, 7, 9, 10, 14, 18, 23, 25] -[1, 5, 6, 8, 12, 11, 13, 15, 17]
# Сергей 16/29 -> 67 вторичных баллов +[1, 2, 5, 6, 8, 11, 13-18, 19-21, 23, 25] -[3, 4, 7, 9, 10, 12, 22, 24]
