# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Цикл for отвечает на запросы: "повтори N раз", "пробежать от А до В"

# Цикл for с функцией range()
'''
# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(3, 10, 3):
    print(i, end=' ')  # 3 6 9
print()

n = 10
for i in range(2, n+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Цикл for с последовательностями
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
print(len(M))  # 5

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Цикл while отвечает на запросы: "пока условие верное - делаем действие", "бесконечный цикл"

'''
n = 10
for i in range(2, n+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2  # i = i + 2
print()
'''

'''
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b  # n = n // b
print(r)  # 1000

b = 2
print(int('1000', b))  # 8
'''

# Универсальная функция перевода в различные системы счисления
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(8, 2))  # 1000
print(convert(8, 3))  # 22
print(convert(10**8, 16))  # 5F5E100


print(int('1000', 2))  # 8
# ValueError: int() base must be >= 2 and <= 36, or 0
'''


# Бесконечный цикл и операторы: break, continue, exit()
'''
k = 0
while True:
     k += 1
     if k % 2 != 0:
         continue  # Прерывает шаг итерации цикла 
     if k == 50_000:
         break  # Прерывает выполнение цикла в котором лежит
     if k == 25_000:
         exit()  # Прерывает полностью выполнение программы
     print(k)

print('Продолжение программы')
'''


# Простая консольная программа по переводу в различные системы счисления
'''
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase
# '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему \n'
                 'case 2: Перевод из b-й в 10-ю систему \n'
                 'case 3: Перевод из b-й в k-ю систему \n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите 10-е число для перевода: '))
        b = int(input('Введите b-ю систему счисления: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} в {b}-ю систему: {r}')

    elif case == '2':
        b = int(input('Введите b-ю систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-й системы: {n}')


    elif case == '3':
        b = int(input('Введите b-ю систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        k = int(input('Введите k-ю систему счисления: '))
        n = int(r, b)
        new_r = convert(n, k)
        print(f'Результат перевода числа {r} из {b}-й системы в {k}-ю: {new_r}')


    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        break

    else:
        print('Я понимаю только команды 1, 2, 3, 0.')
'''


# Проверка паролей

from random import randint
import time

password = 'qwerty'
pas = input('Введите пароль: ')
count = 0
while True:
    count += 1
    if pas == password:
        print('Пароль верный.')
        break
    else:
        if count == 3:
            print('Проверка на робота!')
            a = randint(0, 100)
            b = randint(0, 100)
            x = int(input(f'Решите пример: {a} + {b} = '))
            if x == a + b:
                print('Проверка пройдена успешно.')
                count = 0
            else:
                print('Повторите попытку через 5 минут.')
                time.sleep(5 * 60)

        pas = input('Пароль неверный, повторите попытку: ')

print('Добро пожаловать в программу!')

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Должен +10 минут
