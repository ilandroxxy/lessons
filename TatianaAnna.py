# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038775/step/2?unit=1062778
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range (len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))
'''


# https://stepik.org/lesson/1038775/step/5?unit=1062778
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 7 == 0]
B = [x for x in M if hex(x)[-2:] == '0f']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) % max(B) == 0:
            R.append(x + y)
print(len(R), max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import permutations
print('1 2 3 4 5 6 7')
table = '12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76'
graph = 'AF FA AG GA FC CF FG GF GE EG EB BE BD DB BC CB DC CD'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # A F C G E D B
        # D C F B E A G
'''
# ('G', 'F', 'E', 'D', 'C', 'B', 'A')
# 12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76
# GF GD FG FE FD EF EB EA DG DF DC CD CA BE BA AE AC AB



# № 23260 Основная волна 11.06.25 (Уровень: Базовый)
'''
from itertools import permutations
print('1 2 3 4 5 6 7 8')
table = '13 14 16 23 24 28 31 32 41 42 47 56 57 58 61 65 74 75 78 82 85 87'
graph = 'AE AH AD EA HA DA EG GE GH HG GF FG FC CF CB BC CD DC DB BD BH HB'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''

# № 23185 Основная волна 10.06.25 (Уровень: Базовый)
'''
from itertools import permutations
print('1 2 3 4 5 6 7 8')
table = '14 17 18 23 28 32 35 36 41 45 53 54 63 67 71 76 78 81 82 87'
graph = 'AG GA AH HA GD DG GC CG DE ED EF FE FB BF FH HF HB BH BC CB'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 7, 11
