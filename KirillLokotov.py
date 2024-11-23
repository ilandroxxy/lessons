# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
# Адрес сети = IP-адрес узла & Маской сети
# IP-адресов лежат в Адресе сети

knot = '.'.join([bin(int(x))[2:].zfill(8) for x in '195.102.65.64'.split('.')])
mask = '.'.join([bin(int(x))[2:].zfill(8) for x in '255.255.255.192'.split('.')])
print(knot)
print(mask)

# 11000011.01100110.01000001.01000000
# 11111111.11111111.11111111.11000000
# 11000011.01100110.01000001.01000000

print(bin(12)[2:])
print(bin(6)[2:])

# 255.255.255.192 -> 11111111.11111111.11111111.11000000
# Маска сети имеет вид: 111111...00000 длины 32
'''

'''
from ipaddress import *
net = ip_network('195.102.65.64/255.255.255.192', 0)
print(net)  # 195.102.65.64/26 - где 26 это кол-во единиц в маске сети
print(f'{net.netmask:b}')  # 11111111111111111111111111000000
print(f'{net.netmask:b}'.count('1'))  # 26
'''


# Задание 13 https://education.yandex.ru/ege/task/946e0f2d-56db-4fe1-aa6a-94cd603ea823
'''
from ipaddress import *
cnt = 0
net = ip_network('195.102.65.64/255.255.255.192', 0)
for ip in net:
    s = f'{ip:b}'  # Двоичная запись нашего ip
    if s[24:].count('1') == s[24:].count('0'):
        cnt += 1
print(cnt)
'''


# Задание 13 https://education.yandex.ru/ege/task/0831d7d1-7e14-43ff-bf81-229062898a01
'''
from ipaddress import *
cnt = 0
net = ip_network('192.168.32.48/255.255.255.240', 0)
for ip in net:
    s = f'{ip:b}'  # Двоичная запись нашего ip
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)
'''


# Задание 13 https://education.yandex.ru/ege/task/08aade2d-7fa5-40ae-ab7e-c85bd6f7e570
'''
from ipaddress import *
net1 = ip_network('192.168.56.192/255.255.255.192', 0)
net2 = ip_network('192.168.56.208/255.255.255.240', 0)
cnt = 0
R = []
for ip in net1:
    R.append(ip)
for ip in net2:
    R.append(ip)

for ip in R:
    if (ip in net1) != (ip in net2):
        cnt += 1
print(cnt)
'''


# Задание 13 https://education.yandex.ru/ege/task/ebfa2513-eaf3-49f7-9bb1-828c96fba52c
'''
from ipaddress import *
for A in range(0, 255+1):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break
'''


# Задание 13 https://education.yandex.ru/ege/task/e0a69d93-9830-45fb-981a-804016be561a
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'134.181.67.112/{mask}', 0)
    net2 = ip_network(f'134.181.94.117/{mask}', 0)
    if net1 == net2:
        print(net1.netmask)
'''

'''
from ipaddress import *
count = 0
net = ip_network('112.208.0.0/255.255.128.0', 0)
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 11 == 0:
        count += 1
print(count)
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ = []
# на следующем уроке:
