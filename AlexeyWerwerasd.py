# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]

cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]

cnt = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
'''


# Задание 9 https://education.yandex.ru/ege/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if (len(M) == len(set(M))) != (max(M) > sum(M) - max(M)):
    if (len(M) == len(set(M))) != (M[-1] > sum(M[:-1])):
        cnt += 1
print(cnt)
'''


# Задание 9 https://education.yandex.ru/ege/task/36638a59-7977-4a77-9f1a-361aca12356d
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 6 and len(not_copied) == 2:
        if M.count(min(M)) == 1:
            print(sum(M))
            break
'''


# Задание 9 https://education.yandex.ru/ege/task/4a521e4c-c1ac-440a-8fb2-3aa0bc59172c
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    N = [x for x in M if abs(x) % 10 == 3]
    if len(N) == 3:
        A = [x for x in M if x > 0]
        B = [x for x in M if x < 0]
        if sum(A) ** 2 < sum(B) ** 2:
            cnt += 1
print(cnt)
'''


# Задание 9 https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649

cnt = 0
for s in open('files/9.csv'):
    print(s)
    M = sorted([int(x) for x in s.split(';')])
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3:
        if len(not_copied) == 4:
            print(not_copied)
            if sum(M) < 502:
                cnt += 1
print(cnt)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ = []
# на следующем уроке:
