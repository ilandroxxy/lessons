# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19233 ЕГКР 21.12.24 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'BD DB BE EB BC CB DE ED DG GD EH HE CH HC HF FH FG GF FA AF GA AG'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # E H B D F A C G
'''


# https://education.yandex.ru/ege/inf/task/3179b487-c412-4d3c-ae85-fbb2f27aebfc

print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 13 21 23 25 31 32 34 35 36 37 43 46 52 53 57 63 64 67 73 75 76'
graph = 'АБ БА АВ ВА АГ ГА АД ДА АЕ ЕА АК КА БВ ВБ ВГ ГВ ГД ДГ ДЕ ЕД ЕК КЕ'
for p in permutations('АБВГДЕК', r=7):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # Б В А К Г Е Д
        # К Е А Б Д В Г







''' 
    # i 0    1    2    3    4    5    6    7
    # ('H', 'G', 'F', 'E', 'D', 'C', 'A', 'B')
    #   1    2    3    4    5    6    7    8

    new_table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
    new_table = new_table.replace('1', 'H')
    new_table = new_table.replace('2', 'G')
    new_table = new_table.replace('3', 'F')
    new_table = new_table.replace('4', 'E')
    new_table = new_table.replace('5', 'D')
    new_table = new_table.replace('6', 'C')
    new_table = new_table.replace('7', 'A')
    new_table = new_table.replace('8', 'B')
    print(new_table)  # HG HF HE GH GD GA FH FE FA EH EF EB DG DC DB CD CB AG AF BE BD BC
'''
# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 8, 13, 14, 15, 16, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке: 17, 9, 27
