# region Домашка: ******************************************************************

# https://stepik.org/lesson/1400061/step/3?unit=1417014
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])


for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 0 < y < 10:
        clustersB[0].append([x, y])
    if y > 10 and x > 17:
        clustersB[1].append([x, y])
    if y > 10 and x < 17:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return max(R)[1]


centersA = [center(cl) for cl in clustersA]
print(centersA) # [[3.4435388, 6.1127361], [0.1663069, 16.1520663]]
print(len(clustersA[0])) # 137
print(len(clustersA[1])) # 100
pxA = 0.1663069 * 10000
pyA = 6.1127361 * 10000
print(int(abs(pxA)), int(abs(pyA)))  # 1663 61127


centersB = [center(cl) for cl in clustersB]
print(centersB) # [[18.1424701, 6.1934274], [19.4524463, 14.961161], [14.747434, 21.5194643]]
print(len(clustersB[0])) # 439
print(len(clustersB[1])) # 102
print(len(clustersB[2])) # 98
pxB = 14.747434 * 10000
pyB = 6.1934274 * 10000
print(int(abs(pxB)), int(abs(pyB)))  # 147474 61934
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, 22  (26, 24)
