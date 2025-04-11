# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# номер 2 21401
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = x and (z <= w) and (not y)
                if F == 1:
                    print(x, y, z, w)
'''
from pprint import pformat

# № 21404 Досрочная волна 2025 (Уровень: Базовый)
'''
for n in range(1, 10000):
    b = f'{n:b}'  # b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    r = int(b, 2)
    if r > 480:
        print(n)
        break
'''


# № 21405 Досрочная волна 2025 (Уровень: Базовый)
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат,
# хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Направо 30 Повтори 3 [Направо 150 Вперёд 6 Направо 30 Вперёд 12].

# Определите, сколько точек с целочисленными координатами будут
# находиться внутри области, которая ограничена линией, заданной алгоритмом.
# Точки на линии учитывать не следует.
'''
import turtle as t
t.left(90)
t.screensize(-2000, 2000)
t.tracer(0)
t.down()
s = 60

# Тут будет псевдокод:
t.right(30)
for i in range(3):
    t.right(150)
    t.forward(6 * s)
    t.right(30)
    t.forward(12 * s)

# Тут будут точки:
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*s, y*s)
        t.dot(2, 'red')

t.update()
t.done()
'''

# № 21407 Досрочная волна 2025 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    # if word[0] in 'ДГШ': # слово не должно начинаться с гласной
    if word[0] not in 'ИАЭ': # слово не должно начинаться с гласной
        if word[-1] not in 'ДГШ':
            cnt += 1
print(cnt)
'''

'''
from itertools import product, permutations

for p in permutations('abc', r=3):  # тасовать
    print(*p)
    # a b c
    # a c b
    # b a c
    # b c a
    # c a b
    # c b a

for p in product('abc', repeat=3):
    print(*p)
    # a a a
    # a a b
    # a a c
    # a b a
    # a b b
    # a b c
    # a c a
    # a c b
    # a c c
    # b a a
    # b a b
    # b a c
    # b b a
    # b b b
    # b b c
    # b c a
    # b c b
    # b c c
    # c a a
    # c a b
    # c a c
    # c b a
    # c b b
    # c b c
    # c c a
    # c c b
    # c c c
'''

# № 21408 Досрочная волна 2025 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied3) == 6 and len(uncopied) == 1:
        if max(copied3) > uncopied[0]:
            cnt += 1
print(cnt)
'''


# № 21411 Досрочная волна 2025 (Уровень: Базовый)
'''
for n in range(4, 10000):
    s = '3' + '1' * n

    while '31' in s or '211' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '211' in s:
            s = s.replace('211', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '2', 1)
    summa = sum([int(x) for x in s])
    if summa == 15:
        print(n)
        break
'''

# № 21413 Досрочная волна 2025 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        print((A + B + C) // 20)
'''


# № 21414 Досрочная волна 2025 (Уровень: Базовый)
'''
def F(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# № 21415 Досрочная волна 2025 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

import sys as s
s.setrecursionlimit(10000)

from sys import setrecursionlimit
setrecursionlimit(10000)

from sys import *
setrecursionlimit(10000)

def F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + F(n - 2)

print(F(2126) - F(2122))
'''


# Пример кода КОНФЛИКТОМ ИМЕН
'''
count = 0
# from itertools import *
# from itertools import count, permutations
from itertools import permutations
for p in permutations('abc'):
    word = ''.join(p)
    print(word)
    count += 1
print(count)  # 6
'''
# abc
# acb
# bac
# bca
# cab
# cba


# № 21416 Досрочная волна 2025 (Уровень: Базовый)
# произведение максимального и минимального элементов тройки больше
# суммы всех отрицательных элементов последовательности.
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if x < 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if max(x, y, z) * min(x, y, z) > sum(A):
        R.append(x + y + z)
print(len(R), max(R))  # 10007 7953
'''

'''
# i  0    1    2    3    4     5   6        
M = [24, 453, 543, 234 ,123, -32, 434]
'''


# № 21422 Досрочная волна 2025 (Уровень: Базовый)
'''
def D(x):
    div = []
    for j in range(1, int(x**0.5)+1):  # не равный ни самому числу
        if x % j == 0:
            div.append(j) # {1, 2, 3, 4}
            div.append(x // j) # {6, 8, 12, 24}
    return sorted(set(div))

cnt = 0
for x in range(1_125_000+1, 10**10):
    d = [j for j in D(x) if j != 7 and j % 10 == 7 and j != x]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''
# 24 = {1, 2, 3, 4, sqrt(24), 6, 8, 12, 24}



# 23 21420
'''
def F(a, b):
    if a >= b or a == 35:
        return a == b  # True / False
    h = [F(a+1, b), F(a+2, b), F(a*2, b)]
    return sum(h)

print(F(7, 13) * F(13, 15) * F(15, 51))
'''


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# s - это кол-во камней в куче
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0  # True - Ваня победил / False - Петя победил
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча: -2, /2 вниз | <= 87 | S > 88
'''
from math import ceil, floor

def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(89, 1000) if F(s, 2)])
print([s for s in range(89, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(89, 1000) if F(s, 4) and not F(s, 2)])
'''

# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | 1 ≤ S ≤ 73 | a = 7

def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h) - после неудачного первого хода Пети

print([s for s in range(1, 74) if F(7, s, 2)])  # [19, 20, 21,
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
