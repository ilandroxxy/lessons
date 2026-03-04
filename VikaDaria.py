# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 23 номер Сатград Вариант 1 3.03.2026
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        if str(a)[0] > str(a)[1]:
            return F(int(str(a)[1] + str(a)[0]), b) + F(a - 2, b)
        else:
            return F(a - 2, b)

print(F(57, 13))


def F(a, b):
    if a <= b:
        return a == b
    else:
        if str(a)[0] > str(a)[1]:
            return F(int(str(a)[1] + str(a)[0]), b) + F(a - 2, b)
        else:
            return F(a - 2, b)

print(F(57, 13))
'''

# a = 75  -> int('5' + '7')


# 13 номер Сатград Вариант 1 3.03.2026
'''
from ipaddress import *
for mask in range(1, 32+1):
    # print('1' * mask + '0' * (32 - mask))
    net = ip_network(f'212.145.124.210/{mask}', 0)
    if '212.145.124.0' in str(net):
        print(net, net.network_address, mask, net.netmask)
'''



# 24 номер Сатград Вариант 1 3.03.2026
'''
from re import *
s = open('files/24.txt').readline()
pat = '[A-Z]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M if len(set(x)) == 26]))
'''


# Номер 24
'''
from re import *
s = open('files/24.txt').readline()
pat = '[678][0678]*([*-][678][0678]*)+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)

maxi = 0
for x in M:
    x = x.replace('0-', '0 ').replace('0*', '0 ')
    x = x.split()
    for a in x:
        if maxi < len(a):
            maxi = len(a)
            print(a)

print(maxi)

'788-7707067*766*70', '2423432'
'''


from re import *
s = open('files/24.txt').readline()
pat = '[678][0678]*[678]([*-][678][0678]*[678]|[*-][678][678]*)+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 25]
# на следующем уроке: Повторить 13, разбирать 24 import re

