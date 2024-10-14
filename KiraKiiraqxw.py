# region Домашка: ******************************************************************

# Определение четности числа

# ctrl + alt + L
'''
a = int(input())
if a % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
'''


# Проверка соотношения для пятизначного числа
'''
n = int(input())  # 90435
a = n // 10000  # 9
b = (n // 1000) % 10  # 0
c = (n // 100) % 10  # 4
d = (n // 10) % 10  # 3
e = n % 10  # 5

if a * c == b + d + e:
    print("Да")
else:
    print("Нет")
'''


# Вычисление суммы чисел по определенным условиям
'''
a = int(input())
b = int(input())
c = int(input())
summa = 0
if (a % 7 == 0 and a % 49 != 0) or a % 40 == 0:
    summa += a
if (b % 7 == 0 and b % 49 != 0) or b % 40 == 0:
    summa += b
if (c % 7 == 0 and c % 49 != 0) or c % 40 == 0:
    summa += c
print(summa)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "Повтори N раз", "Повтори от A до B"
'''
# range(STOP-1)
# range(START, STOP-1)
# range(START, STOP-1, STEP)

for i in range(10):  # range(start=0, STOP=10-1, step=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, step=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0):
    print(i, end=' ')  #
print()

for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(len(M))  # 5 - Функция, которая возвращает длину списка (кол-во элементов в нем)

for i in range(5):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()


for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e 
print()
'''


# Цикл while отвечает на запросы: "Пока условие верно, повторяй действие", "Бесконечные циклы"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')   # 2 4 6 8 10
    i += 2
'''


# Перевод в различные системы счисления
'''
n = int(input('Введите десятичное число: '))
b = int(input('Введите систему счисления: '))
r = ''
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 == 0:
        continue  # Прерывает итерацию (шаг) цикла 
    if k == 2_000_000:
        exit()  # Прервали выполнение всей программы
    if k == 1_000_000:
        break  # Прерывает выполнение цикла в котором он находится
    print(k)


print('Тут продолжение программы')
'''


# Проверка паролей пользователя
'''
from random import choice, randint
messages_errors = ['Пароль неверный, повторите попытку: ',
                   'Повторите попытку, пароль неверный: ',
                   'Повторите попытку снова: ']

password = 'qwerty'
pas = input('Введите пароль: ')
count = 0
while True:
    if pas == password:
        print('Пароль верный, добро пожаловать!')
        break
    count += 1
    if count == 3:
        print('Пройдите проверку на робота')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'Решите пример: {a} + {b} = \n'))
        if x == a + b:
            print('Проверка пройденна успешно')
            count = 0
        else:
            print('Проверка не пройдена, подождите 5 минут')
    pas = input(choice(messages_errors))
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
