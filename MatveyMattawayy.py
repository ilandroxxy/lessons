# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def F(x, A):
    B = 50 <= x <= 70
    return (x % A == 0) or (B <= (x % 16 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 17546 Основная волна 08.06.24 (Уровень: Базовый)
'''
# На вход алгоритма подаётся натуральное число N
R = []
for n in range(1, 12+1):

    # 1. Строится двоичная запись числа N.
    s = f'{n:b}'  # s = bin(n)[2:]

    # а) если число чётное, то к двоичной записи слева дописывается 10;
    if n % 2 == 0:
        s = '10' + s

    # б) если число нечётное, то к двоичной записи слева дописывается 1 и справа дописывается 01.
    else:
        s = '1' + s + '01'

    # 3. Результат переводится в десятичную систему и выводится на экран.
    r = int(s, 2)
    R.append(r)

print(max(R))
'''


'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]
'''

'''
import string
alphabet = string.digits + string.ascii_uppercase
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''


'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r
'''


# Найдите сумму цифр строки:
summa = sum(map(int, '12345'))


'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r


for n in range(1, 1000):
    s = convert(n, 2)
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if r > 50:
        print(n)
        break
'''

# № 11478 (Уровень: Базовый)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1, 10000):
    s = convert(n, 3)
    if n % 2 == 0:
        s = '1' + s + '00'
    else:
        s = s + convert(s.count('1') + s.count('2' * 2), 3)
    r = int(s, 3)
    if r > 168:
        print(n)
        break
'''

'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:27]:
    a = int(f'123{x}24',27) + int(f'135{x}78',27)
    if a % 26 == 0:
        print(x, a//26)
'''

# № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
'''
s = 4 * 3125**2019 + 3 * 625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
b = []
while s > 0:
    b = [s % 25] + b
    s //= 25
print(len([i for i in b if i > 10]))
'''

# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
for x in range(2030+1):
    s = 7**91 + 7**160 - x
    b = []
    while s > 0:
        b = [s % 7] + b
        s //= 7
    if b.count(0) == 70:
        print(x)
'''

'''
for x in range(2030+1):
    s = 3 ** 100 - x
    b = []
    while s > 0:
        b = [s % 3] + b
        s //= 3
    if b.count(0) == 5:
        print(x)
'''

R = []
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum(map(int, s))
    R.append(summa)
    print(max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5*, 6, 7, 8*, 12*, 14*, 16, 18, 19-21]
# КЕГЭ  = [5, 14, 15, 23]
# на следующем уроке: 9, 11, 13, 25
