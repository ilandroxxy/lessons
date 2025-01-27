# region Домашка: ******************************************************************

# № 10087 Демоверсия 2024 (Уровень: Базовый)
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r > 151:
        M.append(r)
print(min(M))
'''


# № 16371 ЕГКР 27.04.24 (Уровень: Базовый)
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r >= 195:
        M.append(r)
print(min(M))
'''

'''
s = '012345678'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('5') == 1:
                            if all(p not in num for p in '00 11 22 33 44 55 66 77 88'.split()):
                                cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n == 1:  # при n=1
        return 1  # F(n)=1
    if n > 1:
        return n**3 + F(n - 1)

print(F(2025) - F(2022))
# RecursionError: maximum recursion depth exceeded
'''

# № 19707 (Уровень: Средний)
'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n < 3:
        return n * 4
    if n >= 3 and n % 2 != 0:
        return n * 2
    if n >= 3 and n % 2 == 0:
        return 5 * F(n - 2) + n**2

cnt = 0
for n in range(1, 10000):
    r = F(n)
    if r % 2 == 0 and len(str(r)) == 3:
        cnt += 1
        print(cnt)
'''


'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 13:
        return 13
    if n >= 13 and n % 5 != 0:
        return 13 - F(n-1)
    if n >= 13 and n % 5 == 0:
        return 13 + F(n - 1)

print(F(3013))
'''

'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2*n * F(n - 4)

print((F(13766)- 9*F(13762)) // F(13758))
'''

'''
from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n // 2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)


for i in range(5000):
    F(i)


print((F(4952) + 2 * F(4958) + F(4964)))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 25]
# КЕГЭ  = []
# на следующем уроке:
