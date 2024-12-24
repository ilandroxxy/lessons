# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задача 2
'''
print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                F = (x <= (z == w)) or (not (y <= w))

                if F == 0:
                    print(x, y, z, w)
'''


# Задача 5
'''
def covert(n, b):
    s = ''
    while n > 0:
        s = s + str(n % b)
        n = n // b
    return s[::-1]


M = []
for n in range(1, 1000):
    s = covert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        c = (n % 3) * 4
        s = s + covert(c, 3)
    r = int(s, 3)
    if r < 199:
        M.append(n)

print(max(M))
'''


# Задача 8
'''
from itertools import *
cnt = 0
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in '02468ACE':
            num = num.replace(x, '2')
        for x in '13579BDF':
            num = num.replace(x, '1')
        if '22' not in num and '11' not in num:
            cnt += 1
print(cnt)
'''

# Задача 12
'''
for n in range(4, 10000):
    s = '1' + '8' * n
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    if s.count('1') == 3:
        print(n)
        break
'''


# Задача 14
'''
m = []
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:23]:
    a = int(f'7{x}38596', 23)
    b = int(f'14{x}36', 23)
    c = int(f'61{x}7', 23)
    if (a + b + c) % 22 == 0:
        m.append((a + b + c) // 22)
print(min(m))
'''

# Задача 25
'''
from fnmatch import *

for x in range(2025, 10 ** 8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)
'''

# https://stepik.org/lesson/1038536/step/3?unit=1062771
'''
print('x y z w f')
for x in 0, 1:
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((y <= w) == (x <= (not z))) and (x or w)
                print(x, y, z, w, int(f))
'''


print('x y z w f')
for x in 0, 1:
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y) or (z == x)) and (w <=z)
                print(x, y, z, w, int(f))

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]
