# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

'''
n = 17
b = 8
r = ''  # Пустая строка куда будем записывать результат
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)
'''

'''
n = 17
b = 8
r = ''  # Пустая строка куда будем записывать результат
while n > 0:
    # r += str(n % b)
    r = str(n % b) + r
    n //= b
print(r)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

n = int(input('Введите 10-е число для перевода: '))
b = int(input('Введите base систему счисления: '))
r = ''
while n > 0:
    r = alphabet[n % b] + r
    n //= b
print(f'Результат перевода: {r}')

print(f'Результат обратного перевода: {int(r, b)}')
'''


import time
from string import *
alphabet = digits + ascii_uppercase

# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в base систему счисления. \n'
                 'case 2: Перевод из base системы счисления в 10-ую \n'
                 'case 3: Перевод из base системы счисления в N-ую \n'
                 'case 0: Выход из программы. \n\n'
                 'case: ')
    if case == '1':
        b = int(input('Введите base систему счисления: '))
        n = int(input(f'Введите 10-е число для перевода в {b}-ую систему: '))
        r = ''
        while n > 0:
            r = alphabet[n % b] + r
            n //= b
        print(f'Результат перевода в {b}-ую систему: {r}')
        time.sleep(3)

    elif case == '2':
        b = int(input('Введите base систему счисления: '))
        r = input(f'Введите число в {b}-й системе счисления для перевода в 10-ую: ')
        print(f'Результат перевода: {int(r, b)}')
        time.sleep(3)

    elif case == '3':
        b = int(input('Введите base систему счисления: '))
        N = int(input('Введите N-ую систему счисления: '))
        r = input(f'Введите число в {b}-й системе счисления для перевода в {N}-ую: ')
        n = int(r, b)
        r = ''
        while n > 0:
            r = alphabet[n % N] + r
            n //= N
        print(f'Результат перевода в {N}-ую систему из {b}-ой системы: {r}')
        time.sleep(3)

    elif case == '0':
        print('Спасибо за использование нашей программы! ')
        break


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
