# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# ctrl + B - открывает документацию к функциям

# Типы подключения библиотек
'''
import math  # Самый простой вариант подключения библиотеки
print(math.sqrt(16))

import math as m  # Подключаем библиотеку с коротким именем (имя любое)
print(m.sqrt(16))

from math import sqrt, factorial  # Подключение конкретных функций
print(sqrt(16))

from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(factorial(5))
'''
from email.base64mime import MISC_LEN
from string import digits

# Пример конфликта имен при подключении через *
'''
count = 0
from itertools import permutations
for p in permutations('abc'):
    count += 1
    print(count, p)
    # 1 ('a', 'b', 'c')
    # 2 ('a', 'c', 'b')
    # 3 ('b', 'a', 'c')
    # 4 ('b', 'c', 'a')
    # 5 ('c', 'a', 'b')
    # 6 ('c', 'b', 'a')


count = 0
from itertools import *
for p in permutations('abc'):
    count += 1
    print(count, p)
    # TypeError: unsupported operand type(s) for +=: 'type' and 'int'
'''


# 📌 Список полезных библиотек для успешной сдачи ЕГЭ по информатике!

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
from itertools import permutations, product

combinations = list(product("abc", repeat=2))
for combination in combinations:
    print(combination)
    # ('a', 'a')
    # ('a', 'b')
    # ('a', 'c')
    # ('b', 'a')
    # ('b', 'b')
    # ('b', 'c')
    # ('c', 'a')
    # ('c', 'b')
    # ('c', 'c')

perms = list(permutations("abc"))
for perm in perms:
    print(perm)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
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


# 5⃣ Библиотека fnmatch для решения 25 номера с масками:
'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)
'''


# 6⃣ Библиотека string хранит в себе много полезных элементов:
'''
import string
alphabet = string.ascii_uppercase
print(alphabet)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@^_`{|}~

alp36 = string.digits + string.ascii_uppercase
print(alp36[:2])  # 01
print(alp36[:8])  # 01234567
'''

# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
from math import ceil, floor, dist

print(4 / 3)  # 1.3333
print(round(4 / 3))  # 1 - округление по математике
print(ceil(4 / 3))  # 2 - округление вверх
print(floor(4 / 3))  # 1 - округление вниз

def d(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d([4, 3], [5, 6]))
print(dist([4, 3], [5, 6]))
'''


# Цикл for отвечает на запросы: "повтори N раз", "пробеги от A до B"


# Работа цикла for с функцией range()
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


for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Работа цикла for с последовательностями
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


print(len(M))  # 5 - кол-во элементов в списке M

for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()


for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''



# Цикл while отвечает на запросы: "пока условие верное - делаем действие", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
'''

# Переводы в различные системы счисления
'''
n = 8
b = 2
r = ''
while n != 0:
    r += str(n % b)
    n //= b
r = r[::-1]
print(r)
'''


# Бесконечный цикл и операторы: break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # - Прерывает итерацию (шаг) цикла
    if k == 50_000:
        exit()  # - Полностью прерывает выполнение программы
    if k == 100_000:
        break  #  - Прерывание цикла в которм мы сейчас находимся
    print(k)

print('Продолжение программы')
'''


# Простой пример использования бесконечного цикла
'''
from random import randint
from time import sleep

password = 'qwerty'
count = 1
pas = input('Введите пароль: ')
while True:
    if password == pas:
        print('Добро пожаловать!')
        break
    pas = input('Пароль неверный, повторите попытку: ')
    count += 1
    if count == 3:
        print('Проверка на робота, решите пример: ')
        a = randint(0, 100)
        b = randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            print('Проверка пройдена успешно. ')
            count = 0
        else:
            print('Повторите попытку через 5 минут')
            sleep(5 * 60)
            
print('Рабочий стол')
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
