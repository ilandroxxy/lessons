# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *

table = '13 14 16 17 18 23 26 31 32 36 37 41 45 46 49 54 58 61 62 63 64 69 71 73 78 81 85 87 94 96'
graph = 'АБ БА АГ ГА БГ ГБ БД ДБ ГД ДГ ГЖ ЖГ ЖИ ИЖ ГИ ИГ ДИ ИД ИК КИ КЕ ЕК ЕД ДЕ ВЕ ЕВ ВД ДВ ВБ БВ'

for per in permutations('АБВГДЕЖИК'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), per[i-1])
        if set(new_table.split()) == set(graph.split()):
            print('1 2 3 4 5 6 7 8 9')
            print(*per)
'''


# Тип 1 №16030
from itertools import *

table = '15 16 23 24 27 32 35 37 42 46 51 53 56 61 64 65 72 73'
graph = 'BD DB DC CD CE EC CG GC EG GE GF FG FA AF FB BF BA AB'

for per in permutations('ABCDEGF'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), per[i-1])
        if set(new_table.split()) == set(graph.split()):
            print('1 2 3 4 5 6 7')
            print(*per)

# 1 2 3 4 5 6 7
# A C G D F B E

# 1 2 3 4 5 6 7
# E B F D G C A

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
