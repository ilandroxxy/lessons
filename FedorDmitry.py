# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 2419 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C длиной не более 106 символов.
# Найдите длину самой длинной подцепочки, состоящей из символов C
'''
# Вариант: ctrl + F
s = open('files/24.txt').readline()
print(s)
print(len('CCCCCCCCCCC'))

# Вариант 2

s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'C' and s[i+1] == 'C':
    if s[i:i+2] == 'CC':
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)

# Вариант 3

s = open('files/24.txt').readline()
s = s.replace('B', 'A').replace('A', ' ')
print(max([len(x) for x in s.split()]))
'''

# Вариант 4
'''
from re import *
s = open('files/24.txt').readline()
pat = '[C]+'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''

'''
# [wkiejrf] - только один символ из набора
# [wkiejrf]* - набор любой длины в том числе пустой
# [wkiejrf]+ - набор любой длины, но непустой
# (www) - ищем конкретную последовательность именно этих символом 
# (www)* - ищем последовательности именно этих символом (в том числе пустую)
# (www)+ - ищем последовательности именно этих символом (но непустую)
# | - или 
'''

# № 24895 (Уровень: Средний)
'''
from re import *
s = open('files/24.txt').readline()
pat = '[1-9]+([+*][1-9]+)*'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''


# № 2420 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов
# латинского алфавита A, B, C, D, E, F.
# Найдите длину самой длинной подцепочки, состоящей из
# символов A, B, E, F (в произвольном порядке).
'''
from re import *
s = open('files/24.txt').readline()
pat = '[ABEF]+'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''


# № 2421 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Найдите длину самой длинной подцепочки, не содержащей символа D
'''
s = open('files/24.txt').readline()
s = s.replace('D', ' ')
print(max([len(x) for x in s.split()]))

s = open('files/24.txt').readline()
print(max([len(x) for x in s.split('D')]))

from re import *
s = open('files/24.txt').readline()
pat = '[ABCEF]+'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''

# № 2422 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов X, Y, Z.
# Определите максимальное количество идущих подряд символов,
# расположенных в алфавитном порядке (возможно с повторением символов).
'''
from re import *
s = open('files/24.txt').readline()
pat = '[X]+[Y]+[Z]+'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''


# № 2425 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C, D, E, F. Найдите максимальную длину цепочки
# вида DBACDBACDBAC.... (состоящей из фрагментов DBAC, последний
# фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('DBAC', 'BACD', 'ACDB', 'CDBA'):
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 3
print(maxi)

from re import *
s = open('files/24.txt').readline()
pat = '(DBAC)+(DBA|DB|D)'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''


# № 2426 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов 1, 2, 3, A, B, C.
# Определите максимальное количество идущих подряд цифр.
'''
s = open('files/24.txt').readline()
for x in "ABC":
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))

from re import *
s = open('files/24.txt').readline()
pat = '[123]+'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''


# № 2478 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов и содержит
# только заглавные латинские буквы и десятичные цифры.
# Определите максимальное количество идущих подряд символов,
# среди которых нет трёх одинаковых подряд идущих символов.

s = open('files/24.txt').readline()
for x in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(3 * x, f'{2*x} {2*x}')
print(max([len(x) for x in s.split()]))

s = open('files/24.txt').readline()
for x in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(3 * x, '** **')
print(max([len(x) for x in s.split()]))

# YYYewoirghjerXXX
# YY YYewoirghjerXX XX


s = open('files/24.txt').readline()
for x in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(4 * x, '*** ***')
print(max([len(x) for x in s.split()]))

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
