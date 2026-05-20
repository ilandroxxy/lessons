# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 29357 Открытый вариант 2026 (Уровень: Средний)

from math import dist
from itertools import permutations

cA = [[], []]
pA = [[], []]

cB = [[], [], []]
pB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 15:
        cA[0].append([x, y])
        pA[0].append(z)
    else:
        cA[1].append([x, y])
        pA[1].append(z)


for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y < 30:
        cB[0].append([x, y])
        pB[0].append(z)
    elif x > 16:
        cB[1].append([x, y])
        pB[1].append(z)
    else:
        cB[2].append([x, y])
        pB[2].append(z)



# Будем называть центром кластера точку этого кластера,
# сумма расстояний от которой до всех остальных точек
# кластера минимальна.

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

# print(len(cA[0]), len(cA[1]))  # 121 114

def A(cl, p, cent):
    R = []
    for i in range(len(cl)):
        if 'M' in p[i] and 'III' in p[i]:
            R.append([dist(cl[i], cent), cl[i]])
    return min(R)[1]


Ax, Ay = A(cA[1], pA[1], center(cA[1]))
print(int(Ax * 10000), int(Ay * 10000))


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – расстояние между центрами кластеров
# с наименьшим и наибольшим количеством оранжевых гигантов, и
# B2 – наибольшее расстояние между жёлтыми карликами одного кластера.

def B1(cl, p, cent):
    R = []
    for i in range(len(cl)):
        if 'K' in p[i] and 'III' in p[i]:
            R.append(cl[i])
    return R

# print(len(B1(cB[0], pB[0], center(cB[0]))))  # 87
# print(len(B1(cB[1], pB[1], center(cB[1]))))  # 25
# print(len(B1(cB[2], pB[2], center(cB[2]))))  # 28

B1 = dist(center(cB[0]), center(cB[1]))

def B2(cl, p):
    R = []
    for i in range(len(cl)):
        if 'G' in p[i] and 'V' in p[i] and 'I' not in p[i]:
            R.append(cl[i])
    M = []
    for x in permutations(R, r=2):
        M.append(dist(x[0], x[1]))
    return max(M)


B2 = max(B2(cB[0], pB[0]), B2(cB[1], pB[1]), B2(cB[2], pB[2]))
print(int(B1 * 10000), int(B2 * 10000))


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [9, 13]
# на следующем уроке: 17, 7, 11


# region 📖 Пробник (Вариант 2)

# Студент #Илья
# Дата: #Вторник #03Марта2026
# ✅ Верно: 1, 2, 4, 6, 7, 10, 14, 16, 17, 18, 19, 20, 21, 23
# ⛔️ Неверно: 3, 8, 15
# ❔ Без ответа: 5, 9, 11, 12, 13, 22, 24, 25, 26, 27
# Итог: 14/29 первичных балла ~ 62 вторичных

# endregion 📖 Пробник (Вариант 2)
