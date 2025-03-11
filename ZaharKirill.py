# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/0cee3383-2699-4e0d-a2f1-5f50a85ad086
'''
from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if max(M) < sum(M) - max(M):
    # if M[-1] < M[0] + M[1] + M[2]:
    if M[-1] < sum(M[:-1]):
        if any(P[0] + P[1] == P[2] + P[3] for P in permutations(M)):
            cnt += 1
print(cnt)
'''

'''
from itertools import *
M = [9, 18, 19, 20]
for P in permutations(M):
    print(P)
    # (9, 18, 19, 20)
    # (9, 18, 20, 19)
    # (9, 19, 18, 20)
    # (9, 19, 20, 18)
    # (9, 20, 18, 19)
    # (9, 20, 19, 18)
    # (18, 9, 19, 20)
    # (18, 9, 20, 19)
'''


# https://education.yandex.ru/ege/task/d2c3cbfd-85f3-4d63-a34e-ad3278d25635
'''
from math import prod
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    # if max(M) ** 2 > M[0] * M[1] * M[2] * M[3]:
    if max(M) ** 2 > prod(M[:-1]):
        if (M[-1] + M[-2]) > (M[0] + M[1] + M[3]) * 2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/96c09be1-da8c-4460-b91f-05f352ddaa78
# Определите количество строк таблицы, содержащих числа,
# для которых выполнено строго одно из условий:
# в строке есть повторяющиеся числа;
# в строке есть ровно три нечётных числа.
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(M) != len(set(M)):
        flag += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(M) / 7:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/d73c5edf-63bd-47d8-87cb-7810e03725a0
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(M) == len(set(M)):
        if 5 * (M[0] + M[-1]) >= 3 * (M[1] + M[2] + M[3] + M[4]):
            cnt += 1
print(cnt)
'''


cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(M) == len(set(M)):
         if sum(M) % 3 == 0:
            cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]

# Второй пробник 28.02.25:
# Захар 7/13 -> 43 вторичных баллов +[1, 2, 10, 12, 14, 15, 16] -[4, 5, 6, 8, 13, 17, 23, 25]
# Kirill 6/13 -> 40 вторичных баллов +[2, 10, 13, 14, 15, 16] -[5, 6, 8, 12, 17, 23, 25]