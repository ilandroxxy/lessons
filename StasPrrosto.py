# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# print(f'{16:b}'.zfill(8))  # 10000
# print(int('11111111', 2))  # 255
# print(bin(5)[2:])

# print(102&255)
# print(9&255)
# print(140&192)
# print(219&0)


# Тип 13 №7208
# IP-адрес узла: 102.9.140.219
# Маска: 255.255.192.0
# При записи ответа выберите из приведённых в таблице чисел четыре элемента IP- адреса
# и запишите в нужном порядке соответствующие им буквы, без использования точек.
'''
from ipaddress import *
net = ip_network('102.9.140.219/255.255.192.0', 0)
print(net)  # 102.9.128.0/18
'''

# Тип 13 №69921
# Для узла с IP-адресом 170.155.137.181 адрес сети равен 170.155.136.0.
# Чему равно наибольшее возможное значение третьего слева байта маски?
# Ответ запишите в виде десятичного числа.
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'170.155.137.181/{mask}', 0)
    print(net, net.netmask)
    # 170.155.136.0/21 255.255.248.0
    # 170.155.136.0/22 255.255.252.0
    # 170.155.136.0/23 255.255.254.0
'''

'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'170.155.137.181/{mask}', 0)
    if str(net) == f'170.155.136.0/{mask}':
        print(str(net.netmask).split('.')[2])
'''


# Тип 13 №16888
# Для узла с IP-адресом 98.162.71.94 адрес сети равен 98.162.71.64.
# Чему равно наименьшее количество возможных адресов в этой сети?
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'98.162.71.94/{mask}', 0)
    print(net, net.num_addresses)
    # 98.162.71.64/26 64
    # 98.162.71.64/27 32
'''

# Тип 13 №18624
# Узлы с IP-адресами 98.162.78.139 и 98.162.78.154 находятся в одной сети.
# Чему равно наибольшее количество возможных единиц в маске этой сети?
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'98.162.78.139/{mask}', 0)
    net2 = ip_network(f'98.162.78.154/{mask}', 0)
    if net1 == net2:
        print(mask)
'''


# Тип 13 №69922
# Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0.
# Сколько в этой сети IP-адресов, для которых количество единиц
# в двоичной записи IP- адреса не кратно 5?
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network(f'112.160.0.0/255.240.0.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 != 0:
        cnt += 1
print(cnt)
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
# на следующем уроке: 25
