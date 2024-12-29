# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задача 2
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (z == w)) or (not(y <= w))
                if F == 0:
                    print(x, y, z, w)
'''

# Задача 6
'''
import turtle as t
k = 45
t.screensize(2000,2000)
t.tracer(0)
t.left(90)
t.down()
t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*k)
    t.right(45)

t.right(315)
t.forward(10*k)

for i in range(2):
    t.right(90)
    t.forward(10*k)
t.up()

for x in range(-30,30):
    for y in range(-30,30):
        t.setpos(x*k, y*k)
        t.dot(2, 'blue')
t.update()
t.done()
'''


# Задача 8
'''
# Вариант 1

s = '0123456789ABCDEF'
cnt = 0
s1 = '13579BDF'
s2 = '02468ACE'
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if a != '0':
                if len(num) == len(set(num)):  # все цифры различны
                    # if a in s1 and b in s2 and c in s1:
                    #     cnt += 1
                    # if a in s2 and b in s1 and c in s2:
                    #     cnt += 1
                    for x in s1:
                        num = num.replace(x, '1')
                    for x in s2:
                        num = num.replace(x, '2')
                    if '11' not in num and '22' not in num:
                        cnt += 1
print(cnt)


# Вариант 2

from itertools import *
cnt = 0
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in s1:
            num = num.replace(x, '1')
        for x in s2:
            num = num.replace(x, '2')
        if '11' not in num and '22' not in num:
            cnt += 1
print(cnt)
'''


# Задача 12
'''
for n in range(3, 1000):
    s = '1' + '8' * n

    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)

    if s.count('1') == 3:
        print(n)
        break
'''

# Задача 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:23]:
    A = int(f'7{x}38596',23)
    B = int(f'14{x}36',23)
    C = int(f'61{x}7',23)

    if (A + B + C) % 22 == 0:
        print((A + B + C) // 22)
'''

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2*n + 5 + F(n - 2)


print(F(3027) - F(3023))
# RecursionError: maximum recursion depth exceeded
'''

# https://stepik.org/lesson/1038709/step/5?unit=1062775
'''
import sys
sys.setrecursionlimit(100000000)

def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n + 1) * F(n - 1)

print((F(2024) - 3 * F(2023)) // F(2022))
'''


# https://stepik.org/lesson/1038709/step/4?unit=1062775
'''
from functools import *

@lru_cache(None)
def F(n):
    if n > 1_000_000:
        return n
    if n <= 1_000_000:
        return n + F(2*n)

def G(n):
    return F(n) / n

cnt = 0
r = G(2000)
for n in range(1, 10**6+1):
    if G(n) == r:
        cnt += 1
print(cnt)
'''


# Задача 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        print(n)
'''


# № 17668 Пересдача 04.07.24 (Уровень: Базовый)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


M = []
for n in range(28, 1000):
    s = convert(n, 2)  # s = f'{n:b'}
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if n > 27:
        M.append(r)

print(min(M))
'''




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 16]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
