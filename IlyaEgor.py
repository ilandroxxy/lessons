# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 16 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
# F(n) = (n + 4) * F(n - 5)
# F(257487) = (257487 + 4) * F(257482)
# F(257482) = (257482 + 4) * F(257477)
# F(257477) = (257477 + 4) * F(257472) / F(257472)

# F(257477) = (257477 + 4) * F(257472) / F(257472)

print(((257487 + 4) * (257482 + 4) * (257477 + 4)) / 683)  # 24994252792782
print((257477 + 4) / 67)  # 3843
print(24994252792782 + 3843)  # 24994252796625 (ответ)
'''


# Номер 27 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)

from itertools import permutations
from math import dist
clustersA = [[], []]
paramsA = [[], []]

clustersB = [[], [], []]
paramsB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 10:
        clustersA[0].append([x, y])
        paramsA[0].append(z)
    else:
        clustersA[1].append([x, y])
        paramsA[1].append(z)

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 23:
        clustersB[0].append([x, y])
        paramsB[0].append(z)
    else:
        if x < 20:
            clustersB[1].append([x, y])
            paramsB[1].append(z)
        if x > 20:
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

# Для файла А определите координаты центра каждого кластера, затем
# на йдите два числа: A1 – минимальное расстояние от центра кластера с
# наименьшим количеством точек до красного гиганта, и A2 – максимальное
# расстояние от центра кластера с наименьшим количеством точек до
# красного гиганта.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

print(len(clustersA[0]))  # 92
print(len(clustersA[1]))  # 131

def A1(cl, par, cent):
    R = []
    for i in range(len(cl)):
        if 'Y' in par[i] and 'III' in par[i]:
            R.append(dist(cent, cl[i]))
    return min(R)

A1 = A1(clustersA[0], paramsA[0], center(clustersA[0]))
print(int(A1 * 10000))  # 4940


def A2(cl, par, cent):
    R = []
    for i in range(len(cl)):
        if 'Y' in par[i] and 'III' in par[i]:
            R.append(dist(cent, cl[i]))
    return max(R)

A2 = A2(clustersA[0], paramsA[0], center(clustersA[0]))
print(int(A2 * 10000))  # ....



# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – минимальное расстояние между двумя различными жёлтыми сверхгигантами, расположенными в одном и том же кластере
# B2 – расстояние между центрами кластеров с минимальным и максимальным количеством жёлтых сверхгигантов.

print(center(clustersB[0]))  # [13.9823808, 26.4800432]
print(center(clustersB[1]))  # [15.861917, 18.8540334]
print(center(clustersB[2]))  # [26.6431823, 12.4121727]

def B1(cl, par):
    M = []
    for i in range(len(cl)):
        if 'Z' in par[i] and 'I' in par[i] and 'II' not in par[i] and 'V' not in par[i]:
            M.append(cl[i])
    R = []
    for p in permutations(M, 2):
        R.append(dist(p[0], p[1]))
    return min(R)

print(B1(clustersB[0], paramsB[0]))  # 3  - 0.1962774882347201
# print(B1(clustersB[1], paramsB[1]))  # 1
print(B1(clustersB[2], paramsB[2]))  # 9 - 0.10354459340095963

B1 = B1(clustersB[2], paramsB[2])
print(int(B1 * 10000))  # 1035

# B2 – расстояние между центрами кластеров с минимальным и максимальным количеством жёлтых сверхгигантов.

B2 = dist(center(clustersB[1]), center(clustersB[2]))
print(int(B2 * 10000))  # 125591


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [9, 13]
# на следующем уроке: 17, 25, 7, 11


# region 📖 Пробник (Вариант 2)

# Студент #Илья
# Дата: #Вторник #03Марта2026
# ✅ Верно: 1, 2, 4, 6, 7, 10, 14, 16, 17, 18, 19, 20, 21, 23
# ⛔️ Неверно: 3, 8, 15
# ❔ Без ответа: 5, 9, 11, 12, 13, 22, 24, 25, 26, 27
# Итог: 14/29 первичных балла ~ 62 вторичных

# endregion 📖 Пробник (Вариант 2)
