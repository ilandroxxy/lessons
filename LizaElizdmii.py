# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Типы данных переменных
'''
a = 5   # int (integer) - целочисленные значения
print(a, type(a))  # 5 <class 'int'>
print(2+2, type(2+2))  # 4 <class 'int'>

b = 5.0  # float (число с плавающей точкой) - вещественные значения (дроби)
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>
b2 = 5,0
print(type(b2))  # <class 'tuple'>

c = '5'  # str (string) - строковый тип данных, хранит в себе символы, слова, тексты и тд тп
print(a * 4, c * 5)  # 20 5555 - при умножении строки на целое число, строка дублируется
print('Hello ' * 4)  # Hello Hello Hello Hello
new_message = 'Hello, ' + 'world!'
print(new_message)  # Операция конкатенации (склеивание) строк
# TypeError: can only concatenate str (not "int") to str

d1 = True
d0 = False  # bool (Boolean) - Основы Булевой алгебры (Математическая логика)
print(4 < 10)  # True

n = 5
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''

# - однострочный комментарий ctrl + /

# Типы данных коллекций (последовательностей)
'''
A = [1, 2, 3]  # list (списков)

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка М: {M[0]}')
print(f'Последний элемент списка М: {M[-1]}')

# 1. Могут содержать в себе неограниченное кол-во элементов, различных типов данных
# 2. Каждый элемент имеет свой индивидуальный порядковый номер (индекс)
# 3. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 4. Элементы списка можно брать через индексы, а также изменять их


B = (1, 2, 3)  # tuple (кортеж)
# 1. Полностью идентичен спискам, кроме: менять значения элементов нельзя.

b = 1, 2, 3, 4, 5
print(b, type(b))  # (1, 2, 3, 4, 5) <class 'tuple'>


C = {1, 2, 3, 2, 3}  # set (множества)
# 1. В множествах элементы не могут иметь копий, копии удаляются
print(C)  # {1, 2, 3}


D = {'one': 'один', 'two': 'два'}  # dict (словарь)
# 1. Элементы словаря разбиты на две части: ключ и значение
# 2. Доступ к значению элементы осуществляется через его ключ
# 3. Ключ не могут повторяться, если такое происходит, то произойдет перезапись значения по ключу

print(D['one'])  # один
D['one'] = 1
print(D)  # {'one': 1, 'two': 'два'}
# print(D['three'])  # KeyError: 'three'
print(D.get('three'))  # None

if D.get('three') == None:
    D['three'] = 'три'
else:
    print('Такой элемент уже есть.')
print(D)  # {'one': 1, 'two': 'два', 'three': 'три'}

print(D.keys())  # dict_keys(['one', 'two', 'three'])
print(D.values())  # dict_values([1, 'два', 'три'])
print(D.items())  # dict_items([('one', 1), ('two', 'два'), ('three', 'три')])

for key, value in D.items():
    print(key, value)
    # one 1
    # two два
    # three три
'''


'''
M = [2, 2.0, '2', True, 2+2, 4/2, '2' * 2, 2 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'один': 'one'}]
for elem in M:
    print(type(elem), elem)
    # <class 'int'> 2
    # <class 'float'> 2.0
    # <class 'str'> 2
    # <class 'bool'> True
    # <class 'int'> 4
    # <class 'float'> 2.0
    # <class 'str'> 22
    # <class 'bool'> True
    # <class 'list'> [1, 2, 3]
    # <class 'tuple'> (1, 2, 3)
    # <class 'set'> {1, 2, 3}
    # <class 'dict'> {'один': 'one'}
'''


# Конвертирование типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>
# ValueError: invalid literal for int() with base 10: '5.0'

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>

A = [1, 2, 3, 2, 3]
print(A, type(A))  # [1, 2, 3, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3, 2, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''


# Ввод данных с клавиатуры
'''
s = input('Введите строку с клавиатуры: ')
print(s, type(s))  # 56 <class 'str'>

n = int(input('Введите число с клавиатуры: '))
print(n, type(n))  # 56 <class 'int'>
'''


# Работа с f-строкой
'''
# "Сегодня облачно, а температура 24 градуса!"
weather = 'облачно'
temperature = int(input('Введите температура: '))

print("Сегодня ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня {weather}, а температура {temperature} градуса!")

students = {'Alexander': 1080123898, 'Alexey': 561902196, 'Dmitry': 1062566672, 'Egor': 5227541364 }
message_text = 'Список ваших студентов: \n'
num = 1
for key, value in students.items():
    message_text += f'{num}) name: {key}, id: {value} \n'
    num += 1
print(message_text)
'''


# Базовая арифметика:
'''
a, b = 7, 2

print(f'{a} + {b} = {a+b} \n'
      f'{a} - {b} = {a-b} \n'
      f'{a} * {b} = {a*b}')

print()  # В каждой функции print() есть переход на новую строку '\n'
print(end='\n')

print(f'{a} / {b} = {a/b} \n'  # 3.5 - Вещественное деление (дробное), результат всегда float
      f'{a} // {b} = {a//b} \n'  # 3 - Взятие только лишь целой части от деления 
      f'{a} % {b} = {a%b}')  # 1 - Взятие остатка от деления

print(123 // 10)  # 12
print(123 % 10)  # 3 - таким образом мы можем проверять, на какую цифру заканчивается число

print(1234 // 100)  # 12
print(1234 % 100)  # 34
print(-1234 % 100)  # 66
print(abs(-1234) % 100)  # 34 - Функция abs() берет модуль от числа, то есть отбрасывает минус

print()

print(f'Возведем число {a} в степень {b}: {a ** b}')

print()

from math import sqrt
print(f'Возьмем квадратный корень от числа 16: {sqrt(16)}')  # 4.0
print(f'Возьмем квадратный корень от числа 16: {16 ** (1/2)}')  # 4.0
print(f'Возьмем кубический корень от числа 27: {27 ** (1/3)}')  # 3.0
'''


# Базовые способы подключения библиотек
'''
import math
print(math.sqrt(16))

import math as m  # Переименовали библиотеку в m
print(m.sqrt(16))

from math import sqrt, pow  # Импортируем конкретные функции из библиотеки
print(sqrt(16))

from math import *  # Импортируем все функции из библиотеки
print(sqrt(16))
print(fabs(-20))
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
