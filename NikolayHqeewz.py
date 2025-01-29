# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/3c10485a-aca0-427e-8464-c7669e3315f9
'''
from itertools import *
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if M[-2]**2 > (M[0] * M[-1]):
        if any(B[0] * B[1] == B[-2] * B[-1] for B in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    if len(copied) > 0:
        if len(set(M)) == 5:
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/9222d062-000f-4b29-80d0-86b20f9119d2
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(not_copied) == 4 and len(copied) == 2:
        if copied[0] >= (sum(not_copied) / 4):
            print(n)
            break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Николай 9/19 -> 48 вторичных баллов +[1, 2, 4, 7, 13, 14, 16, 23, 25] -[5, 6, 8, 9, 12, 15, 17, 24]
