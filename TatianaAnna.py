# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 6 ЕГКР 13.12.25 Вариант 2
'''
print(34 * 16 + 21 * 25 - 12 * 21)

import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
size = 20

for i in range(8):
    t.forward(33 * size)
    t.right(90)
    t.forward(15 * size)
    t.right(90)
t.penup()
t.forward(5 * size)
t.right(90)
t.forward(4 * size)
t.left(90)
t.pendown()
for i in range(8):
    t.forward(20 * size)
    t.right(90)
    t.forward(24 * size)
    t.right(90)
t.penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(size * x, size * y)
        t.dot(3, 'red')

t.update()
t.done()
'''
from asyncio.base_subprocess import ReadSubprocessPipeProto

# Задание 7 ЕГКР 13.12.25 Вариант 2
'''
pixels = 1280 * 1024
i = 14
I = pixels * i # бит
T = 200
print((I * T) / 2**23)
'''


# Задание 8 ЕГКР 13.12.25 Вариант 2
'''
L = []
n = 0
cnt = 0
s = sorted('ГРАНИТ')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        num = a + b + c + d + e + f
                        n += 1
                        if num.count('Т') == 1:
                            if a not in 'РТ':
                                if n % 2 == 0:
                                    L.append(n)
print(max(L))
'''



# Задание 15 ЕГКР 13.12.25 Вариант 2
'''
def F(x, a1, a2):
    P = 225 <= x <= 464
    Q = 140 <= x <= 315
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

RES = []
M = [x for x in range(120, 480)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''


def F(x, A):
    y = 78_125 - 4 * x
    return (A > x) and (A > 78_125 - 4 * x)

for A in range(1, 100000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break



for A in range(0, 100000):
    if all(A > x and A > 78125 - 4 * x for x in range(1, 10000)):
        print(A)
        break



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [19-21]
# на следующем уроке: 10, (26)