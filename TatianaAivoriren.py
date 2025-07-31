# region Домашка: ******************************************************************


# https://stepik.org/lesson/1309432/step/6?unit=1324548
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if a % 7 == 0 and a % 49 != 0 or a % 40 == 0:
    summa += a
if b % 7 == 0 and b % 49 != 0 or b % 40 == 0:
    summa += b
if c % 7 == 0 and c % 49 != 0 or c % 40 == 0:
    summa += c
print(summa)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы в Пайтон: while и for

# Цикл for отвечает на запросы: "повтори n раз", "пробеги от числа А до числа В"

# Работа цикла for с функцией range(START, STOP-1, STEP):
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, -1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()
'''

# Работа цикла for с итерируемыми объектами:

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # кол-во элементов в списке (длину списка)


# Это удобный способ пробегать элементы списка и фильтровать их
'''
for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()
'''

# Такой способ позволяет пробежать элементы, фильтровать элементы И ИЗМЕНЯТЬ ЭЛЕМЕНТЫ через индексы
'''
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "повторяй пока условие верно", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''


# Перевод в различные системы счисления
'''
# alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase

n = 8
b = 2
r = ''
while n > 0:
    r = alp[n % b] + r
    n //= b
print(r)
'''


# Идеальная функция перевода в различные системы счисления
'''
# alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(8, 2))
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 50_000:
        exit()  # Функция прерывает выполнение всей программы
    if k == 100_000:
        break  # Прерывает выполнение цикла в котором лежит
    print(k)
print('Продолжение программы')
'''


# Программы перевода в различные системы счисления
'''
from string import digits, ascii_uppercase
alp = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему счисления\n'
                 'case 2: Перевод из b-й в 10-ю систему счисления\n'
                 'case 3: Перевод из b-й в k-ю систему счисления\n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите систему счисления: '))
        print(f'Результат перевода числа {n} в {b}-ю систему: {convert(n, b)}')

    elif case == '2':
        b = int(input('Введите систему счисления: '))
        r = input(f'Введите число в {b}-ой системе счисления: ')

        print(f'Результат перевода числа {r} их {b}-й системы: {int(r, b)}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашим калькулятором!')
        exit()

    else:
        print('Я понимаю только команды 1/2/3/0')
'''

# Проверка пароля
'''
pas = 'qwerty'
password = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный.')
        break
    password = input('Пароль неверный, попробуйте снова: ')
print('Добро пожаловать!')
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
