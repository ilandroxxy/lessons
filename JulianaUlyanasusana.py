# region Домашка: ******************************************************************

# № 6696 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

    if (x + y + z) % 2022 == 0:
        # if (x > 0) or (y > 0) or (z > 0):
        if (x > 0) + (y > 0) + (z > 0) >= 1:
            R.append(x + y + z)
print(len(R), max(R))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
cnt = 0
for s in open('0. files/9.csv'):
    print(s)  # 49;20;13;90;55;28;87
    M = [int(x) for x in s.split(';')]
    print(M)  # [49, 20, 13, 90, 55, 28, 87]
'''

# https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3:
        if len(set(M)) == 5:
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied = [x for x in M if M.count(x) == 2]  # 5 5
    not_copied = [x for x in M if M.count(x) == 1]  # 4 5 6
    if len(copied) == 4 and len(not_copied) == 3:
        # if sum(copied) / len(copied) < sum(M) / len(M):
            print(sum(copied) / len(copied), sum(M) / len(M), copied, M)
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/82c97d22-18da-44ce-aafa-9e25f9e55301
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied = [x for x in M if M.count(x) == 2]
    if len(copied) == 6:
        a, b, c = sorted(set(M))
        if a ** 2 + b ** 2 == c ** 2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    flag = 0
    if len(M) == len(set(M)):  # все числа различны;
        flag += 1
    # if max(M) > sum(M) - max(M):
    if max(M) > sum(M[:-1]):
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
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 14 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]
