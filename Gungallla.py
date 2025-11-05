# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from itertools import permutations
print('1 2 3 4 5 6 7 8')
table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'HD DH HF FH HB BH DA AD AG GA AC CA GE EG GC CG CB BC EF FE'
for per in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*per)
        # 1 2 3 4 5 6 7 8
        # G E B D C H F A
        # G E D B A H F C

'''
from itertools import permutations
print('1 2 3 4 5 6 7')
table = '12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76'
graph = 'AG GA AF FA GE EG EB BE BD DB DC CD BC CB CF FC GF FG'
for p in permutations ('ABCDEFG'):
    new_table=table
    for i in range(1, 7+1):
        new_table=new_table.replace(str(i), p[i-1])
    if set(new_table.split())==set(graph.split()):
        print(*p)
'''


# № 23260 Основная волна 11.06.25 (Уровень: Базовый)
from itertools import permutations
print ('1 2 3 4 5 6 7 8')
table = '13 14 16 23 24 28 31 32 41 42 47 56 57 58 61 65 74 75 78 82 85 87'
graph = 'AE EA EG GE GF FG FC CF CD DC DA AD AH HA HG GH HB BH BC CB BD DB'
for p in permutations('ABCDEFGH'):
    newt=table
    for i in range(1, 8+1):
        newt=newt.replace(str(i), p[i-1])
    if set(newt.split())==set(graph.split()):
        print(*p)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
