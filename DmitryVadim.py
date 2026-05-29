#
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 29333 Открытый вариант 2026 (Уровень: Базовый)
# Определите, какова протяжённость дороги из пункта В в пункт Д.
# В ответе запишите целое число – так, как оно указано в таблице.
'''
print('1 2 3 4 5 6 7')
from itertools import *
table = '12 17 21 25 26 27 36 37 45 52 54 56 62 63 65 67 71 72 73 76'
graph = 'АБ БА БВ ВБ БД ДБ ВД ДВ ВГ ГВ ВЕ ЕВ ДЕ ЕД ДК КД ЕК КЕ ГЕ ЕГ'
for p in permutations('АБВГДЕК'):
    new_table = table
    for i in range(1, 7 + 1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# № 29951 Апробация 14.05.26 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import *
table = '15 16 17 23 24 28 32 37 38 42 47 51 56 58 61 65 71 73 74 82 83 85'
graph = 'BA AB BH HB AH HA HF FH AE EA EG GE FG GF GC CG EC CE FD DF DC CD'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8 + 1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# № 28922 ЕГКР 18.04.26 (Уровень: Базовый)

print('1 2 3 4 5 6 7 8')
from itertools import *
table = '14 17 24 25 28 36 37 41 42 45 52 54 56 63 65 71 73 78 82 87'
graph = 'AB BA AH HA BD DB BG GB GC CG DC CD DF FE HF FH FE EF EG GE'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8 + 1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [4, 5, 12, 13, 14, 19-21]
# на следующем уроке: Задачи 8 на цифры




