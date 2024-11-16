# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 5 https://education.yandex.ru/ege/task/0f0be116-5c24-4561-8675-493fe3c6ba53
'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for n in range(1, 1000):
    s = convert(n, 5)
    if n % 25 == 0:
        s = s[-3:] + s
    else:
        x = (n % 25)
        s += convert(x, 5)
    r = int(s, 5)

    if r > 10000:
        print(n)
        break
'''


# Задание 5 https://education.yandex.ru/ege/task/4e651673-c848-47cd-8dab-813092d13201
'''
cnt = 0
for n in range(100, 1000):
    # if str(n).count('0') == 0:
    if '0' not in str(n):
        if all(n % int(x) == 0 for x in str(n)):
            new_n = int(str(n)[::-1])
            if all(new_n % int(x) == 0 for x in str(new_n)):
                cnt += 1
print(cnt)
'''


# Задание 5 https://education.yandex.ru/ege/task/96524f2d-3f1b-458d-9ee1-9b6d45c39389
'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if len(s) % 2 == 0:
        s = s[:len(s) // 2] + '000' + s[len(s) // 2:]
    else:
        s = '1' + s + '01'
    r = int(s, 2)

    if r > 100:
        print(n)
        break
'''


# Задание 5 https://education.yandex.ru/ege/task/6e679e3e-d6c0-4c26-9e5e-d6b89730c238
'''
M = []
for n in range(1, 13):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if n <= 12:
        M.append(r)
print(max(M))
'''

'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


M = []
for n in range(1, 1000):
    s = convert(n, 3)
    s = ''.join(sorted(s, reverse=True))
    s = s + max(s)  # s[0]
    r = int(s, 3)
    if r < 1200:
        M.append(r)
print(max(M))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6]
# КЕГЭ  = []
# на следующем уроке:
