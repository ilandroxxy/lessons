# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл - какое-то повторяющееся действие

# Цикл for отвечает на запросы: "повтори N раз", "пробеги от А до В"

# Работа цикла for с функцией range()

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)
'''
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):
    print(i, end=' ')  # 2 4 6 8
print()

n = 10
for i in range(2, n+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, -1, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0
print()
'''


# Работа цикла for с последовательностями: list(), str(), tuple(), ...
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


print(len(M))  # 5 - Возвращает длину списка M

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Цикл while отвечает на запросы: "пока условие верно - делаем действие", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''


# Переводы в различные системы счисления
'''
# Алгоритм перевода
n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)

# Хорошая, но не идеальная функция преевода
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

x = convert(8, 2)
print(x)

# Идеальная функция перевода

# alp = '0123456789ABC...'
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

x = convert(10**8, 16)
print(x)  # 5F5E100
print(int('5F5E100', 16))  # 10**8
'''


# Бесконечные циклы и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает шаг итерации цикла
    if k == 100_000:
        break  # Прерывает работу цикла в котором лежит
    if k == 50_000:
        exit()  # Прерывает работу вообще все программы
    print(k)
'''

# Небольшой калькулятор


# Небольшой калькулятор перевода в различные системы счисления
'''
from string import digits, ascii_uppercase

alp = digits + ascii_uppercase  # '0123456789ABCD...'


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
        n = int(input('Введите 10-е число: '))
        b = int(input('Введите систему счиcления: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} в {b}-ю систему счисления: {r}')

    elif case == '2':
        b = int(input('Введите систему счиcления: '))
        r = input(f'Введите число в {b}-ой системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-й системы в 10-ю: {n}')

    elif case == '3':
        b = int(input('Введите b-ю систему счиcления: '))
        r = input(f'Введите число в {b}-ой системе: ')
        k = int(input('Введите k-ю систему счиcления: '))
        n = int(r, b)
        r_new = convert(n, k)
        print(f'Результат: {r_new}')

    elif case == '0':
        print('Спасибо, что пользовались нашей программой!')
        break

    else:
        print('Я понимаю только команды: 1, 2, 3, 0')
        continue
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
