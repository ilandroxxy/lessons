# region Домашка: ******************************************************************

# Задача 6
'''
import turtle as t
t.tracer(0)
t.screensize(-2000,2000)
l=40
t.left(90)


t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*l)
    t.right(45)
t.right(315)
t.forward(10 * l)
for i in range(2):
    t.right(90)
    t.forward(10*l)


t.up()
for x in range(-50,50):
    for y in range(-50, 50):
        t.goto(x*l,y*l)
        t.dot(4,'red')
t.update()
t.done()
'''


# Задача 8
'''
from itertools import *

cnt = 0
chet = '02468ACE'
nechet = '13579BDF'
for x in permutations('0123456789ABCDEF', 3):
    a = ''.join(x)
    if a[0] != '0':
        # if a[0] in chet and a[1] in nechet and a[2] in chet:
        #     cnt += 1
        # if a[0] in nechet and a[1] in chet and a[2] in nechet:
        #     cnt += 1
        for z in chet:
            a = a.replace(z, '2')
        for z in nechet:
            a = a.replace(z, '1')
            
        if '22' not in a and '11' not in a:
            cnt += 1

print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)

# Вариант 1
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break
'''

# Вариант 2
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    k = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == True:
                k += 1
    if k == 9801:
        print(A)
        break
'''

# Вариант 3
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''

# Вариант 4
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


R = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))
'''

# print(min([A for A in range(1, 1000) if all( ((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100))]))


# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

# № 18044 (Уровень: Базовый)
'''
def F(x, a1, a2):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2
    return (not(M or N)) == (not A)


R = []
M = [x / 4 for x in range(30 * 4, 80 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(min(R))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Лиза 11/14 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

