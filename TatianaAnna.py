# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# import turtle as t
# def visual(cl):
#     t.screensize(5000, 5000)
#     t.up()
#     t.tracer(0)
#     size = 100
#     for i in range(len(cl)):
#         for x, y in cl[i]:
#             t.goto(x * size, y * size)
#             t.dot(5, 'red')
#     t.update()
#     t.done()


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
    return min(R)[1]


centersA = [center(cl) for cl in clustersA]
print(centersA) # [[5.7806753, 7.0666221], [3.2865636, 16.3616946]]
print(len(clustersA[0]))  # 137
print(len(clustersA[1]))  # 100
pxA = 3.2865636 * 10000
pyA = 7.0666221 * 10000
print(int(abs(pxA)), int(abs(pyA)))


centersB = [center(cl) for cl in clustersB]
print(centersB)  # [[15.7780749, 6.1170037], [20.1133897, 17.3153227], [14.4062605, 19.5187459]]

print(len(clustersB[0])) # 439
print(len(clustersB[1])) # 102
print(len(clustersB[2])) # 98
#
pxB = 14.4062605 * 10000
pyB = 6.1170037 * 10000
print(int(abs(pxB)), int(abs(pyB)))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 3, 10, 22  (26, 24)
