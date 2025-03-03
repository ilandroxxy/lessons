# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 23
'''
def F(a, b):
    if a > b or a==13:
        return 0
    if a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2,b) + F(a * 3, b)
print(F(3, 8) * F(8,18))
'''

# Номер 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A+B+C) % 17 == 0:
        print((A+B+C) // 17)
'''

# Номер 13
'''
from ipaddress import *
for mask in range(1,32+1):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
        print(net, net.netmask)
        # 111.118.178.0/23 255.255.254.0
'''


# Номер 12
'''
for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122','25', 1)
    summa = sum(map(int,s))
    if summa == 64:
        print(n)
        break
'''


# Номер 8
'''
from itertools import *
n = 0
for p in product(sorted('СБОРНИК'), repeat = 6):
    n += 1
    word = ''.join(p)
    if word.count('Б') == 2 and word.count('К') <= 1 and word[0] != 'Р':
        print(n)
'''


# Номер 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1, 1000):
    s = convert(n,3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 150:
        print(n)
        break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Второй пробник 28.02.25:
# Артем 4/29 -> 27 вторичных баллов +[2, 10, 15, 16] -[1, 5, 6, 8, 12, 13, 14, 23]
