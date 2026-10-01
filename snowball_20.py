# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 31506 Демоверсия 2027(Уровень: Базовый)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if len(M) == len(set(M)):  # – в строке все числа различны;
        if 2 * (max(M) + min(M)) > sum(M) - max(M) - min(M):
            cnt += 1
print(cnt)


cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied1) == len(M):
        if 2 * (max(M) + min(M)) > M[1] + M[2] + M[3]:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/96c09be1-da8c-4460-b91f-05f352ddaa78
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    nechet = [x for x in M if x % 2 != 0]
    flag = 0
    if len(M) != len(set(M)):
        flag += 1
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3:
        if len(set(M)) == 5:
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied2) == 4 and len(copied1) == 3:
        if sum(copied2) / len(copied2) < sum(M) / len(M):
            cnt += 1
print(cnt)
'''



# https://education.yandex.ru/ege/inf/task/c51900be-b855-4ffb-97d5-8402bb52ffd8
'''
from itertools import permutations
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if max(M) < sum(M) - max(M):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M, r=4)):
            cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [14, 22]
# КЕГЭ = []
# на следующем уроке:



