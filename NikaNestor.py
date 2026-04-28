# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 29080 (Уровень: Средний)

from math import dist
clustersA = [[], []]
parmasA = [[], []]

clustersB = [[], [], []]
paramsB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 10:
        clustersA[0].append([x, y])
        parmasA[0].append(z)
    else:
        clustersA[1].append([x, y])
        parmasA[1].append(z)


for s in open('files/27B.txt'):
    cnt = 0
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 23:
        clustersB[0].append([x, y])
        paramsB[0].append(z)
    if y < 23 and y > 15:
        clustersB[1].append([x, y])
        paramsB[1].append(z)
    if y < 23 and y < 15:
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
# A1 – наибольшее расстояние от центра кластера с наименьшим количеством точек до синей звезды светимости 3, и
# A2 – наибольшее расстояние от центра кластера с наибольшим количеством точек до синей звезды светимости 3.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

print(len(clustersA[0]))  # 92
print(len(parmasA[0]))
print(len(clustersA[1]))  # 131

def A(cl, cent, parm):
    R = []
    for i in range(len(cl)):
        if 'L3' in parm[i]:
            R.append(dist(cent, cl[i]))
    return R

A1 = max(A(clustersA[0] + clustersA[1], center(clustersA[0]), parmasA[0] + parmasA[1]))
A2 = max(A(clustersA[0] + clustersA[1], center(clustersA[1]), parmasA[0] + parmasA[1]))
print(int(A1 * 10000), int(A2 * 10000))  # 1641 4058


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – расстояние между центрами кластером с наименьшим и наибольшим количеством синих звёзд, и
# B2 – максимальное расстояние между двумя синими звёздами, находящихся в различных кластерах.

def B(cl, param):
    R = []
    for i in range(len(cl)):
        if 'L' in param[i]:
            R.append(cl[i])
    return R

print(len(B(clustersB[0], paramsB[0])))  # 8
print(len(B(clustersB[1], paramsB[1])))  # 14
print(len(B(clustersB[2], paramsB[2])))  # 77

print(paramsB[2])



B1 = dist(center(clustersB[0]), center(clustersB[2]))

R = []
for p in B(clustersB[0], paramsB[0]):
    for g in B(clustersB[1], paramsB[1]):
        R.append(dist(p, g))

for p in B(clustersB[0], paramsB[0]):
    for g in B(clustersB[2], paramsB[2]):
        R.append(dist(p, g))

for p in B(clustersB[2], paramsB[2]):
    for g in B(clustersB[1], paramsB[1]):
        R.append(dist(p, g))

B2 = max(R)
print(int(B2 * 10000))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [23]
# на следующем уроке:



# region Пробник 2

# Вероника
# Пробник №2
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17,
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных


# Нестор
# Пробник №2
# Дата: #Воскресенье #01Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных

# endregion Пробник 2
