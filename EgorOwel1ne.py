# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for используется для: "Пробеги от А до В", "Повтори n раз"
'''
# range(START=0, STOP, STEP=1)

for i in range(10):  # range(START=0, STOP=10, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):  #  # range(START=10, STOP=1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

# i  01234
s = 'abcde'

print(len(s), len(M))  # 5 5


for i in range(len(M)):  # Пробегаем элементы списка через индексы
    print(i, M[i])

for i in range(len(M)):  # Можем эти элементы через индексы менять
    M[i] = M[i] * i

print(M)  # ['', 'b', 'cc', 'ddd', eeee'']

M = ['a', 'b', 'c', 'd', 'e']

# В таком случае менять элементы нельзя, только если пересоздавать список
for x in M:
    print(x)

# Зато это удобный способ достать элементы и отфильтровать нужные
for x in M:
    if x in 'ae':
        print(x, end=' ')   # a e
'''
from xxsubtype import bench

# Цикл while используется для: "Повторяй пока условие верно", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
'''

# Переводы в различную систему счисления
'''
n = 8
b = 2
r = ''
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)


n = 8
b = 2
r = ''
while n > 0:
    r = str(n % b) + r
    n //= b
print(r)


from string import *
alp = digits + ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', '...
n = 10**8
b = 16
r = ''
while n > 0:
    r = alp[n % b] + r
    n //= b
print(r)

from string import *
alp = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

print(convert(8, 2))  # 1000
'''


# Бесконечный цикл и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает шаг (итерацию) цикла
    if k == 50_000:
        exit()  # Прерывает выполнение всей программы
    if k == 100_000:
        break  # Прерывает цикл в котором он лежит сейчас
    print(k)
print('Программа продолжается ')
'''

# Минипример программы для проверки паролей
'''
password = 'qwerty'
pas = input('Введите пароль: ')
while True:
    if pas == password:
        print('Пароль верный.')
        break
    pas = input('Пароль неверный, повторите попытку: ')

print('Добро пожаловать в программу!')
'''

# Небольшая программа по переводу в различные системы счисления
'''
from string import *
alp = digits + ascii_uppercase

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r


while True:
    case = input('\ncase 1: Перевод из 10-ой в n-ю систему. \n'
                 'case 2: Перевод из n-ой в 10-ю систему. \n'
                 'case 3: Перевод из n-ой в k-ю систему. \n'
                 'case 0: Выход из программы\n'
                 'case: ')

    if case == '1':
        n = int(input('Введите число n: '))
        b = int(input('Введите систему счисления b: '))
        print(f'Результат перевода числа {n} в систему счисления {b}: {convert(n, b)}')

    elif case == '2':
        b = int(input('Введите систему счисления b: '))
        r = input(f'Введите число r в {b}-ой системе счисления: ')
        print(f'Результат перевода числа {r} из {b}-й системы счисления: {int(r, b)}')

    elif case == '3':
        pass

    elif case == '0':
        print('Спасибо, что пользовались нашей программой!')
        exit()

    else:
        print('Не понимаю о чем вы.')
'''


# Строковый тип данных
'''
# i  01234
s = 'abcde'

print(f'Первый элемент строки: {s[0]}')  # a
print(f'Последний элемент строки: {s[-1]}')  # e

# Конкатенация (склеивание) строк
h2 = 'world!'
print('Hello, ' + h2)  # Hello, world!

print('Hello ' * 4)  # дублирование строк при умножении на целое число


for i in range(len(s)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e 
print()

for x in s:
    print(x, end=' ')  # a b c d e
print()

for x in s:
    print(x*2, end=' ')  # aa bb cc dd ee
print()
'''

# Строки нельзя менять, только если через срезы:

# i  012345678
s = '122333221'
# s = s[:3] + '***' + s[6:]
# print(s)  # 122***221
s = s[:3] + '' + s[6:]
print(s)  # 122221


# Срезы на примерах строк срез[START : STOP-1 : STEP]

# i  012345678
s = '122333221'

print(s[:3])  # 122 - Как первые три элемента под индексами 0, 1, 2
print(s[3:])  # 333221 - Все элементы начиная с 3 индекса (включительно)

print(s[-3:])  # 221 - Последние три элемента под индексами: -3, -2, -1
print(s[3:6])  # 333 - Начиная с 3 индекса и до 6 (не включительно)

print(s[1:-1])  # Все элементы кроме первого и последнего
print(s[::])  # Все элементы
print(s[::-1])  # Все элементы в обратном порядке


# Сумма цифр в строке:
'''
n = int(input())
s = str(n)  # '12345'

summa1 = 0
for x in s:
    summa1 += int(x)
print(summa1)

# summa2 = s.count('1') + s.count('2') * 2 + s.count('3') * 3 + ...
summa2 = 0
for i in range(1, 9+1):
    summa2 += s.count(str(i)) * i
print(summa2)

summa3 = sum([int(x) for x in s])
# summa3 = sum([int(x) for x in s if x.isdigit()])
print(summa3)

summa4 = sum(map(int, s))
print(summa4)
'''


# Произведение элементов строки:
'''
from math import prod
total1 = prod([int(x) for x in s])
print(total1)

total2 = 1
for x in s:
    total2 *= int(x)
print(total2)
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
# на следующем уроке: # Функции строк + Методы строк, Cписки строк


