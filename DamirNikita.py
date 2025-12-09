# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# № 23260 Основная волна 11.06.25 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '13 14 16 23 24 28 31 32 41 42 47 56 57 58 61 65 74 75 78 82 85 87'
graph = 'DC CD DB BD DA AD BC CB BH HB HG GH HA AH AE EA EG GE GF FG FC CF'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # G A E H C F B D
'''

'''
    # i 0    1    2    3    4    5    6    7
    # ('H', 'G', 'F', 'A', 'E', 'C', 'B', 'D')
    #   1    2    3    4    5    6    7    8

    new_table = '13 14 16 23 24 28 31 32 41 42 47 56 57 58 61 65 74 75 78 82 85 87'
    new_table = new_table.replace('1', 'H')
    new_table = new_table.replace('2', 'G')
    new_table = new_table.replace('3', 'F')
    new_table = new_table.replace('4', 'A')
    new_table = new_table.replace('5', 'E')
    new_table = new_table.replace('6', 'C')
    new_table = new_table.replace('7', 'B')
    new_table = new_table.replace('8', 'D')
    print(new_table)  # HF HA HC GF GA GD FH FG AH AG AB EC EB ED CH CE BA BE BD DG DE DB
'''


# № 23360 Резервный день 19.06.25 (Уровень: Базовый)

print('1 2 3 4 5 6 7')
from itertools import permutations
table = '13 14 15 24 26 27 31 34 41 42 43 45 46 47 51 54 57 62 64 72 74 75'
graph = 'GA AG GF FG GE EG GD DG GC CG GB BG BC CB CD DC DE ED EF FE FA AF'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # C F B G D A E
        # F C A G E B D



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
