# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
from ipaddress import *

cnt = 0
for mask in range(33):
    net = ip_network(f'68.30.20.77/{mask}', 0)
    net_b = f'{net.network_address:b}'
    if (32 - mask) == net_b.count('1'):
        cnt = 0
        for ip in net:
            ip_b = f'{ip:b}'
            if ip_b.count('1') == 10:
                cnt += 1
print(cnt)
'''

'''
from functools import *

@lru_cache(None)
def F(n):
    if n == 0: return 0
    if n > 0 and n % 4 < 2: return F(n//4) + n % 4
    if n % 4 >= 2: return F(n//4) + n % 4 - 1


for n in range(200_000_000, 300_000_000):
    if F(n) == 27 and F(n+1) == 16:
        print(n)
        break
'''

maxi = 0
s = open('0. files/24.txt').readline()
for x in 'BCD*':
    s = s.replace(x, ' ')
for x in '++ -- +- -+'.split():
    s = s.replace(x, ' ')
s = s.split()
for x in s:
    if 'A' not in x:
        continue
    x = x[x.index('A'):]
    x = x.split('A')
    for y in x:
        try:
            eval(y)
            if y[0] in '+-':
                continue
            if maxi <= len(y):
                maxi = len(y)
                print(maxi, y, eval(y))
        except:
            continue

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [8, 14, 15, 23]
# на следующем уроке:

# Первый пробник 21.12.24:
# 24/25 -> 88 вторичных баллов +[1, 3-25] -[2]

# Второй пробник 10.02.25:
# 23/25 -> 86 вторичных баллов +[1-9, 11-23, 25] -[10, 24]
