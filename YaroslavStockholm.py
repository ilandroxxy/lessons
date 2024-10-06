# region Домашка: ******************************************************************

'''
m = int(input())
product = 1
for i in range(1, m + 1):
    if m % i == 0:
        # product = product * i
        product *= i
print(product)


from math import prod
m = int(input())
R = []
for i in range(1, m + 1):
    if m % i == 0:
        # product = product * i
        R.append(i)
print(prod(R))
'''

'''
x = 5
x += 5
print(x)  # 10

x *= 2
print(x)  # 20

x //= 2
print(x)  # 10
'''


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet)

n = 1234
print(n % 10)  # 4
n //= 10  # 123
print(n % 10)  # 3
n //= 10  # 12
print(n % 10)  # 2
n //= 10  # 1
print(n % 10)  # 1
'''

'''
n = int(input())
count = 0
summa = 0
product = 1
while n > 0:
    x = n % 10
    count += 1
    summa += x
    product *= x
    n //= 10
print(summa)
print(count)
print(product)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from random import randint, choice
from time import sleep

messages_error = [
    "Неправильный пароль, попробуйте снова: ",
    "Пароль введен неверно, повторите попытку: ",
    "Ошибка пароля, введите заново: ",
    "Пароль не подходит, попробуйте ещё раз: ",
    "Некорректный пароль, повторите ввод: ",
    "Пароль неверен, введите снова: ",
    "Пароль ошибочный, повторите попытку: ",
    "Введен неверный пароль, попробуйте ещё раз: ",
    "Пароль не распознан, введите заново: ",
    "Неправильный пароль, введите ещё раз: "
]

user = 'Женя'
password = 'qwerty'


pas = input('Введите пароль: ')
cnt = 0
while True:
    if pas == password:
        print('Пароль верный!', end=' ')
        break
    else:
        cnt += 1
        if cnt == 3:
            print('Пройдите проверку на робота решив пример.')
            a = randint(0, 100)
            b = randint(0, 100)
            x = int(input(f'{a} + {b} = '))
            if x == a + b:
                print('Проверка пройдена успешно.')
                cnt = 0
            else:
                print('Проверка не пройдена \n'
                      'Повторите попытку через 5 минут.')
                sleep(5 * 60)

        pas = input(choice(messages_error))

print(f'Добро пожаловать, {user}.')
# Пароль верный! Добро пожаловать, Женя.
'''


# Функция перевода в различные системы счисления
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


x = convert(123456789, 16)
print(x)  # 75BCD15
print(int(x, 16))  # 123456789
'''

'''
from string import digits, ascii_uppercase


alphabet = digits + ascii_uppercase
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


while True:
    case = int(input(f'\n'
                     f'case 1: Перевод из 10-й в b-ю систему \n'
                     f'case 2: Перевод из b-й в 10-ю систему \n'
                     f'case 3: Перевод из b-й в k-ю систему \n'
                     f'case 0: Выход из программы.\n'
                     f'case: '))

    if case == 1:
        n = int(input('Введите число в 10-й системе: '))
        b = int(input('Введите систему счисления для перевода: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} из 10-й в {b}-ю систему: {r}')

    elif case == 2:
        b = int(input('Введите систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Перевод числа {r} из {b}-й системы в 10-ю: {n}')

    elif case == 3:
        b = int(input('Введите систему счисления b: '))
        r = input(f'Введите число в {b}-й системе: ')
        k = int(input('Введите систему счисления k: '))
        n = int(r, b)  # Перевод числа r (в строчном виде) из b-й в 10-ю систему
        new_r = convert(n, k)
        print(f'Результат перевода числа {r} из {b}-й системы счисления в {k}-ю систему: {new_r}')

    elif case == 0:
        print('Спасибо, что пользовались нашим калькулятором!')
        break

    else:
        print('Эта команда мне не ясна, воспользуйтесь командами: 1, 2, 3, 0')
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
