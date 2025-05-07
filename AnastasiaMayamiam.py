# region Домашка: ******************************************************************
'''
from ipaddress import*
for mask in range(32+1):
    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1 != net2:
        print(mask)
        break
'''


# 112.154.135.252


#  № 12088 (Уровень: Средний) 🌶
'''
from ipaddress import*
net = ip_network('112.154.133.208/255.255.252.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b[:16].count('1') <= b[16:].count('0'):
        if b[16:].count('0') % 2 != 0:
            cnt += 1
print(cnt)
'''

'''
from ipaddress import*
net = ip_network('129.128.0.0/255.128.0.0', 0)
R = []
for ip in net:
    b = f'{ip:b}'
    R.append(b.count('0'))
print(min(R))
'''

# № 21718 ЕГКР 19.04.25 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(7993, 10**10, 7993):
    if fnmatch(str(x), '4*4736*1'):
        print(x, x // 7993)


from re import *
for x in range(7993, 10**10, 7993):
    if fullmatch('4[0-9]*4736[0-9]*1', str(x)):
        print(x, x // 7993)
'''


'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, (24**0.5) , 6, 8, 12, 24]
print(divisors(16))  # [1, 2, (16**0.5), 8, 16]
'''

# № 21422 Досрочная волна 2025 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

k = 0
for x in range(1_125_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 7 and j != x and j != 7]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break
'''


# № 17879 Демоверсия 2025 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


k = 0
for x in range(800_000+1, 10**10):
    d = divisors(x)
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            k += 1
            if k == 5:
                break
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 11, 13, 15, 16, 23, 19-21]
# КЕГЭ  = []
# на следующем уроке: 7, 8, 9, 25

# Первый пробник 21.12.24:
# Анастасия 9/29 -> 48 вторичных баллов +[1, 2, 4, 12, 16, 14, 15, 23, 20-21] -[3, 8, 10, 11, 18, 19]
