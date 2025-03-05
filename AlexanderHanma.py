# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 23 18450
'''
def F(a):
    if a >= 50 or a == 23:
        return a in (50, 51, 52, 53, 54)
    return F(a + 3) + F(a + 4) + F(a * 2)

print(F(11))
'''

# Номер 5 17720
'''
def f(n, b):
    alp = sorted('0123456789')
    res = ''
    while n > 0:
        res += alp[n % b]
        n //= b
    return res[::-1]


R = []
for n in range(0, 1000):
    s = f(n, 5)
    if n % 2 == 0:
        d = str(n % 5)
        s = '3' + s + d
    else:
        a = str(n % 4)
        s = a + s + '4'
    r = int(s, 5)
    if n <= 15:
        R.append(r)
print(max(R))
'''

# Номер 6 17723
'''
import turtle as t
t.screensize(-5000,5000)
t.left(90)
t.tracer(0)
l=20

t.color('teal')
for i in range(2):
    t.forward(77*l)
    t.right(90)
    t.forward(101*l)
    t.right(90)

t.up()
t.forward(29*l)
t.left(90)
t.forward(44*l)
t.right(90)

t.down()
for i in range(7):
    t.forward(88*l)
    t.right(90)
    t.forward(75*l)
    t.right(90)

for x in range(-30,30):
    for y in range(-30,30):
        t.goto(x*l,y*l)
        t.dot(3, 'black')
t.update()
t.done()
'''

# Номер 8 17736
'''
from itertools import *
cnt = 0
for s in product(sorted('0123456'), repeat=7):
    d = ''.join(s)
    if d[0] not in '035' and d.count('0') <= 1 and d[-1] not in '0246':
        cnt += 1
print(cnt)
'''

# Номер 9 18116
'''
summa = 0
n = 0
for s in open('0. files/9.txt'):
    M = sorted([int(x) for x in s.split()])
    n += 1
    copied3 = [x for x in M if M.count(x) == 3 and x % 2 == 0]
    uncopied = [x for x in M if M.count(x) == 1 and x % 2 != 0]
    if len(copied3) == 3 and len(uncopied) == 3:
        if sum(copied3) ** 2 > sum(uncopied) ** 2:
            summa += n
print(summa)
'''

'''
s=132
byte = 4 * 2**20 / 18750
print(byte)  # 223.6962
byte = 224
bit = byte * 8

i = bit / s
print(i)
# 13.5757
i = 14
8193

# 8193
# print(2 ** 13)
'''


# Номер 13 18445
'''
from ipaddress import *
net = ip_network('140.116.194.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s[7] == '0' and s[15] == '0' and s[23] == '0' and s[31] == '0':
        cnt += 1
print(cnt)
'''
# s[:8] s[8:16] s[16:24] s[24:]

'''
def con(n,b):
    alp=sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
    res=''
    while n>0:
        res+=alp[n%b]
        n//=b
    return res[::-1]

x = 9 * 123**2053 + 5*23**3146 + 91 * 47 ** 5533 + 4099
s = con(x, 23)
D = [i for i in s if i > 'f']
print(len(D))
'''

# Номер 17 17943
'''
M = [int(x) for x in open(f'0. files/17.txt')]
R = []
A = [x for x in M if x > 0]
E = [x for x in M if x < 0]
chet = [x for x in M if abs(x) % 2 == 0]
for s in range(len(M) - 1):
    z, a = M[s], M[s + 1]
    if ((z in A) and (a in A)) or ((z in E) and (a in E)):
        if abs(z - a) <= len(chet):
            R.append(z + a)
print(len(R), max(R))
'''




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
