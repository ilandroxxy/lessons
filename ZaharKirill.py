# region Домашка: ******************************************************************

# № 5111 (Уровень: Базовый)
# https://stepik.org/lesson/1038432/step/7?unit=1060804
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    # if s.count('1') % 2 == 0:
    if sum(map(int, s)) % 2 == 0:
        s = '10' + s[2:] + '1'
    else:
        s = '1' + s[2:] + '11'
    r = int(s, 2)
    if r >= 100:
        M.append(n)

print(min(M))
'''
import multiprocessing

# № 7026 (Уровень: Базовый)
# https://stepik.org/lesson/1038432/step/8?unit=1060804
'''
M = []
for n in range(9, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '00'
    else:
        s = s + bin(s.count('1'))[2:]
    r = int(s, 2)
    if r > 88:
        M.append([r, n])

print(min(M)[1])  # [103, 25]
'''



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 14 https://education.yandex.ru/ege/task/12b3aabc-7777-4808-b29a-29993b289cca
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 3 * 3125 ** 8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(convert(n, 25).count('0'))
'''

'''
n = 3 * 3125 ** 8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
M = []
while n > 0:
    M.append(n % 25)
    n //= 25
M = M[::-1]
print(M.count(0))
print(len(set(M)))
print(set(M))
'''

# Задание 14 https://education.yandex.ru/ege/task/c5e4d9a3-018f-4705-b0dc-68403da4763f
'''
n = 3*7**82 - 4*49**21 + 5*343**25
M = []
while n > 0:
    M.append(n % 7)
    n //= 7
M = M[::-1]
print(sum(M))
'''


# Задание 14 https://education.yandex.ru/ege/task/a8c96097-e410-484b-8fe6-9d1034a9e228
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2030):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        print(x)
'''
'''
for x in range(2030):
    n = 7 ** 170 + 7 ** 100 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n //= 7
    M = M[::-1]
    if M.count(0) == 71:
        print(x)
'''

# Задание 14 https://education.yandex.ru/ege/task/eca565e6-aa59-4e06-8e2c-fccdac9e9fd7
'''
from string import *
alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

M = []
for x in alphabet[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        M.append((A + B) // 18)
print(max(M))
'''


# Тип 14 №48387
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:11]:
    for y in alphabet[:11]:
        A = int(f'{x}341{y}', 11)
        B = int(f'56{x}1{y}', 19)
        if (A + B) % 305 == 0:
            print((A + B) // 305)
'''


# Задание 14 https://education.yandex.ru/ege/task/749a92f0-0083-4931-90cf-8c987a48ed9c
'''
M = []
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:16]:
    for y in alphabet[:16]:
        A = int(f'27A{x}23', 16)
        B = int(f'8{y}E5D2', 16)
        if (A + B) % 5 == 0:
            print(x + y, alphabet.index(x) + alphabet.index(y))
            M.append(alphabet.index(x) + alphabet.index(y))
print(max(M))
'''


# Задание 14 https://education.yandex.ru/ege/task/1b5ee551-6d66-4c66-b1ae-8169874ee37b
'''
for x in range(2030):
    n = 3 ** 100 - x
    M = []
    while n > 0:
        M.append(n % 3)
        n //= 3
    M.reverse()
    if M.count(0) == 5:
        print(x)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 12]
# КЕГЭ  = []
# на следующем уроке:
