# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 19885
'''
from itertools import *
print('1 2 3 4 5 6 7')
table = '12 15 21 23 27 32 36 37 45 46 51 54 56 63 64 65 72 73'
graph = 'БА АБ БВ ВБ ВА АВ ВЕ ЕВ ЕЖ ЖЕ ЕД ДЕ ДЖ ЖД ДГ ГД ГА АГ'
for p in permutations('АБВГДЖЕ'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7
# Г А В Ж Д Е Б
# Г Д Е Б А В Ж


# 19888
'''
R = []
for n in range(1, 1000):
    s = f'{n:o}'
    if n % 2 == 0:
        for x in '1357':
            s = s.replace(x, '2')
    else:
        s = '3' + s[1:-1] + '3'
    r = int(s, 8)
    if r < 300:
        R.append(r)
print(max(R))
'''


# 20068
'''
print(25 * 34 + 25 * 17 - (17 * 13))

from turtle import *
lt(90)
tracer(0)
s = 15
screensize(-2000, 2000)

for i in range(777):
    fd(25 * s)
    lt(90)
    fd(34 * s)
    lt(90)
up()
fd(12 * s)
lt(90)
fd(17 * s)
rt(90)
down()
color('green')
for i in range(1996):
    fd(25 * s)
    lt(90)
    fd(17 * s)
    lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')

update()
done()
'''


# 19892
'''
pixels = 1920 * 1080
# print(2 ** 16)
i = 16
bit = pixels * i

print(512 - 52)

for i in range(1, 15):
    print(i, 460 % i)

print(460 / 5)


print((bit * 92) / 2**23)
'''


# 20218
'''
from itertools import *
n = 0
for p in product(sorted('СИНЕРГЯ'), repeat=6):
    word = ''.join(p)
    n += 1
    if 'ГИРЯ' in word:
        print(n)
'''


# 20219
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    A = [x for x in M if len(str(x)) == 3]
    if len(A) >= 3:
        B = [x for x in M if x % 5 != 0]
        if len(B) == 6:
            cnt += 1
print(cnt)
'''


# 19895
'''
alp = 10 + 2040
# print(2 ** 12)
i = 12  # бит на один символ

byte = (369 * 2 ** 10) / 718
print(byte)  # 526.261
byte = 526

bit = byte * 8
sym = bit / i
print(sym)  # 350.66
'''


'''
s = '12121212121>'
s = s[:-1]
summa = sum(map(int, s))
summa = sum([int(x) for x in s if x.isdigit()])
print(summa)
'''

'''
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f'111.233.75.16/{mask}', 0)
    if '111.233.75.0' in str(net):
        print(net.num_addresses)
'''


# 19898
'''
maxi = 0
for x in range(1, 10000):
    n = 7**270 + 7**170 + 7**70 - x
    r = ''
    while n > 0:
        r = str(n % 7) + r
        n //= 7
    if maxi <= r.count('0'):
        maxi = r.count('0')
        print(x, r.count('0'))
'''


# 19899
'''
def F(x, A):
    return (A + 2*x > 400 - A) and ((A % 100) + (120 % A) > 140)

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# 20071
'''
def F(n):
    if n > 2000:
        return 16
    if n <= 2000:
        return 2 * F(n + 3)

s = F(50) // F(110)  # 1048576.0
M = [int(x) for x in str(s)]
total = 1
for x in M:
    if x != 0:
        total *= x
print(total)
'''


# 19900

M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3]
B = [x for x in M if len(str(abs(x))) == 4]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x * y * z) > sum(B):
            R.append(x * y * z)
print(len(R), abs(min(R)))



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
