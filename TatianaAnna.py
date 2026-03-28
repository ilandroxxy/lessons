# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print(7 * 17 + 1 * 16 - 1 * 6)
print(8 * 18 + 2 * 17 - 2 * 7)

# Задание 6
import turtle as t
t.tracer(0)
t.left(90)
t.screensize(5000, 5000)
size = 20

for i in range(2):
    t.forward(1 * size)
    t.left(270)
    t.forward(16 * size)
    t.right(90)

t.up()
t.backward(4 * size)
t.right(90)
t.forward(10 * size)
t.left(90)

t.down()

for i in range(2):
    t.forward(17 * size)
    t.right(90)
    t.forward(7 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(size * x, size * y)
        t.dot(3, 'red')

t.update()
t.done()
'''

# Задание 17 Не правильно
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 43]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < (max(B)) ** 2:
            R.append((x + y) ** 2)
print(len(R), max(R))
'''


# todo глянуть Задание 27
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if 5 < y < 15:
        clustersA[0].append([x, y])
    if 15 < y < 25:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if 25 < x < 35 and 13 < y < 18:
        clustersB[0].append([x, y])
    if 18 < x < 23 and 14 < y < 20:
        clustersB[1].append([x, y])
    if 15 < x < 21 and 25 < y < 31:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
            R.append([summa, p])
    return min(R)[1]

centersA = [center(cl) for cl in clustersA]
print(centersA) # [[6.412136, 10.106562], [8.82346, 21.840848]]
print(len(clustersA[0])) # 301
print(len(clustersA[1])) # 344 - максимальное количество точек

# print(dist([1.0, 1.5], [6.412136, 10.106562]))
A2 = dist([1.0, 1.5], centersA[0]) + dist([1.0, 1.5], centersA[1])
print(int(A2 * 10000))


centersB = [center(cl) for cl in clustersB]
print(centersB) # [[28.939202, 14.512709], [20.757817, 15.787054], [18.749613, 28.956072]]
print(len(clustersB[0])) # 148
print(len(clustersB[1])) # 200
print(len(clustersB[2])) # 902


def B1(cl, center, lenght):
    cnt = 0
    for p in cl:
        if p == center:
            continue
        if dist(center, p) <= lenght:
            cnt += 1
    return cnt

print(B1(clustersB[1], centersB[1], 1.2) )  # Ответ: 38


def B2(cl, center):
    R = []
    for p in cl:
        if p == center:
            continue
        R.append(dist(p, center))
    return min(R)

print(int(B2(clustersB[2], centersB[2]) * 10000))  # Ответ: 1116
'''

# Для файла A определите координаты центра каждого кластера, затем
# найдите два числа: A1 — максимальное количество точек в кластере и A2 —
# сумму расстояний от центров кластеров до точки с координатами (1,0; 1,5).

# 344	294354
# 152	528

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [11, 19-21]
# на следующем уроке: (26)


# region 📖 Пробник (Вариант 2)

# Студент #Татьяна
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 3, 4, 6, 7, 10, 11, 14, 16, 17, 19, 20, 21, 22, 23, 25
# ⛔️ Неверно: 5, 8, 12
# ❔ Без ответа: 9, 13, 15, 18, 24, 26, 27
# Итог: 17/29 первичных балла ~ 70 вторичных


# Студент #Анна
# Дата: #Суббота #28Февраля2026
# ✅ Верно: 1, 2, 4, 7, 8, 11, 12, 14, 15, 16, 17, 18, 23, 25
# ⛔️ Неверно: 3, 5, 6, 10, 19, 20, 21, 27
# ❔ Без ответа: 9, 13, 22, 24, 26
# Итог: 14/29 первичных балла ~ 62 вторичных

# endregion 📖 Пробник (Вариант 2)


