# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 8506 Апробация 17.05 (Уровень: Базовый)
# 1 куча: +1, +4, *3 | s >= 55 | 1 ≤ s ≤ 54
'''
def F(s, n):
    if s >= 55:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 55) if F(s, n=2)])
print([s for s in range(1, 55) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 55) if F(s, n=4) and not F(s, n=2)])
'''


# № 8594 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a * s >= 455 | a = 5 | 1 ≤ s ≤ 90
'''
def F(a, s, n):
    if a * s >= 455:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 91) if F(5, s, n=2)])
print([s for s in range(1, 91) if F(5, s, n=3) and not F(5, s, n=1)])
print([s for s in range(1, 91) if F(5, s, n=4) and not F(5, s, n=2)])
'''

# № 12928 (Уровень: Средний)
# 1 куча: +1, *2 | s >= 21 | 1 ≤ s ≤ 20
'''
def F(s, n):
    if s >= 21:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 55) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 55) if F(s, n=4) and not F(s, n=2)])
print([s for s in range(1, 55) if F(s, n=5) and not F(s, n=3) and not F(s, n=1)])
'''

# № 24103 В1Г2526
'''
from itertools import *
n = 0
for p in product(sorted('БУРАТИНО'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 1:
        if word[0] not in 'УАИО':
            if len(word) == len(set(word)):
                print(n)
'''

# № 24100 В1Г2526
'''
def F(n, b):
    a = ''
    while n > 0:
        a = str(n % b) + a
        n = n//b
    return a

def F(n, b):
    a = ''
    while n > 0:
        a += str(n % b)
        n = n//b
    return a[::-1]

RES = []
for n in range(1, 10000):
    s = F(n, 3)
    if n % 5 == 0:
        s = s + s[-2:]
    else:
        s = s + F((n % 5) * 7, 3)
    r = int(s, 3)
    if r <= 273:
        RES.append(n)
print(max(RES))
'''


# 13
'''
from ipaddress import *
net = ip_network('150.122.11.21/255.255.254.0', 0)
for ip in net:
    print(ip, f'{ip:b}'.count('1'))
'''


# № 24114 В1Г2526
'''
from sys import *  # Подключаем сразу все содержимое
setrecursionlimit(100000)

def F(n):
    return G(n + 1)

def G(n):regtryh
    if n >= 30000:
        return 3
    if n < 30000:
        return G(n + 3) + 7

print(F(1500))
'''

#  Способы подключения библиотеки
'''
import math
math.sqrt(16)

import math as m
m.sqrt(16)

from math import sqrt, factorial
sqrt(16)

from math import *
sqrt(16)
factorial(5)
'''

# Пример конфликта имен
'''
count = 0
from itertools import permutations
for p in permutations('abc'):
    count += 1
    print(count, p)

count = 0
from itertools import *
for p in permutations('abc'):
    count += 1
    print(count, p)
'''


# № 24115 В1Г2526
# 1 куча: +2, +5, *3 | s >= 444 | 1 ⩽ s ⩽ 400
'''
def F(s, n):
    if s >= 444:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+5, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 401) if F(s, n=2)])
print([s for s in range(1, 401) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 401) if F(s, n=4) and not F(s, n=2)])
'''


# № 24070
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if len(M) == len(set(M)):
        if max(M) + min(M) <= sum(M) - max(M) - min(M):
            cnt += 1
print(cnt)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
