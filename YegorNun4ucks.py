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
reg = rf'{num}([*-]{num})*'

M = [x.group() for x in finditer(reg, s)]
for x in M:
    print(x)
print(max([len(x) for x in M]))

print(max([len(x.group()) for x in finditer(reg, s)]))
'''

# № 17878 Демоверсия 2025 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([6789][06789]*|0)'
reg = rf'{num}([*-]{num})*'

# M = [x.group() for x in finditer(reg, s)]
# for x in M:
#     print(x)
# print(max([len(x) for x in M]))

print(max([len(x.group()) for x in finditer(reg, s)]))
'''


# № 17563 Основная волна 08.06.24 (Уровень: Сложный)
# 0 как самостоятельное число (например, в выражении 5 + 0)
# — это значащий ноль, потому что
# он имеет математическую значимость (нейтральный элемент сложения).
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*)'  # натуральные числа (убрали |0 )
reg = rf'{num}([*-]{num})*'

# M = [x.group() for x in finditer(reg, s)]
# for x in M:
#     print(len(x), x)
#
# print(max([len(x) for x in M]))

print(max([len(x.group()) for x in finditer(reg, s)]))
'''


# № 17641 Основная волна 19.06.24 (Уровень: Гроб)
# todo посмотреть видео № 17641 Основная волна 19.06.24 (Уровень: Гроб)

# print(eval('0+0+0+0+0+29162+0+0*0+0*0+0*0+0+0+0+11527+0*0+35268+0+0+68490+0+18442+0+0*0*0+0+0+0+0*0*6455+0*0+0*0*0*31873+0*0+0+0+0+0+0*0*0+0*0*0*0+0+0*0*0'))
# print(0+0+0+0+0+29162+0+0*0+0*0+0*0+0+0+0+11527+0*0+35268+0+0+68490+0+18442+0+0*0*0+0+0+0+0*0*6455+0*0+0*0*0*31873+0*0+0+0+0+0+0*0*0+0*0*0*0+0+0*0*0)
'''
from re import *pr

s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|0)'  # натуральные числа (убрали |0 )
reg = rf'{num}([*+]{num})*'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    if eval(x) == 0:
        maxi = max(maxi, len(x))
    if len(x) == 130:
        print(len(x), eval(x), x)
    if len(x) == 142:
        print(eval(x), x)
print(maxi)
'''
# print(max([len(x) for x in M]))
#
# print(max([len(x.group()) for x in finditer(reg, s) ]))


# № 17756(Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9][0-9]*|0)'
reg = rf'[+*]{num}([*+]{num})*[+*]'

M = [x.group() for x in finditer(reg, s)]
for x in M:
    if len(x) == 191:
        print(len(x), x)
print(max([len(x) for x in M]))

print(max([len(x.group()) for x in finditer(reg, s)]))
'''

# № 18147 (Уровень: Средний)
'''
from re import *
s = open('24_18147.txt').readline()
num = r'([789][789]*)'
reg = rf'{num}([+]{num})+'  # + - 1 или более | * - 0 или более 
# соответственно при * у нас бралось просто число, а не выражение
mx = 0
M = [x.group() for x in finditer(reg, s)]
for x in M:
    if eval(x) > mx:
        mx = eval(x)
        print(x)

print(mx)
'''


# № 18285 (Уровень: Сложный)
'''
from re import *
s = open('24_18285.txt').readline()
num = r'([1-9][0-9]*)'
reg = rf'{num}([*+]{num})+'
mx = 0
M = [x.group() for x in finditer(reg, s)]
for x in M:
    s = x.replace('*', ' ').replace('+', ' ')
    s = s.split()
    mx = max(mx, len(s))

print(mx)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 13, 14, 17, 22, 23, 24]
# на следующем уроке:


# Первый пробник 21.12.24:
# Yegor 21/29 -> 80 вторичных баллов +[1-5, 7, 9-12, 14-16, 18-24, 27] -[6, 8, 13, 25, 26]

# Второй пробник 28.02.25:
# Yegor 26/29 -> 92 вторичных баллов +[1-5, 7-21, 23, 25, 26.1, 26.2, 27.1, 27.2] -[6, 22, 24]
