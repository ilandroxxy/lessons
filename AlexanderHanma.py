# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from sys import *
setrecursionlimit(10000)
from functools import *

@lru_cache(None)
def F(n):
    if n<6:
        return n
    if n>= 6:
        return (3*n -2) * F(n-5)

for i in range(1, 21000):
    F(i)

print((F(20568) - 51702 * F(20563))//F(20553))
'''


# № 4740 (Уровень: Средний)
'''
from math import factorial
from sys import *
from functools import *

setrecursionlimit(1000000)


@lru_cache(None)
def F(n):
    if n >= 5000:
        return factorial(n)
    if 1 <= n < 5000:
        return 2 * F(n + 1) // (n + 1)


for i in range(5500, 1, -1):
    F(i)

print(1000 * F(7) // F(4))
'''

# todo посмотреть задачу Александры № 18536 Сергей Горбачев
'''
from re import *
s= open('0. files/24.txt').readline()
s = s.replace('*', '-').replace('6', '7').replace('7', '9').replace('9', '8')
print(s)
num = r'[8][08]*|[0]'
reg = rf'{num}([-]{num})*'

M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    if len(x) == 108:
        print(x)
    maxi = max(maxi, len(x))
print(maxi)
'''

'''
def f(n, b):
    res = ''
    alp = sorted('012345678')
    while n > 0:
        res += alp[n % b]
        n //= b
    return res[::-1]  # тут return съехал


R = []
for n in range(0, 1000):
    s = f(n, 9)
    b = sum(map(int, s))  # тут сумма цифр
    b = sum(int(x) for x in s)
    if b % 2 == 0:
        s = s + '52'
    else:
        s = '73' + s[2:] + '44'  # тут кривой срез
    r = int(s, 9)  # тут 9
    if r > 13950:
        R.append(n)
print(min(R))
'''


# a = 5, b = 155

# a = 155
# a = 160
# a = 200  a = 40
'''
def f(a, b, c):
    if a > b or a == 40:
        return 0
    elif a == b:
        return 1 and 'BB' not in c
    else:
        return f(a + 1, b, c+'A') + f(a * 2, b, c+'B') + f(a ** 2, b, c+'C')


print(f(5, 80, '') * f(80, 155, ''))


def f(a, b, c):
    if a >= b or a == 40:
        return a == b and 'BB' not in c
    else:
        return f(a + 1, b, c+'A') + f(a * 2, b, c+'B') + f(a ** 2, b, c+'C')


print(f(5, 80, '') * f(80, 155, ''))
'''


# № 17939 Сергей Горбачев
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 4]
T = [x for x in M if x < 0 and abs(x) % 5 == 0]

R = []
for i in range(len(M) - 2):
    x, z, c = M[i:i + 3]
    if (x in D) + (z in D) + (c in D) >= 2:
        if (x + z + c) >= len(T):
            R.append(x + z + c)
print(len(R), min(R))
'''


# № 18322 Сергей Горбачев
'''
def F(x, a1, a2):
    P = 32 <= x <= 55
    Q = 40 <= x <= 79
    A = a1 <= x <= a2
    return ((Q) <= (not A)) <= ((not A) == (not P))


R = []
M = [x / 4 for x in range(20 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

'''
def f(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return (D) <= (((not C) and (not A)) <= (not D))


R = []
E = [x / 4 for x in range(2 * 4, 110 * 4)]
for a1 in E:
    for a2 in E:
        if all(f(x, a1, a2) for x in E):
            R.append(a2 - a1)
print(min(R))
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
