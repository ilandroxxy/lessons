# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19233 ЕГКР 21.12.24 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6 7 8')
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'AG GA AF FA FG GF FH HF HC CH HE EH CB BC BE EB BD DB DE ED DG GD'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

# 1 2 3 4 5 6 7 8
# E H B D F A C G

# AG + DE = 4 + 7 = 11
'''


# № 18308 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6 7 8 9')
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KC CK KB BK BD DB DC CD DH HD DG GD DE ED EF FE FG GF GH HG'
for p in permutations('ABCDEFGHK'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7 8 9
# B G C D K A E F H
# C G B D K A E F H

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]
