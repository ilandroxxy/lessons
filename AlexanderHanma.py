# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
from functools import *
from sys import *
setrecursionlimit(1000000)
@lru_cache(None)
def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2*n*F(n-4)

for i in range(5, 14000):
    F(i)

print((F(13766) - 9*F(13762))//F(13758))
'''


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
l = []
M = [int(s) for s in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) >= 5 and abs(x) % 100 == 43]
for i in range(len(M) - 2):
    x, y, z = M[i], M[i + 1], M[i + 2]
    if (x in D) or (y in D) or (z in D):
        if x ** 2 + y ** 2 + z ** 2 <= max(D) ** 2:
            l.append(x ** 2 + y ** 2 + z ** 2)
print(len(l), min(l))
'''

#
# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
'''
maxi = 0
s = open('files/24.txt').readline()
s = s.split('FSRQ')
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''

#
# № 19237 ЕГКР 21.12.24 (Уровень: Базовый)
'''
alp = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')


def my_convert(number: int, system: int):
    res = ''
    while number > 0:
        res += alp[number % system]
        number //= system
    return res[::-1]


R = []
for n in range(1, 1000):
    s = my_convert(n, 3)
    if n % 3 == 0:
        s += s[-2:]
    else:
        summa = sum([int(x) for x in s])
        s += my_convert(summa, 3)
    r = int(s, 3)
    if r > 220 and r % 2 == 0:
        R.append(r)
print(min(R))
'''

#
# № 19244 ЕГКР 21.12.24 (Уровень: Базовый)
'''
R = []
for n in range(3, 1000):
    s = '1' + n * '2'
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if summa == 15:
        R.append(n)

print(min(R))
'''

'''
from itertools import *
n = 0
for p in product(sorted('ЯНВАРЬ'), repeat=5):
    s = ''.join(p)
    n += 1
    if s[0] != 'Я' and s.count('Ь') <= 1 and 'ЯЯ' not in s:
        print(n)
'''


# № 19233 ЕГКР 21.12.24 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6 7 8')
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'BD DB BE EB BC CB CH HC HE EH FH HF FA AF FG GF AG GA GD DG DE ED'
for p in permutations('BCHFAGED'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)


# 1 2 3 4 5 6 7 8
# E H B D F A C G
'''

'''
from itertools import *
print('1 2 3 4 5 6 7 8')
table = '12 14 17 21 24 28 35 37 38 41 42 46 53 58 64 67 71 73 76 82 83 85'
graph = 'BA AB BH HB AH HA HF FH FD DF DC CD CG GC CE EC AE EA GF FG EG GE'
for p in permutations('BAHFDCGE'):
    new_table = table
    for i in range(1, 9):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


'''
from itertools import *

print('1 2 3 4 5 6 7 8')
tab = '12 14 17 21 24 28 35 37 38 41 42 46 53 58 64 67 71 73 76 82 83 85'
fda = 'BH HB BA AB HF HA AH FH AE EA GE EG GF FG GC CG DF FD DC CD EC CE'
for s in permutations('BHAEGFDC'):
    nwtab = tab
    for i in range(9):
        nwtab = nwtab.replace(str(i), s[i - 1])
    if set(nwtab.split()) == set(fda.split()):
        print(*s)
'''

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 14]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
