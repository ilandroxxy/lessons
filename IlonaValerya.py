# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from itertools import *
print('1 2 3 4 5 6 7 8')
table = '12 13 21 26 28 31 35 38 45 47 48 53 54 57 62 67 74 75 76 82 83 84'
graph = 'AE EA AF FA FD DF FC CF CG GC GB BG GH HG BH HB BD DB DE ED EH HE'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

# 1 2 3 4 5 6 7 8
# A F E B H C G D


from itertools import *
print('1 2 3 4 5 6 7')
table = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
graph = 'AE EA AC CA ED DE EF FE FC CF FG GF CG GC GB BG BD DB'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
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
# ФИПИ = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке:
