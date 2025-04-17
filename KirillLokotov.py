# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# https://education.yandex.ru/ege/task/7102b1d9-1aed-45d5-bb07-8fb3361ed445
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(uncopied) == 3:
        if (max(M) + min(M)) ** 2 < (M[1] ** 2 + M[2] ** 2 + M[3] ** 2):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/d3ce64c1-1875-458b-b8d6-ae96bb169c58
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) > 0:
        if len(uncopied) == 0:
            maxi = 0
        else:
            maxi = max(uncopied)
        if min(copied) > maxi:
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
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 17, 23, 9, 8
