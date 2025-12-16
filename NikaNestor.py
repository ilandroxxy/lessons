# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 21:
        return F(n - 5) + 3480
    if n < 21:
        return 10 * (G(n - 9) - 30)

def G(n):
    if n >= 264685:
        return n / 20 + 33
    if n < 264685:
        return G(n + 9) - 2

for i in range(700):
    F(i)
    G(i)

print(F(675))
'''

'''
res = []
def f(x, y, A):
    return (x * y < A) or (x < 7 * y) or (343 < x)

for A in range(0, 10000):
    if all(f(x, y, A) for x in range(0, 300) for y in range(0, 300)):
        print(A)
        break
'''
# todo 15, 16 ЕГКР пересмотреть

'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

print([x for x in range(1, 100) if is_prime(x)])
print([x for x in range(1, 100) if not is_prime(x)])
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 7, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
