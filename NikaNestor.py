# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


#4
'''print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(x) and z and not(y) and not(w)) or (not(x) and z and y and not(w)) or (not(x) and z and y and w):
                    print(w, x, y, z)'''
import sys
from runpy import run_path

#5
'''res = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r = r + '11'
    if n % 5 != 0:
        r = r + bin(n // 5)[2:]
    d = int(r, 2)
    if d >= 783:
        if n % 2 != 0:
            res.append(n)
print(min(res))'''
#6
'''from turtle import *
tracer(0)
left(90)
m = 20
pd()
for i in range(7):
    forward(15*m)
    right(90)
    forward(23*m)
    right(90)
pu()
forward(3*m)
right(90)
forward(5*m)
left(90)
pd()
for i in range(7):
    forward(252*m)
    right(90)
    forward(398*m)
    right(90)
pu()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*m, y*m)
        dot(5)
done()
print(253*399 + 137)'''
#7
'''v1 =  2493 * 33000 * 37 * 4 #v 30 trekov zvuk
V = 363956352 * 307
#print(v1) 12175812000 bit
#print(363956352 * 307) 111734600064 bit ves i 30 trekov i 30 nazvaniy
#print(V - v1) 99558788064 30 nazvaniy
#print(99558788064 / 30) 1 nazvanie
#print(3318626269 / 8 / 1024) kb 405106'''
#8
'''from itertools import product
res = []
for p in product('0123456789ABCDE', repeat=4):
    word = ''.join(p)
    if word.count('8') == 1:
        if word[0] != '0':
            if word[0] != word[1] and word[1] != word[2] and word[2] != word[3]:
                res.append(word)
print(len(res))
'''
#9
'''k = 0
for i in open('files/9.csv'):
    M = [int(x) for x in i.split(';')]
    c1 = [x for x in M if M.count(x) == 1]
    if (M.count(min(M)) == 2 and len(set(M)) == 7) or (M.count(min(M)) == 3 and len(set(M)) == 6):
        if min(c1)**2 + max(c1)**2 <= (sum(c1) - max(c1) - min(c1))**2:
            k += 1
print(k)'''
#11
'''#print(53 * 1024 * 1024 * 8) 444596224 bit
#print(444596224 / 282952) 1571 bit na nomer
#print(1571 / 102)
print(2**15) 32768'''
#14
'''res = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def con(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r
for x in range(1, 8410):
    n = 29**293 + 29**271 - x
    s = con(n, 29)
    res.append(s.count('0'))
print(max(res))'''
#15
'''res = []
def f(x, y, A):
    return ((y > A) or (152 != 2*y + 3*x) or (A < x))
for A in range(1, 1000):
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        res.append(A)
print(max(res))'''
#16
'''from sys import *
sys.setrecursionlimit(10**8)
def f(n):
    if n <= 10:
        return n
    if n > 10:
        return n - 12 + f(n - 21)
print((f(224356) - f(224272)) / f(59))'''
#17
'''res = []
M = [int(x) for x in open('files/17.txt')]
m = [x for x in M if -1000 < x < -99 and abs(x) % 6 == 0]
for i in range(len(M) - 1):
    if ((M[i] < 0) + (M[i + 1] < 0)) == 1:
        if (M[i] + M[i + 1]) > max(m):
            res.append(M[i]**2 + M[i + 1]**2)
print(len(res), max(res))
'''
#19
'''from math import floor
def f(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s - 3, n - 1), f(floor(s / 5), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)
print(max([s for s in range(505, 63125) if f(s, n = 2)]))'''
#20-21
'''from math import floor
def f(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s - 3, n - 1), f(floor(s / 5), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
print([s for s in range(505, 63125) if f(s, n = 3) and not f(s, n = 1)])
print([s for s in range(505, 63125) if f(s, n = 4) and not f(s, n = 2)])'''

#23
'''def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b) + f(a * 3, b)
print(f(6, 14) * f(14, 48))
print(f(6, 18) * f(18, 48))
print(f(6, 14) * f(14, 18) * f(18, 48))
print((45 + 48) - 24)'''


# 1)105
# 2)xywz
# 3)420
# 4)19
# 5)49
# 6)101084
# 7)405106
# 8)9295
# 9)752
# 10)74
# 11)32768
# 12) —
# 13) —
# 14)24
# 15)30
# 16)12125
# 17)2553 19701728317
# 18) —
# 19)12649
# 20)2533 2534
# 21)2536
# 22) —
# 23) 69
# 24) —
# 25) —
# 26) —
# 27) —


# 12, 13, 18

# Номер 19
'''
from math import floor
def f(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s - 3, n - 1), f(floor(s / 5), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(max([s for s in range(506, 100000) if f(s, n = 2)]))
'''

# Номер 8
'''
from itertools import product
res = []
for p in product('0123456789ABCDE', repeat=4):
    word = ''.join(p)
    if word.count('8') == 1:
        if word[0] != '0':
            if word[0] != word[1] and word[1] != word[2] and word[2] != word[3]:
                res.append(word)
print(len(res))


from itertools import product
res = []
alp = '0123456789ABCDE'
for p in product(alp, repeat=4):
    word = ''.join(p)
    if word.count('8') == 1:
        if word[0] != '0':
            if all(x*2 not in word for x in alp):
                res.append(word)
print(len(res))
'''


# Номер 9
'''
k = 0
for i in open('files/9.csv'):
    M = [int(x) for x in i.split(';')]
    A = [x for x in M if x == min(M)]
    c1 = [x for x in M if M.count(x) == 1]
    # if (M.count(min(M)) == 2 and len(set(M)) == 7) or (M.count(min(M)) == 3 and len(set(M)) == 6):
    # if (2 <= M.count(min(M)) <= 3) and (5 <= len(c1) == 6):
    # if (M.count(min(M)) in (2, 3)) and (len(c1) in (5, 6)):
    if (len(A) in (2, 3)) and (len(c1) in (5, 6)):
        if min(c1)**2 + max(c1)**2 <= (sum(c1) - max(c1) - min(c1))**2:
            k += 1
print(k)
'''


# Номер 7
'''
v1 =  2493 * 33000 * 37 * 4 #v 30 trekov zvuk
V = 363956352 * 307
#print(v1) 12175812000 bit
#print(363956352 * 307) 111734600064 bit ves i 30 trekov i 30 nazvaniy
#print(V - v1) 99558788064 30 nazvaniy
#print(99558788064 / 30) 1 nazvanie
#print(3318626269 / 8 / 1024) kb 405106

a = 4
b = 33000
c = 37
t = 41 * 60 + 33
V30 = a * b * c * t

U = 363_956_352
T = 307
V = U * T

print(((V - V30) / 30) / 2**13)
'''

# Правила для 7 номера:
# 1. Делим большее число на меньшее
# 2. Данные терять нельзя, если есть необходимость, лучше отсавить пустое место
# 3. Желательно все вычисления производить в минимальных единицах измерения


# Номер 13
'''
from ipaddress import *
net = ip_network('167.66.136.176/255.254.0.0', 0)
for ip in net.hosts():
    print(ip)
    break

# 167.66.0.1 -> 1676601
# 167.66.0.1 -> 167 + 66
# 167.66.0.1 -> 167 + 1
# 167.66.0.1 -> 167 + 66 + 0 + 1
print(167 + 66 + 0 + 1)  # 234
'''

# № 17554 Основная волна 08.06.24 (Уровень: Базовый)
# Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0.
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной
# записи IP-адреса не кратно 3?
'''
from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 3 != 0:
        cnt += 1
print(cnt)
'''


# № 12947 (Уровень: Базовый)
# Сеть, в которой содержится узел с IP-адресом 203.111.195.0, задана маской
# сети 255.255.240.0. Сколько в этой сети IP-адресов, в двоичной записи которых
# количество нулей кратно трём,
# а также содержатся три подряд идущие единицы и три подряд идущих нуля одновременно?
'''
from ipaddress import *
net = ip_network('203.111.195.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('0') % 3 == 0:
        if '111' in s and '000' in s:
            cnt += 1
print(cnt)
'''


# № 12088 (Уровень: Средний)
# Сеть задана IP-адресом 112.154.132.0 и маской сети 255.255.252.0.
# Сколько в этой сети узлов (устройств), для которых в двоичной записи
# IP-адреса суммарное количество единиц в левых двух байтах не больше
# суммарного нечётного количества нулей в правых двух байтах.
'''
from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s[16:].count('0') % 2 != 0:
        if s[:16].count('1') <= s[16:].count('0'):
            cnt += 1
print(cnt)

# s = [:8]  # 32 первый байт
# s = [:16]  # 32 первые 2 байта
# s = [:24]  # 32 первые 3 байта
# s = [:32]  # 4 байта
# s = [8:16]  # 2 байт
'''


# № 11770 (Уровень: Базовый)
# Для узла с IP-адресом 251.211.38.240 адрес сети равен 251.211.38.0.
# Для скольких различных значений маски это возможно?
'''
from ipaddress import *
for mask in range(1, 32+1):
    # print('1' * mask + '0' * (32 - mask))
    net = ip_network(f'251.211.38.240/{mask}', 0)
    if '251.211.38.0' in str(net):
        print(net.netmask)
'''


# № 11769 (Уровень: Базовый)
# Для узла с IP-адресом 157.17.164.129 адрес сети равен 157.17.128.0.
# Чему равно наименьшее возможное значение третьего слева байта маски?
'''
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f'157.17.164.129/{mask}', 0)
    if '157.17.128.0' in str(net):
        print(net, mask, 32-mask, net.netmask)
'''


# № 10786 (Уровень: Средний)
# Два узла, находящиеся в разных подсетях, имеют IP-адреса 151.172.115.121 и 151.172.115.156.
# В масках обеих подсетей одинаковое количество единиц.
# Укажите наименьшее возможное количество единиц в масках этих подсетей.
'''
from ipaddress import *
for mask in range(1, 32+1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        print(mask, 32-mask)
'''


# № 12467 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
# Адрес сети равен 183.192.A.0, где А — некоторое допустимое для записи адреса сети число,
# а маска сети 255.255.252.0
# Определите минимальное значение А, для которого для всех IP-адресов этой сети
# в двоичной записи IP-адреса суммарное количество единиц в правых двух байтах больше трёх.
'''
from ipaddress import *
for A in range(0, 255+1):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break

# байт  1   1  1  1  - 4 байта
# бит   8   8  8  8  - 32 бита
# ip = 123.234.0.255
# ip_2 = '01111011.11101010.00000000.11111111'
#          ip[:8]  ip[8:16] ip[16:24] ip[24:32]
'''







# № 11791 (Уровень: Базовый)
# Сеть, в которой содержится узел с IP-адресом 246.51.128.202, задана маской сети 255.255.A.0,
# где A - некоторое допустимое для записи маски число. Определите минимальное значение A,
# для которого для всех IP-адресов этой сети в двоичной записи IP-адреса суммарное количество
# нулей в левых двух байтах не более суммарного количества нулей в правых двух байтах.

from ipaddress import *
for A in [128, 192, 224, 240, 248, 252, 254, 255]:
    net = ip_network(f'246.51.128.202/255.255.{A}.0', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        print(A)  # 254
        break





for mask in range(1, 8+1):
    r = '1' * mask + '0' * (8 - mask)
    print(r, int(r, 2))
    # 10000000 128
    # 11000000 192
    # 11100000 224
    # 11110000 240
    # 11111000 248
    # 11111100 252
    # 11111110 254
    # 11111111 255

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: Минимальное количество идущих подряд
