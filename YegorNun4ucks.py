# region Домашка: ******************************************************************
'''
from itertools import *

R = []
for n, i in enumerate(product(sorted('ПАРУС'), repeat=5), 1):
    s = ''.join(i)
    if s.count('У') <= 1 and 'АА' not in s:
        R.append(n)
print(max(R))
'''

'''
cnt = 0
for s in open('2.csv'):
    M = [int(x) for x in s.split(',')]
    four_copied = [x for x in M if M.count(x) == 4]
    two_copied = [x for x in M if M.count(x) == 2]
    ncopied = [x for x in M if M.count(x) == 1]
    copied = four_copied + two_copied

    if len(four_copied) == 4 and len(two_copied) == 2 and len(ncopied) == 3:
        m = max(copied)
        if sum(ncopied) / len(ncopied) >= m:
            cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if (len(copied) == 3 and len(not_copied) == 4) + (M == sorted(M)) <= 1:
        cnt += 1
print(cnt)

cnt = 0
for s in open('files/9.csv'):
    flag = True
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    ncopied = [x for x in M if M.count(x) == 1]

    for i in range(len(M)-1):
        if M[i] > M[i+1]:
            flag = False

    if (len(copied) == 3 and len(ncopied) == 4) and flag == 1:
        continue
    cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18040 (Уровень: Базовый)
R = []
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 5 == 0:
        s = s[:3] + s
    else:
        x = (n % 5) * 5
        s += f'{x:b}'
    r = int(s, 2)
    if r < 313 and n % 2 != 0:
        R.append(n)

print(max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [8, 9, 17, 25]
# КЕГЭ  = []
# на следующем уроке:
