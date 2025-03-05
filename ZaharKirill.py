# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 23
'''
def F(a, b):
    if (a > b) or (a == 13):
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2, b) + F(a * 3, b)


print(F(3, 8) * F(8, 18))
'''


# Номер 6
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 70
for i in range(4):
    t.forward(10 * size)
    t.right(270)
t.up()
t.forward(3 * size)
t.right(270)
t.forward(5 * size)
t.right(90)
t.down()
for i in range(2):
    t.forward(10 * size)
    t.right(270)
    t.forward(12 * size)
    t.right(270)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')


t.update()
t.done()
'''

# Номер 12
'''
for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace ('52', '11', 1)
        if '2222' in s:
            s = s.replace ('2222', '5', 1)
        if '1122' in s:
            s = s.replace ('1122', '25', 1)
    if s.count('5') * 5 + s.count('2') * 2 + s.count('1') == 64:
        print(n)
        break
'''


# Номер 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 150:
        print(n)
        break
'''


# Для узла с IP-адресом 111.118.179.50 адрес сети равен 111.118.178.0.
# Определите значение третьего байта маски.
# Введите ответ в виде десятичного числа.
'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
        print(net, net.netmask) # 255.255.254.0
'''


# № 17632 Основная волна 19.06.24 (Уровень: Базовый)
# Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0.
# Сколько в этой сети IP-адресов, для которых количество единиц
# в двоичной записи IP-адреса кратно 5?
'''
from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 == 0:
        cnt += 1
print(cnt)
'''

# Номер 25
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
'''


# Номер 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# Номер 8
'''
from itertools import *
n = 0
for p in product(sorted('СОБРНИК'), repeat=6):
    word = ''.join(p)
    n += 1
    if word[0] != 'Р':
        if word.count('Б') == 2:
            if word.count('К') <= 1:
                print(n)
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]

# Второй пробник 28.02.25:
# Захар 7/13 -> 43 вторичных баллов +[1, 2, 10, 12, 14, 15, 16] -[4, 5, 6, 8, 13, 17, 23, 25]
# Kirill 6/13 -> 40 вторичных баллов +[2, 10, 13, 14, 15, 16] -[5, 6, 8, 12, 17, 23, 25]