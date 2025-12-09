# region Домашка: ******************************************************************


# https://stepik.org/lesson/1038609/step/5?unit=1062783
'''
pixels = 1280 * 1024

U =  1_966_080  # бит/с
T = 280
V_39 = U * T

V_1 = V_39 / 39

i = V_1 / pixels
print(i)  # 10.7692 -> 10
print(2 ** 10)
'''
# на передачу одного пакета отводится не более 280 секунд


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from math import dist
from runpy import run_path

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
    if 0 < y < 10:
        clustersB[0].append([x, y])
    if 10 < y < 15:
        clustersB[1].append([x, y])
    if 15 < y < 22:
        clustersB[2].append([x, y])

# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5,], [6, 7]))
# print(dist([4, 5,], [6, 7]))

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


print(center(clustersA[0]))  # [4.8149075, 19.2506778]
print(center(clustersA[1]))  # [4.4107374, 6.6104248]

# PxA - сумму абсцисс центров кластеров
PxA = (4.8149075 + 4.4107374) * 10000

# PyA - сумму ординат центров кластеров
PyA = (19.2506778 + 6.6104248) * 10000

print(int(abs(PxA)), int(abs(PyA)))  # 92256 258611

'''
print(center(clustersB[0]))  # [25.471244, 7.4518469]
print(center(clustersB[1]))  # [14.3169299, 11.7215168]
print(center(clustersB[2]))  # [16.7058365, 17.61278]

# Q1 - минимальное расстояние между центрами, принадлежащими двум различным кластерам
# Q2 - максимальное расстояние между центрами, принадлежащими двум различным кластерам

print(dist([25.471244, 7.4518469], [14.3169299, 11.7215168]))  # 11.9435
print(dist([25.471244, 7.4518469], [16.7058365, 17.61278]))  # 13.41927
print(dist([14.3169299, 11.7215168], [16.7058365, 17.61278]))  # 6.35718

Q1 = 6.357189381731349 * 10000
Q2 = 13.419274574422115 * 10000
print(int(abs(Q1)), int(abs(Q2)))  # 63571 134192
'''

# Q1 - минимальное расстояние между точками, принадлежащими двум различным кластерам
# Q2 - максимальное расстояние между точками, принадлежащими двум различным кластерам

def perebor(cl1, cl2):
    R = []
    for p in cl1:
        for g in cl2:
            R.append(dist(p, g))
    return min(R), max(R)

cl1, cl2 = clustersB[0], clustersB[1]
print(perebor(cl1, cl2))  # (8.104248933147224, 16.163613489499177)

cl1, cl2 = clustersB[0], clustersB[2]
print(perebor(cl1, cl2))  # (10.015986741740884, 17.08163675852804)

cl1, cl2 = clustersB[1], clustersB[2]
print(perebor(cl1, cl2))  # (3.386361735682745, 9.224309533661824)

Q1 = 3.386361735682745 * 10000
Q2 = 17.08163675852804 * 10000
print(int(abs(Q1)), int(abs(Q2)))  # 33863 170816

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 23, 19-21, 25, 27]
# КЕГЭ = []
# на следующем уроке:
