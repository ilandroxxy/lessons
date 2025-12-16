# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 5, 8, 9, 14, 17

# 14
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:23]:
    A = int(f'7{x}38596', 23)
    B = int(f'14{x}36', 23)
    C = int(f'61{x}7', 23)
    if (A + B + C) % 22 == 0:
        print(x, (A + B + C) // 22)
'''


# 5
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


R = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        R.append(n)
print(max(R))
'''

# 8
'''
s = sorted('0123456789ABCDEF')
cnt = 0
for a in s:
    for b in s:
        for c in s:
            n = a + b + c
            if len(n) == len(set(n)):
                if a != '0':
                    for x in '13579BDF':
                        n = n.replace(x, '*')
                    for x in '02468ACE':
                        n = n.replace(x, '#')
                    if '##' not in n and '**' not in n:
                        cnt += 1
print(cnt)


cnt = 0
from itertools import *
for p in permutations('0123456789ABCDEF', r=3):
    n = ''.join(p)
    if n[0] != '0':
        for x in '13579BDF':
            n = n.replace(x, '*')
        for x in '02468ACE':
            n = n.replace(x, '#')
        if '##' not in n and '**' not in n:
            cnt += 1
print(cnt)
'''

# 9
'''
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    n += 1
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if M.count(max(M)) == 1:
            print(n, sum(M))
            break
'''

# 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 39]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) ** 2 <= max(B) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''



# № 25364 ЕГКР 13.12.25 (Уровень: Базовый)
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x > 22:
        clustersB[0].append([x, y])
    if y > 24:
        clustersB[1].append([x, y])
    if 16 < y < 24:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# P1 - минимальное расстояние от точки с координатами (1,0; 1,0) до центра кластера, и
# P2 - максимальное расстояние от этой же точки до центра кластера.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

print(dist([1.0, 1.0], [7.0391548, 12.3587258]))  # 12.864371049450831
print(dist([1.0, 1.0], [3.8471735, 6.1225014]))  # 5.860581671822705

P1 = 5.860581671822705 * 10000
P2 = 12.864371049450831 * 10000
print(int(P1), int(P2))



# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# Q1 - в кластере с наибольшим количеством точек число таких точек,
# которые находятся на расстоянии не более 1,2 от центра кластера, и
# Q2 - в кластере с наибольшим количеством точек число таких точек,
# которые находятся на расстоянии не более 0,75 от центра кластера.

print(center(clustersB[0]))  # [26.6431823, 12.4121727]  (тут)
print(center(clustersB[1]))  # [13.9823808, 26.4800432]
print(center(clustersB[2]))  # [15.861917, 18.8540334]

print(len(clustersB[0]))  # 451  (тут)
print(len(clustersB[1]))  # 74
print(len(clustersB[2]))  # 100

def count_dot(cl, center, length):
    cnt = 0
    for p in cl:
        if dist(p, center) <= length:
            cnt += 1
    return cnt

Q1 = count_dot(clustersB[0], [26.6431823, 12.4121727], 1.2)  # 358
Q2 = count_dot(clustersB[0], [26.6431823, 12.4121727], 0.75)  # 203
print(Q1, Q2)  # 358 203
'''


# № 21929 (Уровень: Базовый)
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])


for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < 10:
        clustersB[0].append([x,y])
    if y > 10 and x < 17:
        clustersB[1].append([x,y])
    if y > 10 and x > 17:
        clustersB[2].append([x,y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


print(center(clustersA[0])) # [3.2865636, 16.3616946]
print(center(clustersA[1])) # [5.7806753, 7.0666221]
P1 = (3.2865636 + 5.7806753) / 2 * 10000
P2 = (16.3616946 + 7.0666221) / 2 * 10000
print(int(P1), int(P2))


print(center(clustersB[0])) # [15.7780749, 6.1170037]
print(center(clustersB[1])) # [14.4062605, 19.5187459]
print(center(clustersB[2])) # [20.1133897, 17.3153227]
P3 = (15.7780749 + 14.4062605 + 20.1133897) / 3 * 10000
P4 = (6.1170037 + 19.5187459 + 17.3153227) / 3 * 10000
print(int(abs(P3)), int(abs(P4)))
'''


# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
