# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


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
        clustersB[1].append([x, y])
    if y < 23 and x < 25:
        clustersB[2].append([x, y])
    if y < 23 and x > 25:
        clustersB[0].append([x, y])

# Проверка:
'''
print(clustersA[0])
print(clustersA[1])

print(clustersB[0])
print(clustersB[1])
print(clustersB[2])
'''


# Поиск расстояния между двумя точками
'''
def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([3, 4], [0, 0]))  # 5.0
print(dist([3, 4], [0, 0]))  # 5.0
'''

# Будем называть центром кластера точку этого кластера,
# сумма расстояний от которой до всех остальных точек
# кластера минимальна.

def center(cluster):
    R = []
    for p in cluster:
        summa = 0
        for g in cluster:
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
print(int(A2 * 10000))  # 294354




# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 - число точек, находящихся на расстоянии не более 1,2 от центра, не включая центр,
# в кластере со средним количеством точек, и
# B2 - минимальное расстояние от центра кластера с наибольшим количеством точек до другой точки этого кластера.

print(center(clustersB[0]))  # [27.979159, 15.559524]
print(center(clustersB[1]))  # [17.885872, 28.168004]
print(center(clustersB[2]))  # [20.226519, 17.396702]

print(len(clustersB[0]))  # 148
print(len(clustersB[1]))  # 902
print(len(clustersB[2]))  # 200

def B1(cluster, center, length):
    cnt = 0
    for p in cluster:
        if p == center:
            continue
        if dist(p, center) <= length:
            cnt += 1
    return cnt

print(B1(clustersB[2], center(clustersB[2]), 1.2))  # 152

def B2(cluster, center):
    R = []
    for p in cluster:
        if p == center:
            continue
        R.append(dist(p, center))
    return min(R)

print(B2(clustersB[1], center(clustersB[1])))  # 0.05287032785977548

print(int(0.05287032785977548 * 10000))  # 528



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 5, 9, 12, 13, 14, 15, 16, 17, 18, 22, 24, 25, 26, 27


# region 📖 Пробник (Вариант 2)

# Студент #Никита
# Дата: #Вторник #17Марта2026
# ✅ Верно: 1, 2, 3, 4, 7, 10, 11, 19, 20, 21, 23
# ⛔️ Неверно: 6, 8
# ❔ Без ответа: 5, 9, 12, 13, 14, 15, 16, 17, 18, 22, 24, 25, 26, 27
# Итог: 11/29 первичных балла ~ 54 вторичных

# endregion 📖 Пробник (Вариант 2)
