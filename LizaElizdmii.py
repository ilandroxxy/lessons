# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# узел сети & маска сети = адрес сети
# в адресе сети (сеть) есть айпи адреса сети

# IP-адрес сети (узел): 192.168.248.176
# Сетевая маска (маска) : 255.255.255.240


print('.'.join([bin(int(num))[2:] for num in '192.168.248.176'.split('.')]))
# 11000000.10101000.11111000.10110000 - двоичная запись нашего узла

print('.'.join([bin(int(num))[2:] for num in '255.255.255.240'.split('.')]))

# & - операция побитовой конъюнкции
# биты информации это 01010101001, например 11110000 - это восемь бит (восьмибитные числа)
# 192.168.248.176 - это четыре числа на каждое из которых выделено по 1 байту - 8 бит

# net = 192.168.248.176 & 255.255.255.240

knot = '11000000.10101000.11111000.10110000'
mask = '11111111.11111111.11111111.11110000'  # маска это 32 бита вида 11111...0000
nat  = '11000000.10101000.11111000.10110000'  # наш адрес сети

print(f'{int("11000000", 2)}.{int("10101000", 2)}.{int("11111000", 2)}.{int("10110000", 2)}')
# 192.168.248.176

from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'192.168.248.176/{mask}', 0)
    if '192.168.248.176' in str(net):
        print(f'{net} - адрес сети / кол-во единиц в маске')
        print(f'Кол-во единиц в маске сети: {mask}')
        print(f'Кол-во нулей в маске сети: {32-mask}')
        print(f'Кол-во айпи адресов в сети: {net.num_addresses}')
        print(f'Маска сети в десятично виде: {net.netmask}')
'''


# № 18928 Новогодний вариант 2025 (Уровень: Базовый)
# IP-адрес сети: 192.168.248.176
# Сетевая маска: 255.255.255.240
# Необходимо узнать, сколько в этой сети IP-адресов,
# для которых количество единиц и нулей в двоичной записи IP-адреса одинаково.
'''
from ipaddress import *
net = ip_network('192.168.248.176/255.255.255.240', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('0') == b.count('1'):
        cnt += 1
print(cnt)
'''


# № 18868 (Уровень: Базовый)
# Сеть задана IP-адресом 222.121.128.0 и маской сети 255.255.224.0.
# Сколько в этой сети IP-адресов, которые оканчиваются на два одинаковых бита?
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('222.121.128.0/255.255.224.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b[-1] == b[-2]:
        cnt += 1
print(cnt)
'''


# № 18159 (Уровень: Базовый)
# Для узла с IP-адресом 205.154.212.20 адрес сети равен 205.154.192.0.
# Чему равно наибольшее возможное значение третьего слева байта маски?
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'205.154.212.2/{mask}', 0)
    if '205.154.192.0' in str(net):
        print(net, net.netmask)
        # 205.154.192.0/18 255.255.192.0
        # 205.154.192.0/19 255.255.224.0
        
# Ответ: 224
'''


# № 19748 (Уровень: Средний)
# Узлы с IP-адресами 157.220.185.237 и 157.220.184.230 принадлежат одной сети.
# Какое наименьшее количество IP-адресов, в двоичной записи которых ровно 15 единиц,
# может содержаться в этой сети?
'''
from ipaddress import *
for mask in range(15, 32+1):
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            b = f'{ip:b}'
            if b.count('1') == 15:
                cnt += 1
        print(cnt)
'''


# № 18487 (Уровень: Средний)
# Сеть, в которой содержится узел с IP-адресом 192.214.A.184,
# задана маской сети 255.255.255.224, где A - некоторое допустимое для
# записи IP-адреса число. Определите минимальное значение A,
# для которого для всех IP-адресов этой сети в двоичной
# записи IP-адреса суммарное количество единиц будет больше 15.
'''
from ipaddress import *
for A in range(255+1):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    if all(f'{ip:b}'.count('1') > 15 for ip in net):
        print(A)
        break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Лиза 11/14 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

