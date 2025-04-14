# region Домашка: ******************************************************************
from os.path import split

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


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


# https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(set(M)) == 5:
        if sum(M) < 502:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/1e999a1a-d2c1-4bcd-9169-6a90e39b17e9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(uncopied) == 5:
        if M.count(max(M)) == M.count(min(M)):
            cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Второй пробник 28.02.25:
# Артем 4/29 -> 27 вторичных баллов +[2, 10, 15, 16] -[1, 5, 6, 8, 12, 13, 14, 23]
