# region Домашка: ******************************************************************

# № 9781 Основная волна 20.06.23 (Уровень: Базовый)
'''
z = []
for n in range(4, 1000):
    s = '1' + '2'*n
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        elif '322' in s:
            s = s.replace('322', '21', 1)
        elif '222' in s:
            s = s.replace('222', '3', 1)
    summa = sum([int(x) for x in s])
    z.append(summa)
print(max(z))
'''


# № 11661 (Уровень: Базовый)
'''
z = []
for n in range(210, 300):
    s = '3' + '7' * n
    while '27' in s or '377' in s or '777' in s:
        if '27' in s:
            s = s.replace('27', '32', 1)
        if '377' in s:
            s = s.replace('377', '27', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
    m = sum([int(x) for x in s])
    if m % 15 == 0:
        z.append(n)

print(max(z))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# По заданным IP-адресу узла и маске определите адрес сети.
# IP-адрес узла: 217.9.191.133
# Маска сети: 255.255.192.0

# Адрес сети = IP-адрес узла & Маска сети
# & - операция побитовой конъюнкции

# IP адрес/узел - это четыре числа разделенные точкой.
# На каждое такое число выделяется по 1 байту. То есть по 8 бит.
# 4 числа * 8 бит = 32 бита

# Маска имеет длину 32 бита и вид: 111111...0000


# print([bin(int(x))[2:].zfill(8) for x in '255.255.192.0'.split('.')])
# ['11111111', '11111111', '11000000', '00000000']
# 11111111.11111111.11000000.00000000


# Тип 13 №3818
# По заданным IP-адресу узла и маске определите адрес сети.
# IP-адрес узла: 217.9.191.133
# Маска: 255.255.192.0
'''
from ipaddress import *
net = ip_network('217.9.191.133/255.255.192.0', 0)
print(net)  # 217.9.128.0/18, где 18 - это кол-во единиц в маске сети
# 11111111.11111111.11000000.00000000
'''


# Тип 13 №18440
# Для узла с IP-адресом 111.81.176.27 адрес сети равен 111.81.160.0.
# Чему равен третий слева байт маски?
# Ответ запишите в виде десятичного числа.
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.81.176.27/{mask}', 0)
    print(net, net.netmask)
    # 111.81.160.0/19 255.255.224.0
'''
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.81.176.27/{mask}', 0)
    if str(net) == f'111.81.160.0/{mask}':
        print(str(net.netmask).split('.')[2])
'''


# Тип 13 №69891
# Сеть задана IP-адресом 106.184.0.0 и маской сети 255.248.0.0.
# Сколько в этой сети IP-адресов, для которых сумма единиц
# в двоичной записи IP-адреса не кратна 2?
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('106.184.0.0/255.248.0.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 2 != 0:
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
# на следующем уроке:
