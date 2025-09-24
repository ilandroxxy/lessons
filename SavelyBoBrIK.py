# region Домашка: ******************************************************************


# https://stepik.org/lesson/1309431/step/8?unit=1324547
'''
print(23 % 5)  # 3
print(28 // 3)  # 9
print(30 % 4)
'''


# https://stepik.org/lesson/1309431/step/13?unit=1324547
'''
k = int(input())
summa = k + k * 11 + k * 111
print(f'Сумма чисел: {summa}')


k = int(input())
k = str(k)
summa = int(k) + int(k * 2) + int(k * 3)
print(f'Сумма чисел: {summa}')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Работа цикла for с функцией range():
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

for i in range(3, 10, 3):
    print(i, end=' ')  # 3 6 9
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Работа цикла for с списками/строками:
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
s = 'abcde'

print(len(L))  # 5

for x in L:
    print(x, end=' ')  # a b c d e
print()

for x in L:
    if x in 'ae':
        print(x, end=' ')  # a b c d e
print()

for i in range(len(L)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(L[i], end=' ')  # a b c d e
print()

# через индексы мы можем изменять элементы списка
for i in range(len(L)):
    L[i] = L[i] * i  
print(L)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "пока условие верно - делаем действие", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''

# Функция перевода в различные системы счисления
'''
n = 8
print(bin(n)[2:])
print(f'{n:b}')

n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)


# Простенькая функция перевода
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

n = 8
b = 2
print(convert(n, b))

x = convert(8, 4)
print(x)
'''

# Универсальная функция перевода
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(10**8, 16))  # 5F5E100
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 100_000:
        break  # Прерывает цикл в котором сейчас лежит
    if k == 50_000:
        exit()  # Прерывает выполнение программы
    print(k)

print('Продолжение программы')
'''


# Пример калькулятора через бесконечный цикл

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
                 'case 1: Перевод из 10-й в b-ю \n'
                 'case 2: Перевод из b-й в 10-ю \n'
                 'case 3: Перевод из b-й в k-ю \n'
                 'case 0: Выход из программы \n'
                 'case: ')

    if case == '1':
        n = int(input('Введите 10-е число: '))
        b = int(input('Введите систему счисления: '))
        print(f'Результат перевода числа {n} в {b}-ю: {convert(n, b)}')

    elif case == '2':
        pass

    elif case == '3':
        b = int(input('Введите систему счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        print(f'Результат перевода: {int(r, b)}')

    elif case == '0':
        print('Спасибо, что пользовались нашей программой!')
        exit()

    else:
        print('Я понимаю только команды: 1, 2, 3, 0')

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
