# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    k = 0
    if len(set(M)) == len(M):
        k += 1
    M = sorted(M)
    if M[-1] > (M[0] + M[1] + M[2] + M[3] + M[4]):
        k += 1
    if k == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/0cee3383-2699-4e0d-a2f1-5f50a85ad086
'''
cnt = 0
from itertools import permutations
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    M = sorted(M)
    if M[-1] < (M[0] + M[1] + M[2]):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/342217d2-3e89-4933-a422-940d9668bfa3
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(uncopied) == 3:
        if sum(copied) ** 2 > sum(uncopied) ** 2:
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 17


# Первый пробник 21.12.24:
# Тимур 6/29 -> 40 вторичных баллов +[12, 14, 16, 19, 23, 25] -[4, 5, 6, 7, 8, 10, 11, 13]

# Второй пробник 28.02.25:
# Тимур 9/29 -> 48 вторичных баллов +[1, 2, 7, 16, 19-21, 23, 25] -[5, 6, 8, 9, 13, 14, 17]
