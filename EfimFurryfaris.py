# region Домашка: ************************************************************

'''
def F(x, a, b):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a <= x <= b
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))


A = []
B = [x / 4 for x in range(10 * 4, 30 * 4)]
for a in B:
    for b in B:
        if all(F(x, a, b) for x in B):
            A.append(b - a)
print(max(A))
'''


# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
M = []
for x in range(2031):
    n = 7 ** 91 + 7 ** 160 - x

    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    s = s[::-1]

    if s.count('0') == 70:
        M.append(x)

print(max(M))
'''

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Три способа создания функции перевода:
'''
# Базова примитивная функция перевода в b-ю систему (диапазон: 2 <= b <= 9)
def convert(n, b):  # n - число для перевода, b - система счисления
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


# Усовершенствованная функция перевода в b-ю систему (диапазон: 2 <= b <= 9)
def convert(n, b):  # n - число для перевода, b - система счисления
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r


# Лучший вариант функции перевода в b-ю систему (диапазон: 2 <= b <= 36)

from string import *
alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):  # n - число для перевода, b - система счисления
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


print(convert(123456789, 16))  # 75BCD15
print(int('75BCD15', 16))  # 123456789

# print(int('234', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0
'''

# ОБЗОР ВСТРОЕННЫХ ФУНКЦИЙ:
'''
n = 2560
print(bin(n)[2:])  # 101000000000
print(f'{n:b}')  # 101000000000

print(oct(n)[2:])  # 5000
print(f'{n:o}')  # 5000

print(hex(n)[2:])  # a00
print(f'{n:x}')  # a00
print(f'{n:X}')  # A00
'''


# № 18122 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):  # n - число для перевода, b - система счисления
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


maxi = 0
R = []
for x in range(5555+1):
    n = 5**150 + 5**135 - x
    s = convert(n, 5)

    if s.count('4') == 134:
        R.append(x)
print(max(R))
'''


# № 13910 (Уровень: Базовый)
'''
for p in range(32, 36+1):  # так как старшая цифра: U (31)
    if int('TH', p) + int('NQ', p) + int('U', p) == int('1L7', p):
        print(p)  # 33
'''

# № 13246 Открытый курс "Слово пацана" (Уровень: Средний)
# (М. Попков) В системе счисления с основанием p выполняется равенство
# 24x9p + yxy3p = x4y0p. Буквами x и y обозначены некоторые цифры
# из алфавита системы счисления с основанием p.
# Определите значение числа xyyp и запишите это значение в десятичной
# системе счисления.
'''
from string import *
alphabet = digits + ascii_uppercase

for p in range(10, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'24{x}9', p) + int(y+x+y+'3', p) == int(f'{x}4{y}0', p):
                print(int(x+y+y, p))
'''


# todo: № 18166 (Уровень: Средний)
# (К. Багдасарян) Значение арифметического выражения,
#  где х – натуральное число в диапазоне от 2 до 2025,
#  записали в системе счисления с основанием 5.
#  Определите максимальное значение x, при котором данная
#  запись содержит наибольшее количество цифр «4».
'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


maxi = 0
R = []
for x in range(2, 2025+1):
    n = 5**2025 + 5**200 - x
    s = convert(n, 5)


    if maxi <= s.count('4'):
        print(x, s.count('4'))
        maxi = s.count('4')
        R.append(x)
print(max(R))
'''


# № 13096 (Уровень: Средний)
# В числе 58x723y49_39 x и y обозначают некоторые цифры из алфавита системы счисления с основанием 39.
# Определите такие значения x и y, при которых приведённое число кратно 38,
# а число yx_39 является полным квадратом натурального числа.
# В ответе запишите значение числа yx_39 в десятичной системе счисления.
'''
def my_int(num: list, base):
    return sum([x*base**i for i, x in enumerate(num[::-1], 0)])


for x in range(39):
    for y in range(39):
        A = my_int([5, 8, x, 7, 2, 3, y, 4, 9], 39)
        if A % 38 == 0:
            R = my_int([y, x], 39)
            # if int(R ** 0.5) == R ** 0.5:
            if (R ** 0.5).is_integer():  # число является полным квадратом
                print(R)  # 1444
'''

'''
from itertools import *
n = 0
for i in product(sorted('МАРКСЛ'), repeat=6):
    s = ''.join(i)
    n += 1
    print(n, s)


from itertools import *
for n, i in enumerate(product(sorted('МАРКСЛ'), repeat=6), 1):
    s = ''.join(i)
    print(n, s)


for n, x in enumerate(['a', 'b', 'c', 'd', 'e'], 1):
    print(n, x)
    # 1 a
    # 2 b
    # 3 c
    # 4 d
    # 5 e
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************




# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14, 15, 16?, 17, 19-21?, 23]
# КЕГЭ = []
# на следующем уроке:
