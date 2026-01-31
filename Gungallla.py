# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 8
'''
n = 0
b = []
from itertools import *
for p in product(sorted('гранит'), repeat=6):
    a = ''.join(p)
    n += 1
    if n % 2 == 0:
        # if a[0] != 'р' and a[0] != 'т':
        if a[0] not in 'рт':
            if a.count('т') == 1:
                b.append(n)
print(max(b))
'''


# 15
'''
def f(a1, a2, x):
    P = 225 <= x <= 464
    Q = 140 <= x <= 315
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

b = []
M = [x / 4 for x in range(120 * 4, 500 * 4)]
for a1 in M:
    for a2 in M:
        if all(f(a1, a2, x) for x in M):
            b.append(a2 - a1)
print(min(b))
'''


# 25
'''
def f(x):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d += [i, x // i]
    return sorted(set(d))

print(f(24))  # [2, 12, 3, 8, 4, 6]

k = 0
for x in range(13_200_001, 10**10):
    a = f(x)
    b = [x for x in a if len(f(x)) == 0]
    if len(b) >= 2:
        M = max(b) + min(b)
        if M > 30000:
            if M % 100 == 55:
                print(x, M)
                k += 1
                if k == 7:
                    break
'''



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 9, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [17, ]
# на следующем уроке: 15, 25, 27
