# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# Адрес сети = Узел сети & Маска сети

print(235 & 255, 86 & 255, 56 & 248, 0 & 0)
# 235 86 56 0

knot = '.'.join([bin(int(x))[2:].zfill(8) for x in '235.86.56.0'.split('.')])
mask = '.'.join([bin(int(x))[2:].zfill(8) for x in '255.255.248.0'.split('.')])
print(knot)
print(mask)
# 11101011.01010110.00111000.00000000
# 11111111.11111111.11111000.00000000
# 11101011.01010110.00111000.00000000

# Маска имеет длину 32 бита
# Маска имеет вид: 111111...0000
'''


# https://education.yandex.ru/ege/task/bb30cfa6-5991-411e-b2df-dc6d007aec69
'''
from ipaddress import *
net = ip_network('235.86.56.0/255.255.248.0', 0)
# print(net)  # 235.86.56.0/21 - где 21 это кол-во единиц в маске сети
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s[-2:] == '11':
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/b6ff76ad-5608-4e7d-833d-dced5a6e2479
# Для узла с IP-адресом 111.81.27.208 адрес сети
# равен 111.81.27.192. Чему равно наименьшее возможное
# значение последнего (самого правого) байта маски?
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.81.27.208/{mask}', 0)
    # print(net, net.netmask, mask, 32-mask)
    print(net, net.netmask)
    # 111.81.27.192/26 255.255.255.192
    # 111.81.27.192/27 255.255.255.224
'''
'''
from ipaddress import *
M = []
for mask in range(32+1):
    net = ip_network(f'111.81.27.208/{mask}', 0)
    if '111.81.27.192' in str(net):
        M.append(int(str(net.netmask).split('.')[-1]))
print(min(M))
'''

# https://education.yandex.ru/ege/task/b5ea1e82-76f7-4781-8ef4-5f462fdc7638
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        print(mask, 32-mask)
'''

# https://education.yandex.ru/ege/task/ebfa2513-eaf3-49f7-9bb1-828c96fba52c

from ipaddress import *
for A in range(255+1):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    flag = True
    for ip in net:
        if f'{ip:b}'[16:].count('1') <= 3:
            flag = False
            break
    if flag == True:
        print(A)
        break

from ipaddress import *
for A in range(255+1):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break

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
