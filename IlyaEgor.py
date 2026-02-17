# region Домашка: ******************************************************************

#2
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = ((not x) and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w)
                if F == 1:
                    print(x,y,z,w)
#ответ: xywz
'''
#5
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n,b):
    r = ''
    while n > 0:
        r = alphabet[n%b] + r
        n //= b
    return r

for N in range(1,1000):
    r = convert(N,2)
    if N % 5 == 0:
        r = r + '11'
    else:
        x = N // 5
        r = r + convert(x,2)
    R = int(r,2)
    if R >= 783:
        print(N)
        break
#ответ: 49
'''
#6
'''
import turtle as t
k = 15
t.screensize(-7000,7000)
t.tracer(0)
t.left(90)
t.down()
for i in range(7):
    t.forward(15*k)
    t.right(90)
    t.forward(23*k)
    t.right(90)
t.up()
t.forward(3*k)
t.right(90)
t.forward(5*k)
t.left(90)
t.down()
for j in range(7):
    t.forward(252*k)
    t.right(90)
    t.forward(398*k)
    t.right(90)
t.up()
for x in range(-50,50):
    for y in range(-50,50):
        t.setpos(x*k,y*k)
        t.dot(3,'red')
t.update()
t.done()
#ответ: 101084
'''
#8
'''
from itertools import product
cnt = 0
for p in product('0123456789ABCDE', repeat =4):
    num = ''.join(p)
    if num.count('8') == 1 and num[0] != '0' and '00' not in num and '11' not in num and '22' not in num and '33' not in num and '44' not in num and '55' not in num and '66' not in num and '77' not in num and '99' not in num and 'AA' not in num and 'BB' not in num and 'CC' not in num and 'DD' not in num and 'EE' not in num:
        cnt += 1
print(cnt)
# ответ: 9295
'''
#9
'''
cnt = 0
for s in open('D:/Загрузки/9 (7).csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    copied3 = [x for x in M if M.count(x) == 3]
    if (len(copied1) == 6 and len(copied2) == 1 and min(copied2) == 2) and len(copied1) == 5 and len(copied3) == 1 and min(copied3) == 3:
        min(copied1)**2 + max(copied1)**2 <= sum(copied1)**2 - min(copied1)**2 - max(copied1)**2
    cnt+=1
print(cnt)
# ответ: 24414
'''
#13
'''
from ipaddress import *
net = ip_network('167.66.136.176/255.254.0.0',0)
print(net[0])
print((167+66+0+0)+1)
# ответ: 234
'''
#14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n,b):
    s = ''
    while n > 0:
        s += alphabet[n%b]
        n //= b
    return s[::-1]

M = []
cnt = 0
for x in range(1,8410+1):
    n = 29**293 + 29**271 - x
    s = convert(n,29)
    if s.count('0') >= 1:
        cnt += 1
        M.append(cnt)
print(max(M))
'''
#15
'''
for A in range(0,1000):
    if all(((y > A) or (152 != 2*y + 3*x) or (A < x)) for x in range(1,100) for y in range(1,100)):
        print(A)
#ответ: 30
'''
#16
'''
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n <= 10:
        return 1
    if n > 10:
        return (n - 12) + F(n-21)
print((F(224356) - F(224272)) / F(59))
'''

#19,20,21
'''
def F(s,n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3,n-1), F(s//5,n-1)]
    return any(h) if (n-1) % 2 == 0 else any(h)


print([s for s in range(1000000,506,-1) if not F(s,1) and F(s,2)])
print([s for s in range(1000000,506,-1) if not F(s,1) and F(s,3)])
print([s for s in range(1000000,506,-1) if not F(s,2) and F(s,4)])
#ответ: 12649---2533 2534---2536
'''

#23
'''def F(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return F(a+1,b) + F(a*2,b) + F(a*3,b)

print(F(6,14) * F(14,18) * F(18,48))
print(F(6,14) * F(14,48))
print(F(6,18) * F(18,48))
print(45+48-24)
#ответ: 69
'''
# 14:20 10.02.2026

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Вариант 1 Статград 23.10.25 Номер 6
'''
print(253 * 399 + 16 * 24 - 19 * 13)

import turtle as t
k = 15
t.screensize(-7000,7000)
t.tracer(0)
t.left(90)
t.down()
for i in range(7):
    t.forward(15*k)
    t.right(90)
    t.forward(23*k)
    t.right(90)
t.up()
t.forward(3*k)
t.right(90)
t.forward(5*k)
t.left(90)
t.down()
for j in range(7):
    t.forward(252*k)
    t.right(90)
    t.forward(398*k)
    t.right(90)
t.up()
for x in range(-50,50):
    for y in range(-50,50):
        t.setpos(x*k,y*k)
        t.dot(3,'red')
t.update()
t.done()
'''
#ответ: 101084


# Вариант 1 Статград 23.10.25 Номер 8
'''
from itertools import product
cnt = 0
for p in product('0123456789ABCDE', repeat =4):
    num = ''.join(p)
    if num.count('8') == 1:
        if num[0] != '0':
            # if '00' not in num and '11' not in num and '22' not in num and '33' not in num and '44' not in num and '55' not in num and '66' not in num and '77' not in num and '99' not in num and 'AA' not in num and 'BB' not in num and 'CC' not in num and 'DD' not in num and 'EE' not in num:
            # if all(pair not in num for pair in '00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE'.split()):
            # if all(x * 2 not in num for x in '0123456789ABCDE'):
            if all(num[i] != num[i+1] for i in range(len(num)-1)):
                cnt += 1
print(cnt)
'''
# ответ: 9295


# i  0  1  2  3   ?
'''
M = [1, 2, 3, 4]

x, y = i, i+1
x = 1, y = 2
x = 3, y = 4
'''


# Вариант 1 Статград 23.10.25 Номер 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied1 = [x for x in M if M.count(x) == 1]
    # if (min(M) in copied2 and len(copied1) == 6) or (min(M) in copied3 and len(copied1) == 5):
    # if (M.count(min(M)) == 2 and len(copied1) == 6) or (M.count(min(M)) == 3 and len(copied1) == 5):
    if (2 <= M.count(min(M)) <= 3) and (5 <= len(copied1) <= 6):
        if min(copied1)**2 + max(copied1)**2 <= (sum(copied1) - min(copied1) - max(copied1)) ** 2:
            cnt+=1
print(cnt)
'''


# Вариант 1 Статград 23.10.25 Номер 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n,b):
    s = ''
    while n > 0:
        s += alphabet[n%b]
        n //= b
    return s[::-1]

R = []
cnt = 0
for x in range(1, 8410+1):
    n = 29**293 + 29**271 - x
    s = convert(n,29)
    R.append(s.count('0'))
print(max(R))
'''


# Вариант 1 Статград 23.10.25 Номер 15
'''
for A in range(0,1000):
    if all(((y > A) or (152 != 2*y + 3*x) or (A < x)) for x in range(1,100) for y in range(1,100)):
        print(A)
#ответ: 30
'''
# натуральные числа range(1, ...)
# целые положительные range(1, ...)  - так как 0 не положительное число
# целые неотрицательные range(0, ...)
# целые числа (17, 27)


# Вариант 1 Статград 23.10.25 Номер 16
'''
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n <= 10:
        return n
    if n > 10:
        return (n - 12) + F(n-21)
print((F(224356) - F(224272)) / F(59))


from functools import *
@lru_cache(None)
def F(n):
    if n <= 10:
        return n
    if n > 10:
        return (n - 12) + F(n - 21)

for n in range(250000):
    F(n)

print((F(224356) - F(224272)) / F(59))
'''



# todo глянуть решение через массивы
'''
F = [0] * 250000

for n in range(0, 250000):
    if n <= 10:
        F[n] = n
    if n > 10:
        F[n] = n - 12 + F[n - 21]

print((F[224356] - F[224272]) / F[59])
'''



'''
from functools import *


@lru_cache(None)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)


@lru_cache(None)
def G(n):
    if n >= 248045:
        return (n / 20) + 28
    if n < 248045:
        return G(n + 9) - 4


for n in range(250000, -1, -1):
    G(n)

for n in range(1000):
    F(n)

print(F(673))
'''


# Вариант 1 Статград 23.10.25 Номер 17
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0 and abs(x) % 6 == 0 and len(str(abs(x))) == 3]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x ** 2 + y ** 2)
print(len(R), max(R))
'''


# # Вариант 1 Статград 23.10.25 Номер 7
'''
a = 4
b = 33000
c = 37
t = 41 * 60 + 33
V_music = a * b * c * t

# V_zagol = ?
# V_all = V_music + V_zagol

U = 363_956_352
T = 307
V_all = U * T

V_zagol = V_all - V_music
print(V_zagol / 30)  # бит
print((V_zagol / 30) / 2**13)  # Кбайт
'''

# # Вариант 1 Статград 23.10.25 Номер 11
sym = 102

byte = 53 * 2**20 / 282952  # Вес в байт на один серийный номер
print(byte)  # 196.4097 -> 196 (отведено не более 53 Мбайт)
bit = 196 * 8
i = bit / sym
print(i)  # 15.37 -> 15 (отведено не более 53 Мбайт)

i = 15
print(f'Максимальная мощность алфавита: {2**15}')
print(f'Минимальная мощность алфавита: {2**14 + 1}')


alp = 129  # i = 8  минимальная
alp = 128  # i = 7

# 25 и 27

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 17, 25, 7, 11
