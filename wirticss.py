


# - это однострочный комментарий


'''
print('Hello, world!') - многострочный комментарий
'''


# Типа данных переменных
'''
a = 5   # int (integer) - целочисленные значения
print(a, type(a))  # 5 <class 'int'>


b = 5.0  # float (число с плавающей точкой) - вещественное значение (дробь)
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>


c = '5'  # str (string) - строковый тип данных для хранения текста и символов
print(c * 4)  # 5555 - если строку умножить на целое число, то она дублируется

c1 = 'Hello, '
c2 = 'world!'
c = c1 + c2  # - операция конкатенации строк (склеивание)
print(c)  # Hello, world!

s = '7' + '5' * 10 + '0'
print(s)  # 755555555550


d1 = True  # bool (Boolean) - основы Булевой алгебры (математическая логика)
d0 = False
print(4 < 10)  # True
print(4 == 10)  # False
'''


# Конвертация типов данных
'''
a = 5
print(type(a), a)  # <class 'int'> 5

a = str(a)
print(type(a), a)  # <class 'str'> 5

a = float(a)
print(type(a), a)  # <class 'float'> 5.0

a = int(a)
print(type(a), a)  # <class 'int'> 5
'''

# Ввод данных с клавиатуры через input()
'''
age = int(input('Введите возраст пользователя: '))
name = input('Введите имя пользователя: ')  # - принимает значение с клавиатуры в виде строки
if age >= 18:
    print('Пользователь: ', name, '. Возраст: ', age, '. Доступ разрешен!')
else:
    print('Пользователь: ', name, '. Возраст: ', age, '. Доступ запрещен!')
'''


# Работа с f-строками
'''
age = int(input('Введите возраст пользователя: '))
name = input('Введите имя пользователя: ')
if age >= 18:
    print(f'Пользователь: {name}. Возраст: {age}. Доступ разрешен!')
else:
    print('Пользователь: ', name, '. Возраст: ', age, '. Доступ запрещен!')
    print('Пользователь: ' + name + '. Возраст: ' + str(age) + '. Доступ запрещен!')
    # TypeError: can only concatenate str (not "int") to str
    print('Пользователь: {}. Возраст: {}. Доступ разрешен!'.format(name, age))
'''


# Базовая арифметика
'''
a, b = 7, 2
print(f'{a} + {b} = {a + b} \n'  # - символ \n переход на новую строку 
      f'{a} - {b} = {a - b} \n'
      f'{a} * {b} = {a * b}')

print()  # - в каждой функции print() есть переход на новую строку \n

# Три типа делений в пайтон
print(f'{a} / {b} = {a / b}')  # 3.5 - вещественное деление (всегда float)
print(f'{a} // {b} = {a // b}')  # 3 - взятие только целой части (всегда int)
print(f'{a} % {b} = {a % b}')  # 1 - взятие остатка от деления (всегда int)


n = 456
print(n // 10)  # 45
print(n % 10)  # 6 - берет последнюю цифру числа

print(n // 100)  # 4
print(n % 100)  # 56 - берет две последние цифры числа

print(n % 1000)  # 456 - берет три последние цифры числа


n = 456  # = - это присваивание значения
if n % 2 == 0:  # == - это сравнение (равны ли они)
    print('Число делится на 2 | Кратно 2 | Число четное')
if n % 2 != 0:  # != - это сравнение (не равны ли они)
    print('Число не делится на 2 | Не кратно 2 | Число нечетное')
if n % 23 == 0:
    print('Число делится на 23 | Число кратно 23')


print(f'Возведение числа 2 в степень 4: {2 ** 4}')
print(f'Взятие квадратного корня от числа 16: {16 ** (1/2)}')
print(f'Взятие кубического корня от числа 27: {27 ** (1/3)}')

import math
print(f'Взятие квадратного корня от числа 16: {math.sqrt(16)}')
'''


# Как использовать бибилиотеки в пайтон
'''
import math   # Самое простое подключение библиотеки
print(math.sqrt(16))

import math as m  # Подключение библиотеки с коротким именем
print(m.sqrt(16))

from math import sqrt, factorial, prod  # Подключение конкретных функций или констант
print(sqrt(16))
print(factorial(5))


from math import *  # Подключение всего содержимого
print(sqrt(16))
print(factorial(5))
print(prod([1, 2, 3, 4, 5]))
'''


# Очень полезные библиотеки Python для ЕГЭ по информатике #tpy

# 🐢  turtle - для графики (№6)
'''
import turtle as t
t.tracer(0)
t.fd(100)
t.rt(90)
t.goto(50, 30)
t.dot(5, 'red')
t.done()
'''


# 🔄 itertools -- для комбинаторики (№1, 8, 9, 17, 24, 25)
# Для этого модуля лучше импортировать только нужные функции, чтобы код оставался понятным.
'''
from itertools import product
for combo in product([1, 2, 3], repeat=2):
    print(combo)
    # (1, 1)
    # (1, 2)
    # (1, 3)
    # (2, 1)
    # (2, 2)
    # (2, 3)
    # (3, 1)
    # (3, 2)
    # (3, 3)

count = 0
from itertools import permutations
for perm in permutations('abc'):
    count += 1
    print(count, ''.join(perm))
    # 1 abc
    # 2 acb
    # 3 bac
    # 4 bca
    # 5 cab
    # 6 cba

count = 0
from itertools import *
for perm in permutations('abc'):
    count += 1
    print(count, ''.join(perm))
    # TypeError: unsupported operand type(s) for +=: 'type' and 'int'
'''


# 🌐  ipaddress -- для сетей (№10)
'''
from ipaddress import *
net = ip_network('192.168.1.64/26', strict=False)
print(net, net.netmask, net.num_addresses)
'''


# 🤔 sys + functools -- для рекурсии (№16)
'''
from sys import setrecursionlimit
setrecursionlimit(10000)

from functools import lru_cache
@lru_cache(None)
def F(n):
    if n <= 3:
        return n
    return F(n - 1) + F(n - 3)
'''


# 🎭 fnmatch - для поиска по маске (№25) или же можно использовать библиотеку re
'''
# № 7095 OpenFIPI(Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# соответствующие маске 1234*54, делящиеся на 21 без остатка.

from fnmatch import *
for x in range(21, 10**8, 21):
    if fnmatch(str(x), '1234*54'):
        print(x, x // 21)

# Библиотека re крайне полезена при решении 24 номера

# Библиотека re дает больше гибкости про оформлении патерна 
from re import *
for x in range(21, 10**8, 21):
    if fullmatch('1234[0-9]*54', str(x)):
        print(x, x // 21)
'''


# 🔤 string - готовые алфавиты
'''
# Алфавит нужен в 5 и 14 номерах, а иногда и в 24 номерах
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])   # ['0', '1'] - двоичная алфавит
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7'] - восьмеричный алфавит

from string import ascii_uppercase, digits, punctuation

alp = digits + ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(alp[:2])  # 01 - двоичная алфавит
print(alp[:8])  # 01234567 - восьмеричный алфавит

print(ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(digits)           # 0123456789
print(punctuation)      # !"#$%&'()*+,-./:;<=>?@]^_`{|}~
'''


#  🔣  math - математические функции
'''
# Пригождается в 19-21 номерах и 27 номере
from math import ceil, floor, prod, dist

print(round(7 / 2))  # 4 - округляет по правилам математики
print(ceil(7 / 2))  # 4 - округляет в большую сторону
print(floor(7 / 2))  # 3 - округялет в меньшую сторону

print(sum([1, 2, 3, 4, 5]))  # 15 - посчитали сумму элементов списка
print(prod([1, 2, 3, 4, 5]))  # 120 - посчитали произведение элементов списка

print(dist((0, 0), (3, 4)))  # 5.0 - расстояние между точкой (0;0) и точкой (3;4)
# То есть в 27 номере ищем расстояние между двумя точкам (при поиске центра кластера)
'''


# Условные операторы if, elif, else
'''
n = int(input('n: '))
if n > 0:
    print('Число положительное')
elif n < 0:
    print('Число отрицательное')
else:
    print('Число равно 0')
'''


# todo На следющем уроке: Логические связки


