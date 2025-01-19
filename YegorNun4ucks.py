# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'61.58.73.42/{mask}', 0)
    net2 = ip_network(f'61.58.75.136/{mask}', 0)

    if net1 == net2:
        print(net1.netmask)

from ipaddress import *
net = ip_network('61.58.75.136/255.255.252.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)
'''

'''
s = open('files/24.txt').readline()
maxi = 0
for x in 'KLMN':
    s = s.replace(x, 'K')
for x in '123':
    s = s.replace(x, '2')
for i in range(len(s)):
    cnt1 = 0
    cnt2 = 0
    for j in range(i+1, len(s)):
        if s[j] == '2':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt2 == cnt1 * 2:
            maxi = max(maxi, len(s[i:j]))
            # print(maxi, cnt2, cnt1, s[i:j])
print(maxi)
'''

'''
from itertools import *

def divs(n):
    res = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)

    return sorted(set(res))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


for i in range(326782, 965325):
    prime_divs = [k for k in divs(i) if is_prime(k)]

    for k in permutations(prime_divs, 3):
        if k[0] * k[1] * k[2] == i:
            if max(prime_divs) - min(prime_divs) <= 12:
                print(i, max(prime_divs) - min(prime_divs))
                break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo № 17537 Основная волна 07.06.24 (Уровень: Средний)

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 14, 17, 22, 24]
# на следующем уроке:


# Первый пробник 21.12.24:
# Yegor 21/27 -> 80 вторичных баллов +[1-5, 7, 9-12, 14-16, 18-24, 27] -[6, 8, 13, 25, 26]
