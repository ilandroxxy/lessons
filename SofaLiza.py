# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Пробник номер 2, задача 14
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''


# Пробник номер 2, задача 8
'''
n = 0
s = sorted('СБОРНИК')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if word[0] != 'Р':
                            if word.count('Б') == 2:
                                if word.count('К') <= 1:
                                    print(n)

n = 0
from itertools import product
for p in product(sorted('СБОРНИК'), repeat=6):
    word = ''.join(p)
    n += 1
    if word[0] != 'Р':
        if word.count('Б') == 2:
            if word.count('К') <= 1:
                print(n)
'''


# Пробник номер 2, задача 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if sum(copied2) / 4 < sum(copied1) / 3:
            cnt += 1
print(cnt)
'''


# Пробник номер 2, задача 17
'''
M = [int(s) for s in open('files/17.txt')]
R = []
B = [x for x in M if abs(x) % 100 == 29]
A = [x for x in M if len(str(abs(x))) == 5]  
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''
#2981 99379'''


# Пробник номер 2, задача 25
'''
print(11 * 11 + 11 * 13 - 48)

import turtle as t
t.tracer(0)
t.screensize(5000, 5000)
size = 20
t.left(90)

for i in range(4):
    t.forward(10 * size)
    t.right(270)

t.up()
t.forward(3 * size)
t.right(270)
t.forward(5 * size)
t.right(90)
t.down()

for i in range(2):
    t.forward(10 * size)
    t.right(270)
    t.forward(12 * size)
    t.right(270)


t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()  
t.done()
'''


# Пробник номер 2, задача 27

from math import dist
clustersA = [[],[]]
clustersB = [[],[],[],[]]

for s in open('files/27A.txt'):
    s = s.replace(',','.')
    x,y = [float(i) for i in s.split()]
    if y < -8:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s =s.replace(',','.')
    x,y = [float(i) for i in s.split()]
    if x > -2:
        clustersB[0].append([x, y])
    if -5 < x < -2:
        clustersB[1].append([x, y])
    if y > -5 and x < -6:
        clustersB[2].append([x, y])
    if y < -6:
        clustersB[3].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return max(R) [1]

print(center(clustersA[0]))
print(center(clustersA[1]))

print(len(clustersA[0]))
print(len(clustersA[1]))

print('-------------')

print(center(clustersB[0]))
print(center(clustersB[1]))
print(center(clustersB[2]))
print(center(clustersB[3]))


print(len(clustersB[0]))
print(len(clustersB[1]))
print(len(clustersB[2]))
print(len(clustersB[3]))


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: Вариант ЕГКР добиваем 27 номер: 8, 9, 17



# Софья Пробник №2
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 3, 5, 7, 8, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 6, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
#
# Итог: 16/29 первичных балла ~ 67 вторичных


# Лиза Пробник №2
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 11, 13, 15, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 6, 8, 9, 10, 12, 14, 17, 22, 24, 25, 26, 27
# ❔ Без ответа: Нет
#
# Итог: 15/29 первичных балла ~ 65 вторичных
