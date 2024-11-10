# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 13 https://education.yandex.ru/ege/task/d3bde6f0-4eae-4994-bb5d-f757607b9d5f
# Адрес сети = Узел сети & Маска сети
'''
from ipaddress import *
net = ip_network('87.226.26.72/255.255.255.252', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('0') % 2 == 0:
        cnt += 1
print(cnt)
'''


# Задание 13 https://education.yandex.ru/ege/task/11ed12f4-9275-4ed0-814c-77afcfe165c4
'''
from ipaddress import *
net = ip_network('123.206.97.128/255.255.255.224', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b[-3:] in ('101', '010'):
        cnt += 1
print(cnt)
'''

# 248.112.56.35
#  1   1  1  1  байт
#  8   8  8  8  бит


# Задание 13 https://education.yandex.ru/ege/task/7a7901a6-c4ac-4554-aaaa-29270d559b19
'''
from ipaddress import *
for A in range(256):
    net = ip_network(f'248.112.{A}.35/255.255.255.240', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        print(A)
'''


'''
import sys
sys.setrecursionlimit(10000)

from functools import *

@lru_cache(None)
def F(n):
    if n <= 10:
        return n * 2
    if n % 2 == 0 and n > 10:
        return F(n - 3) - F(n - 9) * 2
    if n % 2 != 0 and n > 10:
        return F(n - 2) * 2 - F(n - 7)

print(sum([int(x) for x in str(F(3063))]))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 13, 14, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
