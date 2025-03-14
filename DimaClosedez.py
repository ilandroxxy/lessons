# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/946e0f2d-56db-4fe1-aa6a-94cd603ea823
# Сеть задана IP-адресом 195.102.65.64 и маской сети 255.255.255.192.
#
# Сколько в этой сети IP-адресов, в которых одинаковое количество нулей и единиц в правом байте адреса?
'''
from ipaddress import *
net = ip_network('195.102.65.64/255.255.255.192', 0)
cnt = 0
for ip in net:
    ipb = f'{ip:b}'
    if ipb[24:].count('0') == ipb[24:].count('1'):
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/d8ca0667-b307-492b-902f-13aae0569d27
# Сеть задана IP-адресом 128.224.31.192 и маской сети 255.255.255.192.
# Сколько в этой сети IP-адресов, для которых количество нулей в двоичной
# записи IP-адреса является полным квадратом? В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('128.224.31.192/255.255.255.192', 0)
cnt = 0
for ip in net:
    ipb = f'{ip:b}'
    count_0 = ipb.count('0')
    if (count_0 ** 0.5).is_integer():
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/7dc01dcf-a5ee-427d-89a9-7c68f664b615
# Два узла, находящиеся в разных подсетях, имеют IP-адреса 101.96.170.244 и 101.96.126.212.
# В масках обеих подсетей одинаковое количество единиц.
# Найдите наибольшее возможное количество нулей в двоичной записи маски подсети.
'''
from ipaddress import *
R = []
for mask in range(33):
    net1 = ip_network(f'101.96.170.244/{mask}', 0)
    net2 = ip_network(f'101.96.126.212/{mask}', 0)
    if net1 != net2:
        R.append(32 - mask)
print(max(R))
'''


# https://education.yandex.ru/ege/task/7a7901a6-c4ac-4554-aaaa-29270d559b19
# Сеть, в которой содержится узел с IP-адресом (248.112.A.35),
# задана маской сети 255.255.255.240, где (A) — некоторое допустимое для
# записи IP-адреса число. Определите максимальное значение (A), для которого
# для всех IP-адресов этой сети в двоичной записи IP-адреса суммарное количество
# нулей в левых двух байтах не больше суммарного количества нулей в правых двух байтах.
'''
from ipaddress import *
for A in range(255+1):
    net = ip_network(f'248.112.{A}.35/255.255.255.240', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        print(A)
'''

# 1 байт = 8 бит (10101010) -> максимальное число (11111111) -> 255


# https://education.yandex.ru/ege/task/4827e366-3e61-48f6-9a59-a9f3ae25020d
# Для узла с IP-адресом 215.181.200.27 адрес сети равен 215.181.192.0.
# Чему равно наибольшее возможное значение третьего слева байта маски?
# Ответ запишите в виде десятичного числа.
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'215.181.200.27/{mask}', 0)
    if '215.181.192.0' in str(net):
        print(net, net.netmask)
        # 215.181.192.0/18 255.255.192.0
        # 215.181.192.0/19 255.255.224.0
        # 215.181.192.0/20 255.255.240.0
# Ответ: 240
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = []
# на следующем уроке: 13, 14

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


