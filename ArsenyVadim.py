# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 25364 (Уровень: Базовый)

from math import dist
from multiprocessing.forkserver import connect_to_new_process

clustersA = [[], []]
clustersB = [[], [], []]

# from math import dist
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5], [6, 7]))  # 2.8284
# print(dist([4, 5], [6, 7]))  # 2.8284

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
        # print(summa, p)
    return min(R)[1]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 22:
        clustersB[0].append([x, y])
    if 15 < y < 22:
        clustersB[1].append([x, y])
    if y < 15:
        clustersB[2].append([x, y])

# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# P1 - минимальное расстояние от точки с координатами (1,0; 1,0) до центра кластера,
# и P2 - максимальное расстояние от этой же точки до центра кластера.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

P1 = dist([1.0, 1.0], [3.8471735, 6.1225014])  # 5.860581671822705
P2 = dist([1.0, 1.0], [7.0391548, 12.3587258])  # 12.864371049450831
print(int(P1 * 10000), int(P2 * 10000))


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# Q1 - в кластере с наибольшим количеством точек число таких точек,
# которые находятся на расстоянии не более 1,2 от центра кластера,
#
# и Q2 - в кластере с наибольшим количеством точек число таких точек,
# которые находятся на расстоянии не более 0,75 от центра кластера.

print(center(clustersB[0]))  # [13.9823808, 26.4800432]
print(center(clustersB[1]))  # [15.861917, 18.8540334]
print(center(clustersB[2]))  # [26.6431823, 12.4121727]

print(len(clustersB[0]))  # 74
print(len(clustersB[1]))  # 100
print(len(clustersB[2]))  # 451

def result(cl, center, length):
    cnt = 0
    for p in cl:
        if dist(p, center) <= length:
            cnt += 1
    return cnt


Q1 = result(clustersB[2], [26.6431823, 12.4121727], 1.2)
Q2 = result(clustersB[2], [26.6431823, 12.4121727], 0.75)
print(Q1, Q2)

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: +20 минут к след. уроку
