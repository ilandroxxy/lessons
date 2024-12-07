# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 1 https://education.yandex.ru/ege/task/e84c3039-e331-433b-bf3d-068e941beeed
'''
from itertools import *
table = '12 13 15 17 21 26 27 31 34 35 43 45 47 51 53 54 56 57 62 65 67 71 72 74 75 76'
graph = 'KQ QK QA AQ AK KA AC CA QC CQ CB BC BA AB AR RA RB BR BP PB RP PR KB BK KP PK'
print('1 2 3 4 5 6 7')
for p in permutations('KQARPCB'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7
# K Q P R B C A
# K P Q C A R B


# Задание 1 https://education.yandex.ru/ege/task/9d2228f8-6ca3-4819-9708-af4bc8555701

from itertools import *
table = '12 17 21 25 27 29 36 37 46 48 52 59 63 64 67 68 71 72 73 76 78 79 84 86 87 92 95 97'
graph = 'EH HE EB BE HB BH BA AB BD DB AD DA HD DH DC CD CG GC DG GD DF FD FG GF FI IF GI IG '
print('1 2 3 4 5 6 7 8 9')
for p in permutations('EHBDACGFI'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

# 1 2 3 4 5 6 7 8 9
# A B C I E G D F H
# C G A E I B D H F

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
