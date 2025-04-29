# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:  # F == 0
                    print(x, y, z, w, int(F))
'''
from pprint import pformat

# № 21718 ЕГКР 19.04.25 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(7993, 10**10+1, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x, x // 7993)


from re import *
for x in range(7993, 10**10+1, 7993):
    if fullmatch('4[0-9]*4736[0-9]*1', str(x)):
        print(x, x // 7993)
'''


# № 18591 (Уровень: Средний)
'''
from re import *
for x in range(1984, 10**10, 1984):
    if fullmatch('[02468]9[0-9]23[0-9][0-9]*23[13579][02468]', str(x)):
        print(x, x // 1984)
'''


# № 21421 Досрочная волна 2025 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-B][0-B]*[02468A])'

M = [x.group() for x in finditer(num, s)]
maxi = 0
for x in M:
    if len(x) >= maxi:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''

# № 21908 Открытый вариант 2025 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-D][0-D]*[02468AC])'

M = [x.group() for x in finditer(num, s)]
maxi = 0
for x in M:
    if len(x) >= maxi:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''


'''
from string import *
alphabet = digits + ascii_uppercase
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('0. files/24.txt').readline()
for x in alphabet[14:]:
    s = s.replace(x, ' ')

print(max([len(x) for x in s.split() if x[0] != '0']))
maxi = 0
for x in s.split():
    if len(x) == 2:
        continue
    if x[0] == '0':
        while x[0] == '0':
            x = x[1:]
    maxi = max(maxi, len(x))
print(maxi)
'''

'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*[02468])'
reg = rf'{num}([+*]{num})+'
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
reg = rf'{num}([+*]{num})+'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg, s)]
maxi = 0
for x in M:
    if eval(x) == 0:
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


'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([*+]{num})*'
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21.2, 22, 23, 24.2, 25]
# КЕГЭ = []
# на следующем уроке: порешать 2 номера сложные 101


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]

# Второй пробник 28.02.25:
# Дима 10/29 -> 51 вторичных баллов +[1, 4, 7, 8, 13-16, 23, 25] -[5, 9, 12, 17]
# Максим 16/29 -> 67 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-17, 19, 23, 25] -[5, 7, 13, 18]