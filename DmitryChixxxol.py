# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for покрывает запросы: "повтори n раз", "пробеги от А до В"
'''
# Цикл for с функцией range():
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10+1):  # range(START=2, STOP=11-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9 10
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):  # range(START=10, STOP=0-1, STEP=1)
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]
print(len(M))  # Длина списка или кол-во элементов в нем

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # 1 2 3 4 5
print()

for i in range(len(M)):
    M[i] = M[i] ** 2
print(M)  # [1, 4, 9, 16, 25]
'''

# Цикл for с последовательностями:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

for x in M:
    print(x, end=' ')  # 1 2 3 4 5
print()

for x in M:
    if x % 2 == 0:
        print(x, end=' ')  # 2 4 
'''


# Цикл while покрывает запросы: "пока условие верно, выполняем действие", "бесконечные циклы"

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()


# Соберем свою функцию перевода в n-ую систему счисления

'''
n = 8
b = 2
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()
print(M)  # [1, 0, 0, 0]
'''

# Почему 14 номер лучше решать через списки:
'''
n = 729**8 - 3**18 + 85
b = 16
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()
print(M)
print(M.count(0))
# [1, 0, 14, 4, 2, 5, 12, 5, 6, 13, 10, 15, 14, 3, 10, 4, 10, 4, 12, 13]
# 1


n = 729**8 - 3**18 + 85
b = 16
r = ''
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)
print(r.count('0'))
# 104142521563101514130140142131
# 4

from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

n = 729**8 - 3**18 + 85
b = 16
r = ''
while n > 0:
    r += alphabet[n % b]
    n //= b
r = r[::-1]
print(r)
print(r.count('0'))
# 10E425C56DAFE3A4A4CD
# 1
'''

'''
from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase


def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    r = r[::-1]
    return r


n = 729**8 - 3**18 + 85
b = 16
r = convert(n, b)
print(r, r.count('0'))  # 10E425C56DAFE3A4A4CD 1
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # - прерывает итерацию (шаг) цикла
    if k == 1_000_000:
        break  # - прерывает цикл в котором он лежит
    if k == 500_000:
        exit()  # - полностью прерывает выполнение программы
    print(k)

print('Продолжение программы.')
'''


'''
from string import digits, ascii_uppercase


alphabet = digits + ascii_uppercase


def convert(num: int, base: int) -> str:
    """
Функция перевода из 10-й в base систему счисления
    :param num: Это десятичное число для превода
    :param base: Это система счисления в которую будем переводить
    :return: Результат в виде строки, для работы с функцией int(s, b)
    """
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res


while True:
    case = int(input('\n'
                     'case 1: Перевод из 10-й в n-ю систему счисления \n'
                     'case 2: Перевод из n-й в 10-ю систему счисления \n'
                     'case 3: Перевод из n-й в k-ю систему счисления \n'
                     'case 0: Exit'
                     '\n'))

    if case == 1:
        n = int(input('Введите число в 10-й системе: '))
        b = int(input('Введите систему счисления для перевода (2 <= b <= 36): '))
        print(f'Результат перевода числа {n} в {b}-ю систему счисления: {convert(n, b)}')

    elif case == 2:
        b = int(input('Введите систему счисления для перевода: '))
        r = input(f'Введите число в {b}-й системе счисления: ')
        print(f'Результат перевода числа {r} из {b}-й системы в {10}-ю: {int(r, b)}')

    elif case == 3:
        b = int(input('Введите систему счисления для числа: '))
        r = input(f'Введите число в {b}-й системе счисления: ')
        k = int(input('Введите систему счисления для перевода: '))
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-й системы в {k}-ю: {convert(n, k)}')

    elif case == 0:
        print('Спасибо, что воспользовались нашей программой! ')
        break

    else:
        print('Не очень понятно, что вы от меня просите. \n'
              'Повторите попытку нажав клавиши 1, 2, 3, 0')
'''


# Проверка паролей

from random import choice


error_messages = [
    "Неправильный пароль, попробуйте снова: ",
    "Пароль не соответствует, попробуйте ввести его еще раз: ",
    "Ошибка ввода пароля, повторите попытку: ",
    "Пароль неверен, попробуйте ещё раз: ",
    "Введён неправильный пароль, пожалуйста, попробуйте заново: ",
    "Пароль не распознан, повторите ввод: ",
    "Вы ввели неправильный пароль, попробуйте еще раз: ",
    "Пароль некорректен, попробуйте заново: "
]


password = 'qwerty'
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный, добро пожаловать! ')
        break
    pas = input(choice(error_messages))


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
