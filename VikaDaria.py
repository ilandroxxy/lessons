# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 16
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)

def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4

print(F(673))
'''


# Номер 25
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

cnt = 0
for x in range(1_350_050+1, 10**10):
    d = [j for j in divisors(x) if j != 11 and j != x and j % 100 == 11]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Номер 27
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
    if y < 16:
        clustersB[0].append([x, y])
    if 16 < y < 23:
        clustersB[1].append([x, y])
    if y > 23:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa=sum(dist(p, g) for g in cl)
        R.append([summa,p])
    return min(R)[1]

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

# P1 - минимальное расстояние от точки с координатами (1,0; 1,0) до центра кластера
P1 = 5.860581671822705 * 10000
print(dist([1.0, 1.0], [7.0391548, 12.3587258]))  # 12.864371049450831
print(dist([1.0, 1.0], [3.8471735, 6.1225014]))  # 5.860581671822705
P2 = 12.864371049450831 * 10000
# P2 - максимальное расстояние от этой же точки до центра кластера.
print(int(P1), int(P2))  # 58605 128643


print(center(clustersB[0]))  # [26.6431823, 12.4121727]
print(center(clustersB[1]))  # [15.861917, 18.8540334]
print(center(clustersB[2]))  # [13.9823808, 26.4800432]

print(len(clustersB[0]))  # 451
print(len(clustersB[1]))  # 100
print(len(clustersB[2]))  # 74

# Q1 - в кластере с наибольшим количеством точек число таких точек, которые находятся на расстоянии не более 1,2 от центра кластера
# Q2 - в кластере с наибольшим количеством точек число таких точек, которые находятся на расстоянии не более 0,75 от центра кластера.

def proverka(cl, center, l):
    cnt = 0
    for p in cl:
        if dist(p, center) <= l:
            cnt += 1
    return cnt

Q1 = proverka(clustersB[0], [26.6431823, 12.4121727], 1.2)  # 358
Q2 = proverka(clustersB[0], [26.6431823, 12.4121727], 0.75)  # 203

print(Q1, Q2)  # 358 203
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 23, 19-21, 22, 25, 27]
# КЕГЭ = []
# на следующем уроке:
