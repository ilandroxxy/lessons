# region Домашка: ******************************************************************


# https://education.yandex.ru/ege/task/d73b5f1e-ee81-4928-94f5-ea2abff0a9a0
'''
from itertools import *
A='02468'
B='1357'
cnt=0
for x in permutations('01234567', r=4):
    w = ''.join(x)
    if w[0]=='3' and w[-1]=='0':
        if w[1] not in A or w[2] not in A:
            if w[2] not in A or w[-1] not in A:
                cnt+=1
print(cnt)


from itertools import *
A='02468'
B='1357'
cnt=0
for x in permutations('01234567', r=4):
    w = ''.join(x)
    if w[0]=='3' and w[-1]=='0':
        for x in A:
            w = w.replace(x, '2')
        if '22' not in w:
            cnt+=1
print(cnt)
'''


# Определите количество пар элементов последовательности, в которых либо сумма элементов кратна 18,
# либо произведение элементов кратно 18. В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную сумму элементов этих пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
'''
M = [int(x) for x in open ('0. files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1,len(M)):
        x, y = M[i],M[j]
        cnt = 0
        if (x+y)%18==0:
            cnt += 1
        if (x*y)%18==0:
            cnt += 1
        if cnt == 1:
            R.append(x + y)

print(len(R), max(R))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied2 = [x for x in M if M.count(x) == 2]
    copied3 = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(copied3) == 3 and len(uncopied) == 3:
        if copied3[0] > copied2[0]:
            print(n)
'''

# https://education.yandex.ru/ege/task/dcf64491-b2a9-43d3-8307-3d9aad5e7fe4
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(M) / 7:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/dcf64491-b2a9-43d3-8307-3d9aad5e7fe4
'''
cnt = 0
for s in open('0. files/9.txt'):
    M = [int(x) for x in s.split()]
    # uncopied = [x for x in M if M.count(x) == 1]
    # if len(uncopied) == len(M):
    if len(set(M)) == len(M):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(chet) > len(nechet):
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
    if len(M) == len(set(M)):
        if (M[0] + M[-1]) ** 2 > M[1] * M[2] * M[3]:
            summa += n
print(summa)
'''

# https://education.yandex.ru/ege/task/ebbc8b9f-d709-47ff-b8f4-2c2e99ccb13b
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if all(x > 10 for x in M):
        if max(M) ** 3 >= (M[0] * M[1] * M[2]) * 2:

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
# ФИПИ = [2, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]

# Второй пробник 28.02.25:
# Женя 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 13, 14, 15, 16, 23, 25] -[8, 12]
# Ярослав 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 12, 13, 14, 15, 16, 23] -[8, 25]
