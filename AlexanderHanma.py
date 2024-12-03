# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 17747
'''
a = 2
b = 16000
c = 51
t = 26 * 60
V = a * b * c * t

print(V / (2**26))  # 37.9371
'''


# 17766
'''
from itertools import *
n = 0
for p in product(sorted('СЕНТЯБРЬ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] == 'Р' and 'Ь' not in word:
            print(n)
'''


# 17770
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if 2 * (M[-1] + M[-2]) > 3 * (M[0] + M[1] + M[2]):
        D = [x for x in M if abs(x) % 10 == 5]
        if len(D) >= 2:
            cnt += 1
print(cnt)
'''

# 17745
'''
symbols = 256
alphabet = 10 + 4080
# 2**i >= alphabet
i = 12  # сколько бит уходит на один символ*

bit = symbols * i
print(bit / 8)  # 384.0
byte = 384

print((byte * 2**16) / 2**20)
'''


# 17746
'''
s = '9' * 68
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1)
    else:
        s = s.replace('9999', '29', 1)
print(s.count('9'))
'''


# 17767
'''
from ipaddress import *
net = ip_network('228.172.236.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 != 0:
        cnt += 1
print(cnt)
'''


# 17768
'''
n = 4**644 + 4**322 + 16**35 - 64**3
M = []
while n > 0:
    M.append(n % 4)
    n //= 4
M.reverse()
print(M.count(3))
'''

# 17748
'''
def F(A, x, y):
    return (x <= 19) or (y < 2*x + A - 50) or (y > 17)

for A in range(0, 1000):
    if all(F(A, x, y) for x in range(100) for y in range(100)):
        print(A)
        break
'''


# 17755
'''
def F(n):
    if n > 400:
        return n ** n
    if n <= 400:
        return n + 6 + F(n + 12)

print(F(72) - F(108))
'''


# 17750
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 77) + (y % 77) == min(M):
        R.append(x + y)
print(len(R), max(R))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
