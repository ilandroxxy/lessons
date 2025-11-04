# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/inf/task/d2c3cbfd-85f3-4d63-a34e-ad3278d25635
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    M = sorted(M)
    if max(M) ** 2 > (M[0] * M[1] * M[2] * M[3]):
        if M[-1] + M[-2] > 2 * (M[0] + M[1] + M[2]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/7eeb5357-91a8-4e1a-b4ec-dafe92df2f09
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    # в строке только одно число повторяется трижды, остальные числа различны;
    copied1 = [x for x in M if M.count(x) == 1]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(copied1) == 3:
        if 3 * (copied3[0] ** 2) > (copied1[0] ** 2 + copied1[1] ** 2 + copied1[2] ** 2):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/9a4ed264-8f61-4713-91c3-37fceb735e15

cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(set(M)) == len(M):
        flag += 1
    if max(M) > (sum(M) - max(M)):
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 9, 17, 24
