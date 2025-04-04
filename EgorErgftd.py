# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 12097
'''
from itertools import *
n = 0
R = []
for p in product(sorted('ГИРЛЯНДА'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 == 0 and word[0] != 'Я' and word.count('Д') == 3:
        R.append(n)
print(max(R))
'''


# № 12917  (Уровень: Базовый)
'''
from itertools import *
R = []
for p in permutations('ПРОСТО', r=6):
    word = ''.join(p)
    if 'ОО' not in word:
        R.append(word)
print(len(set(R)))
'''

'''
from itertools import *
cnt = 0
for p in set(permutations('ПРОСТО', r=6)):
    word = ''.join(p)
    if 'ОО' not in word:
        cnt += 1
print(cnt)
'''


# № 11827
'''
from itertools import *
cnt = 0
for p in product('01234567', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        chet = [int(x) for x in num if x in '0246']
        if len(chet) == 2:
            for el in '135':
                num = num.replace(el, '*')
                # print(num, num2)
            if '*7' not in num and '7*' not in num and '77' not in num:
                cnt += 1
print(cnt)
'''

# № 20902 Апробация 05.03.25 (Уровень: Базовый)
# Сеть задана IP-адресом 172.16.80.0 и маской сети 255.255.248.0.
#
# Сколько в этой сети IP-адресов, для которых количество
# единиц в двоичной записи IP-адреса не кратно 2?
'''
from ipaddress import *
net = ip_network('172.16.80.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 2 != 0:
        cnt += 1
print(cnt)
'''



# № 11787 (Уровень: Базовый)
#  суммарное количество единиц в левых двух байтах
#  больше суммарного количества единиц в правых двух байтах.
'''
from ipaddress import *
net = ip_network('101.157.240.0/255.255.252.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'  # 32 бит
    if b[:16].count('1') > b[16:].count('1'):
        cnt += 1
print(cnt)
'''
# байт байт байт байт
# b[:8] b[8:16] b[16:24] b[24:]


# № 11770 (Уровень: Базовый)
# Для узла с IP-адресом 251.211.38.240 адрес сети равен 251.211.38.0.
# Для скольких различных значений маски это возможно?
'''
from ipaddress import *
cnt = 0
for mask in range(32+1):
    net = ip_network(f'251.211.38.240/{mask}', 0)
    if '251.211.38.0' in str(net):
        cnt += 1
print(cnt)
'''

'''
from ipaddress import *
cnt = 0
for mask in range(32+1):
    net = ip_network(f'157.17.164.129/{mask}', 0)
    if '157.17.128.0' in str(net):
        print(net.netmask)
'''

'''
from ipaddress import *
cnt = 0
for mask in range(32+1):
    net1 = ip_network(f'201.44.240.33/{mask}', 0)
    net2 = ip_network(f'201.44.240.107/{mask}', 0)
    if net1 == net2:
        if f'{net1.network_address:b}'.count('1') >= 5:
            cnt += 1
print(cnt)
'''

from functools import *
import sys
sys.setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n/2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)

for n in range(5000):
    F(n)

print(F(4952) + 2 *F(4958) + F(4964))



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 7, 11, 19-21, 22, 24

# Первый пробник 21.12.24:
# Михаил 8/18 -> 46 вторичных баллов +[2, 4, 6, 12, 14, 15, 16, 23] -[1, 3, 5, 7, 8, 9, 11, 13, 17, 25]

# Второй пробник 28.02.25:
# Михаил 17/29 -> 70 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-16, 18, 19-20, 23, 25] -[5, 7, 10, 13, 17, 21, 22, 24]
# Егор 16/29 -> 68 вторичных баллов +[1-7, 9, 13, 14-18, 23, 25] -[8, 10, 11, 12, 19-21, 22, 24]
