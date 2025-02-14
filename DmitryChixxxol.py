# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied2 = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(not_copied) == 3:
        if M[0] * M[1] > sum(M[2:]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/f4fdf6fb-9ba6-4a16-b901-0b495310b132

from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[-1] < sum(M[:-1]):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M, r=4)):
            cnt += 1
print(cnt)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]
