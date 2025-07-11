# region Домашка: ******************************************************************

'''
a = []
from fnmatch import *

for x in range(11071, 10 ** 10, 11071):
    if fnmatch(str(x), '?136*1'):
        if str(x)[0] in '13579':
            if str(x)[-2] in '02468':
                a.append([x, x // 11071])

for i in a[-5:]:
    print(*i)
'''
from idlelib.pyshell import usage_msg

'''
A = [1, 2]
A += [3, 4]
print(A)

A = []
A.append([1, 2])
A.append([3, 4])
print(A)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import time
start = time.time()

# def divisors(x):
#     div = []
#     for j in range(1, x+1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            # div.append(j)
            # div.append(x // j)
            div += [j, x // j]
    return sorted(set(div))


print(divisors(100_000_000))

end = time.time()
print(end - start)
'''


# № 20814 Апробация 05.03.25 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(500_000+1, 10**9):
    d = divisors(x)
    if len(d) > 0:
        R = sum(d)
        if R % 10 == 9:
            print(x, R)
            cnt += 1
            if cnt == 5:
                break
'''

# № 18148 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(900_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 100 == 46:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 19755 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(1_200_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) >= 2:
        M = min(d) + max(d)
        if M > 2000 and M % 10 == 8:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 23382 Резервный день 19.06.25 (Уровень: Базовый)

'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

def is_prime(x):
    return x > 1 and all(x % j != 0 for j in range(2, int(x**0.5)+1))


def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            if is_prime(j) and is_prime(x // j):
                if str(j).count('2') == 1 and str(x // j).count('2') == 1:
                    return [j, x // j]
    return []


cnt = 0
for x in range(6_651_220+1, 10**10):
    d = divisors(x)
    if len(d) == 2:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break
'''



# Адрес сети = Узел сети & Маска сети

# & - операция побитовой конъюнкции
# print(14 & 5)  # 4

# net = Узел сети & Маска сети
# for ip in net:

'''
from ipaddress import *
net = ip_network('Узел сети/Маска сети', 0)
'''

# 73.148.145.65 - айпишник
# 255.255.248.0 - маска сети
# Маска сети это 32 бита вида: 111111...0000

# 255_10 -> 11111111_2


# № 23372 Резервный день 19.06.25 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('73.148.145.65/255.224.0.0', 0)
for ip in net:
    print(ip)
'''


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


# № 19748 (Уровень: Средний)
'''
from ipaddress import *
R = []
for mask in range(15, 32+1):
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            s = f'{ip:b}'
            if s.count('1') == 15:
                cnt += 1
        R.append(cnt)
print(min(R))
'''

from ipaddress import *
net=ip_network("218.194.82.148/255.255.255.192", 0)
for ip in net:
    print(net[-2])
    break

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
