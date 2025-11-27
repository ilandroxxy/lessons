# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 0 < y < 10:
        clustersB[0].append([x, y])
    if 10 < y < 21:
        clustersB[1].append([x, y])
    if 21 < y < 30:
        clustersB[2].append([x, y])

# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([3, 4], [5, 6]))
# print(dist([3, 4], [5, 6]))

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


centersA = [center(cl) for cl in clustersA]
print(centersA)
pxA = 6.9663606 * 10000
pyA = 19.2156207 * 10000
print(int(abs(pxA)), int(abs(pyA)))

centersB = [center(cl) for cl in clustersB]
print(centersB)
# [[12.2170442, 7.2915548],
# [8.4874654, 18.9031256],
# [12.1302947, 23.4222296]]

print(len(clustersB[0]))  # 397
print(len(clustersB[1]))  # 131
print(len(clustersB[2]))  # 75

qxB = (12.2170442 - 12.1302947) * 10000
qyB = (23.4222296 - 7.2915548) * 10000
print(int(abs(qxB)), int(abs(qyB)))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
