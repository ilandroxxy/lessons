# region Домашка: ******************************************************************
from idlelib.squeezer import count_lines_with_wrapping
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 0 < y < 10:
        clustersB[0].append([x, y])
    if 10 < y < 21:
        clustersB[1].append([x, y])
    if 21 < y < 30:
        clustersB[2].append([x, y])


for s in open('0. files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5], [5, 6]))
# print(dist([4, 5], [5, 6]))


def center(cl):
    RES = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        RES.append([summa, p])
    return min(RES)[1]


centersA = [center(cl) for cl in clustersA]
pxA = max(x for x, y in centersA) * 10000
pyA = max(y for x, y in centersA) * 10000
print(int(abs(pxA)), int(abs(pyA)))

centersB = [center(cl) for cl in clustersB]
print(centersB)
# [[12.2170442, 7.2915548]
#  [8.6628003, 18.9497112]
#  [12.0183379, 23.6292058]]

print(len(clustersB[0]))  # 397
print(len(clustersB[1]))  # 153
print(len(clustersB[2]))  # 53

qxB = centersB[0][0] - centersB[2][0]
print(int(abs(qxB * 10000)))

qyB = centersB[0][1] - centersB[2][1]
print(int(abs(qyB * 10000)))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 9, 13, 14, 15, 16, 17, 23, 19-21, 25, 27]
# КЕГЭ = []
# на следующем уроке: 6
