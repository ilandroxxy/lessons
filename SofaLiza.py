# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21932 (Уровень: Базовый)
# https://stepik.org/lesson/1400061/step/2?unit=1417014
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

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
    if y < 10:
        clustersB[0].append([x, y])
    if y > 10 and x < 17:
        clustersB[1].append([x, y])
    if y > 10 and x > 17:
        clustersB[2].append([x, y])

# from math import dist
# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([3, 4], [3, 6]))
# print(dist([3, 4], [3, 6]))

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


# Для каждого файла определите координаты центра каждого кластера,
# затем вычислите два числа:
# Px – абсциссу центра кластера с наименьшим числом точек, и
# Py – ординату центра кластера с наибольшим числом точек.

# В ответе запишите четыре числа: в первой строке сначала целую часть произведения
# Px×10000 затем целую часть произведения
# Py×10000 для файла А, во второй строке – аналогичные данные для файла B.

print(center(clustersA[0]))  # [3.2865636, 16.3616946]
print(center(clustersA[1]))  # [5.7806753, 7.0666221]

print(len(clustersA[0]))  # 100
print(len(clustersA[1]))  # 137

PxA = 3.2865636 * 10000
PyA = 7.0666221 * 10000
print(int(PxA), int(PyA))  # 32865 70666


print(center(clustersB[0]))  # [15.7780749, 6.1170037]
print(center(clustersB[1]))  # [14.4062605, 19.5187459]
print(center(clustersB[2]))  # [20.1133897, 17.3153227]

print(len(clustersB[0]))  # 439
print(len(clustersB[1]))  # 98
print(len(clustersB[2]))  # 102

PxB = 14.4062605 * 10000
PyB = 6.1170037 * 10000
print(int(PxB), int(PyB))  # 144062 61170
'''


# № 25364 (Уровень: Базовый) ЕГКР

from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

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
    if y > 23:
        clustersB[0].append([x, y])
    if y < 15:
        clustersB[1].append([x, y])
    if 15 < y < 23:
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

P1 = dist([1.0, 1.0], [3.8471735, 6.1225014])  # 5.860581671822705
P2 = dist([1.0, 1.0], [7.0391548, 12.3587258])  # 12.864371049450831

# В ответе запишите четыре числа: в первой строке - сначала целую часть произведения
# P1 × 10000, затем целую часть произведения P2 × 10 000

print(int(P1 * 10000), int(P2 * 10000))  # 58605 128643



# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# Q1 - в кластере с наибольшим количеством точек число таких точек,
# которые находятся на расстоянии не более 1,2 от центра кластера, и
# Q2 - в кластере с наибольшим количеством точек число таких точек,
# которые находятся на расстоянии не более 0,75 от центра кластера.

print(center(clustersB[0]))  # [13.9823808, 26.4800432]
print(center(clustersB[1]))  # [26.6431823, 12.4121727]
print(center(clustersB[2]))  # [15.861917, 18.8540334]

print(len(clustersB[0]))  # 74
print(len(clustersB[1]))  # 451
print(len(clustersB[2]))  # 100

def F(cl, cent, length):
    cnt = 0
    for p in cl:
        if dist(cent, p) <= length:
            cnt += 1
    return cnt

Q1 = F(clustersB[1], [26.6431823, 12.4121727], 1.2)
Q2 = F(clustersB[1], [26.6431823, 12.4121727], 0.75)
print(Q1, Q2)  # 358 203


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
