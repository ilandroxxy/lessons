# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


from math import dist
clustersA = [[], []]
clustersB = [[], [], []]
# clustersA[0] - первый кластер
# clustersA[1] - второй кластер

for s in open('0. files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 2:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x < 10:
        clustersB[0].append([x, y])
    elif x > 20:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


# Поиск расстояний между двумя точками
'''
def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([4, 5], [6, 7]))
print(dist([4, 5], [6, 7]))
'''

# Поиск центра кластера
def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


centersA = [center(cl) for cl in clustersA]
pxA = sum([x for x, y in centersA]) / 2 * 10000
pyA = sum([y for x, y in centersA]) / 2 * 10000
print(int(pxA), int(pyA))

centersB = [center(cl) for cl in clustersB]
pxB = sum([x for x, y in centersB]) / 3 * 10000
pyB = sum([y for x, y in centersB]) / 3 * 10000
print(int(pxB), int(pyB))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 6, 8, 13, 14, 15, 16, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
