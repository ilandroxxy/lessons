# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# все числа различны:

# 1. if len(M) == len(set(M)):

# 2. if len(set(M)) == 6:

# 3. copied1 = [x for x in M if M.count(x) == 1]
#    if len(copied1) == 6:


# наибольшее число в строке больше суммы остальных чисел в этой строке:

# 1. if max(M) > sum(M) - max(M):

# 2. M = sorted(M)
#    if M[-1] > M[0] + M[1] + M[2] + ...


# https://education.yandex.ru/ege/inf/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
# Выполняются оба условия

# Вариант 1
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if len(M) == len(set(M)):
        if max(M) > sum(M) - max(M):
            cnt += 1
print(cnt)

# Вариант 2
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    if max(M) > sum(M) - max(M):
        flag += 1
    if flag == 2:
        cnt += 1
print(cnt)

# Вариант 2
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if (len(M) == len(set(M))) + (max(M) > sum(M) - max(M)) == 2:
        cnt += 1
print(cnt)


# Выполняется хотя бы одно условие

cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    if max(M) > sum(M) - max(M):
        flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)


# Вариант 2
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if (len(M) == len(set(M))) + (max(M) > sum(M) - max(M)) >= 1:
        cnt += 1
print(cnt)


# Выполняется только одно условие

# Вариант 1
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    if max(M) > sum(M) - max(M):
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)

# Вариант 2
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if (len(M) == len(set(M))) + (max(M) > sum(M) - max(M)) == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/488973a9-be8d-4241-960a-1e41c8dbfe94
'''
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if max(M) in copied1:
            print(sum(M))
            break
'''


# https://education.yandex.ru/ege/inf/task/37e02e25-78d7-4b93-9ef4-7a7a6b9281bd


for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]



# endregion Урок: *************************************************************
#
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 12, 27
