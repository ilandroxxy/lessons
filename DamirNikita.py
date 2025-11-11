# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
n = 8

# Перевод в двоичную систему счисления
print(bin(n)[2:])  # 1000
print(f'{n:b}')  # 1000
print(int('1000', 2))  # 8

# Перевод в восьмеричную систему счисления
print(oct(n)[2:])  # 10
print(f'{n:o}')  # 10
print(int('10', 8))  # 8

# Перевод в шестнадцатеричную систему счисления
print(hex(n)[2:])  # 8
print(f'{n:x}')  # 8
print(int('8', 16))  # 8

# ValueError: int() base must be >= 2 and <= 36, or 0


def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
'''


# № 24886 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]  # s = f'{n:b}'
    if n % 5 == 0:
        s = s + '11'
    else:
        x = n // 5
        s = s + bin(x)[2:]
    r = int(s, 2)
    if n % 2 == 0 and r > 896:
        RES.append(n)
print(min(RES))
'''


# № 23742 Демоверсия 2026 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + f'{x:b}'
    r = int(s, 2)
    if r >= 200:
        RES.append(n)
print(min(RES))
'''


# № 23364 Резервный день 19.06.25 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 100:
        RES.append(n)
print(max(RES))
'''


# № 22456 (Уровень: Базовый)22456
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = '11' + s[2:] + "1"
    else:
        if s.count('0') < s.count('1'):
            s = s + '0'
        else:
            s = s + '1'
    r = int(s, 2)
    if r >= 271:
        RES.append(n)
print(min(RES))
'''

# № 23189 Основная волна 10.06.25 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r < 130:
        RES.append(n)
print(max(RES))
'''

# № 21700 ЕГКР 19.04.25 (Уровень: Базовый)
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r <= 150:
        RES.append(n)
print(max(RES))
'''



# № 16371 ЕГКР 27.04.24 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    s=bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r >= 195:
        RES.append(r)
print(min(RES))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5]
# КЕГЭ = []
# на следующем уроке:
