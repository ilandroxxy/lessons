# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23368 Резервный день 19.06.25 (Уровень: Базовый)
'''
cnt = 0
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    if len(set(M)) == len(M):
        # if 2 * (min(M) + max(M)) == 3 * (sum(M) - min(M) - max(M)):
        M = sorted(M)
        if 2 * (M[0] + M[-1]) == 3 * (M[1] + M[2] + M[3]):
            print(f'Номера строки: {n}')
            cnt += 1
print(f'Кол-во строк: {cnt}')
'''
from subprocess import check_call

# https://education.yandex.ru/ege/inf/task/96c09be1-da8c-4460-b91f-05f352ddaa78
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


# https://education.yandex.ru/ege/inf/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied1) == 3 and len(copied2) == 4:
        if sum(copied2) / 4 < sum(M) / 7:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/82c97d22-18da-44ce-aafa-9e25f9e55301
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied2) == 6:
        a, b, c = sorted(set(M))
        if c**2 == a**2 + b**2:
            cnt += 1
print(cnt)
'''


'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied1) == 3:
        if sum(copied3) ** 2 > sum(copied1)**2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/679cf8d3-a852-4dc0-a42f-e8b4825ea271
'''
n = 0
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied3 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(copied3) == 3 and len(copied1) == 3:
        if copied3[0] > copied2[0]:
            cnt += 1
            print(n)
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/0cee3383-2699-4e0d-a2f1-5f50a85ad086
'''
from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if any(P[0] + P[1] == P[2] + P[3] for P in permutations(M)):
            cnt += 1
print(cnt)
'''
# for P in permutations([1, 2, 3, 4]):
#     print(P)


# https://education.yandex.ru/ege/inf/task/97f8b640-7a4b-4540-a62f-2c161e9507e0
'''
from math import prod
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) >= 2 and len(nechet) >= 2:
        if 3 * sum(nechet) > prod(chet):
            cnt += 1
print(cnt)
'''

# Все числа, содержащиеся в строке, больше 10
'''
M = [35, 34, 23, 123]
# if M[0] > 10 and M[1] > 10 and M[2] > 10 and M[3] > 10:
if all(p > 10 for p in M):
    print(M)
'''


# https://education.yandex.ru/ege/inf/task/c51900be-b855-4ffb-97d5-8402bb52ffd8

from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if all(P[0] + P[1] != P[2] + P[3] for P in permutations(M)):
            cnt += 1
print(cnt)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 9, 14, 15, 16, 17, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке: Из пробника глянуть 8, 17 номера
