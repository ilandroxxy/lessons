# region Домашка: ******************************************************************


# ctrl + alt + L
'''
a = int(input())
b = a % 10
c = a // 10 % 10
d = a // 100 % 10
e = a // 1000 % 10
f = a // 10000
if f * d == e + c + b:
    print("Да")
else:
    print("Нет")
'''
from macholib.mach_o import rpath_command

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Цикл - это некоторое повторяющееся действие

# Цикл for отвечает на вопрос: "повтори n раз", "пробеги от А до В"

# Цикл while отвечает на вопрос: "Делаем действие, пока условие верно"

# Цикл форм может через функцию range() или последовательности

# range(START, STOP-1, STEP)
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

for i in range(10, -1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()


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

# i - index
# Через индексы мы можем изменять содержимое нашего списка
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']


M = [x for x in range(1, 100) if x % 10 == 7]
print(M)  # [7, 17, 27, 37, 47, 57, 67, 77, 87, 97]
'''


# Цикл while
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

x = 2
while x <= 10:
    print(x, end=' ')
    x += 2
print()
print('Конец цикла')
'''


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
n = int(input('Введите число для перевода: '))
b = int(input('Введите систему счисления: '))
r = ''
while n > 0:
    r += alphabet[n % b]
    n //= b
r = r[::-1]
print(r)
'''


# Бесконечный цикл и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итеррацию цикла
    if k == 1_000_000:
        exit()  # Полностью прерывает исполнение программы
    if k == 500_000:
        break  # Прерывает исполняемся цикл
    print(k)
print('Тут программа продолжается')
'''


# Программа на проверку паролей
'''
from random import choice, randint
from time import sleep

messages = [
    "Неверный пароль, попробуйте снова: ",
    "Ошибка в пароле, введите ещё раз: ",
    "Пароль не подходит, повторите ввод: ",
    "Неверный пароль, попытайтесь ещё: ",
    "Пароль введён неправильно, попробуйте ещё раз: ",
    "Ошибка: неверный пароль, введите снова: ",
    "Пароль не совпадает, повторите попытку: ",
    "Неверный пароль, пожалуйста, введите ещё раз: ",
    "Пароль ошибочный, попробуйте ещё раз: ",
    "Не удалось войти, проверьте пароль и повторите: "
]

password = 'qwerty'
pas = input('Введите пароль: ')
captcha = 0
while True:
    if pas == password:
        print('Пароль верный. \n'
              'Добро пожаловать!')
        break
    captcha += 1
    if captcha == 3:
        print('Пройдите проверку на робота!')
        a = randint(1, 100)
        b = randint(1, 100)
        x = int(input(f'Решив задачку: {a} + {b} = '))
        if a + b == x:
            print('Капча пройдена успешно!')
            captcha = 0
        else:
            print('Проверка не пройдена, повторите попытку через 5 минут.')
            sleep(5*60)

    pas = input(choice(messages))


print('Ваш личный кабинет')
'''


# Программа на перевод в различные системы счисления
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    r = r[::-1]
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в n-ю систему. \n'
                 'case 2: Перевод из n-й в 10-ю систему. \n'
                 'case 3: Перевод из n-й в k-ю систему. \n'
                 'case 0: Выход из программы. \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число для перевода: '))
        b = int(input('Введите систему счисления: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} в {b}-ю систему: {r}')

    elif case == '2':
        b = int(input('Введите систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} в {b}-й системе к 10-й: {n}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что вы пользовались нашей программой!')
        exit()

    else:
        print('Я ничего не понимаю кроме команд: 1, 2, 3, 0')
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
