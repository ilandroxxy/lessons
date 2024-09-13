# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# x = 5  # Переменная - это удобный способ взаимодействия с памятью
# print(x, type(x))  # 5 <class 'int'>

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(2 + 2, type(2 + 2))  # 4 <class 'int'>

b = 5.0  # float (число с плавающей точкой) - вещественные значения (дроби)
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

c = '5'  # str (string) - строковый тип данных, хранит в себе символы, слова, текст и тд тп
print(a * 4, c * 4)  # 20 5555 - При умножении строки на целое число эта строка дублируется
print('Hello ' * 4)  # Hello Hello Hello Hello
print('1' * 66)  # 111111111111111111111111111111111111111111111111111111111111111111

new_message = 'Hello, ' + 'world!'  # Конкатенация (склеивание) строк
print(new_message)  # Hello, world!

print('Сегодня я прочитал роман "Война и мир"')
# Сегодня я прочитал роман "Война и мир"

d1 = True
d0 = False  # bool (Boolean) - Основы Булевой алгебры (Математическая логика)
print(4 < 10)  # True

n = 5
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''


# Типы данных коллекций (последовательностей)
'''
A = [1, 2, 3]  # list (список)
# 1. Могут содержать в себе неограниченное кол-во элементов, различных типов данных
# 2. Каждый элемент списка имеет свой порядковый номер: индекс
# 3. Индексы могут считаться слева-направо начиная с 0 или справа-налево начиная с -1
# 4. Элементы списка можно брать через индексы или изменять их значение

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0])  # Первый элемент списка M
print(M[-1])  # Последний элемент списка M

M[0], M[-1] = 'A', 'E'
print(M)  # ['A', 'b', 'c', 'd', 'E']

B = (1, 2, 3)  # tuple (кортеж)
# 1. Полностью идентичен спискам за исключением: элементы кортежа нельзя изменять

C = {1, 2, 3, 2, 3}  # set (множества)
# 1. В множествах не может существовать копии элемента (копии удаляются)
print(C)  # {1, 2, 3}

# Теория множеств:
# P = {2, 3, 5, 7, 11, 13, 17, 19, 23, ..., +int}  - множество простых чисел
# Простые число это числа, которые имеют только лишь два делителя: 1 и само на себя
# N = {1, 2, 3, ..., + inf} - множество натуральных чисел  P ∈ N
# Z = {-inf, ..., -2, -1, 0, 1, 2, ..., + inf} - множество целых чисел  P ∈ N ∈ Z

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Объединение множеств: {1, 2, 3, 4, 5, 6}
# Пересечение множеств: {3, 4}
# Разность множеств: A / B: {1, 2}
# Разность множеств: B / A: {5, 6}

D = {'один': 'one', 'два': 'two'}  # dict (словарь)
# 1. Элементы словаря состоят из двух частей: ключ и значение
# 2. Доступ к значению элемента словаря осуществляется через ключ
# 3. Ключи не могут повторяться, если такое произойдет, то значение по ключу перезапишется

print(D['один'])  # one
D['один'] = 1
print(D)  # {'один': 1, 'два': 'two'}
'''


# Конвертация типов данных
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
s = input('Введите строку: ')
print(s, type(s))  # 56 <class 'str'>

n = int(input('Введите число: '))
print(n, type(n))
'''


# Работа с f-строкой
'''
weather = 'облачно'
temperature = int(input('Введите температуру: '))
# "Сегодня облачно, а температура 24 градуса!"
print("Сегодня ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня {weather}, а температура {temperature} градуса!")
'''


# Базовая арифметика:
'''
a, b = 7, 2

print(f'{a} + {b} = {a + b} \n'
      f'{a} - {b} = {a - b} \n'
      f'{a} * {b} = {a * b}')

print()  # В каждой функции print() есть переход на новую строку '\n'

print(f'{a} / {b} = {a / b} \n'  # 3.5 - Обычное вещественное деление, результат такого деления всегда float
      f'{a} // {b} = {a // b} \n'  # 3 - Взятие только лишь целой части от деления 
      f'{a} % {b} = {a % b}')  # 1 - Взятие остатка от деления

print(123 // 10)  # 12
print(123 % 10)  # 3
print(-123 % 10)  # 7

print(10 / 2, type(10 / 2))  # 5.0 <class 'float'>

print(f'Возведем число 7 в степень 2: {7 ** 2}')
print(f'Возьмем квадратный корень от числа 16: {16 ** (1 / 2)}')  # 4.0
print(f'Возьмем кубический корень от числа 27: {27 ** (1 / 3)}')  # 3.0
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
