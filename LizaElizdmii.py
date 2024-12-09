# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038700/step/10?unit=1062785
'''
from ipaddress import *

a = []
for mask in range(32 + 1):
    net1 = ip_network(f'10.96.180.231/{mask}', 0)
    net2 = ip_network(f'10.96.140.118/{mask}', 0)
    if net1 != net2:
        # print(net1, mask, 32 - mask, net1.netmask)
        a.append(32 - mask)
print(max(a))
'''


# № 11780 (Уровень: Базовый)
# https://stepik.org/lesson/1038700/step/15?unit=1062785
'''
from ipaddress import *
maxi = 0
net = ip_network('185.8.0.0/255.255.128.0', 0)
for ip in net:
    maxi = max(maxi, f'{ip:b}'.count('1'))
print(maxi)
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
            div += [j, x // j]
            # div.append(j)
            # div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16] [1, 2, 4, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)  # 2.9475 -> 0.00036
'''


# Задание 25 https://education.yandex.ru/ege/task/fd10b825-4786-452a-92b6-6c74774db1e0
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


# for x in range(321_654, 654_321+1):
#     d = divisors(x)
#     d1 = [j for j in d if j % 2 == 1]
#     if len(d) == len(d1):
#         if len(d1) > 70:
#             print(x, max(d1))

for x in range(321_654, 654_321+1):
    d = divisors(x)
    if all(j % 2 == 1 for j in d):
        if len(d) > 70:
            print(x, max(d))
'''


# https://education.yandex.ru/ege/task/d02f4351-acc7-4b66-9ca1-83d0d1887db7
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


k = 0
for x in range(700_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 7 and j != 7]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''

'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(177_000, 177_300+1):
    if len(divisors(x)) == 0:
        summa = sum([int(y) for y in str(x)])
        if len(divisors(summa)) == 0:
            print(x, summa)
'''



# https://education.yandex.ru/ege/task/18b1a9da-4ed4-4f31-a23b-e64b03d0760e
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(10**6):
    d = [j for j in divisors(x) if fnmatch(str(j), '4*')]
    if len(d) == 24:
        print(x, max(d))
'''


# https://education.yandex.ru/ege/task/ab0df558-0d92-4a8c-99a2-eee07c7f83a5
'''
from fnmatch import *

for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)
'''


# https://education.yandex.ru/ege/task/85d22d9c-f966-494b-ae80-46b127f51ca3
'''
from fnmatch import *


def divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for i in range(500_000+1, 10 ** 10):
    k = sum(divisors(i))
    if fnmatch(str(k), '*7?'):
        print(i, k)
        cnt += 1
        if cnt == 5:
            break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
