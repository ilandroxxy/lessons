# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18287 (Уровень: Базовый)
'''
sp = []
for n in range(3, 10000):
    bn = bin(n)[2:]
    if len(bn) % 2 == 0:
        bn = bn + '1'
    else:
        bn = '1' + bn + '0'
    r = int(bn, 2)
    if r > 666:
        print(r)
        sp.append(r)
print(min(sp))
'''

'''
n = 0
R = []
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    if M == sorted(M):
        # [311, 325, 348, 1731, 1731]
        # [29, 578, 973, 1763, 1763]
        # [1016, 1016, 1177, 2422, 3711]
        if any(M.count(x) > 1 and sum(map(int, str(x))) % 2 == 0 for x in M):
            R.append(n)
print(max(R))
'''

# № 18258 (Уровень: Сложный)
'''
R = []
for n, s in enumerate(open('files/9.csv'), 1):
    M = [int(x) for x in s.split(';')]
    if M == sorted(M):
        if any(M.count(x) > 1 and sum(map(int, str(x))) % 2 == 0 for x in M):
            R.append(n)
print(max(R))
'''


# № 18257 (Уровень: Средний)
'''
R = []
M = [int(x) for x in open('files/17.txt')]
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    i, j = i+1, i+2
    if (i + j) % 10 == max(M) % 10:
        # print(f'{i}:{x}, {j}:{y}')
        R.append(abs((x+y) - (i+j)))
print(len(R), min(R))
'''


# № 18265 (Уровень: Средний)
'''
from string import *
alphabet = digits + ascii_uppercase

for i in range(len(alphabet)):
    print(i, alphabet[i])

for p in range(30, 37):
    for s in range(10, 35):
        A = int(f'R4', p-1)
        B = int(f'B0', s+2)
        C = int(f'T3NK4', p)
        if (A + B + C) == 23593399:
            print(p * s)
'''

def my_int(R, b):
    return sum([x*b**i for i, x in enumerate(R[::-1], 0)])


R = []
for x in range(10, 67):
    for y in range(0, x):
        A = my_int([7, 3, x, 1, y], 67)
        B = my_int([4, 9, y, 6], x)
        R.append(A + B)
print(len(set(R)))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 9, 8, 11, 12, 13, 14, 15, 16, 17, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:  8, 19-21, 9, 7, 11, 17, 24

# Первый пробник 21.12.24:
# Стас 9/21 -> 48 вторичных баллов +[2, 3-5, 7, 10, 12, 16, 22] -[1, 6, 8, 9, 11, 13, 14, 15, 17-21, 24-25]
