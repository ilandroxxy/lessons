# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21421 Досрочная волна 2025 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-B][0-B]*[02468A]|[02468A])'
M = [x.group() for x in finditer(num, s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 22362 (Уровень: Средний)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-B][0-B]*[13579B])'
M = [x.group() for x in finditer(num, s)]
maxi = 0
res = ''
for x in M:
    if maxi < int(x, 12):
        maxi = int(x, 12)
        res = x
print(maxi)
print(s.index(res))
'''

#
# № 22357 (Уровень: Средний)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-D][0-D]*[02468AC])'
M = [x.group() for x in finditer(num, s)]
maxi = 0
res = ''
for x in M:
    if maxi < int(x, 14):
        maxi = int(x, 14)
        res = x
print(maxi)
print(s.index(res))
'''


#
# № 22358 (Уровень: Средний)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-B][0-B]*)'
M = [x.group() for x in finditer(num, s)]
maxi = 0
res = ''
for x in M:
    if int(x, 12) % 3 == 0:
        if maxi < int(x, 12):
            maxi = int(x, 12)
            res = x
print(maxi)
print(s.index(res))
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
    print(len(x), x)
    maxi = max(maxi, len(x))
print(maxi)
'''


# № 19968 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([+*]{num})*'
M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    print(len(x), x)
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
        print(len(x), x)
    maxi = max(maxi, len(x))
print(maxi)
'''
# 46      1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1
# 51 3021*1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1

'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([-*]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


from re import *
s=open('0. files/24.txt').readline()
num=r'([1-9][0-9]*|[0])'
reg=fr'{num}([+*]{num})*'
reg=fr'(?=({reg}))'
M=[x.group(1) for x in finditer(reg,s)]
maxi=0
for x in M:
    if eval(x)==0:
        print(x)
        maxi=max(maxi,len(x))
print(maxi)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ = []
# на следующем уроке: регулярные выражения, 26, 27


# Первый пробник 21.12.24:
# Лиза 11/29 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

# Второй пробник 28.02.25:
# Лиза 17/29 -> 70 вторичных баллов +[1-17, 23, 25] -[]
