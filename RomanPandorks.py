# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'DG GD DE ED DB BD GA AG GF FG AF FA FH HF HE EH CH HC CB BC BE EB'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # E H B D F A C G
'''

''' #   0    1    2    3    4    5    6    7
    # ('H', 'G', 'D', 'C', 'E', 'A', 'B', 'F')
    #   1    2    3    4    5    6    7    8

new_table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
new_table = new_table.replace('1', 'H')
new_table = new_table.replace('2', 'G')
new_table = new_table.replace('3', 'D')
new_table = new_table.replace('4', 'C')
new_table = new_table.replace('5', 'E')
new_table = new_table.replace('6', 'A')
new_table = new_table.replace('7', 'B')
new_table = new_table.replace('8', 'F')
print(new_table)  # HG HD HC GH GE GB DH DC DB CH CD CF EG EA EF AE AF BG BD FC FE FA
'''

# https://education.yandex.ru/ege/inf/task/82df2109-2dda-4dde-b9b3-280de76e3e32
'''
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 13 14 15 21 31 34 37 41 43 46 47 51 64 73 74'
graph = 'БВ ВБ ВЕ ЕВ ВА АВ ВГ ГВ ГА АГ ГД ДГ ГК КГ АД ДА'
for p in permutations('АБВГДЕК'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # В Б А Г Е К Д
        # В Е А Г Б К Д
'''


# https://education.yandex.ru/ege/inf/task/8ef563df-ce71-4da9-bd5c-9bbe34d9fa0c
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 14 15 16 17 21 27 31 35 37 41 45 46 51 53 54 61 64 71 72 73'
graph = 'DE ED DB BD EC CE BC CB EF FE CF FC CA AC AG GA CG GC FG GF DC CD'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # C A F D E B G H
        # C B E G F A D H
'''


# https://education.yandex.ru/ege/inf/task/481dc321-abd7-4acc-b7e0-84429853ae20
'''
print('1 2 3 4 5 6 7 8 9')
from itertools import permutations
table = '13 14 15 16 18 19 24 29 31 34 35 41 42 43 51 53 58 61 67 68 76 79 81 85 86 91 92 97'
graph = 'АБ БА АГ ГА БД ДБ ГД ДГ ГЖ ЖГ ЖД ДЖ ЗЖ ЖЗ ЗД ДЗ ИЗ ЗИ ДИ ИД ИЕ ЕИ ЕД ДЕ ЕВ ВЕ ВБ БВ'
for p in permutations('АБВГДЕЖЗИ'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 13, 14, 15, 16, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
