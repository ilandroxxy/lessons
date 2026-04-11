# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 8 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
n = 0
alp = sorted('АПРЕЛЬ')
for a in alp:
    for b in alp:
        for c in alp:
            for d in alp:
                for e in alp:
                    word = a + b + c + d + e
                    n += 1
                    # if a != 'Ь' and a != 'Р':
                    if a not in 'ЬР':
                        if word.count('Л') >= 2:
                            if n % 2 == 0:
                                print(n)
'''

# Задание 14 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def G(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 2 * 2187**567 + 729**566 - 2 * 243**565 + 81**564 - 2*27**563 - 6561
n27 = G(n, 27)
print(len([x for x in n27 if x > '9' and x in alp[0::2]]))
'''

# Задание 6 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
import turtle as t
t.tracer(0)
t.left(90)
t.screensize(5000, 5000)
size = 40

t.right(315 * size)
for i in range(7):
    t.forward(12 * size)
    t.right(45)
    t.forward(6 * size)
    t.right(135)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

# Задание 9 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
from itertools import permutations
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    print(M)
    if max(M) < sum(M) - max(M):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M, 4)):
            cnt += 1
print(cnt)
'''


# Задание 17 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
R = []
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if abs(x) % 23 == 0]
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % min(A) == 0) + (y % min(A) == 0) >= 1:
        R.append(x + y)
print(len(R), max(R))
'''

# Задание 16 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 10:
        return 3
    if n >= 10:
        return (n + 4) * F(n - 5)

print((F(2574870) / 683 + F(257477) / 67) / F(257472))
'''
'''
# F(257487) = (257487 + 4) * F(257482)
# F(257482) = (257482 + 4) * F(257477)
# F(257477) = (257477 + 4) * F(257472) / F(257472)

print(((257487 + 4) * (257482 + 4) * (257477 + 4)) / 683)  # 24994252792782.0
print((257477 + 4) / 67)  # 3843.0
print(24994252792782 + 3843)
'''

# № 27771 Апробация 04.03.26 (Уровень: Базовый)
'''
# F(2024) = 2024 * F(2023)
# F(2023) = 2023 * F(2022) / F(2022)

print(2024 * 2023)
print(2023)
print(4094552 - 2*2023)
'''


# Задание 27 Досрочная волна 07.04.26 вариант 1 (https://disk.yandex.ru/i/vSKwP7fEAs4V0g)
'''
from math import dist
clustersA = [[], []]
paramsA = [[], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 10:
        clustersA[0].append([x, y])
        paramsA[0].append(z)
    else:
        clustersA[1].append([x, y])
        paramsA[1].append(z)


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

# print(len(clustersA[0]), clustersA[0])
# print(len(paramsA[0]), paramsA[0])

# Для файла А определите координаты центра каждого кластера, затем
# найдите два числа: A1 – минимальное расстояние от центра кластера с
# наименьшим количеством точек до красного гиганта, и A2 – максимальное
# расстояние от центра кластера с наименьшим количеством точек до
# красного гиганта.

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

A1 = A1(clustersA[0], center(clustersA[0]), paramsA[0])
print(int(A1 * 10000))

def A2(cl, cent, par):
    R = []
    for i in range(len(cl)):
        if 'Y' in par[i] and 'III' in par[i]:
            R.append(dist(cent, cl[i]))
    return max(R)

A2 = A2(clustersA[0], center(clustersA[0]), paramsA[0])
print(int(A2 * 10000))
'''



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [5, 11, 19-21, 25]
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


