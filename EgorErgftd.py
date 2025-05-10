# region Домашка: ******************************************************************
from random import shuffle

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 6309 (12)
'''
from itertools import *

for n in range(270, 1000):
    for p in product('12', repeat=n):
        if p.count('1') == p.count('2'):
            s = '0' + ''.join(p) + '0'

            while '00' not in s:
                s = s.replace('02', '101', 1)
                s = s.replace('11', '2', 1)
                s = s.replace('12', '21', 1)
                s = s.replace('010', '00', 1)
            summa = sum(map(int, s))
            if summa % 2 == 0:
                print(n)
'''

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
    if len(x) == 51:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''
# 46      1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1
# 51 3021*1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1


# № 18619 (Уровень: Сложный)

from re import *
s = open('0. files/24.txt').readline()
num = r'([1-6][1-6]*)'
reg = rf'B{num}([*-]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 22

# Первый пробник 21.12.24:
# Михаил 8/18 -> 46 вторичных баллов +[2, 4, 6, 12, 14, 15, 16, 23] -[1, 3, 5, 7, 8, 9, 11, 13, 17, 25]

# Второй пробник 28.02.25:
# Михаил 17/29 -> 70 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-16, 18, 19-20, 23, 25] -[5, 7, 10, 13, 17, 21, 22, 24]
# Егор 16/29 -> 68 вторичных баллов +[1-7, 9, 13, 14-18, 23, 25] -[8, 10, 11, 12, 19-21, 22, 24]
