# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Номер 5 (ЕГКР 13.12.25 Вариант 1)
'''
def G(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

L = []
for n in range(1, 10000):
    s = G(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = sum([int(i) for i in s]) * 3
        s = s + G(x, 3)

    r = int(s, 3)
    if r > 208 and r % 2 != 0:
        L.append(r)
print(min(L))  # 243
'''


# Номер 14 (ЕГКР 13.12.25 Вариант 1)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for x in range(1, 27000):
    n = 3 * 27**9 + 2 * 27**6 + 27**3 - x
    s = convert(n, 27)
    if s.count('0') == 6:
        R.append(x)
print(min(R))  # 27
'''


# Номер 16 (ЕГКР 13.12.25 Вариант 1)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 19:
        return F(n-4) + 3580
    if n < 19:
        return 6 *(G(n-7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n+9) - 4

for i in range(250000, 0, -1):
    G(i)

for i in range(1, 1000):
    F(i)

print(F(673))
'''

# Вариант 2
'''
G = [0] * 250000
F = [0] * 1000

for n in range(250000-1, 0, -1):
    if n >= 248045:
        G[n] = n / 20 + 28
    if n < 248045:
        G[n] = G[n + 9] - 4

for n in range(1, 1000):
    if n >= 19:
        F[n] = F[n - 4] + 3580
    if n < 19:
        F[n] = 6 * (G[n - 7] - 36)

print(F[673])
'''


# todo глянуть: Номер 15 (ЕГКР 13.12.25 Вариант 1)
'''
def F(x, y, A):
    return (78125 != y + 4*x) or (A > x) and (A > y)

RES = []
for A in range(1, 5000):
    if all(F(x, 78_125 - 4*x, A) for x in range(1, 19531)):
        RES.append(A)
print(min(RES))

# 78_125 != y + 4*x
# y != 78_125 - 4*x

print(78_125 / 4)  # 19531.25
'''

# Номер 9 (ЕГКР 13.12.25 Вариант 1)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(copied1) == 4:
        # if max(M) in copied1:
        # if max(M) not in copied3:
        if M.count(max(M)) == 1:
            cnt += 1
print(cnt)  # 1595
'''


# Номер 17 (ЕГКР 13.12.25 Вариант 1)
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))  # 1032 285423
'''


# Номер 25 (ЕГКР 13.12.25 Вариант 1)
'''
def divisors(x):  # 24
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)  # 4
            d.append(x // j)  # 24 // 4 == 6
    return sorted(set(d))

cnt = 0
for x in range(1_350_050+1, 10**10):
    d = [j for j in divisors(x) if j != x and j != 11 and j % 100 == 11]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# Номер 11 (ЕГКР 13.12.25 Вариант 1)
'''
sym = 105
# alp - ?
# i - ?
# bit - ?

byte = 7 * 2**20 / 65_536
print(byte)  # 112.0  - 112  (потребовалось не менее 7 Мбайт)
bit = 112 * 8  # бит на один пароль

# bit = sym * i
# i = bit / sym
i = bit / sym
print(i)  # 8.533 -> 9 (потребовалось не менее 7 Мбайт)

# При i = 9
print(f'Минимальная возможная мощность алфавита: {2**8 + 1}')
print(f'Максимальная возможная мощность алфавита: {2**9}')

# Ответ: 257


alp = 64  # i = 6

alp = 50  # i = 6

alp = 33 # i = 6  (2**5 + 1) 

alp = 32  # i = 5
'''


# Номер 24 (ЕГКР 13.12.25 Вариант 1)
'''
s = open('files/24.txt').readline()
for x in '02468':
    s = s.replace(x, '*')
s = s.split('F')
maxi = 0
for i in range(len(s)-76):
    r = 'F'.join(s[i:i+77])
    if r.count('*') == 1 and r[0] == '*':
        maxi = max(maxi, len(r))
print(maxi)
'''

# 3, 27

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [19-21]
# на следующем уроке: 10, (26)