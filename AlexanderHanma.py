# region Домашка: ******************************************************************

# https://stepik.org/lesson/1228670/step/13?unit=1242203
'''
from ipaddress import *
cnt = 0
for mask in range(1, 33):
    net1 = ip_network(f'201.44.240.33/{mask}',0)
    net2 = ip_network(f'201.44.240.107/{mask}',0)
    if net1 == net2:
        # print(net1, net1.network_address)
        s = f'{net1.network_address:b}'
        if s.count('1') >= 5:
            cnt += 1

print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


cnt = 0
for x in range(2, 3577000):
    if is_prime(x):
        cnt += 1
print(cnt)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


maxi = 0
for x in range(2031, 14312+1):
    r = convert(x, 11)
    if '2' not in r:
        maxi = x
print(maxi)
'''

'''
def R(N):
    b = bin(N)[2:]
    if N % 2 == 0:
        return int('1' + b + '01', base=2)
    else:
        return int('10' + b , base=2)

a = []
for N in range(1, 13):
    a.append(R(N))

print(max(a))
'''

'''
R = []
for n in range(1, 13):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    R.append(r)
print(max(R))
'''

'''
def f(n ,t):
    if n < t:
        return 0
    elif n == t:
        return 1
    return f(n - 2, t) + f(n // 2, t)

print(f(38, 16) * f(16, 2))



def f(n ,t):
    if n <= t:
        return n == t
    return f(n - 2, t) + f(n // 2, t)

print(f(38, 16) * f(16, 2))
'''

# https://education.yandex.ru/ege/task/e0309b53-310b-4c80-a557-c75800407e4c
'''
pixels = 1440 * 900
colors = 2048   # colors = 2 ** i
i = 11   # бит на один пиксель
bit = pixels * i  # вес одной фотографии
V = bit * 256  # вес пакета
V_all = V * 32   # вес 32 пакетов
U = 21_600 * 2**13  # бит / с
print(V_all / U)  # с
print(660 / 60)
'''

# https://education.yandex.ru/ege/task/eb4d9b1f-9e48-4163-a44c-78007d760e63
'''
t = 150
a = 2
b = 16
c = 48000
bit = a * b * c * t
bit = bit * 0.5
U = 3200
print(bit / U)  # 36000
print((36000 / 60) / 60)
'''


# https://education.yandex.ru/ege/task/1027a3bb-c702-4d3e-9815-3c8d9ac033d6
'''
pixels = 1920 * 1080
i = 32
bit = pixels * i
bit += 120 * 2**3
V = 8*2**33
print(V / bit)
'''


# https://education.yandex.ru/ege/task/6332cc39-3e04-4b5b-acef-8c71dc0f1e3f
'''
pixels = 1024 * 768
i = 12
bit = pixels * i

U = 1_310_720
t = 300
BIT = U * t
print(BIT / bit)
'''
# 41.6666


# https://education.yandex.ru/ege/task/7e9d81e1-0e8a-4d19-b107-ed2daadbbdb4
'''
bit = 256 * 2**23
c = 16000  # гц
a = 1  # моно
t = 1.5 * 60 * 60  # сек

# bit = a * b * c * t
b = bit / (a * c * t)
print(b)
'''

'''
pixels = 2560 * 1440
V = 1 * 2 ** 33
bit = V / 200  # бит на одну фотографию
# bit = pixels * i
i = bit / pixels
print(i)  # 11.6508
print(2 ** 11)
'''


# https://education.yandex.ru/ege/task/7ca1cc68-b078-47db-b54a-e21af25f782d
'''
pixels = 1280 * 960
bit = 320 * 2**13
i = bit / pixels
print(i)  # 2.133333
i = 2
print(2 ** i)
'''

# 7 https://education.yandex.ru/ege/task/2640303f-cc77-424f-989c-f142e11c46f6

i = 24  # 2**24 - цветов
i2 = 8  # 2**8 - прозрачности
pixels = 1024 * 768
# bit = pixels * (i + i2)
bit = pixels * (24 + 8)
print(bit / 2**13)

# Ответ: 3072

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
