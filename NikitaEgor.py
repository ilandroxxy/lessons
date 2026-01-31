# region Домашка: ******************************************************************

# № 23186 Основная волна 10.06.25 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= y) and z and (not w)
                if F == 1:
                    print(x, y, z, w)
'''

# (x or y) and (not(y == z)) and (not w)
# ((x <= y) or (y == w)) and ((x or z) == w)
# ((y <= x) and (z or w)) <= ((x and (not w)) or (y == z))



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: *************************************************************

'''
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76'
graph = 'AG GA AF FA GF FG GE EG EB BE BC CB BD DB DC CD CF FC'
for p in permutations('ABCDEFG'):
    nt = table
    for i in range(1, 7+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # A F C G E D B
        # D C F B E A G
'''


# i 0    1    2    3    4    5    6
# ('G', 'F', 'E', 'D', 'B', 'A', 'C')
#   1    2    3    4    5    6    7

nt = '12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76'
nt = 'G2 G4 2G 23 24 32 36 37 4G 42 45 54 57 63 67 73 75 76'
nt = 'GF G4 FG 23 F4 3F 36 37 4G 4F 45 54 57 63 67 73 75 76'
nt = 'GF G4 FG 2E F4 EF E6 E7 4G 4F 45 54 57 6E 67 7E 75 76'



# № 25340 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '13 16 18 23 24 31 32 36 42 47 56 57 61 63 65 74 75 78 81 87'
graph = 'AC CA AD DA AG GA CG GC CB BC GE EG EF FE FH HF BH HB HD DH'
for p in permutations('ABCDEFGH'):
    nt = table
    for i in range(1, 8+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
'''

# Никита № 23260 Основная волна 11.06.25 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations

table = '13 14 16 23 24 28 31 32 41 42 47 56 57 58 61 65 74 75 78 82 85 87'
graph = 'AD DA DB BD DC CD CF FC CB BC BH HB FG GF GE EG AH HA AE EA HG GH'
for p in permutations('ABCDEGHF'):
    nt = table
    for i in range(1, 8 + 1):
        nt = nt.replace(str(i), p[i - 1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
'''


# № 20598 (Уровень: Базовый)
'''
print ('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 17 21 24 26 27 34 35 37 42 43 46 53 57 62 64 71 72 73 75'
graph = 'АЕ ЕА ЕБ БЕ БЖ ЖБ ЖД ДЖ ДГ ГД ГВ ВГ ВА АВ ЕВ ВЕ ЕЖ ЖЕ ЖГ ГЖ'
for p in permutations ('АБВГДЕЖ'):
    nt = table
    for i in range(1, 7+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set (graph.split()):
        print(*p)
'''

# № 18308 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8 9')
from itertools import permutations
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KC CK KB BK BD DB CD DC DH HD DE ED EF FE FG GF GD DG HG GH'
for p in permutations('ABCDEFGHK'):
    nt = table
    for i in range(1,9+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
