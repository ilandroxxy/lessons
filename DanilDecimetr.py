# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Страшный номер 15 из сборник крылова

'''
def divis(x):
    div = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            div += [i, x // i]
    return sorted(set(div))

def f(x):
    A = 3 <= x <= 60
    return (x in C) <= (A and (x != 3 and x != 59))

B = divis(177)

l = []
for y in range(2, 10000):
    C = divis(y)
    if len(C):
        if all(f(x) == 1 for x in range(0, 10000)):
            l.append(y)
print(max(l))
'''


# 23756
'''
f = [0] * 16000
g = [0] * 16000

for n in range(0, 16000):
    if n < 10:
        g[n] = 2 * n
    if n >= 10:
        g[n] = g[n - 2] + 1
    f[n] = 2 * (g[n - 3] + 8)

print(f[15548])
'''

# Вариант 2
'''
from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

def g(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return g(n - 2) + 1

def f(n):
    return 2 * (g(n - 3) + 8)

print(f(15548))
'''

# 18931
'''
from functools import *

@lru_cache(None)
def f(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return f(n - 2) + (n/2) - f(n - 4)
    if n > 3 and n % 2 != 0:
        return f(n - 1) * n + f(n - 2)

for n in range(5000):
    f(n)

print(f(4952) + 2 * f(4958) + f(4964))
'''

# 7011
'''
def f(c, e):
    if c < e or c == 7: return 0
    if c == e: return 1
    if c > e:
        return f(c-1 , e) + f(c - 4, e) + f(c // 3, e)

print(f(19, 13) * f(13, 2))
'''

# todo Рассмотреть 9964 (даниил)
'''
from functools import *

@lru_cache(None)
def f(c, e, step):
    if c > e:
        return 0
    if c == e:
        return 1 and "CAC" in step
    return f(c + 1, e, step+"A") + f(c * 3, e, step + "B") + f(c + 5, e, step + "C")

print(f(3, 69, ""))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 9, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ = []
# на следующем уроке: 19-21