# region Домашка: ******************************************************************
from ctypes import c_int
from os import pread

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/1fba1cbc-57aa-4874-b06d-1b434166e30c
'''
M = []
for n in range(1, 10000):
    s = f'{n:b}'
    if n % 2 != 0:
        s = '1' + s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)
    if n >= 33:
        M.append(r)
print(min(M))
'''


# https://education.yandex.ru/ege/task/71189626-0f31-4380-b790-94a173acd59a
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

M = []
for n in range(1, 10000):
    s = convert(n, 7)
    z = ''
    for x in s:
        if x in '13579':
            z += str(int(x) + 1)
        else:
            z += x
    summa = sum([int(x) for x in z])
    # summa = sum(map(int, z))
    z = convert(summa, 7) + z
    if z[0] in '13579':
        z = z[0] + z
    r = int(z, 7)
    if r > 2000:
        M.append(r)
print(min(M))
'''


# https://education.yandex.ru/ege/task/11a28b89-356d-4baa-8ab4-3684fa4c1752
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

M = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        z = ''
        for x in s:
            z += x * 2
    else:
        s = s.replace('0', '*')
        s = s.replace('1', '+')
        s = s.replace('2', '0')
        s = s.replace('*', '1')
        s = s.replace('+', '2')
        z = ''
        for x in s:
            z += x * 2
    r = int(z, 3)
    print(r)
    if r > 120:
        M.append(n)
print(min(M))
'''


# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = convert(n, 27)
print(s.count('0'))  # Количество значащих нулей
print(len(s) - s.count('0'))  # Количество ненулевых цифр
print(len([x for x in s if x > '9']))  # количество цифр с числовым значением, превышающим 9.
'''


# № 17869 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 3*3125**8 + 2*625**7 -4*625**6 +3*125**5 - 2*25**4 - 2025
s = convert(n, 25)
print(s.count('0'))
'''


# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for x in range(1, 2030):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        print(x)
'''

# № 23753 Демоверсия 2026 (Уровень: Базовый)
'''
M = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'923{x}874', 29)
    B = int(f'524{x}6152', 29)
    if (A +  B) % 28 == 0:
        M.append((A +  B) // 28)
print(max(M))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 14]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]

# Второй пробник 28.02.25:
# Женя 10/29 -> 51 вторичных баллов +[2, 5, 6, 10, 13, 14, 15, 16, 23, 25] -[8, 12]
