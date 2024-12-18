# region Домашка: ******************************************************************

'''
import sys
sys.setrecursionlimit(100000)
from functools import *
@lru_cache(None)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * F(n - 1)

print((F(2024) - 3 * F(2023)) // F(2022))
'''


'''
import sys
sys.setrecursionlimit(10000)

def F(a, b, c):
    if a >= b:
        return a == b
    else:  # 17 - 7
        return F(a - int(str(a)[1]), b, c+'1') + F(a+12, b, c+'2')


# 15 + 12 + 12+  12 + 12 = 65 - 5 = 60

print(F(15, 60, ''))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 15 https://education.yandex.ru/ege/task/ef01bd15-9cad-4c7d-b3ef-42633c6fc757
'''
# Вариант 1
def F(x, A):
    B = 70 <= x <= 80  # (x ∈ B)
    return (x % A == 0) or (B <= (x % 18 != 0))


R = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        R.append(A)

print(max(R))


# Вариант 2
def F(x, A):
    B = 70 <= x <= 80  # (x ∈ B)
    return (x % A == 0) or (B <= (x % 18 != 0))


R = []
for A in range(1, 1000):
    k = 0
    for x in range(1, 10000):
        if F(x, A) == True:
            k += 1
    if k == 9999:
        R.append(A)

print(max(R))


# Вариант 3

def F(x, A):
    B = 70 <= x <= 80  # (x ∈ B)
    return (x % A == 0) or (B <= (x % 18 != 0))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))


# Вариант 4

def F(x, A):
    B = 70 <= x <= 80  # (x ∈ B)
    return (x % A == 0) or (B <= (x % 18 != 0))


print(max([A for A in range(1, 1000) if all(F(x, A) for x in range(1, 10000))]))
'''

'''
def F(x, A):
    return (x % 72 != 0) or (x % 495 == 0) or (x % A != 0)


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# https://education.yandex.ru/ege/task/ae636d2a-4f9d-4ac3-88b4-f8cfa0888f36
'''
def F(x, y, A):
    return ((y + x)**2 > 1048) or ((x + 20 < A) and (40 - y < A))


for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break
'''


# https://education.yandex.ru/ege/task/e833a9a3-2790-4be4-bec3-c662b6c81fee
'''
def F(x, y, A):
    return (x + 2*y != 58) or ((A - x > 0) == (A + y > 0))


for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# https://education.yandex.ru/ege/task/0891d1fa-be38-4015-8920-47868754e234
'''
def F(x, A):
    return (((x & 28 != 0) or (x & A == 0)) <= (x & 28 != 0)) or (x & A != 0) or (x & 39 == 0)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 70 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 19.0
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
