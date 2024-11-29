# region Домашка: ************************************************************

# № 10776 (Уровень: Базовый)
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    print(net, net.netmask, mask, 32-mask)
    # 111.91.192.0/18 255.255.192.0 18 14
    # 111.91.192.0/19 255.255.224.0 19 13
    # 111.91.192.0/20 255.255.240.0 20 12


from ipaddress import *
R = []
for mask in range(32+1):
    net = ip_network(f'111.91.200.28/{mask}', 0)
    # if str(net) == f'111.91.192.0/{mask}':
    if '111.91.192.0' in str(net):
        R.append(32 - mask)

print(min(R))
'''


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
import time
start = time.time()

# def divisors(n):
#     div = []  # будем складывать делители числа
#     for j in range(1, n+1):
#         if n % j == 0:
#             div.append(j)
#     return div


def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            # div.append(j)
            # div.append(n // j)
            div += [j, n // j]
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)  # 2.9666 -> 0.00033
'''

'''
def divisors(n):
    div = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            div += [j, n // j]
    return sorted(set(div))


for n in range(135_790, 163_228+1):
    d = divisors(n)
    if sum(d) > 460_000:
        print(len(d), sum(d))
'''


# https://education.yandex.ru/ege/task/d02f4351-acc7-4b66-9ca1-83d0d1887db7
'''
def divisors(n):
    div = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            div += [j, n // j]
    return sorted(set(div))


cnt = 0
for n in range(700_000+1, 10**10):
    d = [j for j in divisors(n) if j != 7 and j % 10 == 7]
    if len(d) > 0:
        print(n, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# https://education.yandex.ru/ege/task/41a06b51-e4e0-4204-b3ac-432f00e2ac2c
'''
def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div += [j, n // j]
    return sorted(set(div))


for n in range(977004+1, 977022):
    d = [j for j in divisors(n) if j % 2 == 0]
    if len(d) >= 6:
        print(n, d[-2])
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ = []
# на следующем уроке:
