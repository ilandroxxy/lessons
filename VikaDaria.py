# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 29081 (Уровень: Средний)

from math import dist

clustersA = [[], []]
paramsA = [[], []]

clustersB = [[], [], []]
paramsB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 10:
        clustersA[0].append([x, y])
        paramsA[0].append(z)
    else:
        clustersA[1].append([x, y])
        paramsA[1].append(z)

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 23:
        clustersB[0].append([x, y])
        paramsB[0].append(z)
    if y < 23 and x < 20:
        clustersB[1].append([x, y])
        paramsB[1].append(z)
    if y < 23 and x > 20:
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


# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# A1 – минимальное расстояние от центра кластера до квазара из этого же кластера, и
# A2 – максимальное расстояние от центра кластера до квазара из этого же кластера.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

def A(cl, cent, parm):
    R = []
    for i in range(len(cl)):
        if 'VII' in parm[i] and 'VIII' not in parm[i]:
            R.append(dist(cent, cl[i]))
    return R

R1 = A(clustersA[1], center(clustersA[1]), paramsA[1])
R2 = A(clustersA[0], center(clustersA[0]), paramsA[0])

A1 = min(R1 + R2) * 10000
A2 = max(R1 + R2) * 10000
print(int(A1), int(A2))  # 1495 16955


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – минимальное расстояние между двумя звёздами светимостью не менее 8,
# расположенными в различных кластерах, и
# B2 – cреднее расстояние между двумя различными звёздами светимостью не менее 8,
# расположенными в одном кластере.

def B(cl, parm):
    R = []
    for i in range(len(cl)):
        if parm[i][1] >= '8':
            R.append(cl[i])
    return R

k0 = B(clustersB[0], paramsB[0])
k1 = B(clustersB[1], paramsB[1])
k2 = B(clustersB[2], paramsB[2])

from itertools import permutations
r = [dist(p[0], p[1]) for p in permutations(k0 + k1 + k2, r=2) if not(p[0] in k0 and p[1] in k0) and not(p[0] in k1 and p[1] in k1) and not(p[0] in k2 and p[1] in k2)]
B1 = int(min(r) * 10000)


r0 = [dist(p[0],p[1]) for p in permutations(k0, r=2) if p[0] != p[1]]
r1 = [dist(p[0],p[1]) for p in permutations(k1, r=2) if p[0] != p[1]]
r2 = [dist(p[0],p[1]) for p in permutations(k2, r=2) if p[0] != p[1]]

B2 = int( sum(r0 + r1 + r2) / len(r0 + r1 + r2) * 10000)
print(B1, B2)

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 14, 16, 25]
# на следующем уроке:  15 номера руками


# region 📖 Пробник (Вариант 2)

# Студент #Дарья
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 4, 5, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27
# ⛔️ Неверно: 3, 6, 7, 10, 24, 26
# ❔ Без ответа: Нет
# Итог: 22/29 первичных балла ~ 83 вторичных

# Студент #Маша
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 21, 23
# ⛔️ Неверно: 10, 18
# ❔ Без ответа: 9, 17, 22, 24, 25, 26, 27
# Итог: 18/29 первичных балла ~ 72 вторичных

# Студент #Вика
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 6, 7, 8, 13, 14, 16, 17, 19, 20, 21, 25, 27
# ⛔️ Неверно: 5, 9, 12, 15, 23
# ❔ Без ответа: 3, 4, 10, 11, 18, 22, 24, 26
# Итог: 15/29 первичных балла ~ 65 вторичных

# endregion 📖 Пробник (Вариант 2)

