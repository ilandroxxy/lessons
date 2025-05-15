# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# 19968 (24)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-5][0-5]*|[0])'
reg = rf'{num}([*+]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg,s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi,len(x))
print(maxi)
'''


# 19751 (24)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([1-9]+)'
# num = r'([1-9][1-9]*)'
reg = rf'A{num}([+]{num})*'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg,s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, eval(x[1:]))
print(maxi)  # 67622777

print(eval('4+4+4+4'))  # 16
print(eval('5+22'))  # 27
'''


# № 18147 (Уровень: Средний)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][789]*)'
reg = rf'{num}([+]{num})+'
reg = rf'(?=({reg}))'
M = [x.group(1) for x in finditer(reg,s)]
maxi = 0
for x in M:
    print(x)
    maxi = max(maxi, eval(x))
print(maxi)
'''
# 89797978998877
# 9988877898985


# № 20909 Апробация 05.03.25 (Уровень: Средний)
# Определите в прилагаемом файле максимальное количество
# идущих подряд символов, среди которых пара AB (в указанном порядке)
# cвстречается ровно 100 раз.

s = open('0. files/24.txt').readline()
s = s.split('AB')
maxi = 0
for i in range(len(s)-100):
    r = 'A' + 'AB'.join(s[i:i+101]) + 'B'
    maxi = max(maxi, len(r))
print(maxi)



s = open('0. files/24.txt').readline()
s = s.split('ABC')
maxi = 0
for i in range(len(s)-100):
    r = 'BC' + 'ABC'.join(s[i:i+101]) + 'AB'
    maxi = max(maxi, len(r))
print(maxi)


s = open('0. files/24.txt').readline()
s = s.split('ABCD')
maxi = 0
for i in range(len(s)-100):
    r = 'BCD' + 'ABCD'.join(s[i:i+101]) + 'ABC'
    maxi = max(maxi, len(r))
print(maxi)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Николай 9/19 -> 48 вторичных баллов +[1, 2, 4, 7, 13, 14, 16, 23, 25] -[5, 6, 8, 9, 12, 15, 17, 24]

# Второй пробник 28.02.25:
# Николай 12/19 -> 56 вторичных баллов +[1-4, 8-10, 12, 13, 15, 16, 23] -[5, 6, 14, 17, 18-22, 24, 25]
