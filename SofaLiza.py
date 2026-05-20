# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import product
RES = []
n = 0
for p in product(sorted('ХШЮЕЖЧЭВ'), repeat = 4):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] not in 'В':
            if word[-1] not in 'В':
                if word.count('Ч') >= 3:
                    RES.append(n)
print(min(RES))
'''


'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 25:
        return F(n - 5) + 5580
    if n < 25:
        return 12 * (G(n-11) - 14)

@lru_cache(None)
def G(n):
    if n >= 395881:
        return n / 6 + 34
    if n < 395881:
        return 13 + G(n + 39)

for n in range(400_000-1, -1, -1):
    G(n)

for n in range(0, 950, 1):
    F(n)

print(F(937))
'''

# № 29970 Апробация 14.05.26 (Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def G(n):
    if n <= 20:
        return n + 2
    if n > 20:
        return G(n - 3) + 1

def F(n):
    return 3 * G(n - 3) + 7

for n in range(0, 38000, 1):
    G(n)

print(F(37811))
'''


# № 28937 ЕГКР 18.04.26 (Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def G(n):
    if n >= 22560:
        return n / 23 + 33
    if n < 22560:
        return G(n + 11) - 4

@lru_cache(None)
def F(n):
    if n >= 21:
        return F(n - 8) + 1095
    if n < 21:
        return 10 * (G(n - 7) - 36)

for n in range(23000-1, -1, -1):
    G(n)

for n in range(600):
    F(n)

print(F(548))
'''

'''
print('1 2 3 4 5 6 7 8 9')
from itertools import permutations
table = '12 17 21 25 27 29 36 37 46 48 52 59 63 64 67 68 71 72 73 76 78 79 84 86 87 92 95 97'
graph = 'EH HE EB BE BH HB BA AB HD DH BD DB AD DA DC CD DG GD DF FD FG GF GC CG GI IG FI IF'
for p in permutations('EHBADCFGI'):
    new_table = table
    for i in range(1,9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# https://education.yandex.ru/ege/inf/task/600fe533-49f2-4cb5-a1c9-461910039669
# Сеть задана IP-адресом 172.16.168.0 и маской сети 255.255.248.0.
# Сколько в этой сети IP-адресов, для которых количество единиц
# в двоичной записи IP-адреса не кратно 5?
'''
from ipaddress import *
net = ip_network('172.16.168.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('1') % 5 != 0:
        cnt += 1
print(cnt)
'''

# Сеть задана IP-адресом 195.102.65.64 и маской сети 255.255.255.192.
# Сколько в этой сети IP-адресов, в которых одинаковое количество нулей
# и единиц в правом байте адреса?
'''
from ipaddress import *
net = ip_network('195.102.65.64/255.255.255.192', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2[24:].count('1') == ip2[24:].count('0'):
        cnt += 1
print(cnt)
'''

# Адрес сети и широковещательный адрес не могут быть использованы для адресации сетевых устройств.
# Сеть задана IP-адресом одного из входящих в неё узлов 73.148.145.65 и сетевой маской 255.224.0.0.
# Найдите наибольший в данной сети IP-адрес, который может быть назначен компьютеру. В ответе укажите найденный IP-адрес без разделителей.

'''
from ipaddress import *
net = ip_network('73.148.145.65/255.224.0.0', 0)
for ip in net:
    print(ip)  # 73.159.255.254
'''


# https://education.yandex.ru/ege/inf/task/3f319a67-ed81-47b3-acb0-6d3f7cacce6a
# Для узла с IP-адресом 117.73.208.27 адрес сети равен 117.73.192.0.
# Каково наименьшее возможное количество нулей в разрядах маски?
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'117.73.208.27/{mask}', 0)
    if '117.73.192.0' in str(net):
        print(net, mask, 32-mask)
'''

# https://education.yandex.ru/ege/inf/task/389410cf-5a37-48e7-a5be-507c52171bd0
'''
cnt = 0
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    if '76.155.48.0' in str(net):
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/311278cb-12ec-4f14-bde6-571d7045cc02
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.81.208.27/{mask}', 0)
    if '111.81.192.0' in str(net):
        print(net, mask, net.netmask)
        # 111.81.192.0/18 18 255.255.192.0
        # 111.81.192.0/19 19 255.255.224.0
'''


# https://education.yandex.ru/ege/inf/task/efa830d3-9d5f-40b1-8630-3c767db89078
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'121.171.5.70/{mask}', 0)
    net2 = ip_network(f'121.171.5.107/{mask}', 0)
    if net1 == net2:
        print(net1.num_addresses)
'''

# Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.240.
# Сколько в этой сети IP-адресов, для которых количество нулей в двоичной записи IP-адреса больше 21?
'''
from ipaddress import *

net = ip_network('192.168.32.160/255.255.255.240', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('0') > 21:
        cnt += 1
print(cnt)
'''

# Сеть задана IP-адресом 123.222.99.192 и маской сети 255.255.255.248.
# Сколько в этой сети IP-адресов, в которых нулей в двоичной записи IP-адреса меньше, чем единиц?
'''
from ipaddress import *
cnt = 0
net = ip_network('123.222.99.192/255.255.255.248', 0)
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('0') < ip2.count('1'):
        cnt += 1
print(cnt)
'''



#5 https://stepik.org/lesson/1228670/step/6?unit=1242203
'''
from ipaddress import *
net = ip_network('112.154.133.208/255.255.252.0', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2[:16].count('1') <= ip2[16:].count('0'):
        if ip2[16:].count('0') % 2 != 0:
            cnt += 1
print(cnt)
'''

#8 https://stepik.org/lesson/1228670/step/9?unit=1242203
'''
from ipaddress import *
RES = []
for mask in range(32 + 1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        RES.append(mask)
print(min(RES))
'''

#9 https://stepik.org/lesson/1228670/step/10?unit=1242203
'''
from ipaddress import *
net = ip_network('214.96.0.0/255.240.0.0', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('0') % 3 == 0:
        cnt += 1
print(cnt)
'''


# https://stepik.org/lesson/1228670/step/11?unit=1242203
# Сеть задана IP-адресом 123.222.111.192 и маской сети 255.255.255.248
# Сколько в этой сети IP-адресов, для которых сумма единиц в двоичной
# записи четвёртого байта IP-адреса не делится без остатка на 3?
'''
from ipaddress import *
net = ip_network('123.222.111.192/255.255.255.248', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2[24:].count('1') % 3 != 0:
        cnt += 1
print(cnt)
'''


# № 29082 (Уровень: Средний)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 19:
        return 5
    if n >= 19:
        return (n + 4) * F(n - 7)

for i in range(0, 158000):
    F(i)

print((F(157163) // 234 + F(157149) // 533) // F(157142))


# F(157163) = (157163 + 4) * F(157156)
# F(157156) = (157156 + 4) * F(157149)
# F(157149) = (157149 + 4) * F(157142) / F(157142)

h1 = (157163 + 4) * (157156 + 4) * (157149 + 4) / 234
h2 = (157149 + 4) / 533
print(h1 + h2)
'''



# № 29970 Апробация 14.05.26 (Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def F(n):
    return 3 * G(n - 3) + 7

@lru_cache(None)
def G(n):
    if n <= 20:
        return n + 2
    if n > 20:
        return G(n - 3) + 1

for i in range(0, 38000, 1):
    G(i)

print(F(37811))
'''


# № 28937 ЕГКР 18.04.26 (Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 21:
        return F(n - 8) + 1095
    if n < 21:
        return 10 * (G(n-7) - 36)

@lru_cache(None)
def G(n):
    if n >= 22560:
        return n / 23 + 33
    if n < 22560:
        return G(n + 11) - 4

for i in range(23000-1, -1, -1):
    G(i)

for i in range(600):
    F(i)

print(F(548))
'''

# № 25397 (Уровень: Средний)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    if n <= 40:
        return 3 * (G(n - 2) - 15)


@lru_cache(None)
def G(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return G(n + 7) - 21


for i in range(302000 - 1, -1, -1):
    G(i)
for i in range(2100):
    F(i)

print(F(2026))
'''


# № 25355 ЕГКР 13.12.25 (Уровень: Базовый)
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)


@lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4


for i in range(250000 - 1, -1, -1):
    G(i)

for i in range(700):
    F(i)
print(F(673))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [22, 6, 7, 10, 11, 12, 17]
# на следующем уроке: 22, 17 24 27 26


# region 📖 Пробник (Вариант 2)

# Студент #Софья
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 3, 5, 7, 8, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 6, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# Студент #Лиза
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# endregion 📖 Пробник (Вариант 2)
