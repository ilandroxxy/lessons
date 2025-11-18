# region Домашка: ******************************************************************

# № 8594 (Уровень: Базовый)
'''
def F(a, s, n):
    if a*s >= 455:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s , n-1), F(a, s+1, n-1), F(a*2, s , n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 90+1) if F(5, s, n=2)])
print([s for s in range(1, 90+1) if F(5, s, n=3) and not F(5, s, n=1)])
print([s for s in range(1, 90+1) if F(5, s, n=4) and not F(5, s, n=2)])
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 21911 Открытый вариант 2025 (Уровень: Базовый)
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 4:
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

def center(cl):
    R = []
    for p in cl:
        # summa = sum(dist(p, g) for g in cl)
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

centersA = [center(cl) for cl in clustersA]
pxA = sum(x for x, y in centersA) / 2 * 10000
pyA = sum(y for x, y in centersA) / 2 * 10000
print(int(pxA), int(pyA))

centersB = [center(cl) for cl in clustersB]
pxB = sum(x for x, y in centersB) / 3 * 10000
pyB = sum(y for x, y in centersB) / 3 * 10000
print(int(pxB), int(pyB))
'''


# № 23284 Основная волна 11.06.25 (Уровень: Базовый)
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('0. files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 15:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('0. files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 20 <= x <= 30:
        clustersB[0].append([x, y])
    if 10 <= x < 20:
        clustersB[1].append([x, y])
    if 0 <= x < 10:
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
pxA = sum(x for x, y in centersA) * 10000
pyA = sum(y for x, y in centersA) * 10000
print(abs(int(pxA)), abs(int(pyA)))

centersB = [center(cl) for cl in clustersB]
q1 = dist(centersB[0], centersB[1])
q2 = dist(centersB[0], centersB[2])
q3 = dist(centersB[1], centersB[2])
Q1 = min(q1, q2, q3) * 10000
Q2 = max(q1, q2, q3) * 10000
print(abs(int(Q1)), abs(int(Q2)))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
