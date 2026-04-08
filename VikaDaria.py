# region Домашка: ******************************************************************
from runpy import run_path

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 27780 Апробация 04.03.26 (Уровень: Базовый)
'''
from math import dist
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
    if y > 23:
        clustersB[0].append([x, y])
    else:
        if x < 25:
            clustersB[1].append([x, y])
        if x > 25:
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
# A1 - максимальное количество точек в кластере и A2 - cумму расстояний от центров
# кластеров до точки с координатами (1,0; 1,5).

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
# B2 - минимальное расстояние от центра кластера с наибольшим количеством
# точек до другой точки этого кластера.

print(center(clustersB[0]))  # [17.885872, 28.168004]
print(center(clustersB[1]))  # [20.226519, 17.396702]
print(center(clustersB[2]))  # [27.979159, 15.559524]

print(len(clustersB[0]))  # 902
print(len(clustersB[1]))  # 200
print(len(clustersB[2]))  # 148


def B1(cl, cent, length):
    cnt = 0
    for p in cl:
        if p == cent:
            continue
        if dist(p, cent) <= length:
            cnt += 1
    return cnt

print(B1(clustersB[1], [20.226519, 17.396702], 1.2))  # 152

def B2(cl, cent):
    R = []
    for p in cl:
        if p == cent:
            continue
        R.append(dist(p, cent))
    return min(R)

print(int(B2(clustersB[0], [17.885872, 28.168004]) * 10000))  # 528
'''


# № 27593 (Уровень: Базовый)
'''
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
    if  18 < x < 26:
        clustersB[0].append([x, y])
    else:
        if 12 < x < 18 and 20 < y < 30:
            clustersB[1].append([x, y])
        if 6 < x < 16 and 10 < y < 20:
            clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

# Для файла А определите координаты центров каждого кластера, затем найдите два числа:
# Px - минимальное расстояние между центром кластера и точкой (5,5; 9,1), и
# Py - расстояние между этой же точкой и серединой отрезка, соединяющего центры кластеров.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

print(dist([7.0391548, 12.3587258], [5.5, 9.1]))  # 3.6039272104120923
print(dist([3.8471735, 6.1225014], [5.5, 9.1]))  # 3.405485773293468

Px = int(3.405485773293468 * 10000)


xc = (7.0391548 + 3.8471735) / 2
yc = (12.3587258 + 6.1225014) / 2

Py = int(dist([xc, yc], [5.5, 9.1]) * 10000)

print(Px, Py)

# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# Q1 - количество точек всех кластеров, находящихся на расстоянии не более 10 от центра
# кластера с наибольшим количеством точек (включая сам центр), и
# Q2 - количество точек всех кластеров, находящихся на расстоянии более 5 от центра кластера
# с наименьшим количеством точек. Гарантируется, что во всех кластерах количество точек различно.

print(center(clustersB[0]))  # [21.3946551, 24.7510816]
print(center(clustersB[1]))  # [14.6275088, 23.5024317]
print(center(clustersB[2]))  # [11.555522, 14.5042082]

print(len(clustersB[0]))  # 100
print(len(clustersB[1]))  # 113
print(len(clustersB[2]))  # 407

def Q1(cent, cl0, cl1, cl2, length):
    cnt = 0
    for p in cl0 + cl1 + cl2:
        if dist(p, cent) <= length:
            cnt += 1
    return cnt

print(Q1([11.555522, 14.5042082], clustersB[0], clustersB[1], clustersB[2], 10))  # 492


def Q2(cent, cl0, cl1, cl2, length):
    cnt = 0
    for p in cl0 + cl1 + cl2:
        if dist(p, cent) > length:
            cnt += 1
    return cnt

print(Q2([21.3946551, 24.7510816], clustersB[0], clustersB[1], clustersB[2], 5))  # 520
'''



from math import dist
clustersA = [[], []]
param_A = [[], []]


clustersB = [[], [], []]
param_B = [[], [], []]
for s in open('files/27_A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 10:
        clustersA[0].append([x, y])
        param_A[0].append(z)
    else:
        clustersA[1].append([x, y])
        param_A[1].append(z)

for s in open('files/27_B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 23:
        clustersB[0].append([x, y])
        param_B[0].append(z)
    if y < 23 and x < 20:
        clustersB[1].append([x, y])
        param_B[1].append(z)
    if y < 23 and x > 20:
        clustersB[2].append([x, y])
        param_B[2].append(z)


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

print(len(clustersA[0]))  # 92
print(len(clustersA[1]))  # 131

def A1(cl, cent, par):
    R = []
    for i in range(len(cl)):
        if 'Y' in par[i] and 'III' in par[i]:
            R.append(dist(cent, cl[i]))
    return min(R)

print(int(A1(clustersA[0], [7.0391548, 12.3587258], param_A[0]) * 10000))  # 4940

def A2(cl, cent, par):
    R = []
    for i in range(len(cl)):
        if 'Y' in par[i] and 'III' in par[i]:
            R.append(dist(cent, cl[i]))
    return max(R)

print(int(A2(clustersA[0], [7.0391548, 12.3587258], param_A[0]) * 10000))







print(center(clustersB[0]))  # [13.9823808, 26.4800432]
print(center(clustersB[1]))  # [15.861917, 18.8540334]
print(center(clustersB[2]))  # [26.6431823, 12.4121727]

def yellow(cl, par):
    R = []
    for i in range(len(cl)):
        if 'Z' in par[i] and 'IV' in par[i]:
            R.append(cl[i])
    return R

from itertools import permutations
R = []
for p in permutations(yellow(clustersB[2], param_B[2]), 2):
    R.append(dist(p[0], p[1]))
B1 = int(min(R) * 10000)
print(B1)  # 1825


def count_yellow(cl, par):
    cnt = 0
    for i in range(len(cl)):
        if 'Z' in par[i] and 'IV' in par[i]:
            cnt += 1
    return cnt

print(count_yellow(clustersB[0], param_B[0]))  # 1
print(count_yellow(clustersB[1], param_B[1]))  # 3
print(count_yellow(clustersB[2], param_B[2]))  # 10

B2 = dist([13.9823808, 26.4800432], [26.6431823, 12.4121727])
print(int(B2 * 10000))  # 189261


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 16, 25]
# на следующем уроке:


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

