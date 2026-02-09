# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 9 Статграл 23.10.25 вариант 1
'''
mini = 0
n = 0
for i in open('files/9_6.csv'):
    M = sorted([int(x) for x in i.split(';')])
    copied1 = [x for x in M if M.count(x) == 1]
    mini = min(M)
    # if 2 <= M.count(mini) <= 3 and 5 <= len(copied1) <= 6:
    if M.count(mini) in (2, 3) and len(copied1) in (5, 6):

        if copied1[-1] ** 2 + copied1[0] ** 2 <= (sum(copied1) - min(copied1) - max(copied1)) ** 2:
            n += 1
print(n)
'''


# Номер 17 Статграл 23.10.25 вариант 1
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0 and abs(x) % 6 == 0 and len(str(abs(x))) == 3]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))
'''


# Номер 27 Статграл 23.10.25 вариант 1

from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 92:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x > 10:
        if y > 41:
            clustersB[0].append([x, y])
        elif y < 32:
            clustersB[1].append([x, y])
        else:
            clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return max(R)[1]


print(center(clustersA[0]))  # [16.99841482246666, 95.6727515672738]
print(center(clustersA[1]))  # [63.94062638636294, 87.77751031781972]

print(len(clustersA[0]))  # 102
print(len(clustersA[1]))  # 113

P1 = 16.99841482246666 + 95.6727515672738
P2 = 63.94062638636294 + 87.77751031781972
print(int(abs(P1 * 10000)), int(abs(P2 * 10000)))  # 1126711 1517181


print(center(clustersB[0]))  # [21.38834573144159, 48.899310705252915]
print(center(clustersB[1]))  # [23.329917580199655, 26.41328219493777]
print(center(clustersB[2]))  # [22.1707588150025, 39.65891347675987]

print(dist([0, 0], [21.38834573144159, 48.899310705252915]))  # 53.37231417670156
print(dist([0, 0], [23.329917580199655, 26.41328219493777]))  # 35.24126176243305
print(dist([0, 0], [22.1707588150025, 39.65891347675987]))  # 45.43536028898788

Qx = 21.38834573144159
Qy = 26.41328219493777
print(int(abs(Qx * 10000)), int(abs(Qy * 10000)))  # 213883 264132

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
