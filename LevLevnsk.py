# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 20486 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    t = ''
    while n > 0:
        t = alphabet[n % b] + t
        n = n // b
    return t


R = []
for n in range(4, 10000):
    # s = bin(n)[2:]
    # s = f'{n:b}'
    s = convert(n, 2)
    if n % 2 == 0:
        s = s + s[:3]
    else:
        s = '1' + s + '0'
    r = int(s, 2)
    if r > 600:
        R.append(r)
print(min(R))
'''
# Ответ: 612


# № 19551 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    t = ''
    while n > 0:
        t = alphabet[n % b] + t
        n = n // b
    return t


for n in range(1, 10000):
    s = convert(n, 3)
    s = s.replace('2', '*')
    s = s.replace('0', '2')
    s = s.replace('*', '0')
    r = int(s, 3)
    res = abs(n - r)
    if res == 378:
        print(n)
        break
'''

# Пора бы освежить пост про all
# print(all(x % 2 == 0 for x in (2, 4, 6)))  # True
# print(all(x % 2 == 0 for x in (2, 5, 6)))  # False

# № 20580 (Уровень: Базовый)
'''
def F(x, y, A):
    return (9*x + y > A) or (x >= 36) or (y >= 18)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)  
'''


# № 20577 (Уровень: Базовый)
'''
def F(x, A):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 20584 (Уровень: Базовый)
'''
def F(x, A):
    return ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or (B <= (x % 22 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 18930 Новогодний вариант 2025 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = a1 <= x <= a2
    return (Q <= P) or ((not A) <= R)


R = []
M = [x / 4 for x in range(0, 320 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 79.75 -> 80
'''


# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


R = []
M = [x / 10 for x in range(5 * 10, 120 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14, 15]
# КЕГЭ = []
# на следующем уроке: 5, 8, 9, 12, 23, 25, 26/27


# Первый пробник 7.03.25:
# Лев 8/46 -> _ вторичных баллов +[2, 5, 15, 16, 19, 20, 23, 25] -[8, 9, 12, 21]
