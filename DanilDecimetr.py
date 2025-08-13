# region Домашка: ******************************************************************

# https://stepik.org/lesson/1309432/step/11?unit=1324548

# "Ночь" — если время с 00:00 до 05:29.
# "Утро" — если время с 05:30 до 12:14.
# "День" — если время с 12:15 до 17:44.
# "Вечер" — если время с 17:45 до 23:59.
'''
H = int(input())
M = int(input())

if 0 <= H <= 4:
    print('Ночь')
elif H == 5:
    if 0 <= M <= 29:
        print('Ночь')
    else:
        print('Утро')
elif 6 <= H <= 11:
    print('Утро')
elif H == 12:
    if 0 <= M <= 14:
        print('Утром')
    else:
        print('День')
elif 13 <= H <= 16:
    print('День')
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори 5 раз", "пробеги от 10 до 100", "пробеги элементы списка"


# Работа цикла for с функцией range()
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

for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Работа цикла for с последовательностями (list, str, tuple, ...)
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
T = ('a', 'b', 'c', 'd', 'e')
s = 'abcde'

print(len(L))  # 5 - Возвращает кол-во элементов в последовательности (длину)
'''

# Через индексы мы можем изменять элементы списка
'''
for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()


for i in range(len(L)):
    L[i] = L[i] * i
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Напрямую через элементы последовательности удобно пробегать, если нужно фильтровать элементы
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']

for x in L:
    print(x, end=' ')  # a b c d e
print()

for x in L:
    if x in 'ea':
        print(x, end=' ')  # a e
print()
'''


# Цикл while отвечает на запросы: "пока условие верно, делаем действие", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()


n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)
'''

# Универсальную функцию перевода в различные системы счисления
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


print(convert(8, 2))  # 1000
print(convert(10**8, 16))  # 5F5E100
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 50_000:
        exit()  # Прерывает выполнение всей программы
    if k == 100_000:
        break  # Прерывает выполнение цикла в котором сейчас лежит
    print(k)

print('Продолжение программы')
'''

# Простой пример консольного калькулятор перевода в различные системы счисления
'''
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ


def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему счисления \n'
                 'case 2: Перевод из b-й в 10-ю систему счисления \n'
                 'case 3: Перевод из b-й в k-ю систему счисления\n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите систему счисления: '))
        print(f'Результат перевода числа {n} в {b}-ю систему: {convert(n, b)}')


    elif case == '2':
        b = int(input('Введите систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        print(f'Результат перевода числа {r} из {b}-й системы в 10-ю: {int(r, b)}')


    elif case == '3':
        b = int(input('Введите систему счисления b: '))
        r = input(f'Введите число в {b}-й системе: ')
        k = int(input('Введите систему счисления k: '))
        print(f'Результат перевода числа {r} из {b}-й системы в {k}-ю: {convert(int(r, b), k)}')


    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        exit()

    else:
        print('Я понимаю только команды: case 1, 2, 3, 0')
'''


# Простенькая консольная программа проверки паролей
'''
from random import randint
from time import sleep

password = 'qwerty'
pas = input('Введите пароль от учетной записи: ')
count = 1
while True:
    if pas == password:
        print('Пароль верный.')
        break
    count += 1
    pas = input('Пароль неверный, повторите попытку: ')
    if count == 3:
        print('Превышено кол-во попыток, пройдите проверку на робота: ')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'Решите задачку: {a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка пройдена успешно')
        else:
            print('Повторите попытку через 5 минут.')
            sleep(5 * 60)

print('Добро пожаловать в программу!')
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: