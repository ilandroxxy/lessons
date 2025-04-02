# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#
# № 7264 OpenFIPI (Уровень: Базовый)
'''
n = 343**515 - 6*49**520 + 5*49**510 - 3*7**530 - 550
R = []
while n > 0:
    R.append(n % 7)
    n //= 7
R.reverse()
print(R.count(6))
'''

'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

n = 343**515 - 6*49**520 + 5*49**510 - 3*7**530 - 550
print(convert(n, 7).count('6'))
'''


# № 20904 Апробация 05.03.25 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for x in range(1, 2030):
    n  = 3**100 - x
    s = convert(n, 3)
    if s.count('0') == 1:
        print(x)
'''


# № 20808 Апробация 05.03.25 (Уровень: Средний)
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


R = []
for x in range(1, 2030):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    R.append([s.count('0'), x])

print(max(R))
'''
# [73, 1715]


# № 19359 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

for x in alphabet[:22]:
    A = int(f'A23{x}AC0', 22)
    B = int(f'GB{x}21670', 22)
    if (A + B) % 21 == 0:
        print((A + B) // 22)
'''

'''
Z = []
for x in range(1, 2031):
    s = 7**91 + 7**160 - x

    R = []
    while s > 0:
        R.append(s%7)
        s//=7
    R = R[::-1]
    if R.count(0) == 70:
        Z.append(x)
        print(x)
print(max(Z))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ = []
# на следующем уроке: ТИ решение кодом

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


