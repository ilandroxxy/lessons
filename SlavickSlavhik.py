# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 1
'''
for p in range(2, 9):
    n = 636
    R = []
    while n > 0:
        R.append(n % p)
        n //= p
    R.reverse()
    if len(R) == 4:
        print(p)
        break
'''

# Задача 2
'''
n = 5**2004 - 5**1016 - 5**400 + 25**250
R = []
while n > 0:
    R.append(n % 5)
    n //= 5
R.reverse()
print(R.count(4))
'''

# Задача 3
'''
n = 2*3**30 + 2*3**25 + 3**6 + 7*3**4 + 2*9**2 + 1
R = []
while n > 0:
    R.append(n % 9)
    n //= 9
R.reverse()
print(R.count(0))
'''


# Задача 4
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:6]:
    A = int(f'12{x}35', 6)
    B = int(f'1{x}243', 6)
    if (A + B) % 5 == 0:
        print((A + B) // 5)
'''

# Задача 5
'''
for n in range(1, 1000):
    s = f'{n:b}'
    for i in range(2):
        s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 335:
        print(n)
        break
'''


# Задача 6
'''
from itertools import *
for n, p in enumerate(product(sorted('ЕНОТ'), repeat=4), 1):
    word = ''.join(p)
    if n == 225:
        print(word)
'''


# Задача 7
'''
from itertools import *
cnt = 0
for p in (product('СЛОН', repeat=5)):
    word = ''.join(p)
    if word.count('С') <= 2:
        cnt += 1
print(cnt)
'''

# Задача 10
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'196.204.84.103/{mask}', 0)
    if '196.204.84.96' in str(net):
        print(net.netmask)
'''


# Задача 11
'''
from ipaddress import *
maxi = 0
for mask in range(32+1):
    net = ip_network(f'148.76.112.147/{mask}', 0)
    if '148.76.112.144' in str(net):
        maxi = max(maxi, net.num_addresses)
print(maxi)
'''

# Задача 12
'''
pixels = 400*600
V = 600 * 2**13
i = V / pixels
print(i)
i = 20
print(2**i)
'''

# Задача 15
'''
def F(x, a1, a2):
    P = 20 <= x <= 32
    Q = 17 <= x <= 27
    A = a1 <= x <= a2
    return (P <= A) and ((not Q) or A)

R = []
M = [x / 4 for x in range(10*4, 40*4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

'''
def F(x, A):
    return ((x % A == 0) <= ((x % 15 == 0) + (x % 23 != 0))) and (x + A >= 150)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w <= y) and ((x <= z) == (y <= x))
                if F == 1:
                    print(x, y, z, w)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ  = [22, 25]
# на следующем уроке:
