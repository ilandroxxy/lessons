# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/5e46684b-8408-47c0-92e8-9065796469f1
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3]  # x -> 978 304 '-273'
B = [x for x in A if abs(x) % 10 == 5]  # 305, 235, 555
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    # if (x in A) or (y in A):
    if (x in A) + (y in A) >= 1:  #  которых хотя бы один
        if (x + y) % min(B) == 0:
            R.append(x + y)
print(len(R), max(R))
'''
from pprint import pformat

# https://education.yandex.ru/ege/task/d4439e7b-ef28-49d4-9c2f-1a0c67026188
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 21 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    # if (x % min(A) == 0) or (y % min(A) == 0):
    if (x % min(A) == 0) + (y % min(A) == 0) >= 1:
        R.append(x + y)
print(len(R), max(R))
'''


# https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]  # [3, 3, 3, 4, 5, 6, 7]
    if len(copied) == 3:  # copied = [3, 3, 3]
        if len(set(M)) == 5:  #  {3, 4, 5, 6, 7}
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/d73c5edf-63bd-47d8-87cb-7810e03725a0
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(M) == len(set(M)):
        if 5 * (min(M) + max(M)) >= 3 * (M[1] + M[2] + M[3] + M[4]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/41a06b51-e4e0-4204-b3ac-432f00e2ac2c
'''
def divisors(x):  # 24
    div = []
    for j in range(1, int(x ** 0.5)+1):
        if x % j == 0:
            div.append(j)  # 4
            div.append(x // j)  # 24 // 4 = 6
    return sorted(set(div))


for x in range(977004, 977022+1):
    div = [j for j in divisors(x) if j % 2 == 0]
    if len(div) > 6:
        print(x, div[-2])
'''


# https://education.yandex.ru/ege/task/08b93dc7-c401-48a3-9078-75af3fa2e240
'''
from fnmatch import *
for x in range(13, 10**8, 13):
    if fnmatch(str(x), '123*678'):
        print(x, x // 13)
'''


# https://education.yandex.ru/ege/task/c624bf95-c3d7-48d7-898f-7a8868480573
'''
def divisors(x):
    div = []
    for j in range(1, int(x ** 0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(326496, 649632+1):
    d = divisors(x)
    chet = [j for j in d if j % 2 == 0]
    nechet = [j for j in d if j % 2 != 0]
    if len(chet) == len(nechet):
        if len(chet) >= 70:
            print(x, min([j for j in d if j > 1000]))
'''


print(float(5))  # 5.0

print(float(5.5))  # 5.5
print(int(5.5))  # 5

print(4 / 2, type(4 / 2))
# 2.0 <class 'float'>

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 22, 24.1 повторять

# Второй пробник 28.02.25:
# Дарья 10/29 -> 51 вторичных баллов +[1, 2, 4, 7, 10, 11, 13, 15, 16, 18] -[3, 6, 12, 22]

