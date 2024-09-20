# region Домашка: ******************************************************************

# Произведение и сумма цифр пятизначного числа
'''
n = 123
print(n // 100)  # 1
print((n // 10) % 10)  # 2
print(n % 10)  # 3

p = int(input())
a = p // 10000
b = (p // 1000) % 10
c = (p // 100) % 10
d = (p // 10) % 10
e = p % 10

print(a * b * c * d * e)
print(a + b + c + d + e)
'''

'''
# i  01234
s = '34256'
print(int(s[0]))  # 3

A = input()  # 34256

a = int(A[0])
b = int(A[1])
c = int(A[2])
d = int(A[3])
e = int(A[4])
print(a * b * c * d * e)
print(a + b + c + d + e)
'''

'''
import string
print(string.digits)  # 0123456789
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase  
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
alphabet = sorted('01234567890QWERTYUIOPASDFGHJKLZXCVBNM')

M = []
for x in input():
    if x.isdigit() and x in '02468':
        M.append(int(x))
print(M)

M = [int(x) for x in input() if x.isdigit() and x in '02468']
print(M)

from math import *
M = [int(x) for x in input()]
print(prod(M))
print(sum(M))
'''

# PEP8 - общепринятые нормы по оформлению кода на Пайтон

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Способы взаимодействия с библиотеками
'''
M = [1, 2, 3, 4, 5]

import math
print(math.prod(M))  # 120


import math as m  # Подключили библиотеку math и переименовали ее в m
print(m.prod(M))  # 120


# ctrl + B - поиск по библиотекам/функциям python
from math import prod, sqrt  # Импортировали только определенные функции/константы
print(prod(M))  # 120


from math import *  # Импортировали сразу все содержимое библиотеки
print(prod(M))  # 120
print(sqrt(16))  # 4.0
'''


# 📌 Список полезных библиотек для успешной сдачи ЕГЭ по информатике! #tpy #useful

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

combinations = list(product("abc", repeat=3))
for combination in combinations:
    print(''.join(combination))
    # aaa
    # aab
    # aac
    # aba
    # abb
    # abc
    # aca
    # acb
    # acc
    # baa
    # bab
    # bac
    # bba
    # bbb
    # bbc
    # bca
    # bcb
    # bcc
    # caa
    # cab
    # cac
    # cba
    # cbb
    # cbc
    # cca
    # ccb
    # ccc


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
'''
# Одна увеличивает глубину рекурсии:
import sys
sys.setrecursionlimit(10000)


# Вторая ускоряет вычисления через использование кэширования:
from functools import *
@lru_cache(None)
def F(n):
    pass
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


# Условные операторы (ветвление): if, elif, else

# if - если
# elif - иначе если
# else - иначе

# x = int(input('x: '))
# y = int(input('y: '))
'''
x, y = -5, 6

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print('Лежит на осях')

print('Продолжение программы')
'''

# Логические связки: and, or, in, not, ^, !=, ==
'''
flag = True
print(not flag)  # False
print(not (not flag))  # True

s = '2132134231'
for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 2 4 2
print()

a, b, c = 5, -6, 7
if a > 0 and b > 0:
    print(1)  # and - гарантирует, что все условия выполняются
if a > 0 or b > 0:
    print(2)  # or - говорит о том, что хотя бы одно верно
if (a > 0) ^ (b > 0):
    print(3)  # ^, != - гарантируют, что только одно выполняется
if (a > 0) != (b > 0):
    print(3)
    
print(True + True + False)  # 2

a, b, c = 5, -6, 7
#    True  +  False  +  True
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только два условия выполняются')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух выполняются')
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
