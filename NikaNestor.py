# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import math
print(math.sqrt(16))

print(help(math.sqrt))  # - Возвращает документацию
# sqrt(x, /)
#     Return the square root of x.

# ctrl + B - показывает содержимое библиотеки/документацию к функции
'''
import copy
from email import message_from_bytes
from runpy import run_path
from traceback import print_tb

# Способы подключения библиотек
'''
import math  # - Стандартный способ подключения библиотеки
print(math.sqrt(16))

import math as m  # - Подключение библиотеки через короткое имя
print(m.sqrt(16))

from math import sqrt, factorial, pi  # - Подключаем конкретные функции и константы
print(sqrt(16))

from math import *  # - Подключение сразу всего содержимого библиотеки
print(sqrt(16))
print(pi)
'''

# Пример, почему не стоит использовать подключение через *
'''
count = 0
from itertools import permutations
for p in permutations('abc'):
    count += 1
    print(count, p)


count = 0
from itertools import *
for p in permutations('abc'):
    count += 1
    print(count, p)
'''


# Список полезных библиотек для успешной сдачи ЕГЭ по информатике!


# 1⃣ Библиотека черепашки для решения 6 номера кодом:
'''
import turtle as t

t.tracer(0)

t.fd(10)  # t.bk(10)
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

perms = list(permutations("abc"))
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
# Одна увеличивает глубину рекурсии:
'''
import sys
sys.setrecursionlimit(10000)
'''
# Вторая ускоряет вычисления через использование кэширования:
'''
from functools import *
@lru_cache(None)
def F(n):
'''

# 5⃣ Библиотеки fnmatch и re для решения 25 номера с масками и 24 номера с регулярными выражениями:
'''
from fnmatch import *
for x in range(0, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)


from re import *
for x in range(0, 10**10, 1917):
    if fullmatch('3[0-9]12[0-9]14[0-9]*5', str(x)):
        print(x, x // 1917)
'''

# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=_`{|}~

alp = string.digits + string.ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist, prod, factorial

print(4 / 3)  # 1.3333
print(ceil(4 / 3))  # 2
print(floor(4 / 3))  # 1


def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print(d([3, 4], [5, 6]))
print(dist([3, 4], [5, 6]))


print(prod([1, 2, 3, 4, 5]))  # 120
print(factorial(5))  # 120
'''


# Массивов в Пайтон нет, а есть коллекции (последовательности)

# Типы данных коллекций
'''
A = [1, 2, 3]  # list (список)
# 1. Может хранить в себе неограниченное кол-во данных
# 2. Элементы могут быть различных типов данных (в отличие от массивов)
# 3. Все элементы имеют свой порядковый номер: индекс
# 4. Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1

# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка L: {L[0]}')
print(f'Последний элемент списка L: {L[4]}')
print(f'Последний элемент списка L: {L[len(L) - 1]}')
print(f'Последний элемент списка L: {L[-1]}')


# 5. Через индексы мы можем изменять элементы списка (в отличие от кортежа, множества, строки)
L[0], L[-1] = 'e', 'a'
print(L)  # ['e', 'b', 'c', 'd', 'a']


B = (1, 2, 3)  # tuple (кортеж)
# 1. Тоже самое, что и списки, но нельзя изменять элементы


C = {1, 2, 2, 3, 3, 3}  # set (множество)
print(C)  # {1, 2, 3}
# 1. Удаляет копии элементов


D = {'один': 'one', 'два': 'two'}  # dict (словарь)
# 1. Элементы словаря состоят из двух частей: ключ и значение
# 2. Доступ к значению элемента осуществляется через ключ
print(D['один'])  # one

# 3. Ключи не могут повторяться иначе произойдет перезапись
D['один'] = 'ONE'
print(D)  # {'один': 'ONE', 'два': 'two'}

for key, value in D.items():
    print(key, value)
    # один ONE
    # два two
'''

# Элементы могут быть различных типов данных (в отличие от массивов)
'''
M = [2, 2.0, '2', True, 2+2, 7/2, '2'*2, 4<10, [1, 2, 3], (1, 2, 3), {1, 2 ,3}, {'один': 'one', 'два': 'two'}]
for x in M:
    print(type(x), x)
    # <class 'int'> 2
    # <class 'float'> 2.0
    # <class 'str'> 2
    # <class 'bool'> True
    # <class 'int'> 4
    # <class 'float'> 3.5
    # <class 'str'> 22
    # <class 'bool'> True
    # <class 'list'> [1, 2, 3]
    # <class 'tuple'> (1, 2, 3)
    # <class 'set'> {1, 2, 3}
    # <class 'dict'> {'один': 'one', 'два': 'two'}
'''


# Срезы списков, строк и других итерируемых объектов
'''
# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

# СРЕЗ[START : STOP - 1 : STEP]

print(L[1:4])  # ['b', 'c', 'd'] - Все элементы с 1 по 4 индекс (не включая конец)
print(L[:4])  # - Все элементы слева от 4 (не включая конец)
print(L[2:])  # - Все элементы начиная с 2 и до конца

print(L[2:])  # - Все элементы кроме первых двух
print(L[-3:])  # - Последние три элемента
print(L[1:-1])  # - Все кроме первого и последнего

print(L[:])
print(L[::])  # - Все элементы

print(L[::2])  # ['a', 'c', 'e'] - Все элементы с четными индексами
print(L[1::2])  # ['b', 'd'] - Все элементы с нечетными индексами

print(L[::-1])  # ['e', 'd', 'c', 'b', 'a'] - Все элементы в обратном порядке 
'''


# Функции списков
'''
L = [1, 3, 3, 3, 2, 2]
print(len(L))  # - Возвращает кол-во элементов в списке (длину списка)
print(sum(L))  # - Возвращает сумму числовых значений
print(min(L), max(L))

print(sorted(L))  # Сортирует по возрастанию
print(sorted(L, reverse=True))  # Сортирует по убыванию

print(reversed(L))  # <list_reverseiterator object at 0x10072aa70>
print(list(reversed(L)))  # [2, 2, 3, 3, 3, 1] - Разворачивает список 

print(set(L))  # Убирает копии элементов 
'''


# Все методы списков в Python, которые понадобятся на ЕГЭ


# .APPEND()
# Метод .append() используется для добавления элемента в конец списка. Пример:
'''
my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
print(my_list)  # Вывод: [1, 2, 3, 4, 5]
'''
# Можно реализовать через конкатенацию (склеивание) списков:
'''
my_list = [1, 2, 3]
my_list = [0] + my_list + [4, 5]
print(my_list)  # Вывод: [0, 1, 2, 3, 4, 5]
'''

# .REVERSE()
# Метод .reverse() изменяет порядок элементов в списке на обратный. Пример:
'''
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Вывод: [4, 3, 2, 1]
'''
# Можно записать по другому через срез:
'''
my_list = [1, 2, 3, 4]
my_list = my_list[::-1]
print(my_list)  # Вывод: [4, 3, 2, 1]
'''

# .COUNT()
# Метод .count() возвращает количество вхождений заданного элемента в список. Пример:
'''
my_list = [1, 2, 2, 3, 4, 2]
print(my_list.count(2))  # Вывод: 3
'''


# .REMOVE()
# Метод .remove() удаляет первое вхождение указанного элемента из списка. Пример:
'''
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # Первая найденная двойка
print(my_list)  # Вывод: [1, 3, 2, 4]


my_list = [1, 2, 3, 2, 4]
while 2 in my_list:
    my_list.remove(2)
print(my_list)  # [1, 3, 4]
'''

# Можно удалить элемент через его индекс используя del:
'''
my_list = [1, 2, 3, 2, 4]
del my_list[1]  # Индекс удаляемого элемента
print(my_list)  # Вывод: [1, 3, 2, 4]
'''


# .INDEX()
# Метод .index() возвращает индекс первого вхождения заданного элемента в списке. Пример:
'''
my_list = [1, 2, 3, 2, 4]
print(my_list.index(2))  # Вывод: 1
'''

# .SORT()
# Метод .sort() сортирует элементы списка по возрастанию (по умолчанию) или в обратном порядке, если передан аргумент reverse=True. Пример:
'''
my_list = [4, 1, 3, 2]
my_list.sort()
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list.sort(reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]
'''
# Скажу честно я не любитель этого метода, считаю, что удобнее будет использовать функцию sorted():
'''
my_list = [4, 1, 3, 2]
my_list = sorted(my_list)
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list = sorted(my_list, reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]

print(sorted('0123456789QWQWIEJWQIOJDWE'))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'D', 'E', 'E', 'I', 'I', 'J', 'J', 'O', 'Q', 'Q', 'Q', 'W', 'W', 'W', 'W']
'''
'''
A = [1, 2, 3]
B = A
C = A.copy()

A.clear()
print(A)
print(B)
print(C)
'''

'''
s = '238457349857'
print(map(int, s))  # <map object at 0x100a25540>
print(list(map(int, s)))  # [2, 3, 8, 4, 5, 7, 3, 4, 9, 8, 5, 7]
summa = sum(map(int, s))
print(summa)
'''


# Генераторы списков

# ГЕНЕРАТОР[что_кладем откуда_берем]
M = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ГЕНЕРАТОР[что_кладем откуда_берем при_каком_условии]
M = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

M = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

print(M)


from random import randint
n = randint(5, 15)
R = [randint(0, 100) for _ in range(n)]
print(R)

chet = [x for x in R if x % 2 == 0]
print(chet)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Генераторы списков через 17 номер 
