# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 9 Статград вариант 1 (23.10.25)

# if len(M) == len(set(M)): - все элементы строки различные
# if len(M) != len(set(M)): - есть повторяющиеся элементы
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    P = [x for x in M if M.count(x) == 1]
    # M  = [3, 3, 3, 4, 6, 7, 8, 9]
    # if (M.count(min(M)) == 2 and len(P) == 6) or (M.count(min(M)) == 3 and len(P) == 5):
    if 2 <= M.count(min(M)) <= 3 and 5 <= len(P) <= 6:
        if (min(P) ** 2 + max(P) ** 2) <= (sum(P) - max(P) - min(P)) ** 2:
            cnt += 1
print(cnt)
'''


# Номер 23 Статград вариант 1 (23.10.25)
# ctrl + alt + L
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b) + F(a * 3, b)

print(F(6, 14) * F(14, 18) * F(18, 48))  # 24
print(F(6, 14) * F(14, 48))  # 45
print(F(6, 18) * F(18, 48))  # 48

print(45 + 48 - 24)  # 69
'''

# Номер 6 Статград вариант 1 (23.10.25)
'''
print(16 * 24 + 253 * 399 - 19 * 13)  # 101084

import turtle as t
t.tracer(0)
t.screensize(5000, 5000)
t.left(90)
size = 30

# Тут пишем псевдокод
for i in range(7):
    t.forward(15 * size)
    t.right(90)
    t.forward(23 * size)
    t.right(90)

t.up()
t.forward(3 * size)
t.right(90)
t.forward(5 * size)
t.left(90)
t.down()

for i in range(7):
    t.fd(252 * size)
    t.rt(90)
    t.fd(398 * size)
    t.rt(90)

# Тут перебираем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

# Номер 15 Статград вариант 1 (23.10.25)
'''
def f(x, y):
    return (y > A) or (152 != 2 * y + 3 * x) or (A < x)

for A in range(1, 10000):
    if all(f(x, y) == 1 for x in range(1, 100) for y in range(1, 100)):
        print(A)
'''

# Номер 19-21 Статград вариант 1 (23.10.25)
'''
from math import ceil, floor
def F(s, n):
   if s <= 505:
       return n % 2 == 0
   if n == 0:
       return 0
   h = [F(s - 3, n-1), F(floor(s / 5), n-1)]
   # return any(h) if (n - 1) % 2 == 0 else any(h)  # 19 номер (при неудачном)
   return any(h) if (n - 1) % 2 == 0 else all(h)  # для всех остальных случаев

# print(max([s for s in range(506, 100000) if F(s, n=2)]))
print([s for s in range(506, 100000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(506, 100000) if F(s, n=4) and not F(s, n=2)])
'''

# Номер 17 Статград вариант 1 (23.10.25)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if x < 0 and abs(x) % 6 == 0 and len(str(abs(x))) == 3]
count = 0
maxi = 0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            count += 1
            maxi = max(maxi, x**2 + y**2)
print(count, maxi)


M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if x < 0 and abs(x) % 6 == 0 and len(str(abs(x))) == 3]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))
'''

# Номер 25 Статград вариант 1 (23.10.25)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(1_325_000-1, 0, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        S = sum(d)
        if S <= 30_000 and S % 5 == 0:
            print(x)
            cnt += 1
            if cnt == 5:
                break
'''


# Номер 24 Статград вариант 1 (23.10.25)
'''
from re import *
s = open('files/24.txt').readline()
p = '[1-9]+([+*][1-9]+)*'
M = [x.group(0) for x in finditer(p, s)]
print(M)
print(max([len(x) for x in M]))
'''



# Номер 27 Статград вариант 1 (23.10.25)
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 90:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x > 10:
        if 24 <= y <= 33:
            clustersB[0].append([x, y])
        if 33 <= y <= 42:
            clustersB[1].append([x, y])
        if 42 <= y <= 50:
            clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return max(R)[1]


print(center(clustersA[0]))  # [16.99841482246666, 95.6727515672738]
print(center(clustersA[1]))  # [63.94062638636294, 87.77751031781972]

print(len(clustersA[0]))  # 102
print(len(clustersA[1]))  # 113

P1 = 16.99841482246666 + 95.6727515672738
P2 = 63.94062638636294 + 87.77751031781972
print(int(abs(P1 * 10000)), int(abs(P2 * 10000)))  # 1126711 1517181

print(center(clustersB[0]))  # [23.329917580199655, 26.41328219493777]
print(center(clustersB[1]))  # [22.1707588150025, 39.65891347675987]
print(center(clustersB[2]))  # [21.38834573144159, 48.899310705252915]

print(dist([0, 0], [23.329917580199655, 26.41328219493777]))  # 35.24126176243305
print(dist([0, 0], [22.1707588150025, 39.65891347675987]))  # 45.43536028898788
print(dist([0, 0], [21.38834573144159, 48.899310705252915]))  # 53.37231417670156

Qx = 21.38834573144159
Qy = 26.41328219493777
print(int(abs(Qx * 10000)), int(abs(Qy * 10000)))  # 213883 264132
'''


# Вика
# 3, 18, 22



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке:
# Повторить 9 сложные задачи
# Повторить 25 сложные с простыми сомножителями
# Разбирать задачи 24 номера по типу арифметика и символ X 80 раз (как 51993 решу егэ)
