# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(4 + 5, type(4 + 5))  # 9 <class 'int'>

b = 5.0  # float (число с плавающей точкой) - вещественные значения (дроби)
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>

c = '5'  # str (string) - строковый тип данных, хранит в себе символы, буквы, слова, текст и тд
print(a * 4, c * 4)  # 20 5555

print('Hello ' * 4)  # Hello Hello Hello Hello
# При умножении строки на целое число, строка дублируется
print('Hello, ' + 'world!')
# Строки можно между собой конкатенировать (склеивать)

d0 = False  # bool (Boolean) - элементы Булевой алгебры (Математическая логика)
d1 = True
print(4 % 2 == 0)  # True
print('3' not in '02468')  # True

n = int(input('Введите число: '))
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
'''


# Типы данных коллекций (последовательностей)
'''
A = [1, 2, 3]   # list (список)
# 1. Могу хранить в себе неограниченное кол-во данных, любых типов (в отличие от массива)
# 2. Каждый элемент имеет свой порядковый номер - индекс
# 3. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# 4. Используя индексы элементов мы можем изменять их


# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0], M[-1])  # Выводим первый и последний элементы списка М
M[0], M[-1] = 'A', 'E'
print(M)  # ['A', 'b', 'c', 'd', 'E']


B = (1, 2, 3)  # tuple (кортеж)
# 1. Почти полностью идентичен спискам, но нельзя изменять элементы кортежа

C = {1, 2, 3}  # set (множество)
# 1. В множествах не может храниться несколько копий элементов, то есть
# все элементы множества - различные

print({1, 2, 3, 3, 4})  # {1, 2, 3, 4}
'''


'''
M = [2, 2.0, '2', True, 2+2, 4/2, '2'*2, 2 != 4, [1, 2, 3], (1, 2, 3), {1, 2, 3}]
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


A = [1, 2, 2, 3, 3, 4]
print(A, type(A))  # [1, 2, 2, 3, 3, 4] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 2, 3, 3, 4) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3, 4} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3, 4] <class 'list'>

A = list(A)
print(A, set(A))  # [1, 2, 3, 4] {1, 2, 3, 4}
'''


# Ввод данных с клавиатуры
'''
s = input('Введите текст: ')  # 56
print(s, type(s))  # 56 <class 'str'>

x = int(input('Введите число: '))
print(x, type(x))  # 56 <class 'int'>
# ValueError: invalid literal for int() with base 10: 'ergegrre'
'''


# Работа с f-строками
'''
weather = 'облачно'
temperature = int(input('Введите температуру: '))
# "Сегодня облачно, а температура 24 градуса!"
print("Сегодня ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня {weather}, а температура {temperature} градуса!")
'''


# Базовая арифметика в python
'''
a, b = 7, 2
print(f'{a} + {b} = {a+b} \n'  # \n - переход на новую строку 
      f'{a} - {b} = {a-b} \n'
      f'{a} * {b} = {a*b}')

# print(a * b)  # 14
print()  # в каждой функции print() есть переход на новую строку '\n'


print(f'{a} / {b} = {a/b} \n'   # 3.5 - Обычное вещественное деление (дроби)
      f'{a} // {b} = {a//b} \n'  # 3 - Целочисленное деление, то есть берем только целую часть 
      f'{a} % {b} = {a%b}')  # 1 - Остаток от деления (от вещественного числа)  3 целых (1/2)

n = 123
print(n % 10)  # 3 - так можно взять последнюю цифру числа
print(n % 100)  # 23 - так можно взять две последних цифры числа

n = -123
print(n % 10)  # 7
print(n % 100)  # 77 - нужно быть аккуратнее с отрицательными числами

n = -123
print(abs(n) % 10)  # 3
# abs() - взятие модуля от числа


n = 1243  # длина (кол-во разрядов 4)
print(len(str(n)))
# len() взятие длины/кол-во элементов в строке/списке/кортеже

n = -1243  # длина (кол-во разрядов 5)
print(len(str(n)))  # 5
print(len(str(abs(n))))  # 4

print()

print(f'Возведем число {a} в степень {b}: {a} ** {b} = {a ** b}')
# Возведем число 7 в степень 2: 7 ** 2 = 49


from math import sqrt
print(f'Возьмем квадратный корень от числа 16: {sqrt(16)}')
# Возьмем квадратный корень от числа 16: 4.0

print(f'Возьмем квадратный корень от числа 16: {16 ** (1/2)}')
# Возьмем квадратный корень от числа 16: 4.0

print(f'Возьмем кубический корень от числа 27: {27 ** (1/3)}')
# Возьмем кубический корень от числа 27: 3.0
'''


# Обусдим как пользоваться библиотеками
'''
import math  # Самый простой способ подключения библиотеки, но везде придется таскать math.
print(math.factorial(5))  # 120
print(math.sqrt(16))  # 4.0

import math as m  # Короткий способ подключения библиотеки с коротким именем m
print(m.sqrt(16))  # 4.0

from math import sqrt, factorial, fmod  # Подключаем конкретные функции из библиотеки
print(sqrt(16))  # 4.0

from math import *  # Подключаем сразу все содержимое
print(sqrt(16))  # 4.0
print(factorial(5))  # 120
'''

# 📌 Список полезных библиотек для успешной сдачи ЕГЭ по информатике! #tpy #useful


# 1⃣ Библиотека черепашки для решения 6 номера кодом:
'''
import turtle as t

t.tracer(0)

size = 40
for i in range(4):
    t.fd(10 * size)  # t.bk(10)
    t.rt(90)  # t.lt(90)

t.up()
t.down()

x, y = 0, 0
t.goto(x, y)
t.dot(2, 'red')

t.done()
'''

# 2⃣ Библиотека itertools для решения 1, 8, 9, 12, 24 номеров кодом:
'''
from itertools import product, permutations

combinations = list(product([1, 2, 3], repeat=2))
for combination in combinations:
    print(combination)
    # (1, 1)
    # (1, 2)
    # (1, 3)
    # (2, 1)
    # (2, 2)
    # (2, 3)
    # (3, 1)
    # (3, 2)
    # (3, 3)

perms = list(permutations("abc", r=2))
for perm in perms:
    print(''.join(perm))
    # abc
    # acb
    # bac
    # bca
    # cab
    # cba
'''

# 3⃣ Библиотека ipaddress для решения нового 13 номера:
'''
from ipaddress import *
net = ip_network('адрес узла/маска', 0)
print(net, net.netmask, net.num_addresses)
'''

# 4⃣ Две библиотеки для решения 16 номера:
'''
# Одна увеличивает глубину рекурсии:
import sys
sys.setrecursionlimit(10000)


# Вторая ускоряет вычисления через использование кэширования:
from functools import *
@lru_cache(None)
def F(n):
 '''


# 5⃣ Библиотека fnmatch для решения 25 номера с масками:
'''
from fnmatch import fnmatch
if fnmatch('123', '*?3'):
    pass
'''

# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

alphabet = string.digits + string.ascii_uppercase
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(alphabet[:16])  # 0123456789ABCDEF
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
import math as m
print(m.sqrt(16))
print(m.ceil(7/2))

print(round(5.5))  # 6 - округление по матемактике
print(m.floor(5.5))  # 5 - округляет вниз
print(m.ceil(5.2))  # 6 - округляет вверх
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
