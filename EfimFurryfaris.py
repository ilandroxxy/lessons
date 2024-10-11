# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

"""
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = y and (x or z) or (not(y or z)) or w
                if F == False:
                    print(x, y, z, w, F)
"""

'''
M = []
for n in range(1, 10000):
    a = f'{n:b}'  # a = bin(i)[2:]
    if n % 5 == 0:
        a = a[:3] + a
    else:
        x = (n % 5) * 5
        a = a + bin(x)[2:]
    r = int(a, 2)
    if r < 313:
        M.append(n)

chet = [x for x in M if x % 2 != 0]
print(max(chet))  # 35
'''

'''
# i  0     1    2
M = ['a', 'b', 'c']
for i in range(len(M)):
    print(i, end=' ')  # 0 1 2 
'''


"""
from turtle import *

left(90)
m = 30
tracer(0)

for i in range(2):
    forward(11 * m)
    right(90)
    forward(17 * m)
    right(90)

up()
forward(7 * m)
left(90)
backward(1)
right(90)
down()

for i in range(2):
    forward(15 * m)
    right(90)
    forward(7 * m)
    right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
done()
"""


'''
s = 'ЛЮСТРА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for g in s:
                    word = a + b + c + d + g
                    if word.count('Ю') <= 2:
                        if g not in 'СРТЛ':
                            count += 1
print(count)


# Вариант 2
from itertools import *
cnt = 0
for p in product('ЛЮСТРА', repeat=5):
    word = ''.join(p)
    if word.count('Ю') <= 2:
        if word[-1] not in 'СРТЛ':
            cnt += 1
print(cnt)
'''


'''
count = 0
for a in open('9.txt'):
    M = sorted([int(i) for i in a.split()])
    if M[3] < M[1] + M[2] + M[0]:
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if sum(chet) == sum(nechet):
            count += 1
print(count)
'''


'''
s = 111 * '3'
while '33333' in s or '1111' in s:
    if s.count('33333'):
        s = s.replace('33333', '111', 1)
    else:
        s = s.replace('111', '33', 1)

print(s)
'''


'''
from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphbaet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

A = []
for x in alphbaet[:24]:
    a = int(f'12{x}734', 24) + int(f'8{x}95{x}3', 24) + int(f'24{x}796', 24)
    if a % 23 == 0:
        A.append(a // 23)
print(max(A))
'''



'''
def f(x, a1, a2):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2
    return (not(M or N)) == (not A)


K = []
M = [i / 4 for i in range(20 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(f(x, a1, a2) for x in M):
            K.append(a2 - a1)
print(min(K))
'''


"""
from sys import *
setrecursionlimit(4100)
def F(n):
    if n<5:
        return 4**4
    if n>4:
        return 4*F(n-4)+4
print(F(4048)//F(4036))
"""

M = [int(i) for i in open('17.txt')]
D = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i+1]
    if abs(x) % 10 + abs(y) % 10 == len(D):
        R.append(x + y)
print(len(R), min(R))


'''
def F(a, b):
    if a < b or a == 24:
        return 0
    if a == b:
        return 1
    return F(a - 2, b) + F(a - 3, b) + F(a//4, b)

print(F(36, 13))


# Вариант 2
def F(a, b):
    if a <= b or a == 24:
        return a == b  
    return F(a - 2, b) + F(a - 3, b) + F(a//4, b)

print(F(36, 13))


print(True + False + True)  # 2
'''
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14?, 15?, 16?, 17, 19-21?, 23]
# КЕГЭ = []
# на следующем уроке:
