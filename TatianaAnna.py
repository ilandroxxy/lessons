# region Домашка: ******************************************************************


# № 21718 ЕГКР 19.04.25 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность произвольной длины; в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10, найдите все числа,
# соответствующие маске 4*4736*1, которые делятся на 7993 без остатка.
'''
from fnmatch import *
for x in range(7993, 10**10, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x)

from re import *
for x in range(7993, 10**10, 7993):
    if fullmatch('4[0-9]*4736[02468]+1', str(x)):
        print(x)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 2419 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C длиной не более 10**6 символов.
# Найдите длину самой длинной подцепочки, состоящей из символов C

# Вариант 1: ctrl + F
'''
s = open('0. files/24.txt').readline()
print(s)
'''


# Вариант 2: исследование пар символов
'''
s = open('0. files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] == 'C' and s[i+1] == 'C':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''

s = 'ABCBABCBACBCBABCBCCCCABCBABCCCCCCACBABCBCBCCCABCBABCBAS'
#   C   C  C C   C CCCC  C   CCCCCC C   C C CCC  C   C  S

# Вариант 3: Через замену
'''
s = open('0. files/24.txt').readline()
s = s.replace('A', 'B').replace('B', ' ')
print(max([len(i) for i in s.split()]))
'''

# Вариант 4: import re
'''
from re import *
s = open('0. files/24.txt').readline()
print(max([len(x.group(0)) for x in finditer(r'[C]+', s)]))
'''

'''
s = 'ABCBABCBACBCBABCBCCCCABCBABCCCCCCACBABCBCBCCCABCBABCBAS'
from re import *
# print([x.group(0) for x in finditer(r'[C]+', s)])
# ['C', 'C', 'C', 'C', 'C', 'CCCC', 'C', 'CCCCCC', 'C', 'C', 'C', 'CCC', 'C', 'C']
longest = max([len(x.group(0)) for x in finditer(r'[C]+', s)])
print(longest)
'''


# № 2420 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C, D, E, F. Найдите длину самой длинной подцепочки,
# состоящей из символов A, B, E, F (в произвольном порядке).
'''
# Вариант 1

s = open('0. files/24.txt').readline()
s = s.replace('D', 'C').replace('C', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 2

from re import *
s = open('0. files/24.txt').readline()
print(max([len(x.group(0)) for x in finditer(f'[ABEF]*', s)]))
'''


# № 2421 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C, D, E, F. Найдите длину самой длинной подцепочки,
# не содержащей символа D.

# Вариант 1
'''
s = open('0. files/24.txt').readline()
s = s.replace('D', ' ')
print(max([len(x) for x in s.split()]))
'''

# Вариант 2
'''
from re import *
s = open('0. files/24.txt').readline()
print(max([len(x.group(0)) for x in finditer(f'[ABCEF]*', s)]))
'''

# Вариант 3
'''
s = open('0. files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != 'D' and s[i+1] != 'D':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''


# № 2425 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C, D, E, F. Найдите максимальную длину
# цепочки вида DBACDBACDBAC.... (состоящей из фрагментов DBAC, последний
# фрагмент может быть неполным).

# Вариант 1: ctrl + F
'''
s = open('0. files/24.txt').readline()
print(s)
print(len('DBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBA'))
'''

# Вариант 2
'''
s = open('0. files/24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('DBAC', 'BACD', 'ACDB', 'CDBA'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 3
print(maxi)
'''

# Вариант 3
'''
from re import *
s = open('0. files/24.txt').readline()
print(max([len(x.group(0)) for x in finditer(f'(D(BACD)*(BAC|BA|B)?)', s)]))
'''

# D
# DBAC
# DBA
# DB
# DBACDBACDBACD
# DBACD
# DBACDBAC
# DBACDBA
# DBACDB
# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, (26)
