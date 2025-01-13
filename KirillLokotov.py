# region Домашка: ************************************************************

# https://stepik.org/lesson/1038775/step/5?unit=1062778
'''
M = [int(x) for x in open('files/17.txt')]
# D = [x for x in M if f'{x:X}'[-2:] == '0F']
# D = [x for x in M if f'{x:x}'[-2:] == '0f']
D = [x for x in M if hex(x)[-2:] == '0f']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 7 == 0) != (y % 7 == 0):
        if (x + y) % max(D) == 0:
            R.append(x + y)
print(len(R), max(R))
'''
# 2 9487


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# № 19241 ЕГКР 21.12.24 (Уровень: Базовый)
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 6 and len(not_copied) == 1:
        if sum(copied) / len(copied) < not_copied[0]:
            print(n)
'''


# № 18364 (Уровень: Средний)
'''
from math import *
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) != len(set(M)):
        copied = [x for x in M if M.count(x) > 1]
        not_copied = [x for x in M if M.count(x) == 1]
        if 3 * sum(not_copied) <= prod(copied):
            cnt += 1
print(cnt)
'''


# № 17968 (Уровень: Средний)
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if max(M) < M[0] + M[1] + M[2]:
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if sum(chet) == sum(nechet):
            cnt += 1
print(cnt)
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ = []
# на следующем уроке:
