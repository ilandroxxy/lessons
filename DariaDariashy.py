# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 23
'''
def F(a, b):
    if a > b or a == 31:
        return 0
    if a == b:
        return 1
    else:
        return F(a+3, b) + F(a+5, b) + F(a*3, b)

print(F(12, 15) * F(15, 52) * F(52, 80))
'''


# 15
'''
def F(x, a1, a2):
    B = 66 <= x <= 75
    C = 71 <= x <= 85
    A = a1 <= x <= a2
    return (not A) <= (B == C)

R = []
M = [x / 4 for x in range(50 * 4, 100 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

'''
def F(x, A):
    return (x & A == 0)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 1000)):
        print(A)
        break
'''

# 14
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

R = []
for x in range(1, 2000):
    n = 4**210 - 4**110 - x
    s = convert(n, 4)
    if s.count('0') == 0:
        print(x)
#     R.append(s.count('0'))
# print(min(R))
'''
# Ответ: 1707


# 13
'''
from ipaddress import *
net = ip_network('208.74.51.243/255.255.252.0', 0)
for ip in net:
    print(ip)
'''

# 11
'''
sym = 240
# alp - ?
# i - ?

byte = 55 * 2**20 / 154_789  # сколько байт на один серийный номер
print(byte)  # 372.582 -> 372
bit = 372 * 8  # сколько бит на один серийный номер

# bit = sym * i
i = bit / sym
print(i)  # 12.4 -> 12

print(f'Максимальная мощность: {2**12}')
print(f'Минимальная мощность: {2**11+1}')
'''


# 8
'''
n = 0
s = sorted('ПЛЮШКА')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if n % 2 != 0:
                            if a != 'А':
                                if len(word) == len(set(word)):
                                    print(n)
                                    exit()
'''

# 7
'''
pixels = 3620 * 2180
colors = 2**16  # i -> 16
i = 16  # это бит на один пиксель
bit = pixels * i  # бит на одну фотографию

card = 4*2**33  # бит

cnt = card / bit
print(cnt)  # 272.122 -> 272

print(3500 // 272)  # 12 - это кол-во полных таких карт
print(3500 % 272)  # 236 - это кол-во оставшихся 
'''
# Ответ: 236


# 5

def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

R = []
for n in range(1, 1000):
    s = bin(n)[2:]
    # s = convert(n, 2)
    # s = f'{n:b}'
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if n > 10:
        R.append(r)

print(min(R))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ = []
# на следующем уроке: 22, 24.1 повторять

# Второй пробник 28.02.25:
# Дарья 10/29 -> 51 вторичных баллов +[1, 2, 4, 7, 10, 11, 13, 15, 16, 18] -[3, 6, 12, 22]

