# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def con(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(1, 1000):
    s = con(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + con(x, 3)
    r = int(s, 3)
    if r < 199:
        print(n)
'''


'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    if '213.168.64.0' in str(net):
        print(32-mask)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:23]:
    A = int(f'7{x}38596', 23)
    B = int(f'14{x}36', 23)
    C = int(f'61{x}7', 23)
    if (A + B + C) % 22 == 0:
        print((A + B + C) // 22)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = alphabet[:16]
s1 = '13579BDF'
s2 = '02468ACE'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if a != '0':
                if len(num) == len(set(num)):
                    if a in s1 and b in s2 and c in s1:
                        cnt += 1
                    if a in s2 and b in s1 and c in s2:
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
# ФИПИ = [2, 5, 6, 8, 12, 13, 14]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 14 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]
