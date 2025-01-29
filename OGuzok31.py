# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        R.append(A)
print(max(R))


# Вариант 2

def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))


# Вариант 2.2
print(max([A for A in range(1, 10000) if all(( ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) for x in range(1, 10000))]))
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)

for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''

'''
def F(x, a1, a2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not(C or J)) <= (not A)


R = []
M = [x / 4 for x in range(40*4, 120*4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))
'''

#
# № 19748 (Уровень: Средний)

'''
from ipaddress import *
for mask in range(15, 32+1):
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            b = f'{ip:b}'
            if b.count('1') == 15:
                cnt += 1
        print(cnt)
'''


'''
n = 8
print(bin(n)[2:])  # 1000
print(f'{n:b}')  # 1000

print(oct(n)[2:])  # 10
print(f'{n:o}')  # 10

print(hex(n)[2:])  # 8
print(f'{n:x}')  # 8
'''


# № 18966 (Уровень: Базовый)

from ipaddress import *
net = ip_network('5.2.5.0/255.255.0.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('0') % 25 == 0:
        cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2? сопоставление, 3, 4, 5, 7, 8, 9-, 11-, 12-, 13-, 14, 15, 16-, 19-21-, 22]
# КЕГЭ  = []
# на следующем уроке:
