# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20911 Апробация 05.03.25 (Уровень: Базовый)
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])


for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 5:
        clustersB[0].append([x, y])
    if -5 < y < 5:
        clustersB[1].append([x, y])
    if y < -5:
        clustersB[2].append([x, y])

# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5], [6, 7]))
# print(dist([4, 5], [6, 7]))


# # endregion Урок: *************************************************************
# #
# #


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

#                                   x              y
print(center(clustersA[0]))  # [3.7046261187, 5.757797218]
print(center(clustersA[1]))  # [2.0161619849, -3.6989345413]

# PxA – среднее арифметическое абсцисс центров кластеров
PxA = (3.7046261187 + 2.0161619849) / 2 * 10000

# PyA – среднее арифметическое ординат центров кластеров.
PyA = (5.757797218 + -3.6989345413) / 2 * 10000

print(int(abs(PxA)), int(abs(PyA)))  # 28603 10294


print(center(clustersB[0]))  # [10.6474896077, 9.7540330133]
print(center(clustersB[1]))  # [3.6152550029, -0.0975921536]
print(center(clustersB[2]))  # [4.1152564179, -13.0184433974]

PxB = (10.6474896077 + 3.6152550029 + 4.1152564179) / 3 * 10000
PyB = (9.7540330133 + -0.0975921536 + -13.0184433974) / 3 * 10000
print(int(abs(PxB)), int(abs(PyB)))  # 61260 11206
'''


# № 23384 Резервный день 19.06.25 (Уровень: Базовый)

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
    if 0 < y < 15:
        clustersB[0].append([x, y])
    if 15 < y < 21:
        clustersB[1].append([x, y])
    if 21 < y < 30:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

print(center(clustersA[0]))  # [7.0404312, 12.9983695]
print(center(clustersA[1]))  # [3.9752601, 6.6649179]

# PxA - сумму абсцисс центров кластеров
PxA = (7.0404312 + 3.9752601) * 10000

# PyA - сумму ординат центров кластеров
PyA = (12.9983695 + 6.6649179) * 10000

print(int(abs(PxA)), int(abs(PyA)))  # 110156 196632



print(center(clustersB[0]))  # [23.0815601, 11.5546013]
print(center(clustersB[1]))  # [13.2331173, 18.1812725]
print(center(clustersB[2]))  # [13.1689743, 23.9396534]

print(dist([23.0815601, 11.5546013], [0, 0]))  # 25.81215271634417
print(dist([13.2331173, 18.1812725], [0, 0]))  # 22.487197762167156
print(dist([13.1689743, 23.9396534], [0, 0]))  # 27.32268085357277

# Q1 - минимальное расстояние от центра кластера до начала координат
Q1 = 22.487197762167156 * 10000

# Q2 - максимальное расстояние от центра кластера до начала координат.
Q2 = 27.32268085357277 * 10000

print(int(abs(Q1)), int(abs(Q2)))  # 224871 273226



# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
