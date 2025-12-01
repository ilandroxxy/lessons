# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/inf/task/7eeb5357-91a8-4e1a-b4ec-dafe92df2f09
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied1) == 3:
        if (3 * (copied3[0] ** 2)) > (copied1[0] ** 2 + copied1[1] ** 2 + copied1[2] ** 2):
            cnt += 1
print(cnt)


cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied1) == 3:
        flag += 1
    if len(copied3) == 3 and len(copied1) == 3:
        if (3 * (copied3[0] ** 2)) > (copied1[0] ** 2 + copied1[1] ** 2 + copied1[2] ** 2):
            flag += 1
    if flag == 2:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/22cf7ea4-d582-409f-b6ab-8fe3b9fe4728
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) > 1]
    if len(copied) > 0:
        M = sorted(M)
        if 2 * (min(M) ** 2) > (M[1] * M[2]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/9222d062-000f-4b29-80d0-86b20f9119d2
'''
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(copied1) == 4:
        if copied2[0] >= sum(copied1) / 4:
            print(n)
            break
'''


# https://education.yandex.ru/ege/inf/task/f4fdf6fb-9ba6-4a16-b901-0b495310b132
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





# # endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 27
