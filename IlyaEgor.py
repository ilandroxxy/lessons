# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Кол-во строк подходящих по условию
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if ....:
        cnt += 1
print(cnt)
'''

# Номер строки подходей по условию
'''
R = []
n = 0
for s in open('files/9.csv'):
    n += 1
    M = [int(x) for x in s.split(',')]
    if ....:
        R.append(n)
print(min(R), max(R))
'''

# https://education.yandex.ru/ege/inf/task/98f82f6a-421e-427a-809c-3f82763d9559
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    # if len(set(M)) == 4:
    # if len(set(M)) == len(M):
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied1) == 4:
        if (max(M) + min(M)) / 2 > (sum(M) - min(M) - max(M)) / 2:
            cnt += 1
print(cnt)

cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(set(M)) == len(M):
        if (M[-1] + M[0]) / 2 > (M[1] + M[2]) / 2:
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
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/d3ce64c1-1875-458b-b8d6-ae96bb169c58
# - Определите количество строк таблицы, для которых выполнены оба условия:
# в строке хотя бы одно число повторяется дважды (ровно 2 раза);
# - каждое из повторяющихся дважды (ровно 2 раза) чисел превышает
# каждое неповторяющееся.
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) > 0:
        if len(copied1) == 0:
            cnt += 1
            continue
        if min(copied2) > max(copied1):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/96c09be1-da8c-4460-b91f-05f352ddaa78
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    k = 0
    if len(M) != len(set(M)):
        k += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        k += 1
    if k == 1:
        cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке:
