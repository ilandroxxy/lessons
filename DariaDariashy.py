# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((((((w and x) == x) or 1) <= z) or (not x)) and y))
                if F == 0:
                    print(x, y, z, w)
'''

'''
from ipaddress import *
for mask in range(32, -1, -1):
    net1 = ip_network(f'61.58.73.42/{mask}', 0)
    net2 = ip_network(f'61.58.75.136/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            if f'{ip:b}'.count('1') % 2 != 0:
                cnt += 1
        print(cnt)
        break

        # print(net1)  # 61.58.64.0/19 - 19 это кол-во единиц в маске сети
        # print(net1.network_address)  # 61.58.64.0
'''


# https://education.yandex.ru/ege/task/380757d9-1361-41c9-b23d-f25fc5439be8
'''
from ipaddress import *
net = ip_network('172.30.0.0/255.254.0.0', 0)
cnt = 0
for ip in net:
    if f'{ip:b}'.count('1') % 12 != 0:
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/946e0f2d-56db-4fe1-aa6a-94cd603ea823
'''
from ipaddress import *
net = ip_network('195.102.65.64/255.255.255.192', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s[24:].count('1') == s[24:].count('0'):
        cnt += 1
print(cnt)
'''
# 10100101.102.65.10101010
#   [:8]  [8:16]  [16:24]  [24:]


# https://education.yandex.ru/ege/task/bc025b29-5204-4401-bee3-8b880a428d2b
'''
from ipaddress import *
cnt = 0
for mask in range(0, 32+1, 2):
    net = ip_network(f'174.213.57.95/{mask}', 0)
    if '174.213.0.0' in str(net):
        cnt += 1
        # print(net, mask, net.netmask)
print(cnt)
'''
# print(net, mask, net.netmask)
# 174.213.57.92/30 30 255.255.255.252
# 255.255.255.252 -> 11111111.11111111.11111111.11111100


# https://education.yandex.ru/ege/task/ebdb9a1e-1e94-4af0-8ce6-003009385c7d
'''
from ipaddress import *
net = ip_network('172.16.8.0/255.255.252.0', 0)
cnt = 0
for ip in net:
    cnt += 1
print(cnt)  # 1022 (минус широковещательного адреса)

print(cnt / 33)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке:
