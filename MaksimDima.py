# region Домашка: ******************************************************************

# № 17535 Основная волна 07.06.24 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline().split('CD')
maxi = 0
for i in range(len(s)-160):
    r = 'D' + 'CD'.join(s[i:i+161]) + 'C'
    maxi = max(maxi, len(r))
print(maxi)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19410 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6')
table = '12 14 15 21 23 26 32 35 41 45 51 53 54 62'
graph = 'ГБ БГ ВБ БВ БА АБ АД ДА ДВ ВД ДЕ ЕД ЕВ ВЕ'
for p in permutations('АБВГДЕ'):
    new_table = table
    for i in range(1, 6+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6
# В Б А Е Д Г


'''
from itertools import *
print('1 2 3 4 5 6 7 8 9')
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KC CK KB BK CD DC BD DB DH HD DG GD DE ED EF FE FG GF GH HG'
for p in permutations('ABCDEFGHK'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7 8 9
# B G C D K A E F H
# C G B D K A E F H

# Ответ: 8 + 15 = 23

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo разобрать задачку Тип 24 №59847
'''
s = open('0. files/24.txt').readline()
s = s.replace('WW', ' ')
s = s.split()
maxi = 0
for i in range(len(s)-100):
    r = 'W' + 'WW'.join(s[i:i+101]) + 'W'
    maxi = max(maxi, len(r))
print(maxi)
'''

from turtle import *
print(bk)

# зацепка может быть тут https://inf-ege.sdamgia.ru/problem?id=59729
# В строке TTTT пара символов встречается ровно 3 раза.

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 4, 5, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]
