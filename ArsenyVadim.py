# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 7 Демоверсия 23.08.25 Вариант 1
'''
pixels = 1024 * 768
i = 30  # Сколько бит выделяется на один пиксель (2 ** i >= colors)
I = pixels * i

pixels2 = 800 * 600
i2 = 28
I2 = pixels2 * i2

print((I - I2) * 100)
print(((I - I2) * 100) / 2**13)  # 123937
'''



# Номер 11 Демоверсия 23.08.25 Вариант 1
'''
sym = 2783
# alp - ?
# i - ?
# bit - ?

byte = 11 * 2**30 / 3_845_627
print(byte)  # 3071.322 -> 3072 (так как требуется не менее 11 Гбайт)
bit = 3072 * 8

# bit = sym * i
i = bit / sym
print(i)  # 8.8307 -> 9 (так как требуется не менее 11 Гбайт)

i = 9
print(f'Максимальная мощность алфавита: {2 ** 9}')
print(f'Минимальная мощность алфавита: {2 ** 8+1}')

alp = 129  # i = 8

alp = 128  # i = 7

alp = 100  # i = 7

alp = 65   # i = 7

alp = 64  # i = 6 
'''


# Номер 15 Демоверсия 23.08.25 Вариант 1
'''
def F(x, a1, a2):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

R = []
M = [x / 4 for x in range(20 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68  # x ∈ D
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return (D) <= (((not C) and (not A)) <= (not D))


R = []
M = [x / 10 for x in range(5 * 10, 110 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(min(R))  # 21.8 -> 21.75 -> 21.9 -> 22
'''

# Номер 27 Демоверсия 23.08.25 Вариант 1

from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 10 < y < 20:
        clustersB[0].append([x, y])
    if 20 < y < 30 and x > 18:
        clustersB[1].append([x, y])
    if 20 < y < 30 and x < 18:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

Px = 3.8471735 * 10000
Py = 6.1225014 * 10000
print(int(abs(Px)), int(abs(Py)))  # 38471 61225


print(center(clustersB[0]))  # [11.555522, 14.5042082]
print(center(clustersB[1]))  # [21.3946551, 24.7510816]
print(center(clustersB[2]))  # [14.6275088, 23.5024317]

print(len(clustersB[0]))  # 407
print(len(clustersB[1]))  # 100
print(len(clustersB[2]))  # 113

Q1 = dist([11.555522, 14.5042082], [21.3946551, 24.7510816])
print(int(abs(Q1 * 10000)))  # 142058

def F(cl, center):
    R = []
    for p in cl:
        R.append(dist(center, p))
    return max(R)

print(F(clustersB[0], center(clustersB[0])))  # 2.5299751856733765
print(F(clustersB[1], center(clustersB[1])))  # 2.235667728613032
print(F(clustersB[2], center(clustersB[2])))  # 2.3038511238511417

Q2 = 2.5299751856733765 * 10000
print(int(abs(Q2)))  # 25299

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
