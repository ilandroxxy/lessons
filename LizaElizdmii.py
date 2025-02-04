# region Домашка: ******************************************************************

# № 7038 (Уровень: Средний) 🌶
'''
M = [int(x) for x in open('0. files/17.txt')]
N = [x for x in M if str(x)[-1] == '1']

avg = 0
mini = 10**9
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (x in N) + (y in N) == 1:
        avg = max(avg, (x + y) / 2)
        mini = min(mini, min(x, y))

cnt = 0
maxi = 0
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (x in N) + (y in N) == 1:
        if (x < avg) + (y < avg) == 2:
            cnt += 1
            if mini in (x, y):
                maxi = max(maxi, max(x, y))

print(cnt, maxi)
'''


# № 16264 Джобс 03.05.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 2 and x % sum(map(int, str(x))) == 0]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (x % min(D) == 0) + (y % min(D) == 0) >= 1:
        R.append(x + y)
print(len(R), max(R))
'''


# № 7029 Danov2303 (Уровень: Базовый)
'''
from itertools import *

for n, p in enumerate(product(sorted('МАРИН'), repeat=8), 1):
    word = ''.join(p)
    if word == 'МАРИАННА':
        print(n)
        break
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/c51900be-b855-4ffb-97d5-8402bb52ffd8
'''
from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if max(M) < sum(M) - max(M):
    if M[-1] < sum(M[:-1]):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/342217d2-3e89-4933-a422-940d9668bfa3
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(not_copied) == 3:
        if sum(copied3) ** 2 > sum(not_copied) ** 2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/82c97d22-18da-44ce-aafa-9e25f9e55301
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied_2 = [x for x in M if M.count(x) == 2]
    if len(copied_2) == 6:
        a, b, c = sorted(set(copied_2))
        if a**2 + b**2 == c**2:
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
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Лиза 11/14 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

