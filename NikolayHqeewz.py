# region Домашка: ******************************************************************

# № 1408 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return (n + F(n - 2)) // 5
    if n > 2 and n % 2 != 0:
        return (2 * n + F(n - 1) + F(n - 2)) // 4

print(F(50))
'''


# № 8159 (Уровень: Базовый)
'''
def F(x, y, A):
    B = 50 <= x <= 70
    return (2*x + y != 150)  or (not B) or (A > y)

R = []
for A in range (1, 1000):
    if all(F(x, y, A) for x in range (1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from itertools import *
print('1 2 3 4 5 6')
table = '12 14 15 21 23 26 32 35 41 45 51 53 54 62'
graph = 'ГБ БГ БВ ВБ БА АБ АД ДА ДВ ВД ДЕ ЕД ЕВ ВЕ'
for p in permutations('АБВГДЕ'):
    new_teble = table
    for i in range(1, 6+1):
        new_teble = new_teble.replace(str(i), p[i-1])
    if set(new_teble.split()) == set(graph.split()):
        print(*p)

# 1 2 3 4 5 6
# В Б А Е Д Г

# БВ + ЕД = 14 + 8 = 22


# № 18308 (Уровень: Базовый)
'''
from itertools import *
print('1 2 3 4 5 6 7 8 9')
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KC CK KB BK BD DB DC CD DH HD DG GD DE ED EF FE FG GF GH HG'
for p in permutations('ABCDEFGHK'):
    new_teble = table
    for i in range(1, 9+1):
        new_teble = new_teble.replace(str(i), p[i-1])
    if set(new_teble.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7 8 9
# B G C D K A E F H
# C G B D K A E F H

# FE + ED = 8 + 15 = 23


# № 19748 (Уровень: Средний)
# Узлы с IP-адресами 157.220.185.237 и 157.220.184.230 принадлежат одной сети.
# Какое наименьшее количество IP-адресов, в двоичной записи которых
# ровно 15 единиц, может содержаться в этой сети?
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


# № 18966 (Уровень: Базовый)
# Сеть задана IP-адресом 5.2.5.0 и маской сети 255.255.0.0.
# Сколько в этой сети IP-адресов, для которых количество
# нулей в двоичной записи IP-адреса кратно 25?
# В ответе укажите только число.
'''
from ipaddress import *
net = ip_network('5.2.5.0/255.255.0.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('0') % 25 == 0:
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
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Николай 9/19 -> 48 вторичных баллов +[1, 2, 4, 7, 13, 14, 16, 23, 25] -[5, 6, 8, 9, 12, 15, 17, 24]
