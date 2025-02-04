# region Домашка: ******************************************************************


# № 12249 ЕГКР 16.12.23 (Уровень: Базовый)
'''
D = [int(x) for x in open('0. files/17.txt')]
R = []
L = [x for x in D if abs(x) % 10 == 3]
T = [x for x in L if len(str(abs(x))) == 5]
for i in range(len(D) - 2):
    x, y, z = D[i], D[i + 1], D[i + 2]
    if ((x in L) + (y in L) + (z in L)) >= 1:
        if (x + y + z) <= max(T):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 12471 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if x % 2 == 0]
B = [x for x in M if len(str(abs(x))) == 2]
D = [x for x in M if abs(x) % 100 == 13]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i], M[i + 1], M[i + 2]
    if ((x in A) + (y in A) + (z in A) == 3) or ((x in B) + (y in B) + (z in B) >= 1):
        if (x + y + z) <= max(D):
            R.append((x + y + z))
print(len(R), sum(R) // len(R))
'''


# № 9547 Джобс 14.06.23 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 3 and abs(x) % 100 == 11]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if ((len(str(abs(x))) == 3) + (len(str(abs(y))) == 3)) == 1:
        if (abs(x - y)) % min(D) == 0:
            R.append(x + y)
print(len(R), max(R))  
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/1db660ae-e018-4537-be70-be01199dfa29
'''
from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if (max(M) + min(M)) % 3 == 0:
        if any(p[0] - p[1] == p[2] - p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/d62dc568-941a-44da-870b-b8cc21faee9f
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if sum(nechet) > sum(chet):
        flag += 1
    copied2 = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(not_copied) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/d3ce64c1-1875-458b-b8d6-ae96bb169c58
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    coped2 = [x for x in M if M.count(x) == 2]
    not_coped = [x for x in M if M.count(x) == 1]
    if len(coped2) >= 2:
        if len(not_coped) == 0:
            not_coped = [0]
        if min(coped2) > max(not_coped):
            cnt += 1
print(cnt)
'''
# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке: 24


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
