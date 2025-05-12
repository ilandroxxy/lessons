# region Домашка: ******************************************************************
from pprint import pformat

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21895 Открытый вариант 2025 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(set(M)) == len(M):
        M = sorted(M)
        if M[-1] + M[-2] <= M[0] + M[1] + M[2]:
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/589b20f9-9916-4971-bd8a-5123b74eac00
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 4 and len(uncopied) == 3:
        if sum(uncopied) / 3 <= sum(M) / 7:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/4a521e4c-c1ac-440a-8fb2-3aa0bc59172c
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    A = [x for x in M if abs(x) % 10 == 3]
    if len(A) == 3:
        C = [x for x in M if x > 0]
        D = [x for x in M if x < 0]
        if sum(C) ** 2 < sum(D) ** 2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/96c09be1-da8c-4460-b91f-05f352ddaa78
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(set(M)) != len(M):
        flag += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 24, 26, 27
