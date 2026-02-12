# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Статград вариант 2 23.10.25 (Номер 23)
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a*3, b)

print(F(6, 14) * F(14, 18) * F(18, 48))  # И - пересечение 24
print(F(6, 14) * F(14, 48))  # 45
print(F(6, 18) * F(18, 48))  # 48

print(48 + 45 - 24)  # 69
'''


# Статград вариант 2 23.10.25 (Номер 25)
'''
def divisors(n):
    d = []
    for j in range(2, int(n**0.5)+1):  # не считая самого числа.
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

cnt = 0
for x in range(1_325_000-1, 0, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        S = sum(d)
        if S <= 30000 and S % 5 == 0:
            print(x)
            cnt += 1
            if cnt == 5:
                break
'''


# Статград вариант 2 23.10.25 (Номер 24)
'''
from re import *
s = open('files/24.txt').readline()
pat = '[1-9]+([+*][1-9]+)*'
M = [x.group(0) for x in finditer(pat, s)]
print(M)

maxi = 0
for x in M:
    t = x.replace('*', '+').split('+')
    if len(t) > 50:
        print(len(t), '*'.join(t))
    if len(x) > maxi and len(t) <= 50:
        maxi = len(x)
print(maxi)
'''


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
        if y < 32:
            clustersB[0].append([x, y])
        elif y > 42:
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
    return max(R)[1]  # центр - min(), антицентр - max()


print(center(clustersA[0]))  # [16.99841482246666, 95.6727515672738]
print(center(clustersA[1]))  # [63.94062638636294, 87.77751031781972]

print(len(clustersA[0]))  # 102
print(len(clustersA[1]))  # 113

P1 = 16.99841482246666 + 95.6727515672738
P2 = 63.94062638636294 + 87.77751031781972
print(int(abs(P1 * 10000)), int(abs(P2 * 10000)))  # 1126711 1517181

print(center(clustersB[0]))  # [23.329917580199655, 26.41328219493777]
print(center(clustersB[1]))  # [21.38834573144159, 48.899310705252915]
print(center(clustersB[2]))  # [22.1707588150025, 39.65891347675987]

print(dist(center(clustersB[0]), [0, 0]))  # 35.24126176243305
print(dist(center(clustersB[1]), [0, 0]))  # 53.37231417670156
print(dist(center(clustersB[2]), [0, 0]))  # 45.43536028898788
Px = 21.38834573144159
Py = 26.41328219493777
print(int(abs(Px * 10000)), int(abs(Py * 10000)))  # 213883 264132

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, 12, 24, 26
