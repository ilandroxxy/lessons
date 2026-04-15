# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 27780 Апробация 04.03.26 (Уровень: Базовый)

"""
from math import dist
'''
def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
'''

print(dist([3, 4], [0, 0]))  # 5.0

clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 15:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 22:
        clustersB[0].append([x, y])
    if y < 22 and x < 25:
        clustersB[1].append([x, y])
    if y < 22 and x > 25:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# A1 - максимальное количество точек в кластере и
# A2 - cумму расстояний от центров кластеров до точки с координатами (1,0; 1,5).

print(center(clustersA[0]))  # [8.815578, 20.944823]
print(center(clustersA[1]))  # [6.017217, 8.334924]

print(len(clustersA[0]))  # 344
print(len(clustersA[1]))  # 301

A1 = 344

A2 = dist([8.815578, 20.944823], [1.0, 1.5]) + dist([6.017217, 8.334924], [1.0, 1.5])
print(A1, int(A2 * 10000))  # 344 294354


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 - число точек, находящихся на расстоянии не более 1,2 от центра, не включая центр,
# в кластере со средним количеством точек, и


print(center(clustersB[0]))  # [17.885872, 28.168004]
print(center(clustersB[1]))  # [20.226519, 17.396702]
print(center(clustersB[2]))  # [27.979159, 15.559524]

print(len(clustersB[0]))  # 902
print(len(clustersB[1]))  # 200
print(len(clustersB[2]))  # 148

def B1(cl, center, length):
    cnt = 0
    for p in cl:
        if p == center:
            continue
        if dist(p, center) <= length:
            cnt += 1
    return cnt

B1 = B1(clustersB[1], center(clustersB[1]), 1.2)


# B2 - минимальное расстояние от центра кластера с наибольшим количеством точек до другой
# точки этого кластера.

def B2(cl, center):
    R = []
    for p in cl:
        if p == center:
            continue
        R.append(dist(p, center))
    return min(R)

B2 = B2(clustersB[0], center(clustersB[0]))
print(B1, int(B2 * 10000))  # 152 528
"""


# № 28766 Досрочная волна 2026 (Уровень: Базовый)
'''
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
        paramsA[1].append([x, y])


for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 22:
        clustersB[0].append([x, y])
        paramsB[0].append(z)
    if y < 22 and x < 20:
        clustersB[1].append([x, y])
        paramsB[1].append(z)
    if y < 22 and x > 20:
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
# A1 – минимальное расстояние от центра кластера с наименьшим количеством точек до красного гиганта, и
# A2 – максимальное расстояние от центра кластера с наименьшим количеством точек до красного гиганта.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

print(len(clustersA[0]))  # 92
print(len(clustersA[1]))  # 131

def A1(cl, center, param):
    R = []
    for i in range(len(cl)):
        if 'Y' in param[i] and 'III' in param[i]:
            R.append(dist(center, cl[i]))
    return min(R)

A1 = A1(clustersA[0], center(clustersA[0]), paramsA[0])
print(int(A1 * 10000))  # 4940




# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – минимальное расстояние между двумя различными жёлтыми сверхгигантами, расположенными в одном и том же кластере, и
# B2 – расстояние между центрами кластеров с минимальным и максимальным количеством жёлтых сверхгигантов.

print(center(clustersB[0]))  # [13.9823808, 26.4800432]
print(center(clustersB[1]))  # [15.861917, 18.8540334]
print(center(clustersB[2]))  # [26.6431823, 12.4121727]
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 27]
# КЕГЭ = [8, 15, 23]
# на следующем уроке:


# region 📖 Пробник (Вариант 2)

# Студент #Федор
# Дата: #Вторник #03Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 10, 17, 22, 24, 27
# ❔ Без ответа: 26
# Итог: 19/29 первичных балла ~ 75 вторичных

# Студент #Вадим
# Дата: #Суббота #04Апреля2026
# ✅ Верно: 1, 2, 7, 10, 11, 12, 13, 14, 15, 16, 19, 20, 23, 25
# ⛔️ Неверно: 3, 4, 5, 6, 8, 9, 18, 21, 22, 24
# ❔ Без ответа: 17, 26, 27
# Итог: 14/29 первичных балла ~ 62 вторичных


# endregion 📖 Пробник (Вариант 2)



