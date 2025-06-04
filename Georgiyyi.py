# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 21414 Досрочная волна 2025 (Уровень: Базовый)
'''
def F(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)


for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# № 19485 (Уровень: Базовый)
'''
def F(x, A):
    B = 170 <= x <= 220
    return (x % A == 0) or ((B) <= (x % 24 != 0))

cnt = 0
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        cnt += 1
print(cnt)
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 18595 (Уровень: Базовый)
'''
def F(x, a1, a2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not (C or J)) <= (not A)

R = []
M = [x / 4 for x in range(40 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))  # 52.0 -> 52
'''


# № 21411 Досрочная волна 2025 (Уровень: Базовый)
# Дана программа для Редактора:
#
#    ПОКА нашлось (31) ИЛИ нашлось (211) ИЛИ нашлось (1111)
#      ЕСЛИ нашлось (31)
#        ТО заменить (31, 1)
#      ЕСЛИ нашлось (211)
#        ТО заменить (211, 13)
#      ЕСЛИ нашлось (1111)
#        ТО заменить (1111, 2)
'''
for n in range(4, 10000):
    s = '3' + '1' * n

    while '31' in s or '211' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '211' in s:
            s = s.replace('211', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '2', 1)


    summa = sum([int(x) for x in s if x.isdigit()])
    # summa = sum(map(int, s))
    if summa == 15:
        print(n)
        break
'''

'''
from string import *
alp = digits + ascii_uppercase

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(8, 2))

n = 10**8
print(bin(n)[2:])  # 101111101011110000100000000
print(oct(n)[2:])  # 575360400
print(hex(n)[2:])  # 5f5e100

print(f'{n:b}')  # 101111101011110000100000000
print(f'{n:o}')  # 575360400
print(f'{n:X}')  # 5F5E100

print(convert(n, 2))  # 101111101011110000100000000
print(convert(n, 8))  # 575360400
print(convert(n, 16))  # 5F5E100
print(convert(n, 3))  # 20222011112012201
print(convert(n, 4))  # 11331132010000
'''


# № 21700 ЕГКР 19.04.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for n in range(3, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r <= 150:
        R.append(n)
print(max(R))
'''


# № 21474 (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

R = []
for n in range(1, 1000):
    s = convert(n, 6)
    if sum(map(int, s)) % 5 == 0:
        s = s.replace('0', '*').replace('3', '0').replace('*', '3')
        s = '11' + s
    else:
        s = s[0] + '05' + s[3:] + '44'
    r = int(s, 6)
    if r > 1500:
        if r == 1504:
            print(n)
        R.append(r)
print(min(R))
'''


def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]

print(convert(8, 2))

minim = 100000000
for n in range(1, 10000):
    s = convert(n, 3)
    if sum([int(i) for i in s]) % 4 == 0:
        s = '10' + s.replace('1', '*').replace('2', '1').replace('*', '2')
    else:
        s  = s[0]+ '02' + s[3:] + '20'
    r = int(s, 3)
    if r > 302:
        if r < minim:
            minim = r
        if r == minim:
            print(n)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 12, 15, 19-21]
# КЕГЭ = []
# на следующем уроке: 14, 17, 9, 18, 25 и 7, 11 повторить 8


