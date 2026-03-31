# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Номер 5 Апробация вариант 1
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if 125 < r < 130:
        RES.append(n)
print(max(RES))
'''


# Номер 13 Апробация вариант 1
'''
from ipaddress import *
net = ip_network('172.16.96.0/255.255.224.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 == 0:
        cnt += 1
print(cnt)
'''

# Номер 11 Апробация вариант 1
'''
alp = 10 + 26 + 8164
print(alp, 2**14)
i = 14

byte = 156 * 2 ** 10 / 835
print(byte) # 191.3101 -> 192
bit = 192 * 8

sym = bit / i
print(sym)  # 109.714 -> 109
'''

# № 27766 Апробация 04.03.26 (Уровень: Базовый)
# На предприятии каждой изготовленной детали присваивают серийный номер,
# содержащий десятичные цифры, 26 латинских букв (без учёта регистра)
# и символы из 34-символьного специального алфавита. В базе данных для
# хранения каждого серийного номера отведено одинаковое и минимально
# возможное число байт. При этом используется посимвольное кодирование
# серийных номеров, все символы кодируются одинаковым и минимально
# возможным числом бит. Известно, что для хранения 1142 серийных номеров
# требуется более 305 Кбайт памяти. Определите минимально возможную длину
# серийного номера. В ответе запишите только целое число.
'''
alp = 10 + 26 + 34
# #print(alp, 2**7)
i = 7

byte = 305 * 2 ** 10 / 1142
print(byte) # 273.48511 -> 274
bit = 274 * 8

sym = bit / i
print(sym)  # 313.1428 -> 313 
'''


# Номер 9 Апробация вариант 1
'''
n = 0
RES = []
for i in open('files/9.csv'):
    M = [int(x) for x in i.split(',')]
    n += 1
    if len(M) == len(set(M)):
        # M = sorted(M)
        # if M[4] - M[0] == M[1] + M[2] + M[3]:
        if max(M) - min(M) == sum(M) - max(M) - min(M):
            RES.append(n)
print(min(RES))
'''

# Номер 17 Апробация вариант 1
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 43]
RES = []
i = 0
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < max(B) ** 2:
            RES.append((x+y) ** 2)
print(len(RES), max(RES))
'''


# Номер 6 Апробация вариант 1
'''
print(3 * 10 + 16 * 8 - 2*3)
print(4 * 11 + 17 * 9 - 3*4)

import turtle as t

t.tracer(0)
t.screensize(5000, 5000)
size = 20
t.left(90)

for i in range(2):
    t.forward(3 * size)
    t.left(90)
    t.back(10 * size)
    t.left(90)

t.up()
t.back(10 * size)
t.right(90)
t.forward(8 * size)
t.left(90)

t.down()
for i in range(2):
    t.forward(16 * size)
    t.right(90)
    t.forward(8 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# Номер 27 Апробация вариант 1
"""
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
    if y > 25:
        clustersB[0].append([x, y])
    if y < 25 and x > 25:
        clustersB[1].append([x, y])
    if y < 25 and x < 25:
        clustersB[2].append([x, y])

# Проверка, что класетры не пустые:
'''
print(clustersA[0])
print(clustersA[1])
print(clustersB[0])
print(clustersB[1])
print(clustersB[2])
'''

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


print(center(clustersA[0]))  # [8.856, 20.903738]
print(center(clustersA[1]))  # [6.016644, 8.404493]

print(len(clustersA[0]))  # 344
print(len(clustersA[1]))  # 301

A1 = 301

A2 = dist([8.856, 20.903738], [-1.0, 1.3]) + dist([6.016644, 8.404493], [-1.0, 1.3])
print(int(A2 * 10000))  # 319272


print(center(clustersB[0]))  # [17.867681, 28.209279]
# print(center(clustersB[1]))  # [27.887459, 15.531916]
print(center(clustersB[2]))  # [20.396937, 17.39094]

print(len(clustersB[0]))  # 902
# print(len(clustersB[1]))  # 148
print(len(clustersB[2]))  # 200

def B1(cl, center, length):
    cnt = 0
    for p in cl:
        if p == center:
            continue
        if dist(p, center) <= length:
            cnt += 1
    return cnt

print(B1(clustersB[2], [20.396937, 17.39094], 1.6))  # 182

def B2(cl, center):
    R = []
    for p in cl:
        R.append(dist(p, center))
    return max(R)

print(int(B2(clustersB[0], [17.867681, 28.209279]) * 10000))  # 26825
"""


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 25, 27]
# КЕГЭ = [12, 17]
# на следующем уроке: 6 8 9 10 14 22 26 27


# region 📖 Пробник (Вариант 2)

# Студент #Софья
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 3, 5, 7, 8, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 6, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# Студент #Лиза
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# endregion 📖 Пробник (Вариант 2)
