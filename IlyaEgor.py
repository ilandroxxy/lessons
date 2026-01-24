# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from itertools import *
graph = 'AC CA AD DA AG GA GC CG GE EG EF FE FH HF HD DH HB BH BC CB'
table = '13 16 18 23 24 31 32 36 42 47 56 57 61 63 65 74 75 78 81 87'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1,8+1):
        new_table=new_table.replace(str(i),p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке:
