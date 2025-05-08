# region Домашка: ******************************************************************
from sys import base_prefix
from zoneinfo import reset_tzpath


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *
cnt = 0
for s in product('0123456789', repeat=4):
    sl = ''.join(s)
    if sl[0] != '0':
        if len(sl) == len(set(sl)):
            for a in '02468':
                sl = sl.replace(a, '*')
            for a in '13579':
                sl = sl.replace(a, '+')
            if '**' not in sl and '++' not in sl:
                print(sl)
                cnt += 1
print(cnt)
'''

'''
cnt=0
for s in open('0. files/9.csv'):
    M=sorted([int(x) for x in s.split(';')])
    numb=[x for x in M if M.count(x)==1]
    if len(numb)==5:
        if M[-1]+M[-2]<=M[0]+M[1]+M[2]:
            cnt+=1
print(cnt)
'''

'''
M = [int(x) for x in open('0. files/17.txt')]
ok15 = min([x for x in M if len(str(abs(x))) == 3 and abs(x) % 100 == 15])
od = [x for x in M if x > 0]
nod = [x for x in M if x < 0]
R = []
for i in range(len(M) - 2):
    a, b, c = M[i], M[i + 1], M[i + 2]
    if ((a in od) + (b in od) + (c in od) == 3) or ((a in nod) + (b in nod) + (c in nod) == 3):
        if min(a, b, c) * max(a, b, c) > ok15 ** 2:
            R.append(min(a, b, c) * max(a, b, c))
print(len(R), min(R))
'''

# v = pixels * i
# colors = 2 ** i
'''
pixels = 1024 * 768
i = 23  # бит
v = pixels * i * 100

pixels2 = 800 * 600
i2 = 22  # бит
v2 = pixels2 * i2 * 100

print((v - v2) / 2**13)
'''


# bit = sym * i
'''
sym = 246

byte = 77 * 2**20 / 703_569  # байт на один серийный номер
print(byte)  # 114.7582 -> 114
byte = 114
bit = byte * 8

i = bit / 246
print(i)  # 3.7073
i = 3  # alp[5:8]
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
