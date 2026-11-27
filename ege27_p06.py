# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if ....:
        cnt += 1
print(cnt)

n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    n += 1
    if ....:
        print(n)
'''

# № 31506 Демоверсия 2027(Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке пять
# натуральных чисел. Определите количество строк таблицы, для которых
# выполнены оба условия:
# – в строке все числа различны;
# – удвоенная сумма максимального и минимального чисел строки больше
# суммы оставшихся трёх её чисел.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    # if len(M) == len(set(M)):
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied1) == len(M):
        if 2 * (min(M) + max(M)) > sum(M) - min(M) - max(M):
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
    if len(copied1) == 3 and len(copied2) == 4:
        if sum(copied2) / len(copied2) < sum(M) / len(M):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/a0782df8-aa0e-44a4-b6f5-ad22798c940b
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(set(M)) == len(M):
        if 2 * (M[-1] + M[0]) <= 3 * (M[1] + M[2] + M[3]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(set(M)) == 5:
        if sum(M) < 502:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/97f8b640-7a4b-4540-a62f-2c161e9507e0
'''
from math import prod
cnt = 0
for s in open('files/9.txt'):
    M = sorted([int(x) for x in s.split()])
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) >= 2 and len(nechet) >= 2:
        if 3 * sum(nechet) > prod(chet):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/5c54e314-516a-44fb-b41f-b06ffe3345af
'''
cnt = 0
from itertools import permutations
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if max(M) < sum(M) - max(M):
        if sum(M) % 2 == 0:
            if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M, r=4)):  # четыре числа строки можно разбить на две пары чисел с равными суммами
                cnt += 1
print(cnt)
'''


# четыре числа строки можно разбить на две пары чисел с равными суммами
# if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M, r=4)):

# if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M, r=4)):
# четыре числа строки нельзя разбить на две пары чисел с равными суммами






# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 8, 9, 10, 15, 16, 19-21, 23, 25]
# КЕГЭ = []
# todo на следующем уроке: 17, 24
