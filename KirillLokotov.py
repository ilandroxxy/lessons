# region Домашка: ************************************************************

'''
M = [2, 2.0, '2', True, 2+2, 4/2, '2'*2, 2<4, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'один': 'one', 'два': 'two'}]
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
    # <class 'dict'> {'один': 'one', 'два': 'two'}
'''


'''
# x = int(input())
x = 23453
print(x % 10)  # 3
x = x // 10  # x //= 10
# x = 2345
print(x % 10)  # 5
x = x // 10
# x = 234
'''

'''
x = int(input())
a = x // 10000
b = (x // 1000) % 10
c = (x // 100) % 10
d = (x // 10) % 10
e = x % 10
print(a * b * c * d * e)
print(a + b + c + d + e)
'''

'''
s = int(input())
A = []
for i in str(s):
    A.append(int(i))
a = A[0]
b = A[1]
c = A[2]
d = A[3]
e = A[4]
print(a * b * c * d * e)
print(a + b + c + d + e)
'''

'''
# Генератор списков, который принимает строку и выводит из нее только четные цифры
print([int(x) for x in list(input()) if int(x) % 2 == 0])
'''


# A = tuple(input())
# a = int(A[0])
# b = int(A[1])
# c = int(A[2])
# d = int(A[3])
# e = int(A[4])
# print (a * b * c * d * e)
# print (a + b + c + d + e)

'''
from math import prod  
M = [int(x) for x in input()]
print(prod(M))  # возвращает произведение элементов последовательности
print(sum(M))
'''

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Способы импортирования библиотек в Python
'''
M = [2, 3, 4]

import math
print(math.prod(M))  # 24

import math as m  # Дали библиотеке math сокращенное имя m
print(m.prod(M))  # 24

from math import prod, gcd, sqrt  # Импортировали конкретные функции из библиотеки math
print(prod(M))  # 24
print(gcd(24, 4))  # 4

from math import *  # Импортировали сразу все функции
print(prod(M))  # 24
print(gcd(24, 4))  # 4
'''


# 📌 Список полезных библиотек для успешной сдачи ЕГЭ по информатике! #tpy #useful

#  1⃣ Библиотека черепашки для решения 6 номера кодом:
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

# 2⃣ Библиотека itertools для решения 1, 2, 8, 9, 12, 24 номеров кодом:
'''
from itertools import product
from itertools import permutations

combinations = list(product([1, 2, 3], repeat=2))
for combination in combinations:
    print(combination)

perms = list(permutations("abc"))
for perm in perms:
    print(''.join(perm))
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
'''


# 7⃣ Библиотека math хранит в себе много полезных математических функций:
'''
import math as m
print(m.sqrt(16))
print(m.ceil(7/2))
'''

# Условные операторы: if, elif, else

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -5, 6
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежат на осях')
'''

# Логические операторы: not, or, and, ^, !=
'''
d = True
print(not d)  # False
print(not(not d))  # True

a, b = 5, -7
if a > 0 and b > 0:  # and - гарантирует, что выполняются все условия
    print('YES 1')
if a > 0 or b > 0:  # or - говорит о том, что выполняется хотя бы одно условие
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^, != - гарантируют, что только одно условие выполняется 
    print('YES 3')
if (a > 0) != (b > 0):
    print('YES 3')

a, b, c = 5, -7, 6
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более более двух выполняются')
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:
