# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'BD DB BE EB BC CB CH HC HE EH HF FH DE ED DG GD GA AG GF FG AF FA'
for p in permutations('ABCDEGHF'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # E H B D F A C G

# AG + DE = 68 + 41 = 4 + 7 = 11


'''
    #   0    1    2    3    4    5    6    7
    # ('F', 'H', 'G', 'E', 'D', 'A', 'C', 'B')
    #   1    2    3    4    5    6    7    8

new_table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
new_table = new_table.replace('1', 'F')
new_table = new_table.replace('2', 'H')
new_table = new_table.replace('3', 'G')
new_table = new_table.replace('4', 'E')
new_table = new_table.replace('5', 'D')
new_table = new_table.replace('6', 'A')
new_table = new_table.replace('7', 'C')
new_table = new_table.replace('8', 'B')
print(new_table)  # FH FG FE HF HD HC GF GE GC EF EG EB DH DA DB AD AB CH CG BE BD BA
'''


# https://education.yandex.ru/ege/inf/task/3179b487-c412-4d3c-ae85-fbb2f27aebfc
'''
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 13 21 23 25 31 32 34 35 36 37 43 46 52 53 57 63 64 67 73 75 76'
graph = 'АБ БА АВ ВА АГ ГА АД ДА АЕ ЕА АК КА БВ ВБ ВГ ГВ ГД ДГ ДЕ ЕД ЕК КЕ'
for p in permutations('АБВГДЕК'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # Б В А К Г Е Д
        # К Е А Б Д В Г
'''
# 1 2 3 4 5 6 7
# Б В А К Г Е Д

# ВГ + ДЕ = 25 + 76 = 6 + 13 = 19


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


print('1 2 3 4 5 6 7 8')
from itertools import *
table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'HD DH HB BH HF FH DA AD AG GA AC CA GC CG GE EG EF FE BC CB'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
# 1 2 3 4 5 6 7 8
# G E B D C H F A
# GE + FH = 12 + 76 = 15 + 37 = 52


print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'AD AG AC BC BH CA CB CG DA DH EF EG FE FH GE GA GC HB HD HF'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 13, 14, 15, 16, 17, 23, 19-21, 25, 27]
# КЕГЭ = []
# на следующем уроке:
