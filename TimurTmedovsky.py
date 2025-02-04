# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19878 (Уровень: Средний)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(not_copied) == 4:
        if sum(not_copied) / 4 <= copied3[0]:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/2c9beda9-8bb0-497c-b6d3-d4fd322f0df0
'''
summa = 0
n = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    n += 1

    if len(set(M)) == len(M):
        if (M[0] + M[-1]) ** 2 > M[1] * M[2] * M[3]:
            summa += n

print(summa)
'''


# https://education.yandex.ru/ege/task/ebbc8b9f-d709-47ff-b8f4-2c2e99ccb13b
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if (M[-1] ** 3) >= 2 * (M[0] * M[1] * M[2]):
        if all(x > 10 for x in M):
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
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Тимур 6/14 -> 40 вторичных баллов +[12, 14, 16, 19, 23, 25] -[4, 5, 6, 7, 8, 10, 11, 13]
