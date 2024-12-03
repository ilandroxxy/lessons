# region Домашка: ******************************************************************


# https://stepik.org/lesson/1038667/step/8?unit=1062772
'''
M = []
from itertools import *

for p in permutations('СОТОЧКА'):
    num = ''.join(p)
    if ('ОО' in num) or ('ОА' in num) or ('АО' in num):
        M.append(num)
print(len(set(M)))
'''


# https://stepik.org/lesson/1038667/step/15?unit=1062772
'''
from itertools import *
s1 = '1357'
s2 = '2468'
cnt = 0
for p in product(s1, s2, s1, s2, s1, s2, s1, s2, s1):
    num = ''.join(p)
    if all(num.count(x) <= 3 for x in num):
        cnt += 1

for p in product(s2, s1, s2, s1, s2, s1, s2, s1, s2):
    num = ''.join(p)
    if num[0] != '0':
        if all(num.count(x) <= 3 for x in num):
            cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# Адрес сети = Узел сети & Маска сети
# & - это побитовая конъюнкция

# Любой айпишник это 4 числа на каждое из которых выделяется по 1 байту = 8 бит

print(192 & 255, 168 & 255, 0 & 192, 0 & 0)
# Адрес сети: 192 168 0 0

# 255_10 -> 11111111_2

# Маска сети: 255.255.192.0 всегда имеет длину 32 бита
# И вид 111111...00000

print('.'.join([bin(int(x))[2:].zfill(8) for x in '255.255.192.0'.split('.')]))
# 11111111.11111111.11000000.00000000
'''


# Задание 13 https://education.yandex.ru/ege/task/2f051464-92d4-4df3-a837-b8939edd9174

# Сеть задана IP-адресом 192.168.0.0 и маской сети 255.255.192.0.
# Сколько в этой сети IP-адресов, в двоичной записи которых единиц больше, чем нулей?
'''
from ipaddress import *
net = ip_network('192.168.0.0/255.255.192.0', 0)
print(net)  # 192.168.0.0/18, где 18 - это кол-во единиц в маске сети

cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') > s.count('0'):
        cnt += 1
print(cnt)
'''

# Задание 13 https://education.yandex.ru/ege/task/94693776-a73a-4e59-bebb-b7e6107fe688
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.81.93.127/{mask}', 0)
    print(net, net.netmask)
    # 111.81.80.0/20 255.255.4.0
'''


# Задание 13 https://education.yandex.ru/ege/task/6e7e8afe-2b32-46d8-9bf1-bf68113fff24
'''
from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240', 0)

cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('0') > 21:
        cnt += 1
print(cnt)
'''


# Задание 13 https://education.yandex.ru/ege/task/b5ea1e82-76f7-4781-8ef4-5f462fdc7638
# Два узла, находящиеся в разных подсетях, имеют IP-адреса 151.172.115.121 и 151.172.115.156.
# В масках обеих подсетей одинаковое количество единиц.
# Укажите наименьшее возможное количество единиц в масках этих подсетей.
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        print(mask)
        break
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14]
# КЕГЭ  = []
# на следующем уроке:
