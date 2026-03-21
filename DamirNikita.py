# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 6
'''
from turtle import *
lt(90)
screensize(2000,2000)
tracer(0)
k=30
down()


for i in range(4):
    fd(10*k)
    right(270)
up()
fd(3*k)
right(270)
fd(5*k)
right(90)
down()
for i in range(2):
    fd(10*k)
    right(270)
    fd(12*k)
    right(270)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*k,y*k)
        dot(3, 'red')
done()
'''
from sys import float_info

# 8
'''
from itertools import *
n = 0
for x in product(sorted('сборник'), repeat=6):
    a = "".join(x)
    n += 1
    if a[0] != 'р' and a.count("б") == 2 and a.count('к') <= 1:
        print(n)
'''

# 5
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


RES = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 150:
        RES.append(n)
print(min(RES))
'''


# 14
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''


# 15
'''
def F(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)

RES = []
for A in range(0, 1000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        RES.append(A)
print(min(RES))
'''


# 16
'''
import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 1 + F(n - 1)

print(F(2024) - F(2022))
'''

# Вариант 2
'''
from functools import *

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 1 + F(n - 1)

for n in range(2025):
    F(n)

print(F(2024) - F(2022))
'''


# 13
'''
from ipaddress import *
for mask in range(1, 32+1):
    # print('1' * mask + '0' * (32 - mask))
    net = ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
        print(net.netmask)
'''


# 25
'''
from fnmatch import *
for x in range(0, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
'''


# 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if sum(copied2) / 4 < sum(copied1) / 3:
            cnt += 1
print(cnt)
'''


# 17

M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 5, 9, 12, 13, 14, 15, 16, 17, 18, 22, 24, 25, 26, 27


# region 📖 Пробник (Вариант 2)

# Студент #Никита
# Дата: #Вторник #17Марта2026
# ✅ Верно: 1, 2, 3, 4, 7, 10, 11, 19, 20, 21, 23
# ⛔️ Неверно: 6, 8
# ❔ Без ответа: 5, 9, 12, 13, 14, 15, 16, 17, 18, 22, 24, 25, 26, 27
# Итог: 11/29 первичных балла ~ 54 вторичных

# endregion 📖 Пробник (Вариант 2)
