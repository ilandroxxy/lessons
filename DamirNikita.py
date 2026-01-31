# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/inf/task/6e9942aa-9ba7-4271-a4fb-aaa4511870bb
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    n += 1
    if len(M) == len(set(M)):
        if 2 * (max(M) + min(M)) == 3 * (sum(M) - min(M) - max(M)):
            print(n)
'''


# https://education.yandex.ru/ege/inf/task/4a521e4c-c1ac-440a-8fb2-3aa0bc59172c
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    A = [x for x in M if abs(x) % 10 == 3]
    if len(A) == 3:
        L = [x for x in M if x > 0]
        K = [x for x in M if x < 0]
        if sum(L) ** 2 < sum(K) ** 2:
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/342217d2-3e89-4933-a422-940d9668bfa3
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied1) == 3:
        if sum(copied3) ** 2 > sum(copied1) ** 2:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/96c09be1-da8c-4460-b91f-05f352ddaa78
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(M) != len(set(M)):
        flag += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/dcf64491-b2a9-43d3-8307-3d9aad5e7fe4

cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied1) == 6:
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(chet) > len(nechet):
            cnt += 1
print(cnt)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 27
