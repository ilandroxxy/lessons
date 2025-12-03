# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23547 Пересдача 03.07.25 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76'
graph = 'AF FA AG GA FC CF FG GF CB BC CD DC DB BD BE EB GE EG'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # A F C G E D B  2 + 5 = 7
        # D C F B E A G  5 + 2 = 7
'''


# № 23360 Резервный день 19.06.25 (Уровень: Базовый)

print('1 2 3 4 5 6 7')
from itertools import permutations
table = '13 14 15 24 26 27 31 34 41 42 43 45 46 47 51 54 57 62 64 72 74 75'
graph = 'GA AG GF FG GE EG GC CG GB BG GD DG AF FA FE EF ED DE DC CD CB BC'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '13 14 16 23 24 28 31 32 41 42 43 45 46 47 51 54 57 62 64 72 74 75'
graph = 'GA AG GF FE GE EG GC CG GB BG GD DG AF FA FE EF ED DE DC CD CB BC'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

# endregion Урок: *************************************************************
#
# ФИПИ = [1, 2, 5, 6, 8, 13, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
