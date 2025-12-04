# region Домашка: ******************************************************************

# https://stepik.org/lesson/1228674/step/3?unit=1242207
'''
k=0
for s in open('0. files/9_12463.csv'):
    a=[int(x) for x in s.split(',')]
    cop4=[x for x in a if a.count(x)==4]
    cop2=[x for x in a if a.count(x)==2]
    cop24=cop4+cop2
    cop1=[x for x in a if a.count(x)==1]
    if len(set(cop4))==1:
        if len(set(cop2))==1:
            if len(cop1)==3:
                if sum(cop1)/3>=max(cop24):
                    k+=1
print(k)
'''


# https://stepik.org/lesson/1228674/step/6?unit=1242207
'''
from itertools import *
summa = 0
for s in open('0. files/9_11228.csv'):
    a = sorted([int(x) for x in s.split(';')])
    cop3 = [int(x) for x in a if a.count(x) == 3]
    cop2 = [int(x) for x in a if a.count(x) == 2]
    if len(set(cop3)) == 1 and len(set(cop2)) == 2:
        if any((p[0] + p[1]) % 2 != 0 and (p[2] + p[3]) % 2 != 0 for p in permutations(a[:4])):
            summa += sum(a)
print(summa)
'''


# https://stepik.org/lesson/1228674/step/11?unit=1242207
'''
k = 0
for s in open('0. files/9_9696.csv'):
    a = [int(x) for x in s.split(';')]
    cop2 = [int(x) for x in a if a.count(x) == 2]
    cop1 = [int(x) for x in a if a.count(x) == 1]
    if len(cop2) == 4:
        a = sorted(cop2)
        if a[0] < cop1[0] < a[-1]:
            k += 1
print(k)
'''


# https://stepik.org/lesson/1228674/step/13?unit=1242207
'''
from itertools import permutations
k=0
for s in open('0. files/9_9156.csv'):
    a=[int(x) for x in s.split(';')]
    if (max(a)+min(a))%3==0:
        if any(abs(p[0] - p[1]) == abs(p[2] - p[3]) for p in permutations(a)):
                k+=1
print(k)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27_А.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < 2:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x < 10:
        clustersB[0].append([x, y])
    if 10 < x < 21:
        clustersB[1].append([x, y])
    if x > 21:
        clustersB[2].append([x, y])

# def d(A, B):
#     x1, y1 = A
#     x2, y2 = B
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# print(d([4, 5], [6, 7]))
# print(dist([4, 5], [6, 7]))



def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


centersA = [center(cl) for cl in clustersA]
print(centersA)  # [[3.981033369, -1.961127579], [1.262277635, 6.797635538]]
pxA = (3.981033369 + 1.262277635) / 2 * 10000
pyA = (-1.961127579 + 6.797635538) / 2 * 10000
print(int(abs(pxA)), int(abs(pyA)))

centersB = [center(cl) for cl in clustersB]
print(centersB)  # [[4.309073189, 6.615238685], [15.75501912, 13.34466476], [25.20349762, -0.833550091]]
pxB = (4.309073189 + 15.75501912 + 25.20349762) / 3 * 10000
pyB = (6.615238685 + 13.34466476 + -0.833550091) / 3 * 10000
print(int(abs(pxB)), int(abs(pyB)))


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25, 27]
# КЕГЭ  = []
# на следующем уроке:
