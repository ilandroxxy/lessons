# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# № 20808 Апробация 05.03.25 (Уровень: Средний)
'''
# from string import *
# alphabet = digits + ascii_uppercase

def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


maxi = 0
for x in range(1, 2030):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if maxi <= s.count('0'):
        maxi = s.count('0')
        print(maxi, x)
'''


# № 20486 (Уровень: Базовый)
'''
def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


R = []
for n in range(4, 1000):
    # s = bin(n)[2:]
    # s = f'{n:b}'
    s = convert(n, 2)
    if n % 2 == 0:
        s = s + s[:2+1]
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if r > 600:
        R.append(r)
print(min(R))
'''


# № 20182 (Уровень: Базовый)
'''
def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for n in range(1, 1000):
    s = convert(n, 3)
    summa = sum([int(x) for x in s])
    if summa % 2 == 0:
        s = '12' + s[2:] + '0'
    else:
        s = '10' + s[2:] + '2'
    r = int(s, 3)
    if r  > 105:
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Михаил 8/18 -> 46 вторичных баллов +[2, 4, 6, 12, 14, 15, 16, 23] -[1, 3, 5, 7, 8, 9, 11, 13, 17, 25]

# Второй пробник 28.02.25:
# Михаил 17/29 -> 70 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-16, 18, 19-20, 23, 25] -[5, 7, 10, 13, 17, 21, 22, 24]
# Егор _/29 -> _ вторичных баллов +[] -[]
