# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 5 ЕГКР
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + convert(sum(map(int, s)) * 2, 3)
    r = int(s, 3)
    if r % 2 != 0:
        if r > 520:
            R.append(r)
print(min(R))
'''


'''
cnt = 0
for s in open('9 (2) (1).csv'):
    M = [int(x) for x in s.split(',')]
    if M == sorted(M) and len(M) == len(set(M)):
        if M[0] + M[4] <= M[1]+ M[2] + M[3]:
                cnt += 1
print(cnt)
'''

# Номер 13 ЕГКР
'''
from ipaddress import *
net = ip_network('191.89.109.206/255.255.224.0', 0)
for ip in net:
    print(ip)

print(191 + 89 + 127 + 254)
'''

# Номер 23 ЕГКР
'''
def F(a, b):
    if a <= b or a == 73:
        return a == b
    return F(a - 3, b) + F(a - 8, b) + F(a // 2, b)

print(F(76, 41) * F(41, 12))
'''



# № 29357 Открытый вариант 2026 (Уровень: Базовый)

from itertools import permutations
from math import dist
clustersA = [[], []]
paramsA = [[], []]


clustersB = [[], [], []]
paramsB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 15:
        clustersA[0].append([x, y])
        paramsA[0].append(z)
    else:
        clustersA[1].append([x, y])
        paramsA[1].append(z)

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y < 30:
        clustersB[0].append([x, y])
        paramsB[0].append(z)
    if y > 30 and x < 16:
        clustersB[1].append([x, y])
        paramsB[1].append(z)
    if y > 30 and x > 16:
        clustersB[2].append([x, y])
        paramsB[2].append(z)


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

# Для файла А определите координаты центра каждого кластера, затем найдите два числа
# Ax и Ay – абсциссу и ординату красного гиганта, ближайшего к центру кластера,
# который содержит наименьшее количество точек.

print(center(clustersA[0]))  # [7.717373, 20.05071]
print(center(clustersA[1]))  # [4.960398, 7.34545]

print(len(clustersA[0]))  # 121
print(len(clustersA[1]))  # 114

def A(cl, cent, parm):
    R = []
    for i in range(len(cl)):
        if 'M' in parm[i] and 'III' in parm[i]:
            R.append([dist(cent, cl[i]), cl[i]])
    return min(R)[1]

Ax, Ay = A(clustersA[1], center(clustersA[1]), paramsA[1])
print(int(Ax * 10000), int(Ay * 10000))  # 44694 69754


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – расстояние между центрами кластеров
# с наименьшим и наибольшим количеством оранжевых гигантов, и
# B2 – наибольшее расстояние между жёлтыми карликами одного кластера.

def B1(cl, parm):
    R = []
    for i in range(len(cl)):
        if 'K' in parm[i] and 'III' in parm[i]:
            R.append(cl[i])
    return R

print(len(B1(clustersB[0], paramsB[0])))  # 87
print(len(B1(clustersB[1], paramsB[1])))  # 28
print(len(B1(clustersB[2], paramsB[2])))  # 25

B1 = dist(center(clustersB[0]), center(clustersB[2]))
print(int(B1 * 10000))  # 138716

def B2(cl, parm):
    R = []
    for i in range(len(cl)):
        if 'G' in parm[i] and 'V' in parm[i]:
            R.append(cl[i])

    M = []
    if len(R) >= 2:
        for p in permutations(R, r=2):
            M.append(dist(p[0], p[1]))
    return max(M)

print(B2(clustersB[0], paramsB[0]))  # 4.378988382912428
print(B2(clustersB[1], paramsB[1]))  # 3.6313769840811108
print(B2(clustersB[2], paramsB[2]))  # 3.630219009495848


# # endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [7, 11, ]
# на следующем уроке: немного 5 и переходим к 8, 4, 17, 12, 22, 27, 24, 26


# region 📖 Пробник (Вариант 2)

# Студент #Иван
# Дата: #Пятница #06Марта2026
# ✅ Верно: 1, 2, 3, 6, 7, 9, 11, 13, 14, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 5, 8, 10, 12, 15, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных


# Студент #Egor
# Дата: #Понедельник #16Марта2026
# ✅ Верно: 1, 2, 3, 15, 16, 19, 20, 21, 25
# ⛔️ Неверно: 6
# ❔ Без ответа: 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 22, 23, 24, 26, 27
# Итог: 9/29 первичных балла ~ 48 вторичных

# region 📖 Пробник (Вариант 2)
