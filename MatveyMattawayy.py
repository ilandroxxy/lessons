# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import sys
sys.setrecursionlimit(15000)
def F(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return F(n+1) + F(n+2)
print (F(12345) *  1 + F(10101))
'''


'''
def F(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return F(n - 1) + F(n - 2) + 1
    if n > 1 and n % 3 != 0:
        return G(n - 3)

def G(n):
    if n > 100:
        return n
    if n <= 100:
        return G(n + 2) + 1


print(F(15) + F(12))
'''

# s = '12345'
# print(sum(map(int, s)))  # 15


# КЕГЭ № 8585 (Уровень: Базовый)
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a - sum(map(int, str(a))), b) + F(a//2, b) + F(a-1, b)

print(F(40, 25) * F(25, 10))
'''

'''
from functools import *

@lru_cache(None)
def F(a, b):
    if a > b or a == 100:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + a % 10, b) + F(a + (a % 68), b) + F(a ** 2, b)


print(F(2, 68) * F(68, 680))
'''


# № 17558 Основная волна 08.06.24 (Уровень: Базовый)

M = [int(x) for x in open('17.txt')]
D = [x for x in M if x % 32 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x < 0 or y < 0:
        if (x + y) < len(D):
            R.append(x + y)
print(len(R), max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1+, 2+, 3, 4, 5*, 6, 7, 8*, 10+, 12*+, 14*, 16, 18, 19-21+]
# КЕГЭ  = [5, 8, 9, 12, 13, 14, 15, 16, 17, 23]
# на следующем уроке: 9, 11
