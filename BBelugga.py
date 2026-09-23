# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 31502 Демоверсия 2027(Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    # n2 = bin(n)[2:]
    n2 = f'{n:b}'
    if n % 2 == 0:
        n2 = '11' + n2 + '11'
    else:
        n2 = '1' + n2 + '00'
    r = int(n2, 2)
    if r > 95:
        RES.append(r)
print(min(RES))
'''

# № 31351 Пересдача 08.07.26(Уровень: Базовый)
'''
RES = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    # if n2.count('1') % 2 == 0:
    if sum(map(int, n2)) % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2, 2)
    if r >= 16:
        RES.append(n)
print(min(RES))
'''


# Способы подключения библиотек
'''
import math
print(math.sqrt(16))


import math as m  # Подключение библиотеки с коротким именем (сове имя)
print(m.sqrt(16))


from math import sqrt, fabs, factorial  # Подключаем только необходимое
print(sqrt(16))


from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(factorial(5))


count = 0
from itertools import product, permutations
for p in permutations('abc'):
    count += 1
    print(count, p)

count = 0
from itertools import *
for p in permutations('abc'):
    count += 1
    print(count, p)
# TypeError: unsupported operand type(s) for +=: 'type' and 'int'
'''


# Функция перевода в различные системы счисления (ВЫУЧИТЬ)
'''
from string import *
alp = digits + ascii_uppercase
print(alp[:8])  # 01234567

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']


alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(8, 2))
print(convert(10**8, 16))  # 5F5E100
print(int('5F5E100', 16))  # 100000000
'''


# № 29956 Апробация 14.05.26(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for n in range(1, 1000):
    n3 = convert(n, 3)
    if n % 3 == 0:
        n3 = '1' + n3 + '02'
    else:
        x = (n % 3) * 5
        n3 = n3 + convert(x, 3)
    r = int(n3, 3)
    if r >= 177:
        RES.append(n)
print(min(RES))
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5]
# КЕГЭ = []
# на следующем уроке:



