# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 9 №51978
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                cnt += 1
print(cnt)
'''


# Тип 9 №61355
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):
        if (max(M) + min(M)) / 2 > (sum(M) - max(M) - min(M)) / 4:
            cnt += 1
print(cnt)

cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if len(M) == len(set(M)):
        if (M[0] + M[-1]) / 2 > sum(M[1:-1]) / 4:
            cnt += 1
print(cnt)
'''


# Тип 9 №68510
'''
from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[-1] < sum(M[:-1]):
        if any(m[0] + m[1] == m[2] + m[3] for m in permutations(M)):
            cnt += 1
print(cnt)
'''


# Тип 9 №63058
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if len(M) != len(set(M)):
        if M.count(max(M)) == 1:
            copied = [x for x in M if M.count(x) > 1]
            if sum(copied) < max(M):
                cnt += 1
print(cnt)
'''


# № 18924 Новогодний вариант 2025 (Уровень: Средний)

cnt = 0
for s in open('0. files/9.csv'):
    flag = 0
    M = sorted([int(x) for x in s.split(';')])
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        flag += 1
    if sum([x**2 for x in copied]) > sum(not_copied) ** 2:
        flag += 1
    if flag != 2:
        cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]
