# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
from ipaddress import *
for mask in range(32+1):
    net1 = ip_network(f'121.171.15.149/{mask}', 0)
    net2 = ip_network(f'121.171.15.143/{mask}', 0)
    if net1 == net2:
        print(mask, net1.num_addresses)
'''

# № 19748 (Уровень: Средний)
# Узлы с IP-адресами 157.220.185.237 и 157.220.184.230 принадлежат
# одной сети. Какое наименьшее количество IP-адресов,
# в двоичной записи которых ровно 15 единиц, может содержаться
# в этой сети?
'''
from ipaddress import *
for mask in range(15, 32+1):
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    cnt = 0
    if net1 == net2:
        for ip in net1:
            b = f'{ip:b}'
            if b.count('1') == 15:
                cnt += 1
        print(cnt)
'''


def F(x, A):
    return ((x % A != 0) and (x % 21 == 0)) <= (x % 14 != 0)

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 8, 12, 13, 14, 15, 16, 23]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Роман 2/5 -> 14 вторичных баллов +[2, 12] -[5, 6, 8]
