# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
from fnmatch import fnmatch
for x in range(6072, 10**8, 6072):
    if fnmatch(str(x), '5*4?48'):
        print(x, x//6072)
'''
'''
from fnmatch import *
x=10**4
while x%6072!=0:
    x+=1
for n in range(x, 10**8+1, 6072):
    if fnmatch(str(n), '5*4?48'):
        print(n, n//6072)
'''


# 11 из пробника
'''
sym = 15
alp = 12
i = 4
bit = sym * i
print(bit / 8)  # 7.5 -> 8
byte = 8

# user = byte + dop
user = 400 / 20

dop = user - byte
print(dop)
'''


# 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if 10000 <= abs(x) <= 99999 or len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 22]

R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 21710 ЕГКР 19.04.25 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= ((B) == (C))

R = []
M = [x / 4 for x in range(30*4, 120*4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

def f(x, a1, a2):
    D=7<=x<=68
    C=29<=x<=100
    A=a1<=x<=a2
    return D <= (((not C) and (not A)) <= (not D))
R=[]
M=[x/4 for x in range(1*4, 120*4)]
for a1 in M:
    for a2 in M:
        if all(f(x, a1, a2) for x in M):
            R.append(a2-a1)
print(min(R))
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 7.03.25:
# Арина 12/29 -> 56 вторичных баллов +[1, 2, 3, 4, 5, 8, 9, 11, 12, 14, 15, 23] -[7, 13, 17, 19-21, 18, 25]

# Второй пробник 20.05.25:
# Арина 21/29 -> 80 вторичных баллов +[1-5, ..] -[6, 11, 17, 24, 26, 27]
