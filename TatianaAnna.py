# region Домашка: ******************************************************************

# 1, 2, (3), (4), 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, (18), 19-21, 23, 24, 25, 27
'''
# Задание 1 25
from itertools import permutations
print(1, 2, 3, 4, 5, 6, 7)
table = '14 17 23 25 27 32 35 36 37 41 46 52 53 56 63 64 65 71 72 73'
graph = 'FB BF FE EF FC CF CE EC CG GC GE EG GA AG AD DA BD DB BE EB'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
        if set(new_table.split()) == set(graph.split()):
            print(*p)
'''
'''
# Задание 2 xzyw
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not(y))) and (not(y == z)) and (not(w))
                if F == 1:
                    print(x, y, z, w)
'''
'''
# Задание 3 2000
# Задание 4 7

# Задание 5 17

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
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + G(x, 3)
    r = int(s, 3)
    if r > 150:
        L.append(n)
print(min(L))



def three(n, b):
    r = ''
    while n > 0:
         # r = r + str(n % b)
         r = str(n % b) + r
         n //= b
    # return r[::-1]
    return r


for n in range(1, 1000):
    n3 = three(n, 3)
    if n % 3 == 0:
        n3 = n3 + n3[-3:]
    else:
        n3 = n3 + three((n % 3) * 3, 3)
    r = int(n3, 3)
    if r > 150:
        print(n)
        break
'''



'''
# Задание 6 4
import turtle as t
t.tracer(0)
t.left(90)
t.screensize(5000, 5000)
size = 20

for i in range(4):
    t.forward(10 * size)
    t.right(270)

t.up()

t.forward(3 * size)
t.right(270)
t.forward(5 * size)
t.forward(90)

t.down()

for i in range(2):
    t.forward(10 * size)
    t.right(270)
    t.forward(12 * size)
    t.right(270)

t.up()

for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(size * x, size * y)
        t.dot(3, 'red')

t.update()
t.done()
'''
'''
# Задание 7 512
pixel = 1024*512
byte = 4
U = 32_768
i = 32
I = pixel * i
T = I / U
print(T)

'''
'''
# Задание 8 117601
L = []
n = 0
s = sorted('СБОРНИК')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if word[0] != 'Р':
                            if word.count('Б') == 2:
                                if word.count('К') <= 1:
                                    L.append(n)
print(max(L))
'''


# Задание 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied1) == 3 and len(copied2) == 4:
        if sum(copied2) / 4 < sum(copied1) / 3:
            cnt += 1
print(cnt)
'''

# Задание 10 9
'''
# Задание 11 256
sym = 32
alp = 16
i = 4

bit = sym * i
print(bit) # 128
byte = 128 / 8
print(byte) # 16
all = 16_384
print(byte * all / 2**10)
'''

# Задание 12 999

# Задание 13
'''
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    # if '111.118.178.0' in str(net):
    if '111.118.178.0' == str(net.network_address):
        print(net, mask, 32-mask, net.network_address, net.netmask)  # 255.255.254.0
'''


'''
# Задание 14 1405686
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print(x, (A + B + C) // 17)
'''


'''
# Задание 15 25
def F(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)

RES = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''


'''
# Задание 16 4045
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 1 + F(n-1)
print(F(2024) - F(2022))
'''
'''
# Задание 17 2089 99343
M = [int(x) for x in open('files/17 (1).txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# Задание 18 2292 524

# Задание 19-21
'''
def F(s, n):
    if s >= 473:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+5, n-1), F(s*4, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 473) if F(s, n=2)]) # 30
print([s for s in range(1, 473) if F(s, n=3) and not F(s, n=1)]) # 8 9
print([s for s in range(1, 473) if F(s, n=4) and not F(s, n=2)]) # 2
'''


'''
# Задание 23 200
def F(a, b):
    if a > b or a == 13:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)
print(F(3, 8) * F(8, 18))
'''
'''
# Задание 24
M = open('files/24.txt').readline()
print(M)
'''
'''
# Задание 25
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
# 2381071 1177
# 21801871 10777
# 22611071 11177
# 24431771 12077
# 27061671 13377
# 29691571 14677
'''

# Задание 27
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if -12 < x < -9 and -12 < y < -8:
        clustersA[0].append([x, y])
    if -10 < x < -7 and -2 < y < 2:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if -5 < x < -2 and -9 < y < -6:
        clustersB[0].append([x, y])
    if -10 < x - 6 and -8 < y < -5:
        clustersB[1].append([x, y])
    if -4 < x < -1 and -5 < y < -2:
        clustersB[2].append([x, y])
    if -4 < x < 0 and -2 < y < 1:
        clustersB[3].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
            R.append([summa, p])
    return min(R)[1]

centersA = [center(cl) for cl in clustersA]
pxA = sum( x for x, y in centersA) / len(centersA)
pyA = sum( y for x, y in centersA) / len(centersA)
print(int(pxA * 10000), int(pyA * 10000)) # -95076 -52743

centersB = [center(cl) for cl in clustersB]
pxB = sum(x for x, y in centersB) / len(centersB)
pyB = sum(y for x, y in centersB) / len(centersB)
print(int(pxB * 10000), int(pyB * 10000)) # -27190 -47251
'''



def f(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)

for A in range(1000):
       if all(f(x, y, A) for x in range(100) for y in range(100)):
           print(A)
           break

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [11, 19-21]
# на следующем уроке: 10, (26)

# 📖 Пробник (Вариант 2)

# Студент #Татьяна сдал ответы на пробник, вот результаты:
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 3, 4, 6, 7, 10, 11, 14, 16, 17, 19, 20, 21, 22, 23, 25
# ⛔️ Неверно: 5, 8, 12
# ❔ Без ответа: 9, 13, 15, 18, 24, 26, 27
# Итог: 17/29 первичных балла ~ 70 вторичных


# Студент #Анна сдал ответы на пробник, вот результаты:
# Дата: #Суббота #28Февраля2026
# ✅ Верно: 1, 2, 4, 7, 8, 11, 12, 14, 15, 16, 17, 18, 23, 25
# ⛔️ Неверно: 3, 5, 6, 10, 19, 20, 21, 27
# ❔ Без ответа: 9, 13, 22, 24, 26
# Итог: 14/29 первичных балла ~ 62 вторичных


