# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 21891 Открытый вариант 2025 (Уровень: Базовый)
'''
for n in range(1, 1000):
    # s = bin(n)[2:]
    s = f'{n:b}'
    for _ in range(2):
        s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 253:
        print(n)
        break
'''


# Про системы счисления
'''
n = 10**8
print(bin(n)[2:])
print(oct(n)[2:])
print(hex(n)[2:])

print(f'{n:b}')
print(f'{n:o}')
print(f'{n:x}')


from string import *
alp = digits + ascii_uppercase

# alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

print(convert(n, 2))
print(convert(n, 8))
print(convert(n, 16))
'''

'''
from string import *
alp = digits + ascii_uppercase

# alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for n in range(1, 1000):
    # s = bin(n)[2:]
    s = f'{n:b}'
    for _ in range(2):
        s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 253:
        print(n)
        break
'''


# № 21700 ЕГКР 19.04.25 (Уровень: Базовый)

from string import *
alp = digits + ascii_uppercase

# alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for n in range(3, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r <= 150:
        print(n)




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
