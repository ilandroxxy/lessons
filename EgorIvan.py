# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 25348 ЕГКР 13.12.25 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '13 16 18 23 24 31 32 36 42 47 56 57 61 63 65 74 75 78 81 87'
graph = 'HD DH HF FH HB BH FE EF EG GE GC CG GA AG AC CA AD DA BC CB'
for p in permutations('ABCDEFHG'):
    nt = table
    for i in range(1, 8+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # A E G F B C H D
        # C E G F D A H B
'''

'''
    #   0    1    2    3    4    5    6    7
    # ('G', 'H', 'F', 'E', 'D', 'A', 'C', 'B')
    #   1    2    3    4    5    6    7    8

    nt = '13 16 18 23 24 31 32 36 42 47 56 57 61 63 65 74 75 78 81 87'
    nt = nt.replace('1', 'G')
    nt = nt.replace('2', 'H')
    nt = nt.replace('3', 'F')
    nt = nt.replace('4', 'E')
    nt = nt.replace('5', 'D')
    nt = nt.replace('6', 'A')
    nt = nt.replace('7', 'C')
    nt = nt.replace('8', 'B')
    print(nt)
    # GF GA GB HF HE FG FH FA EH EC DA DC AG AF AD CE CD CB BG BC
'''




# № 19233 ЕГКР 21.12.24 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'BD DB BE EB BC CB CH HC HE EH HF FH ED DE DG GD GF FG GA AG AF FA'
for p in permutations('ABCDEFHG'):
    nt = table
    for i in range(1, 8+1):`
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # E H B D F A C G
'''


print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '13 18 24 27 31 35 38 42 46 47 48 53 57 64 67 72 74 75 76 81 83 84'
graph = 'CD DC DH HD CH HC CB BC HG GH FB BF FA AF AE EA BE EB AG GA AB BA '
for p in permutations('ABCDEFHG'):
    nt = table
    for i in range(1, 8+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)

# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
