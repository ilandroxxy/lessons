# region Домашка: ******************************************************************

'''
from math import dist
clustersA = [[],[]]
clustersB = [[],[],[]]

for s in open('files/27A.txt'):
    s = s.replace(',','.')
    x,y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s =s.replace(',','.')
    x,y = [float(i) for i in s.split()]
    if y < 10:
        clustersB[0].append([x, y])
    if y > 10 and x < 17:
        clustersB[1].append([x, y])
    if y > 10 and x > 17:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return max(R)[1]

print(center(clustersA[0]))  # [0.1663069, 16.1520663]
print(center(clustersA[1]))  # [3.4435388, 6.1127361]

print(center(clustersB[0]))  # [18.1424701, 6.1934274]
print(center(clustersB[1]))  # [14.747434, 21.5194643]
print(center(clustersB[2]))  # [19.4524463, 14.961161]

print(len(clustersA[0]))  # 100
print(len(clustersA[1]))  # 137

print(len(clustersB[0]))  # 439
print(len(clustersB[1]))  # 98
print(len(clustersB[2]))  # 102

PxA = 0.1663069 * 10000
PyA = 6.1127361 * 10000
print(int(PxA), int(PyA))  # 1663 61127

PxB = 14.747434 * 10000
PyB = 6.1934274 * 10000
print(int(PxB), int(PyB))  # 147474 61934
'''


# № 21930 (Уровень: Базовый)
'''
from math import dist
clustersA = [[],[]]
clustersB = [[],[],[]]

for s in open('files/27A.txt'):
    s = s.replace(',','.')
    x,y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s =s.replace(',','.')
    x,y = [float(i) for i in s.split()]
    if y < 10:
        clustersB[0].append([x, y])
    if y > 10 and x < 17:
        clustersB[1].append([x, y])
    if y > 10 and x > 17:
        clustersB[2].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return max(R) [1]


# Вариант 1 для третьей части

print(center(clustersA[0]))  # [0.1663069, 16.1520663]
print(center(clustersA[1]))  # [3.4435388, 6.1127361]

PxA = (0.1663069 + 3.4435388) / 2
PyA = (16.1520663 + 6.1127361) / 2
print(int(PxA * 10000), int(PyA * 10000))  # 18049 111324


# Вариант 2 для третьей части
centersA = [center(cl) for cl in clustersA]
print(centersA)  # [[0.1663069, 16.1520663], [3.4435388, 6.1127361]]

PxA = sum([x for x, y in centersA]) / 2 * 10000
PyA = sum([y for x, y in centersA]) / 2  * 10000
print(int(PxA), int(PyA)) # 18049 111324



print(center(clustersB[0]))  # [18.1424701, 6.1934274]
print(center(clustersB[1]))  # [14.747434, 21.5194643]
print(center(clustersB[2]))  # [19.4524463, 14.961161]

PxB = (18.1424701 + 14.747434 + 19.4524463) / 3
PyB = (6.1934274 + 21.5194643 + 14.961161) / 3
print(int(PxB * 10000), int(PyB * 10000))  # 174474 142246
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#  № 25345 (Уровень: Базовый)
# Черепаха выполнила следующую программу:
# Повтори 6 [Вперёд 33 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Вперёд 3 Направо 90 Вперёд 9 Налево 90
# Опустить хвост
# Повтори 6 [Вперёд 24 Направо 90 Вперёд 25 Направо 90]

import turtle as t   # Даем короткое имя библиотеки
t.tracer(0)  # Отключения анимации отрисовки
t.screensize(5000, 5000)
size = 20
t.left(90)

for i in range(6):
    t.forward(33 * size)
    t.right(90)
    t.forward(20 * size)
    t.right(90)

t.up() # Поднять хвост
t.forward(3 * size)
t.right(90)
t.forward(9 * size)
t.left(90)
t.down()  # # Опустить хвост

for i in range(6):
    t.fd(24 * size)
    t.rt(90)
    t.fd(25 * size)
    t.rt(90)

# Момент отрисовки точек
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()  # Для корректной работы t.tracer()
t.done()  # Зафиксировать вывод отрисовки

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
