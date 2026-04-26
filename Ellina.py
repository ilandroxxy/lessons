
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 28766 Досрочная волна 2026 (Уровень: Базовый)

from math import dist
cla = [[], []]
para = [[], []]

clb = [[], [], []]
parb = [[], [], []]

for i in open('files/27A.txt'):
    i = i.replace(',', '.')
    x, y, z = [x for x in i.split()]
    x, y = float(x), float(y)
    if y > 10:
        cla[0].append([x, y])
        para[0].append(z)
    else:
        cla[1].append([x, y])
        para[1].append(z)

for i in open('files/27B.txt'):
    i = i.replace(',', '.')
    x, y, z = [x for x in i.split()]
    x, y = float(x), float(y)
    if y > 22:
        clb[0].append([x, y])
        parb[0].append(z)
    if y < 22 and x < 20:
        clb[1].append([x, y])
        parb[1].append(z)
    if y < 22 and x > 20:
        clb[2].append([x, y])
        parb[2].append(z)

def center(cl):
    r = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        r.append([summa, p])
    return min(r)[1]

# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# A1 – минимальное расстояние от центра кластера с наименьшим количеством точек до красного гиганта, и
# A2 – максимальное расстояние от центра кластера с наименьшим количеством точек до красного гиганта.

print(len(cla[0]))  # 92
print(len(cla[1]))  # 131

def A(cl, cent, par):
    R = []
    for i in range(len(cl)):
        if 'Y' in par[i] and 'III' in par[i]:
            R.append(dist(cent, cl[i]))
    return R


A1 = min(A(cla[0], center(cla[0]), para[0]))
A2 = max(A(cla[0], center(cla[0]), para[0]))
print(int(A1 * 10000), int(A2 * 10000))  # 4940 4940


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – минимальное расстояние между двумя различными жёлтыми сверхгигантами, расположенными в одном и том же кластере, и
# B2 – расстояние между центрами кластеров с минимальным и максимальным количеством жёлтых сверхгигантов.

def B(cl, par):
    R = []
    for i in range(len(cl)):
        if 'Z' in par[i] and 'I' in par[i] and 'II' not in par[i] and 'V' not in par[i]:
            R.append(cl[i])
    return R


from itertools import permutations
r0 = min(dist(p[0], p[1]) for p in permutations(B(clb[0], parb[0]), r=2))
r2 = min(dist(p[0], p[1]) for p in permutations(B(clb[2], parb[2]), r=2))
B1 = min(r0, r2)

print(len(B(clb[0], parb[0])))  # 3
print(len(B(clb[1], parb[1])))  # 1
print(len(B(clb[2], parb[2])))  # 9

B2 = dist(center(clb[1]), center(clb[2]))
print(int(B1 * 10000), int(B2 * 10000))  # 1035 125591





'''
cla = [[], []]
clb = [[], [], []]
for i in open('files/27A.txt'):
    i = i.replace(',', '.')
    x, y = [float(x) for x in i.split()]
    if x > 0:
        cla[0].append([x, y])
    else:
        cla[1].append([x, y])

for i in open('files/27B.txt'):
    i = i.replace(',', '.')
    x, y = [float(x) for x in i.split()]
    if y > -4:
        clb[0].append([x, y])
    elif y < -4 and x > -3:
        clb[1].append([x, y])
    else:
        clb[2].append([x, y])

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return abs(x2 - x1) + abs(y2 - y1)

def center(cl):
    r = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += d(p, g)
        r.append([summa, p])
    return min(r)[1]


# Для каждого файла определите координаты центра каждого кластера,
# затем вычислите два числа: Px − среднее арифметическое абсцисс столиц
# районов, и Py − среднее арифметическое ординат столиц районов.


print(center(cla[0]), center(cla[1]))

A1 = (1.1418865969470884 + -7.416790730200546) / 2 * 10000
A2 = (4.375102181201649 + 0.6379249752247481) / 2 * 10000
print(int(A1), int(A2))

print(center(clb[0]), center(clb[1]), center(clb[2]))


# -30712
# 23820
#
# -31599
# -49340
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [12, 13, 19-21, 24.1, 27]
# КЕГЭ = []
# на следующем уроке: 27 номер с досрока

# Получаются: 1, 2, 3, 4, 6, 10, 11, 15, 17, 18, 23
# 50 / 50: 5, 7, 9, 16,
# Не получаются: 8, 14, 22, 25
# Не разбирали: 24, 26


# region 📖 Пробник (Вариант 2)

# Студент #Эллина
# Дата: #Понедельник #16Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17, 18, 22, 27
# ❔ Без ответа: 6, 14, 24, 26
# Итог: 20/29 первичных балла ~ 78 вторичных

# endregion 📖 Пробник (Вариант 2)



