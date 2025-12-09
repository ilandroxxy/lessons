# region Домашка: ******************************************************************

# Номер 8
'''
cnt = 0
from itertools import permutations
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        chet = '02468ACE'
        nechet = '13579BDF'
        if (num[0] in chet and num[1] in nechet and num[2] in chet) or (num[0] in nechet and num[1] in chet and num[2] in nechet):
            cnt += 1
print(cnt)


cnt = 0
from itertools import permutations
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
'''


# Номер 5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

RES = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        RES.append(n)
print(max(RES))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Таблица измерения единиц информации (101010101001011 бит)
# 1 бит - минимальная единица измерения информации
# 1 байт - 8 бит - 2**3 бит
# 1 Кбайт - 1024 байт - 2**10 байт - 2**13 бит
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит


# Три типа задач 11 номера
# 1. sym, alp = byte
# 2. sym, byte = alp
# 3. alp, byte = sym


# Номер 11 (первый прототип - 1. sym, alp = byte)
'''
sym = 10
alp = 52   # alp <= 2**i

# i - это кол-во бит выделяемых на один символ
i = 6   #  2**6 = 64 >= alp

bit = sym * i
print(bit)  # 60 бит на один пароль

print(bit / 8)  # 7.5 -> 8
byte = 8  # 8 байт на один пароль

print((byte * 65_536) / 2**10)
'''


# https://education.yandex.ru/ege/inf/task/30431c9e-dfcf-41dc-8b5d-1c0fd87fcb2e
# (первый прототип - 1. sym, alp = byte)
'''
sym = 31
alp = 10 + 26
i = 6  # 2**6 >= alp

bit = sym * i
print(bit / 8)  # 23.25 -> 24
byte = 24

# user = byte + dop

user = (12 * 2**10) / 128
print(user - byte)  # 72
'''


# https://education.yandex.ru/ege/inf/task/a4132687-04dc-4ed6-85e0-76ebd94d668a
# (второй прототип - 2. sym, byte = alp)
'''
sym = 197

byte = (25 * 2**20) / 178_080
print(byte)  # 147.2057 -> 148 (отведено более 25 Мбайт памяти)
bit = 148 * 8

i = bit / sym
print(i)  # 6.0101 -> 7 (отведено более 25 Мбайт памяти)

print(f'Определите максимальную возможную мощность алфавита: {2**7}')
print(f'Определите минимально возможную мощность алфавита: {2**6+1}')

alp = 129  # i = 8

alp = 128  # i = 7
alp = 64  # i = 6

alp = 65  # i = 7
'''


# https://education.yandex.ru/ege/inf/task/b7bccef2-d2fe-4064-8fcd-69ea6cd792c2
# (второй прототип - 2. sym, byte = alp)
'''
sym = 172

byte = 54 * 2**20 / 356_984
print(byte)  # 158.6152 -> 159 (потребовалось не менее 54 Мбайт памяти)
bit = 159 * 8

i = bit / sym
print(i)  # 7.395 -> 8 (потребовалось не менее 54 Мбайт памяти)

print(f'Определите максимальную возможную мощность алфавита: {2**8}')
print(f'Определите минимально возможную мощность алфавита: {2**7+1}')
'''


# https://education.yandex.ru/ege/inf/task/90b2bc03-59cf-406d-b7b5-e2bca0b8580a
# (третий прототип - 3. alp, byte = sym)
'''
alp = 10 + 27
i = 6

byte = 12 * 2**10 / 3548
print(byte)  # 3.4633 -> 4 (необходимо более 12 Кбайт памяти)
bit = 4 * 8

sym = bit / i
print(sym)  # 5.3333 -> 5
'''

# endregion Урок: *************************************************************
#
# ФИПИ = [1, 2, 5, 6, 8, 11, 13, 14, 15, 16, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: + 10 минут, 7 номер, 17, 9, 27
