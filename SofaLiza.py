# region Домашка: ******************************************************************

'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n >= 10000:
        return 1
    if n < 10000 and n % 2 == 0:
        return F(n + 3) + 7
    if n < 10000 and n % 2 != 0:
        return F(n + 1) - 3

print(F(50) - F(57))
'''


# https://stepik.org/lesson/1038709/step/14?unit=1062775
"""
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 3 * G(n-1)

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) - 2 * G(n-1)


# print(F(18))
x = F(18)
# x = 790171309

print(sum([int(i) for i in str(x)]))
'''
print(sum(map(int, str(x))))

summa = 0
while x > 0:
    summa += x % 10
    x //= 10
print(summa)
'''
"""

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 20801 Апробация 05.03.25 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
graph = 'DB BD DE ED EF FE EA AE AC CA CF FC CG GC FG GF GB BG'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # B G E F A D C

# CF - 74, AE - 53
'''


'''
print('1 2 3 4 5 6 7')
from itertools import *
t = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
g = 'DB BD DE ED EF FE EA AE AC CA CF FC CG GC FG GF GB BG'
for p in permutations('ABCDEFG'):
    nt = t
    for i in range(1, 7+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(g.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # B G E F A D C
'''


'''    
    print(p)

    #   0    1    2    3    4    5    6 
    # ('G', 'F', 'E', 'D', 'A', 'B', 'C')
    #   1    2    3    4    5    6    7

new_table = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
new_table = new_table.replace('1', 'G')
new_table = new_table.replace('2', 'F')
new_table = new_table.replace('3', 'E')
new_table = new_table.replace('4', 'D')
new_table = new_table.replace('5', 'A')
new_table = new_table.replace('6', 'B')
new_table = new_table.replace('7', 'C')
print(new_table)
# GF GB FG FD FC ED EA EB DF DE DC AE AC BG BE CF CD CA
# DB BD DE ED EF FE EA AE AC CA CF FC CG GC FG GF GB BG
'''

'''
print('1 2 3 4 5 6 7')
from itertools import *
t = '12 13 21 23 25 31 32 34 35 36 37 43 46 52 53 57 63 64 67 73 75 76'
g = 'АБ БА АВ ВА АГ ГА АД ДА АЕ ЕА АК КА БВ ВБ ВГ ГВ ГД ДГ ДЕ ЕД ЕК КЕ'
for p in permutations('АБВГДЕК'):
    nt = t
    for i in range(1, 7+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(g.split()):
        print(*p)
'''

print('1 2 3 4 5 6 7')
from itertools import permutations
table = '21 31 12 32 52 13 23 43 53 63 73 34 64 25 35 75 36 46 76 37 57 67'
graph = 'АБ БА АВ ВА АГ ГА АД ДА АЕ ЕА КА АК ВБ БВ ВГ ГВ ГД ДГ ДЕ ЕД ЕК КЕ'
for p in permutations('АБВГДЕК'):
    new_table = table
    for i in range(1, 7 + 1):
        new_table = new_table.replace(str(i), p[i - 1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # Б В А К Г Е Д

# ВГ - 25, ДЕ - 76


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 13, 14, 15, 16, 19-21, 23]
# КЕГЭ = []
# на следующем уроке:
