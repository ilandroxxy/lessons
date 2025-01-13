# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 2
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (z == w)) or (not(y <= w))
                if F == 0:
                    print(x, y, z, w)

# Ответ: zwyx
'''

# Задание 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


number = 0
R = []
for n in range(1, 100):
    s = convert(n, 3)

    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        number = (n % 3) * 4
        s += convert(number, 3)

    r = int(s, 3)
    if r < 199:
        R.append(n)

print(max(R))

# Ответ: 20
'''


# Задание 6
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
l = 25
t.down()

# Тут пишем псевдокод
t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10 * l)
    t.right(45)
t.right(315)
t.forward(10 * l)
for i in range(2):
    t.right(90)
    t.forward(10 * l)

# Тут перебираем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(4, 'red')

t.update()
t.done()
'''
# Ответ: 203


# Задание 12
'''
for n in range(3, 10000):
    s = '1' * 1 + '8' * n
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)

    if s.count('1') == 3:
        print(n)
        break
'''


# Задание 13
'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    if '213.168.64.0' in str(net):
        print(32 - mask)
'''
# Ответ: 14

# Задание 14
'''
from string import *
alphabet = digits + ascii_uppercase
for x in alphabet[:23]:
    A = int(f'7{x}38596', 23)
    B = int(f'14{x}36', 23)
    C = int(f'61{x}7', 23)
    if (A + B + C) % 22 == 0:
        print((A + B + C) // 22)
        break
        
# Ответ: 47163321
'''

''' # Задание 16
import sys
sys.setrecursionlimit(123123)
def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n - 2)

print(f(3027) - f(3023))
'''

# Задание 23
'''
def F(a, b):
    if a < b or a == 7:
        return 0
    elif a == b:
        return 1
    else:
        return F(a - 1, b) + F(a - 3, b) + F(a // 2, b)


print(F(19, 10) * F(10, 3))
'''

''' # Задание 25

from fnmatch import  *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)
'''


# Задание 7
'''
# V = a * b * c * t

a = 2
b = 48000
c = 24
# t = ?
V = 288 * 2**23  # 2**10 * 2**10 * 2**3
t = V / (a * b * c)  # сек
print(t / 60)  # мин
'''
# Ответ: 17.47626

# Задание 11
'''
symbols = 10
alphabet = 52  # alphabet = 2 ** i
i = 6  # 2 ** i >= alphabet, где i это количество бит на один символ

bit = symbols * i  # бит
print(bit / 8)  # 7.5 -> 8
byte = 8  # байт

print(byte * 65_536)  # байт
print((byte * 65_536) / 2**10)  # Кбайт
'''
# Ответ: 512


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 19-21+-, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Тимур 6/14 -> 40 вторичных баллов +[12, 14, 16, 19, 23, 25] -[4, 5, 6, 7, 8, 10, 11, 13]
