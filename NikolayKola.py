# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#
# № 17554 Основная волна 08.06.24 (Уровень: Базовый)
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
# Ответ: 1043


# № 11780 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('185.8.0.0/255.255.128.0', 0)
R = []
for ip in net:
    s = f'{ip:b}'
    R.append(s.count('1'))
print(max(R))
'''


# № 11777 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('119.124.96.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    # if s.endswith('0'):
    if s[-1] == '0':
        cnt += 1
print(cnt)
'''

'''
from ipaddress import *
net = ip_network('235.86.56.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s[-2:] == '11':
        cnt += 1
print(cnt)
'''


# № 11769 (Уровень: Базовый)
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'157.17.164.129/{mask}', 0)
    print(net, net.netmask)
    # 157.17.128.0/17 255.255.128.0
    # 157.17.128.0/18 255.255.192.0
    # 255.255.192.0  11111111.11111111.11000000.00000000
'''

# № 10786 (Уровень: Средний)
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        print(mask)
        break
'''


# № 10780 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('214.120.249.18/255.255.240.0', 0)
print(net)  # 214.120.240.0/20
'''


'''
M = [int(x) for x in open('17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if ((x % 18) + (y % 18)) % min(M) == 0:
        R.append(x + y)
print(len(R), max(R))
'''

# № 17558 Основная волна 08.06.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('17.txt')]
D = [x for x in M if x % 32 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x < 0 or y < 0:  # хотя бы одно число отрицательно
        if (x + y) < len(D):  # а сумма чисел пары меньше количества чисел последовательности, кратных 32
            R.append(x + y)
print(len(R), max(R))
'''


# № 17530 Основная волна 07.06.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x % 55 == min(M) or y % 55 == min(M):
        R.append(x + y)
print(len(R), min(R))
'''


# № 16383 ЕГКР 27.04.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('17.txt')]
D = [x for x in M if str(x)[-2:] == '21' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in D) != (y in D):
        if (x**2 + y**2) >= max(D)**2:
            R.append(x + y)
print(len(R), max(R))
'''

# № 14952 (Уровень: Средний)

M = [int(x) for x in open('17.txt')]
D = [x for x in M if len(str(abs(x))) == 4 and x % 2 == 0]
B = [x for x in M if str(x)[-3:] == '121']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) + (y in D) + (z in D) <= 1:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1+, 2*+, 3, 4+, 6+, 7, 9*+, 10+, 11, 18+, 19-21, 22+]
# КЕГЭ  = [2, 3, 5, 7, 11, 12, 13, 14, 15, 16, 17, 23]
# на следующем уроке:
