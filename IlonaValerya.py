# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17522 Основная волна 07.06.24 (Уровень: Базовый)
# [20, 72, 11, 24] {20, 72, 11, 24} нет
# [20, 72, 11, 11] {20, 72, 11} два
# [20, 20, 11, 11] {20, 11} нет
# [11, 72, 11, 11] {11, 72} нет
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if len(set(M)) == 3:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/4a521e4c-c1ac-440a-8fb2-3aa0bc59172c
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    D = [x for x in M if str(x)[-1] == '3']
    if len(D) == 3:
        A = [x for x in M if x > 0]
        B = [x for x in M if x < 0]
        if sum(A) ** 2 < sum(B) ** 2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    k = 0
    if len(M) == len(set(M)):
        k += 1
    if M[5] > M[0] + M[1] + M[2] + M[3] + M[4]:
        k += 1
    if k == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/679cf8d3-a852-4dc0-a42f-e8b4825ea271
'''
n = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    n += 1
    copied2 = [x for x in M if M.count(x) == 2]
    copied3 = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(copied3) == 3 and len(uncopied) == 3:
        if copied3[0] > copied2[0]:
            print(n)
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
