# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/f89886b4-de58-4c14-b999-c17d6276c1a8
'''
def F(x, A):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)

R = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 20801 Апробация 05.03.25 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6 7')
table = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
graph = 'AC CA AE EA CF FC CG GC GF FG FE EF ED DE DB BD BG GB'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
'''

# i 0    1    2    3    4    5    6
# ('G', 'E', 'B', 'C', 'D', 'F', 'A')
'''
new_table = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
new_table = 'G2 16 2G 24 27 34 35 36 42 43 47 53 57 6G 63 72 74 75'
new_table = 'GE 16 EG E4 E7 34 35 36 4E 43 47 53 57 6G 63 7E 74 75'
new_table = 'GE 16 EG E4 E7 B4 B5 B6 4E 4B 47 5B 57 6G 6B 7E 74 75'
'''


# № 18308 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6 7 8 9')
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KB BK KC CK CD DC BD DB DE ED DG GD DH HD HG GH GF FG FE EF'
for p in permutations('ABCDEFGHK'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7 8 9
# B G C D K A E F H
# C G B D K A E F H

# FE = 8, ED = 15, итого: 23

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]

# Второй пробник 28.02.25:
# Женя 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 13, 14, 15, 16, 23, 25] -[8, 12]
# Ярослав 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 12, 13, 14, 15, 16, 23] -[8, 25]
