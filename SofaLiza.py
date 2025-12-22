# region Домашка: ******************************************************************


# 5 ЕГКР 25344
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        summa = sum(map(int, s))
        x = summa * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 208 and r % 2 != 0:
        RES.append(r)
print(min(RES))
'''

# Номер 25 25362
'''
def divisors(x):
    d = []
    for j in range(1,int(x**0.5)+1):
        if x % j == 0:
            d += [j,x//j]
    return sorted(set(d))

print(divisors(24))

cnt = 0
for x in range(1_350_050+1, 10**10):
    d = [j for j in divisors(x) if j % 100 == 11 and j != x and j != 11]
    if len(d) > 0:
        print(x,min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Номер 17 25356
'''
R = []
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 25348 ЕГКР 13.12.25 (Уровень: Базовый)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if M.count(max(M)) == 1:
        copied3 = [x for x in M if M.count(x) == 3]
        copied1 = [x for x in M if M.count(x) == 1]
        if len(copied1) == 4 and len(copied3) == 3:
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/7eeb5357-91a8-4e1a-b4ec-dafe92df2f09
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied1) == 3 and len(copied3) == 3:
        if 3 * (copied3[0]) ** 2 > (copied1[0] ** 2 + copied1[1] ** 2 + copied1[2] ** 2):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/5c54e314-516a-44fb-b41f-b06ffe3345af
'''
from itertools import permutations
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if sum(M) % 2 == 0:
            if any(P[0] + P[1] == P[2] + P[3] for P in permutations(M)):
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/679cf8d3-a852-4dc0-a42f-e8b4825ea271
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied3 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied2) == 2 and len(copied1) == 3:
        if copied3[0] > copied2[0]:
            print(n)
'''


# https://education.yandex.ru/ege/inf/task/96c09be1-da8c-4460-b91f-05f352ddaa78
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    # if len(M) == len(set(M)):  # В строке все числа различные
    if len(M) != len(set(M)):  # В строке есть повторяющиеся числа
        flag += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 27
