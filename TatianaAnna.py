# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Номер 5 Статград вариант 2

L = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 5 == 0:
        s = s + '11'
    else:
        s = s + bin(n // 5)[2:]

    r = int(s, 2)
    if r > 896 and n % 2 == 0:
        L.append(n)
print(min(L))


# Номер 7 Статград вариант 2
'''
a = 2
b = 56000
c = 15
t = 1647
# print(27 * 60 + 27)
I_music = a * b * c * t  # Только вес МУЗЫКИ


U = 367_217_732
T = 332
I_all = U * T  # Вес МУЗЫКИ и ЗАГОЛОВКОВ

print(I_all - I_music)  # Вес ЗАГОЛОВКОВ
print((I_all - I_music) / 28)  # бит на один ЗАГОЛОВОК
print(((I_all - I_music) / 28) / 2**13)  # бит на один ЗАГОЛОВОК
'''
# 519449.842285 -> 519449



# Номер 8 Статград вариант 2
'''
cnt = 0
s = sorted('0123456789ABCDEF')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                num = a + b + c + d
                if a != '0':
                    if num.count('3') == 1:
                        if num[0] != num[1] and num[1] != num[2] and num[2] != num[3]:
                            cnt += 1
print(cnt) # 13500
'''

# Номер 17 Статград вариант 2
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0 and len(str(abs(x))) == 4 and abs(x) % 9 == 0]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x**2 + y**2)
print(len(R), min(R))
'''

# Номера 19-21 Статград вариант 2
'''
from math import ceil, floor
def F(s, n):
    if s <= 537:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-4, n-1), F(floor(s/5), n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)  # else any(h)

print(max([s for s in range(538, 20000) if F(s, n=2)])) # 13449
print([s for s in range(538, 20000) if F(s, n=3) and not F(s, n=1)]) # 542 543
print([s for s in range(538, 20000) if F(s, n=4) and not F(s, n=2)]) # 546
'''


# Номер 9 Статград вариант 2
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    if 3 <= M.count(max(M)) <= 4 and 4 <= len(copied1) <= 5:
        if min(copied1) + max(copied1) <= sum(copied1) - max(copied1) - min(copied1):
            cnt += 1
print(cnt)
'''


# Номер 24 Статград вариант 2
'''
from re import *
s = open('files/24.txt').readline()
pat = '[1-9]+([+*][1-9]+)*'
M = [x.group(0) for x in finditer(pat, s)]

maxi = 0
for x in M:
    s = s.replace('+', '*')
    test = s.split('*')
    if max([len(i) for i in test]) > 40:
        continue
    maxi = max(maxi, len(x))
print(maxi)
'''

# Номер 6 Статград вариант 2
'''
import turtle as t

t.tracer(0)
t.left(90)
t.screensize(5000, 5000)
size = 10

for i in range(7):
    t.forward(17 * size)
    t.right(90)
    t.forward(26 * size)
    t.right(90)

t.up()

t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)

t.down()

for i in range(7):
    t.forward(278 * size)
    t.right(90)
    t.forward(345 * size)
    t.right(90)

t.up()

for x in range(-25, 25):
    for y in range(-25, 25):
        t.goto(size * x, size * y)
        t.dot(3, 'red')

t.update()
t.done()
'''



from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if 25 < y < 31 and 22 < x < 29:
        clustersB[0].append([x, y])
    if 34 < y < 41 and 20 < x < 27:
        clustersB[1].append([x, y])
    if 43 < y < 50 and 19 < x < 26:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
            R.append([summa, p])
    return min(R)[1]


print(center(clustersB[0])) # [27.076197499885254, 26.453819388436255]
print(center(clustersB[1])) # [21.71746862058927, 37.42511852914926]
print(center(clustersB[2])) # [20.46221682747454, 44.66104487492894]

print(dist([0.0, 0.0], [27.076197499885254, 26.453819388436255])) # 37.853996239350984
print(dist([0.0, 0.0], [21.71746862058927, 37.42511852914926])) # 43.26994268781911
print(dist([0.0, 0.0], [20.46221682747454, 44.66104487492894])) # 49.12546434197848

QxB = 20.46221682747454 * 10000
QyB = 26.453819388436255 * 10000
print(int(QxB), int(QyB))

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [19-21]
# на следующем уроке: 10, (26)