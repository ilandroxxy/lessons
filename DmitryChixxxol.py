# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Встроенные функции перевода:
'''
n = 125
print(bin(n))  # 0b1111101
print(f'{n:b}')  # 1111101
print(bin(n)[2:])  # 1111101
print(int('1111101', 2))  # 125

print(oct(n))  # 0o175
print(f'{n:o}')  # 175
print(oct(n)[2:])  # 175
print(int('175', 8))  # 125

print(hex(n))  # 0x7d
print(f'{n:x}')  # 7d
print(f'{n:X}')  # 7D
print(hex(n)[2:])  # 7d
print(int('7d', 16))  # 125
'''

# Задание 5 https://education.yandex.ru/ege/task/ab4983f7-5f98-4cf2-9d3a-eee472c7d5ee
'''
result = []
for n in range(1, 10000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s, 2)  # Перевод из 2-ой в 10-ую
    # r = int(s, 16)  # Перевод из 16-ой в 10-ую
    if r > 225:
        result.append(r)
print(min(result))
'''

# Задание 5  https://education.yandex.ru/ege/task/de9a2152-8133-4115-9a90-d0d5eace5dcc
'''
result = []
for n in range(1, 1000):
    s = bin(n)[2:]
    for i in range(2):
        s += str(s.count('1') % 2)
    r = int(s, 2)
    if r < 86:
        result.append(n)

print(max(result))
'''


# Задание 5 https://education.yandex.ru/ege/task/96524f2d-3f1b-458d-9ee1-9b6d45c39389
'''
result = []
for n in range(1, 1000):
    s = f'{n:b}'
    if len(s) % 2 == 0:
        s = s[:len(s) // 2] + '000' + s[len(s) // 2:]
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if r > 100:
        result.append(n)
print(min(result))
'''

# Задание 5 https://education.yandex.ru/ege/task/b737ae42-5491-4d18-9318-0f179d8e670a
'''
n = 116
s = f'{n:b}'
A = [x for x in s]
l = len(A) // 2
if len(s) % 2 != 0:
    del A[l]
    s = ''.join(A)
else:
    del A[l-1]
    del A[l-1]
    s = ''.join(A)
r = int(s, 2)
print(r)
'''

# Задание 5 https://education.yandex.ru/ege/task/a579a1b6-fe4b-45e9-afc3-57649ff2fa75
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


result = []
for n in range(1, 10000):
    s = convert(n, 7)
    if s.count('2') % 2 == 0:
        s += '555'
    else:
        s = '1' + s
    r = int(s, 7)
    if r < 3799:
        result.append(n)

print(max(result))
'''

# Задание 5 https://education.yandex.ru/ege/task/066b8088-3cdb-4504-8403-9d62e96d195e
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1, 10000):
    s = convert(n, 5)

    summa = sum([int(x) for x in s])
    if summa % 2 != 0:
        s = s[-1] + s[:-1]
    else:
        s += convert((n % 10) * 3, 5)

    r = int(s, 5)
    if convert(r, 5).count('0') >= 2:
        print(r)
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
# ФИПИ = [2, 5, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:
