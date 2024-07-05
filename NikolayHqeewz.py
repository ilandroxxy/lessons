# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Циклы в python (цикл - повторяющееся событие)

# for: Отвечает на запросы: "повтори n раз", "пробеги от a до b"

# Работа с циклом for через функцию range()
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - все четные числа (кратные 2)
print()


for i in range(1, 10, 2):  # range(START=1, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - все нечетные числа
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


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5  len() - возвращает длину последовательности (кол-во элементов).
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i]
print(M)  # ['a', 'b', 'c', 'd', 'e']


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Работа с циклом for напрямую через итерируемый (последовательность) объект
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()


for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e
print()


M = [int(x) for x in open('17.txt')]
chet = [x for x in M if x % 2 == 0]
otric = [x for x in M if x < 0]
copied = [x for x in M if M.count(x) > 1]
not_copied = [x for x in M if M.count(x) == 1]
print(not_copied)
'''


# while: Отвечает на запросы: "повторяй пока условие истинно", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

# Неконтролируемый бесконечный цикл
'''
i = 0
while i < 10:
    print(i)
'''

# Перевод в base систему счисления
'''
x = 8
base = 2
M = []
while x > 0:
    M.append(x % base)  # .append() - добавляет новый элемент в конец списка
    x //= base
M.reverse()
print(M)  # [1, 0, 0, 0]
'''

'''
x = int(input('Введите число в 10-й системе: '))
base = int(input('Введите систему счисления base: '))
r = ''
while x > 0:
    r += str(x % base)
    x //= base
r = r[::-1]
print(r)  # 1000
'''

# Универсальное решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
x = int(input('Введите число в 10-й системе: '))  # 567894325345
base = int(input('Введите систему счисления base: '))  # 25
r = ''
while x > 0:
    r += alphabet[x % base]
    x //= base
r = r[::-1]
print(r)  # 3I129BKDK
'''


# Бесконечные циклы while:

# Операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла 
    if k == 100000:
        break  # Прерывает цикл (тот в котором он лежит)
        exit()  # Прерывает всю программу
    print(k)

print('Hello')
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = int(input('\ncase 1: Перевод из 10-й в base систему счисления \n'
                     'case 2: Перевод из base в 10-ю систему счисления \n'
                     'case 3: Перевод из base в n-ю систему счисления \n'
                     'case 0: exit \n'))

    if case == 1:
        x = int(input('Введите число в 10-й системе: '))
        base = int(input('Введите систему счисления base: '))
        r = ''
        while x > 0:
            r += alphabet[x % base]
            x //= base
        r = r[::-1]
        print(f'Результат перевода: {r}')

    elif case == 2:
        base = int(input('Введите систему счисления base: '))
        r = input(f'Введите число в {base}-й системе счисления: ')
        print(f'Результат перевода: {int(r, base)}')

    elif case == 3:
        pass

    elif case == 0:
        exit()

    else:
        print('Команда введена ошибочно, повторите попытку снов. \n\n')
'''


'''
from random import randint, choice
from time import sleep


errors = [
    "Пароль неверный, пожалуйста, попробуйте снова: ",
    "Неправильный пароль, повторите ввод: ",
    "Пароль не совпадает, попробуйте еще раз: ",
    "Неверный ввод пароля, повторите попытку: ",
    "Попробуйте еще раз, этот пароль неверен: ",
    "Пароль некорректный, повторите попытку: ",
    "Повторите ввод пароля, он неверный: ",
    "Пароль не распознан, введите снова: ",
    "Ошибка в пароле, повторите пожалуйста: ",
    "Неверный пароль, введите еще раз: "
]


password = 'qwerty'
pas = input('Введите пароль от своего аккаунта: ')
cnt = 0
while True:
    if pas == password:
        print('Welcome!')
        break
    cnt += 1
    if cnt == 3:
        a = randint(0, 100)
        b = randint(0, 100)
        print('Слишком много попыток.')
        x = int(input(f'Пройдите проверку на робота, решив пример: {a} + {b} = '))
        if x == a + b:
            cnt = 0
            print('Проверка успешно пройдена!')
        else:
            print('Проверка не пройдена, повторите попытку через 5 минут.')
            sleep(5 * 60)

    pas = input(choice(errors))

print('Вы попали в личный кабинет.')
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
