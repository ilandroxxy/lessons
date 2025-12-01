# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/inf/task/d88de653-d533-48d5-b4eb-2b1f629bfa77
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27A.txt'):
     s = s.replace(',', '.')
     x, y = [float(i) for i in s.split()]
     if y > 2:
         clustersA[0].append([x, y])
     else:
         clustersA[1].append([x, y])


for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x < 10:
        clustersB[0].append([x, y])
    if x > 10 and x < 20:
        clustersB[1].append([x, y])
    if x > 20:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


# Дальше решение аналитическое       x             y
print(center(clustersA[0]))  # [1.262277635, 6.797635538]
print(center(clustersA[1]))  # [3.981033369, -1.961127579]

# pxA — среднее арифметическое абсцисс центров кластеров
pxA = (1.262277635 + 3.981033369) / 2 * 10000
print(int(abs(pxA)))  # 26216

# pyA — среднее арифметическое ординат центров кластеров.
pyA = (6.797635538 + -1.961127579) / 2 * 10000
print(int(abs(pyA)))  # 24182


print(center(clustersB[0]))  # [4.309073189, 6.615238685]
print(center(clustersB[1]))  # [15.75501912, 13.34466476]
print(center(clustersB[2]))  # [25.20349762, -0.833550091]


# pxB — среднее арифметическое абсцисс центров кластеров
pxB = (4.309073189 + 15.75501912 + 25.20349762) / 3 * 10000
print(int(abs(pxB)))  # 150891

# pyB — среднее арифметическое ординат центров кластеров.
pyB = (6.615238685 + 13.34466476 + -0.833550091) / 3 * 10000
print(int(abs(pyB)))  # 63754
'''


# https://education.yandex.ru/ege/inf/task/3aac44db-1223-46e5-a03b-c0ebb6af2f8f
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27A.txt'):
     s = s.replace(',', '.')
     x, y = [float(i) for i in s.split()]
     if y > 15:
         clustersA[0].append([x, y])
     else:
         clustersA[1].append([x, y])


for s in open('0. files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 0 < y < 10:
        clustersB[0].append([x, y])
    if 10 < y < 21:
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


# Дальше решение аналитическое

# Для файла А определите координаты центра каждого кластера
print(center(clustersA[0]))  # [6.9663606, 19.2156207]
print(center(clustersA[1]))  # [3.9100466, 6.6396418]

# pxA — максимальную из абсцисс центров кластеров
pxA = 6.9663606 * 10000
print(int(abs(pxA)))  # 69663

# pyA — максимальную из ординат центров кластеров.
pyA = 19.2156207 * 10000
print(int(abs(pyA)))  # 192156


# Для файла B определите координаты центра каждого кластера
print(center(clustersB[0]))  # [12.2170442, 7.2915548]
print(center(clustersB[1]))  # [8.4874654, 18.9031256]
print(center(clustersB[2]))  # [12.1302947, 23.4222296]

print(len(clustersB[0]))  # 397
print(len(clustersB[1]))  # 131
print(len(clustersB[2]))  # 75

# qxB — разность абсцисс центров кластеров с минимальным и максимальным количеством точек
qxB = (12.2170442 - 12.1302947) * 10000
print(int(abs(qxB)))

# qyB — разность ординат центров кластеров с минимальным и максимальным количеством точек.
qyB = (23.4222296 - 7.2915548) * 10000
print(int(abs(qyB)))
'''


# https://stepik.org/lesson/1400061/step/2?unit=1417014

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
    if y < 10:
        clustersB[0].append([x, y])
    if 10 < y and x > 17:
        clustersB[1].append([x, y])
    if 10 < y and x < 17:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


# Дальше решение аналитическое



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 13, 14, 15, 16, 17, 23, 19-21, 25, 27]
# КЕГЭ = []
# на следующем уроке:
