# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************




# Пример работы f-строки
'''
name = input('Введите свое имя: ')
print('Имя пользователя:', name)
print(f'Имя пользователя: {name}')
'''
from pydoc import apropos

"""
''' Привет, Илья! Сегодня облачно, а температура 24 градуса! '''

from random import choice
name = input('Введите свое имя: ')
weather = choice(['облачно', 'мрачно', 'солнечно'])
print('Сегодня погода:', weather)
temperature = int(input('Введите температуру: '))

print('Привет, ', name, '! Сегодня ', weather, ', а температура ', temperature, ' градуса!')
print('Привет, ' + name + '! Сегодня ' + weather + ', а температура ' + str(temperature) + ' градуса!')
print('Привет, {}! Сегодня {}, а температура {} градуса!'.format(name, weather, temperature))
print(f'Привет, {name}! Сегодня {weather}, а температура {temperature} градуса!')
"""


# Функции перевода в различные системы счисления
'''
# Перевод в двоичную запись
n = 8
print(bin(n)[2:])  # 1000
print(f'{n:b}')  # 1000
print(int('1000', 2))  # 8 - Перевод из 2-й в 10-ю

# Перевод в восьмеричную запись
n = 8
print(oct(n)[2:])  # 10
print(f'{n:o}')  # 10
print(int('10', 8))  # 8 - Перевод из 8-й в 10-ю

# Перевод в шестнадцатеричная запись
n = 10**8
print(hex(n)[2:])  # 5f5e100
print(f'{n:x}')  # 5f5e100
print(f'{n:X}')  # 5F5E100
print(int('5F5E100', 16))  # 10**8 - Перевод из 16-й в 10-ю
# ValueError: int() base must be >= 2 and <= 36, or 0
'''

# Своя функция перевода из 10-й в b-ю систему
'''
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase

# alp = '0123456789ABCDE...'

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b  # n = n // b
    return r

print(convert(8, 2))  # 1000
print(convert(8, 3))  # 22
print(convert(10**8, 16))  # 5F5E100
'''


# № 23364 Резервный день 19.06.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

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


# № 23742 Демоверсия 2026 (Уровень: Базовый)
'''
RES = []
for n in range(1, 10000):
    # s = convert(n, 2)
    # s = bin(n)[2:]
    s = f'{n:b}'
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

'''
a, b = 7, 2
a, b = b, a
print(a, b)  # 2 7

# Замена через третью переменную
# 2 -> 3, 3 -> 2
s = '1231232313212323'  
s = s.replace('2', '*')
print(s)  # 1*31*3*313*1*3*3
s = s.replace('3', '2')
print(s)  # 1*21*2*212*1*2*2
s = s.replace('*', '3')
print(s)  # 1321323212313232
'''


# № 22272 (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for n in range(1, 10000):
    s = convert(n, 9)
    if s[0] == '7':
        s = s.replace('6', '*')
        s = s.replace('3', '6')
        s = s.replace('*', '3')
        s = s + '34'
    else:
        # s = '3' + s + '45'  # дописать
        s = '3' + s[1:] + '45'  # заменить
    r = int(s, 9)
    if r < 2876:  # 2795
        RES.append([r, n])
print(max(RES))  # [2795, 79]
'''


# № 19237 ЕГКР 21.12.24 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        summa = s.count('1') + s.count('2') * 2
        s = s + convert(summa, 3)
    r = int(s, 3)
    if r > 220 and r % 2 == 0:
        RES.append(r)
print(min(RES))
'''


# Вычисляется сумма цифр полученной троичной записи
'''
s = '1298712349847'

summa = 0
for x in s:
    summa += int(x)
open(summa)

summa = sum([int(x) for x in s])

summa = sum(map(int, s))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5]
# КЕГЭ = []
# на следующем уроке:
