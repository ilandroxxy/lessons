# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# № 21415 Досрочная волна 2025 (Уровень: Базовый)
'''
F = [0] * 2500
for n in range(1, 2500):
    if n <= 5:
        F[n] = 1
    if n > 5:
        F[n] = n + F[n - 2]

print(F[2126] - F[2122])
'''


# № 21711 ЕГКР 19.04.25 (Уровень: Базовый)

# Вариант 1
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)
    
print((F(47872) - 290 * F(47858)) / F(47858))
'''


# Вариант 2
'''
from functools import *
@lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)

for n in range(50000):
    F(n)

print((F(47872) - 290 * F(47858)) / F(47858))
'''


# Вариант 3
'''
F = [0] * 50000
for n in range(1, 50000):
    if n < 20:
        F[n] = n
    if n >= 20:
        F[n] = (n - 6) * F[n - 7]

print((F[47872] - 290 * F[47858]) / F[47858])
'''


# № 23756 Демоверсия 2026 (Уровень: Базовый)
'''
F = [0] * 16000
G = [0] * 16000

for m in range(1, 16000):
    if m < 10:
        G[m] = 2 * m
    if m >= 10:
        G[m] = G[m - 2] + 1

for n in range(1, 16000):
    F[n] = 2 * (G[n - 3] + 8)

print(F[15548])
'''


# todo: № 25355 (Уровень: Базовый)
'''
F = [0] * 800
G = [0] * 250000

for m in range(1, 250000):
    if m >= 248045:
        G[m] = m / 20 + 28
    if m < 248045:
        G[m] = G[m + 9] - 4

for n in range(1, 800):
    if n >= 19:
        F[n] = F[n - 4] + 3580
    if n < 19:
        F[n] = 6 * (G[n - 7] - 36)

print(F[673])
'''




# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 3 раза.

s = 'xxTxxxxxTxTxxxxxTxxxTxxxxxxxTxxxxxx'
# ['xx', 'xxxxx', 'x', 'xxxxx', 'xxx', 'xxxxxxx', 'xxxxxx']

# ['xx', 'xxxxx', 'x', 'xxxxx']
# ['xxxxx', 'x', 'xxxxx', 'xxx']
# ['x', 'xxxxx', 'xxx', 'xxxxxxx']
# ['xxxxx', 'xxx', 'xxxxxxx', 'xxxxxx']

# 16 xxTxxxxxTxTxxxxx
# 17 xxxxxTxTxxxxxTxxx
# 19 xTxxxxxTxxxTxxxxxxx
# 24 xxxxxTxxxTxxxxxxxTxxxxxx
'''
s = 'xxTxxxxxTxTxxxxxTxxxTxxxxxxxTxxxxxx'
maxi = 0
s = s.split('T')
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
print(maxi)  # 24
'''

# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 4 раза.

s = 'xxTxxxxxTxTxxxxxTxxxTxxxxxxxTxxxxxx'
# ['xx', 'xxxxx', 'x', 'xxxxx', 'xxx', 'xxxxxxx', 'xxxxxx']

# ['xx', 'xxxxx', 'x', 'xxxxx', 'xxx']
# ['xxxxx', 'x', 'xxxxx', 'xxx', 'xxxxxxx']
# ['x', 'xxxxx', 'xxx', 'xxxxxxx', 'xxxxxx']

# 20 xxTxxxxxTxTxxxxxTxxx
# 25 xxxxxTxTxxxxxTxxxTxxxxxxx
# 26 xTxxxxxTxxxTxxxxxxxTxxxxxx
'''
s = 'xxTxxxxxTxTxxxxxTxxxTxxxxxxxTxxxxxx'
maxi = 0
s = s.split('T')
for i in range(len(s)-4):
    r = 'T'.join(s[i:i+5])
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)  # 26
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)  # 133
'''


# № 13715 (Уровень: Средний)
# Текстовый файл состоит из символов A, B, C, D и E.
# Определите в прилагаемом файле максимальное количество идущих
# подряд символов, среди которых комбинация символов AB встречается ровно 50 раз.
'''
s = open('files/24.txt').readline()
s = s.split('AB')
maxi = 0
for i in range(len(s)-50):
    r = 'B' + 'AB'.join(s[i:i+51]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)  
'''

# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
#
# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в прилагаемом файле максимальное количество
# идущих подряд символов, среди которых подстрока FSRQ встречается ровно 80 раз.
'''
s = open('files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)  
'''


# № 19489 (Уровень: Средний)
# (Л. Шастин) Текстовый файл состоит из символов F, S и W.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов, среди которых подстрока WWF встречается не более 120 раз,
# а подстрока WSFWW не встречается совсем.
'''
s = open('files/24.txt').readline()
s = s.split('WWF')
maxi = 0
for i in range(len(s)-120):
    r = 'WWF'.join(s[i:i+121])
    for x in r.split('WSFWW'):
        maxi = max(maxi, len(x))
print(maxi)
'''
# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: Минимальное количество идущих подряд
