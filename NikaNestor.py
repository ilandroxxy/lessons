# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
def F(x, a1, a2):
    Q = 21 <= x <= 57
    P = 3 <= x <= 38
    A = a1 <= x <= a2
    return (Q <= P) <= (not A)

R = []
M = [x / 4 for x in range(1 * 4, 70 * 4)]
for a1 in M:
    for a2 in M:
        if all(not F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))  # 18.75 -> 18.799 -> 18.9 -> 19
'''
# Ответ: 19



# № 20959 (Уровень: Базовый)
# Сеть задана IP-адресом 203.68.128.0 и сетевой маской 255.255.192.0.
# Сколько в этой сети IP-адресов, для которых количество единиц
# в двоичной записи IP-адреса не кратно 7?
'''
from ipaddress import *
net = ip_network('203.68.128.0/255.255.192.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 7 != 0:
        cnt += 1
print(cnt)
'''


# № 12947 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if '101' not in s:
        cnt += 1
print(cnt)
'''


# № 12947 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network(f'203.111.195.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('0') % 3 == 0:
        if '111' in s and '000' in s:
            cnt += 1
print(cnt)
'''


# № 21899 Открытый вариант 2025 (Уровень: Базовый)
# Адрес сети и широковещательный адрес не могут
# быть использованы для адресации сетевых устройств.

# Сеть задана IP-адресом одного из входящих в неё
# узлов 98.81.154.195 и сетевой маской 255.252.0.0.

# Найдите наибольший в данной сети IP-адрес, который
# может быть назначен компьютеру.
'''
from ipaddress import *
net = ip_network('98.81.154.195/255.252.0.0', 0)
for ip in net:
    print(ip)
    # 98.83.255.254 - ответ
    # 98.83.255.255 - широковещательный адрес

from ipaddress import *
net = ip_network('98.81.154.195/255.252.0.0', 0)
for ip in net.hosts():
    print(ip)  # 98.83.255.254
'''


# № 18159 (Уровень: Базовый)
'''
from ipaddress import *
# mask - это кол-во единиц в двоичной записи
for mask in range(1, 32+1):
    net = ip_network(f'205.154.212.20/{mask}', 0)
    if '205.154.192.0' in str(net):
        print(net, mask, net.netmask)
        # 205.154.192.0/18 18 255.255.192.0
        # 205.154.192.0/19 19 255.255.224.0
'''


# № 16260 Джобс 03.05.24 (Уровень: Средний)
# Известно два узла с IP-адресами 123.20.103.136 и 123.20.103.151
# принадлежат разным сетям с одинаковой маской.
# Определите значение 4 байта маски в этих сетях.
'''
from ipaddress import *
for mask in range(1, 32+1):
    net1 = ip_network(f'123.20.103.136/{mask}', 0)
    net2 = ip_network(f'123.20.103.151/{mask}', 0)
    if net1 != net2:
        print(net1.netmask)
        # 255.255.255.240
        # 255.255.255.248
        # 255.255.255.252
        # 255.255.255.254
        # 255.255.255.255
'''


# https://education.yandex.ru/ege/inf/task/94693776-a73a-4e59-bebb-b7e6107fe688
'''
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f'111.81.93.127/{mask}', 0)

    if '111.81.80.0' in str(net):
        print(net.netmask)
'''


# № 17879 Демоверсия 2025 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(800_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''

# № 24896 (Уровень: Базовый)
'''
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):  # не считая самого числа
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(1_475_000-1, 0, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        s = sum(d)
        if s != 0 and s <= 42000 and s % 6 == 0:
            print(x, s)
            cnt += 1
            if cnt == 5:
                break
'''


# № 23569 Пересдача 03.07.25 (Уровень: Средний)

def prime(x):
    d = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))


def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            if len(prime(j)) == 2 and len(prime(x // j)) == 2:
                if str(j).count('6') == 1 and str(x // j).count('6') == 1:
                    d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(6_086_055+1, 10**10):
    d = divisors(x)
    if len(d) > 0:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 7, 13, 14, 15, 16, 17, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 18
