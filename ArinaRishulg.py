# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Номер 7
'''
X=(1024*512*4*8)/32768
print(X)
'''
# Ответ: 512


# Номер 13

# 111.118.178.0 - 4 байта - 32 бита -> максимальное число 255, потому что оно в двоичном виде 11111111
# маска тоже имеет длину 32 бита, и имеет вид: 111111...0000 сначала единица затем нули

# 1. 100000.. -> 31 нулик
# 2. 1100000.. -> 30 нулик
# 3. 11100000.. -> 29 нулик

# mask - это количество единиц в двочиной записи маски

from ipaddress import *  # ctrl + B
from pickletools import uint1
from runpy import run_path

for mask in range(1, 32+1):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
        print(net.netmask)
        # 255.255.254.0

# Ответ: 254

'''
print(bin(179)[2:])
print(bin(178)[2:])

# 10110011
# 10110010
# 11111110
print(int('11111110', 2))  # 254
'''

# Адрес сети = Узлу сети & Маска сети
# & - побитовая конъюнкция
'''
print(f'{12:b}')
print(f'{6:b}')

print(12 & 6)  # 4

print(int('0100', 2))  # 4
print(int('0100', 8))  # 64
'''

# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 4 and len(uncopied) == 3:
        if sum(copied) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''


M = [8]
M.append(5)
print(M)  # [8, 5]
M.append(6)
print(M)  # [8, 5, 6]


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 19-21]
# КЕГЭ = []
# на следующем уроке: 22, 13, 17, 16, 9, 10, 18, 19-21


# Первый пробник 7.03.25:
# Арина 12/29 -> _ вторичных баллов +[1, 2, 3, 4, 5, 8, 9, 11, 12, 14, 15, 23] -[7, 13, 17, 19-21, 18, 25]
