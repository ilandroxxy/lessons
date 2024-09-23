# region Домашка: ******************************************************************


# Определение четности числа
'''
a = int(input())
if a % 2 == 0:
    print(f'Чётное')
elif a % 2 == 1:
    print('Нечётное')
else:
    print(f'Число равно {a}')
'''

'''
A = tuple(input())
print(A[0], A[-1])


s = input()
print(s[0], s[-1])
'''


'''
a = int(input())
b = int(input())
c = int(input())
A = []
if a % 7 == 0 and a % 49 != 0 or a % 40 == 0:
    A.append(a)
if b % 7 == 0 and b % 49 != 0 or b % 40 == 0:
    A.append(b)
if c % 7 == 0 and c % 49 != 0 or c % 40 == 0:
    A.append(c)
print(sum(A))


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
print(sum(A))
'''

# Разработка программы для определения вида треугольника
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''

# Сравнение двух чисел и проверки деления
'''
a = int(input())
b = int(input())
if max(a, b) % min(a, b) == 0:
    print('Делится')
else:
    print('Не делится')
'''


# Фильтрация чисел
'''
a = int(input())
if 1 <= a <= 5:
    print(f'Оценка: {a}')
else:
    print('Слишком большое число')
'''

# Проверка длины слова
'''
a = input()
if len(a) > 10 or len(a) % 2 == 0:
    print('ДА')
else:
    print('НЕТ')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Цикл for отвечает на запросы: "Повтори n раз", "Пробеги от А до В"

# Работа с циклом for через функцию range()
# range(START, STOP, STEP)
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

n = 10
for i in range(2, n+1, 2):  # range(START=2, STOP=11-1, STEP=2)
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

print(len(M))  # len() - возвращает длину последовательности (то есть кол-во элементов)

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i

print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Работа с циклом фор через последовательность
'''
M = ['a', 'b', 'c', 'd', 'e']

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')
print()  # a e

print(*[x for x in M if x in 'ae'])  # a e
'''


# Циклы while отвечает на запросы: "Пока условие верно, выполняй действие", "Бесконечные циклы"

'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')
    i += 2  # 0 1 2 3 4 5 6 7 8 9
print()
'''

'''
n = 8  # 1000_2
b = 2
R = []
while n > 0:
    R.append(n % b)
    n //= b
R.reverse()  # R = R[::-1]
print(R)

print(int('1000', 2))  # 8 - перевели строку из 2-й в 10-ую систему


# Вариант перевода через строку (неполный)
n = 8  # 1000_2
b = 2
r = ''
while n > 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)

print(int(r, 2))  # 8 - перевели строку из 2-й в 10-ую систему


from string import *
alphbaet = digits + ascii_uppercase
print(alphbaet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphbaet[n % b]
        n //= b
    r = r[::-1]
    return r


print(convert(8, 2))  # 1000
print(convert(123456789, 16))  # 75BCD15
print(int('75BCD15', 16))  # 123456789
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # continue - прерывает итерацию (шаг) цикла
    if k == 2_000_000:
        break  # break - прерывает цикл в котором он лежит
    if k == 1_000_000:
        exit()  # exit() - прерывает исполнение вей программы
    print(k)

print('Продолжение программы')
'''

'''
from random import randint, choice
from time import sleep

error_messages = [
    'Пароль указан неверно, пожалуйста, повторите попытку: ',
    'Упс, кажется, вы ввели неверный пароль. Попробуйте ещё раз: ',
    'Ошибка! Ваш пароль не подходит, попробуйте ввести его снова: ',
    'Не удалось войти, пароль не совпадает. Пожалуйста, попробуйте снова: ',
    'Введённый вами пароль неверен, пожалуйста, проверьте его и попытайтесь вновь: ',
    'Пароль не распознан. Пожалуйста, попробуйте ввести его еще раз: ',
    'Неверный пароль. Пожалуйста, введите его заново: ',
    'Увы, введённый вами пароль оказался ошибочным. Попробуйте еще раз: ',
    'Пароль неправильный, попробуйте снова ввести его: ',
    'К сожалению, пароль не верен. Пожалуйста, повторите попытку: '
]

password = 'qwerty'
pas = input('Введите свой пароль для проверки: ')
count = 0
while True:
    if pas == password:
        print('Добро пожаловать!')
        break
    count += 1
    if count == 3:
        print('Пройдите проверку на робота, решив пример:')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка пройдена успешно')
        else:
            print('Неудачная попытка, попробуте снова через 5 минут')
            sleep(5*60)
    pas = input(choice(error_messages))
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
