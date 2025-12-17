# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038775/step/2?unit=1062778
'''
RES = []
M = [int(s) for s in open('0. files/17.txt')]
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            RES.append(x+y)
print(len(RES), max(RES))
'''
from dis import code_info

# https://stepik.org/lesson/1038775/step/2?unit=1062778
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if hex(x)[-2:] == '0f']
A = [x for x in M if f'{x:x}'[-2:] == '0f']
A = [x for x in M if f'{x:X}'[-2:] == '0F']
print(A)
'''


# № 2491 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
avg = sum(M) / len(M)
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x < avg) + (y < avg) + (z < avg) >= 1:
        # if ('9' in str(x)) + (str(y).count('9') > 0) + ('9' in str(z)) == 3:
        if all('9' in str(p) for p in (x, y, z)):
            R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 34517460


# 5
'''
print('1 2 3 4 5 6 7')
from itertools import *
t = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
g = 'FD DF DG GD GE EG EC CE CB BC BA AB AF FA AC CA DE ED'
for p in permutations('ABCDEFG'):
    nt = t
    for i in range(1, 7+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(g.split()):
        print(*p)

# 1 2 3 4 5 6 7
# C G B E D A F
# E B G C A D F
'''
# 1 4


# 5
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        RES.append(n)
print(max(RES))
'''


# 8
'''
cnt = 0
from itertools import *
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in '02468ACE':
            num = num.replace(x, '*')
        for x in '13579BDF':
            num = num.replace(x, '+')
        if '**' not in num and '++' not in num:
            cnt += 1
print(cnt)
'''


# 13
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    if '213.168.64.0' in str(net):
        print(net, mask, 32 - mask, net.netmask)
'''


# 17
# в которых только один из элементов является четырёхзначным числом
# квадрата максимального элемента последовательности,
# являющегося четырёхзначным числом и оканчивающегося на 39
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in A if abs(x) % 100 == 39]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) ** 2 <= max(B) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''

# 25
'''
from fnmatch import *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 8954 (Уровень: Базовый)
'''
RES = []
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if hex(x)[-2:] == '0f']
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 7 == 0) + (y % 7 == 0) == 1:
        if (x+y) % max(A) == 0:
            RES.append(x + y)
print(len(RES), max(RES))
'''

'''
RES = []
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if hex(x)[-2:] == '0f']
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 7 == 0 and y % 7 != 0) or (x % 7 != 0 and y % 7 == 0):
        if (x+y) % max(A) == 0:
            RES.append(x + y)
print(len(RES), max(RES))
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 9, 27
