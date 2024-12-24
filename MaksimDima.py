# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задача 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


M = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        M.append(n)

print(max(M))
'''


# Задача 7
'''
# 1 бит - минимальная единица измерения информации 
# 1 байт - 8 бит - 2**3 бит 
# 1 Кбайт - 1024 байт - 2**10 байт - 2**13 бит 
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит 
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит 

# bit (бит) = a (каналов) * b (гц) * c (бит) * t (сек)

a = 2
b = 48000
c = 24
# t - ? сек
bit = 288 * 2**23  # 2**10 кбайт * 2**10 байт * 2**3 бит

t = bit / (a * b * c)
print(t / 60)  # 1048.576 сек  ->  17.4762 мин
'''

# Задача 8
'''
from itertools import *
cnt = 0
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in '02468ACE':
            num = num.replace(x, '2')
        for x in '13579BDF':
            num = num.replace(x, '1')
        if '11' not in num and '22' not in num:
            cnt += 1
print(cnt)


from itertools import *
cnt = 0
s2 = '02468ACE'
s1 = '13579BDF'
for p in permutations('0123456789ABCDEF', r=3):
    n = ''.join(p)
    if n[0] != '0':
        if n[0] in s2 and n[1] in s1 and n[2] in s2:
            cnt += 1
        if n[0] in s1 and n[1] in s2 and n[2] in s1:
            cnt += 1
print(cnt)
'''

# Задача 11
'''
symbols = 10
alphabet = 52  # alphabet = 2 ** i, где i это кол-во бит на один символ
i = 6  # alphabet <= 2 ** 6
bit = symbols * i
print(bit / 8)  # 7.5 -> 8

byte = 8  # на один пароль

byte_all = 65536 * byte
print(byte_all / 2**10)
'''
# Ответ: 512


# Задача 12
'''
for n in range(4, 10000):
    s = '1' + '8'*n
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    if s.count('1') == 3:
        print(n)
        exit()
'''

# Задача 13
'''
from ipaddress import *
for m in range(33):  # m - кол-во единица
    # длина маски 32 бита
    # кол-во нулей это 32 - m
    net = ip_network(f'213.168.83.190/{m}', 0)
    if '213.168.64.0' in str(net):
        print(m, 32 - m)
'''


# Задача 23
'''
def F(a, b):
    if a <= b or a == 7:
        return a == b
    return F(a-1, b) + F(a-3, b) + F(a//2, b)


print(F(19, 10) * F(10, 3))
'''

# Задача 25
'''
from fnmatch import *
for i in range(2025, 10**8+1, 2025):
    if fnmatch(str(i), '12*34?5'):
        print(i, i // 2025)
'''


# Задача 1
'''
from itertools import *
print('1 2 3 4 5 6 7')
table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
graph = 'GD DG GE EG DE ED DF FD FA AF AC CA AB BA BC CB CE EC'
for p in permutations('ABCDEFG'):
    new_table = table
    #   1    2    3    4    5    6    7
    # ('G', 'F', 'E', 'D', 'A', 'C', 'B')
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7
# C G B E D A F
# E B G C A D F


# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
# Вариант 1

def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)

for A in range(0, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break

# Вариант 2

def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)

for A in range(0, 1000):
    k = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == True:
                k += 1
    if k == 9801:
        print(A)
        break


# Вариант 3
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


R = []
for A in range(0, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))

# Вариант 4

print(min([A for A in range(0, 1000) if all( ((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100))]))
'''


# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''


# № 14655 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
def F(x, A):
    return (x & A != 0) <= ((x & 168 == 0) <= (x & 69 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 14352 (Уровень: Базовый)
'''
def F(x, A):
    B = 120 <= x <= 180
    return (x % A == 0) or (B <= ((x % 16 != 0) or (x + A <= 204)))


for A in range(1, 10000):  # 999
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 14349 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    A = a1 <= x <= a2
    return C <= ((B and (not A)) <= (not C))


R = []
M = [x / 4 for x in range(50 * 4, 160 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(min(R))  # 42.0, 42.25 -> 42, 42.5/42.75 -> 43
'''


# № 13895 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 34 <= x <= 72
    C = 32 <= x <= 61
    A = a1 <= x <= a2
    return (B <= A) and ((not C) or A)


R = []
M = [x / 4 for x in range(30 * 4, 80 * 4)]

for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(min(R))
'''


# № 18489 (Уровень: Базовый)
'''
def cif(x, y):
    return str(x)[-1] == str(y)[-1]


def F(x, A):
    return ((not cif(x, 5)) and cif(x, 4)) <= (x > A - 11)


for A in range(1, 1000):
    if all(F(x, A)  for x in range(1, 10000)):
        print(A)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]
