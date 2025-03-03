# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
n = 8
print(bin(n))  # 0b1000
print(bin(n)[2:])  # 1000 - 2-я
print(oct(n)[2:])  # 10 - 8-я
print(hex(n)[2:])  # 8 - 16-я

print(f'{n:b}')  # 1000 - 2-я
print(f'{n:o}')  # 10 - 8-я
print(f'{n:x}')  # 8 - 16-я
print(f'{n:X}')  # 8 - 16-я


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


print(convert(8, 2))  # 1000
print(convert(8, 8))  # 10
print(convert(8, 16))  # 8

print(convert(8, 3))  # 22
'''

# Номер 5
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        # s = s + s[-3] + s[-2] + s[-1]
        s = s + s[-3:]
    else:
        s = s + convert((n % 3) * 3, 3)
    r = int(s, 3)
    if r > 150:
        print(n)
        break
'''

# Номер 14
'''
from string import *
alphabet = digits + ascii_uppercase

for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''


# Номер 13
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
        print(net, mask, 32-mask, net.netmask)
        # 111.118.178.0/23 23 9 255.255.254.0
'''
# Ответ: 254


# Номер 8
'''
from itertools import *
n = 0
for i in product('СБОРНИК', repeat=6):
    st = ''.join(i)
    n += 1
    if st[0] != 'Р' and st.count('Б')== 2 and st.count('К') <= 1:
        print(n)
'''

# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(uncopied) == 3 and len(copied) == 4:
        if sum(copied) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''

# Номер 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 2089 99343

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке: 5, 8, 9, 13, 14, 17


# Первый пробник 21.12.24:
# Тимур 6/29 -> 40 вторичных баллов +[12, 14, 16, 19, 23, 25] -[4, 5, 6, 7, 8, 10, 11, 13]

# Второй пробник 28.02.25:
# Тимур 9/29 -> 48 вторичных баллов +[1, 2, 7, 16, 19-21, 23, 25] -[5, 6, 8, 9, 13, 14, 17]
