# region Домашка: ******************************************************************


# № 12923  (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


s = 3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024
s = convert(s, 25)
print(s.count('0'))
'''


# № 17633 Основная волна 19.06.24 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


R = []
for x in range(1, 2030+1):
    s = 6**260 + 6**160 + 6**60 - x
    s = convert(s, 6)
    if s.count('0') == 202:
        print(x)
        break
'''


# № 12246 ЕГКР 16.12.23 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


# c = 0
n = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
r = convert(n, 9)
print(len(r) - r.count('0'))

# for i in range(len(r)):
#     if r[i] != '0':
#         c += 1
# print(c)
'''


# № 11663 (Уровень: Базовый)
'''
Z = []
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:27]:
    A = int(f'17{x}35', 27)
    B = int(f'{x}742M', 27)
    C = int(x, 27) ** 3
    if (A + B + C) % 23 == 0:
        Z.append((A + B + C) // 23)
print(max(Z))
'''

# Пример перевода из 2-й в 10-ю
'''
# i  0  1  2  3
L = [1, 0, 0, 0]
b = 2
summa = 0
for i, x in enumerate(L[::-1], 0):
    print(i, x)
    summa += x * b ** i
print(summa)
'''


# Универсальная функция перевода из b-ой системы в n-ую
'''
def my_int(L: list, b: int):
    return sum(x * b ** i for i, x in enumerate(L[::-1], 0))


n = 8
print(bin(n)[2:])
print(int('1000', 2))
print(my_int([1, 0, 0, 0], 2))
'''

# A = int(f'73{x}1{y}', 67)
# ValueError: int() base must be >= 2 and <= 36, or 0

'''
def my_int(L: list, b: int):
    return sum(x * b ** i for i, x in enumerate(L[::-1], 0))


R = []
for x in range(10, 67):
    for y in range(0, x):
        A = my_int([7, 3, x, 1, y], 67)
        B = my_int([4, 9, y, 6], x)
        R.append(A + B)
print(len(set(R)))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20801 Апробация 05.03.25 (Уровень: Базовый)
'''
from itertools import permutations
print('1 2 3 4 5 6 7')
table = '12 16 21 24 27 34 35 36 42 43 47 53 57 61 63 72 74 75'
graph = 'AC CA AE EA CF FC CG GC GB BG GF FG FE EF ED DE DB BD'
for p in permutations('ACBDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7
# B G E F A D C


# № 18308 (Уровень: Базовый)
'''
from itertools import permutations
print('1 2 3 4 5 6 7 8 9')
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KC CK BK KB CD DC BD DB DH HD DG GD DE ED EF FE FG GF GH HG'
for p in permutations('ACBDEFGKH'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7 8 9
# C G B D K A E F H
# B G C D K A E F H

# FE: 8, ED: 15
# FE + ED = 23

'''
from itertools import permutations
print('1 2 3 4 5 6 7')
table = '14 15 17 25 26 27 34 35 41 43 46 51 52 53 62 64 67 71 72 76'
graph = 'AB BA AF FA FE EF EG GE EC CE GB BG CB BC CD DC FD DF AD DA'
for p in permutations('ACBDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
#1 2 3 4 5 6 7
#C A G E B F D
#C F G B E A D
# A + F = 2, D + C = 8 => 8 + 2 = 10

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
