# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 17726 номер 6
'''
from turtle import *
screensize(-10000, 10000)
tracer(0)
left(90)
l=10
for i in range(55):
    fd(69*l)
    lt(90)
    fd(84*l)
    lt(90)
up()
fd(60*l)
rt(90)
fd(47*l)
rt(90)
down()
for i in range(31):
    fd(104*l)
    lt(90)
    fd(140*l)
    lt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*l,y*l)
        dot(3, 'red')
update()
done()
'''


# 17730 номер 7
'''
pixels = 1920 * 1080

V = ((3 * 2 ** 23) / 100) * 128  # бит
print(V / pixels)  # 15.534
print(2 ** 15)  # 15.53

V2 = (3 * 2 ** 23) / 0.72
print(V2 / pixels)  # 16.8
print(2 ** 16)

V3 = (3 / 0.72) * 2 ** 23
print(V3 / pixels)
'''



# 17737 номер 8
'''
from itertools import *
cnt = 0
alp=sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for s in product(alp[:16],repeat=5):
    n = ''.join(s)
    num = n
    if n[0] != '0':
        for x in alp[:16:2]:
            num = num.replace(x, '2')
        for x in alp[1:16:2]:
            num = num.replace(x, '1')
        if num[0] != '1' and num[-1] != '2':
            if all(n[i] != n[i+1] for i in range(len(n) - 1)):
                cnt += 1
print(cnt)  # 177184
'''


# 18449 номер 23
'''
def F(a, b):
    if a <= b:
        return a == b
    summa = 0
    summa += F(a - 1, b)
    if a % 2 == 0:
        summa += F(a // 2, b)
    if a % 3 == 0:
        summa += F(a // 3, b)
    return summa


print(F(122, 57) * F(57, 11))
'''


# todo разобрать 18537 номер 24
'''
maxi = 0
s = open('0. files/24.txt').readline()
s = s.split('A')
for i in range(len(s) - 22):
    r = 'A'.join(s[i:i + 23])
    maxi = max(maxi, max([len(x) for x in r.split('F')]))
print(maxi)
'''

# 17942 номер 17
'''
C = [int(a) for a in open('0. files/17.txt')]
R = []
V = [x for x in C if abs(x) % 11 == 0 and abs(x) % 10 == 3]

for i in range(len(C) - 2):
    x, y, z = C[i], C[i + 1], C[i + 2]
    if (x in V) + (y in V) + (z in V) == 2:
        R.append(2 * (x + y + z))
print(len(R), min(R))
'''

# номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n = [x for x in M if M.count(x) == 2]
    z = [x for x in M if M.count(x) == 1]
    if len(n) == 4 and len(z) == 3:
        if (sum(n) / 4) < (sum(z) / 3):
            cnt += 1
print(cnt)
'''

# номер 17
'''
R = []
M = [int(x) for x in open('0. files/17.txt')]
b = [x for x in M if len(str(abs(x))) == 5]
a = [x for x in M if abs(x) % 100 == 29]
for i in range(len(M) - 2):
    z, e, c = M[i], M[i + 1], M[i + 2]
    if (z in b) + (e in b) + (c in b) == 2:
        if (z + e + c) <= max(a):
            R.append(z + e + c)
print(len(R), max(R))
'''

s=32
a=16
i= 4
print((32 * 4) / 8)
b=16  # байт
print((16*16384)/2**10)
print((16*16384)//2**10)

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
