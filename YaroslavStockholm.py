# region Домашка: ******************************************************************

# № 10776 (Уровень: Базовый)
'''
from ipaddress import *
R = []
for mask in range(32+1):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    # '111.91.192.0' in str(111.91.192.0/19)
    if '111.91.192.0' in str(net):
        # print(net, mask, 32-mask)
        # 111.91.192.0/18 18
        # 111.91.192.0/19 19
        # 111.91.192.0/20 20
        R.append(32 - mask)
print(min(R))
'''

'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    #     кол-во ip адресов    адрес сети         адресе сети/кол-во 1   кол-во 1    кол-во 0   маска в 10-й записи
    print(net.num_addresses, net.network_address,        net,             mask,      32-mask,      net.netmask)
    #            4              111.91.200.28      111.91.200.28/30       30          2          255.255.255.252
'''


'''
from ipaddress import *


net = ip_network('192.168.32.48/255.255.255.240', 0)
cnt = 0
k = 0
for ip in net:
    k += 1
    a = f'{ip:b}'
    if a.count('1') % 2 != 0:
        cnt += 1
print(cnt)
print(k)  # 16
print(net.num_addresses)  # 26
'''

'''
from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240',0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 12255 ЕГКР 16.12.23 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(98591, 10**12, 98591):
    if fnmatch(str(x), '12?3*456??9'):
        print(x, x // 98591)
        # '12?3  * 456??9'
        #  1203 13 456439
'''


# № 14438 (Уровень: Средний)
'''
from fnmatch import *
for x in range(86513, 10**12, 86513):
    if fnmatch(str(x), '17*46??8'):
        summa = sum(map(int, str(x)))
        summa = sum([int(i) for i in str(x)])
        if (summa**0.5).is_integer():
            print(x, x // 86513)
'''

# № 13868 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '112?57*4'):
        summa = sum(map(int, str(x)))
        if summa % 2 != 0:
            print(x, x // 2024)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 25.1]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]
