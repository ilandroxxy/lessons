




# Напишите программу, которая запрашивает у пользователя
# три числа и выводит следующие арифметические операции:
# разность первого и второго чисел, сумму первого и третьего числа,
# остаток от деления первого числа на второе. Результаты каждой
# операции должны быть выведены на экран, каждое на отдельной строке.
'''
a = int(input())
b = int(input())
c = int(input())
print(a - b)
print(a + c)
print(a % b)
'''

'''
a = int(input())
V = a * a * a
S = 6 * a ** 2
print(V)
print(S)
'''



# Как подключаются библиотеки
'''
import math
print(math.sqrt(16))  # 4.0
print(math.factorial(5))
print(math.prod([1, 2, 3, 4]))


import math as m  # Подключение библиотеки с кортким именем (меняем название библиотеки)
print(m.sqrt(16))
print(m.factorial(5))


from math import sqrt, factorial, prod  # Подключили только необходимые функции из библиотеки
print(sqrt(16))
print(factorial(5))


from math import *  # Подключение сразу всего содержимого библиотеки
print(sqrt(16))
print(factorial(5))
print(prod([1, 2, 3, 4, 5]))
'''


# 🔥 Очень полезные библиотеки Python для ЕГЭ по информатике #tpy

# 🐢  turtle -- для графики (№6)
'''
from turtle import *
tracer(0)
fd(100)
rt(90)
goto(50, 30)
dot(5, 'red')
done()
'''


# 🔄 itertools -- для комбинаторики (№1, 8, 9, 12, 24)
# Для этого модуля лучше импортировать только нужные функции, чтобы код оставался понятным.
'''
from itertools import product, permutations

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

for perm in permutations('abc'):
    print(''.join(perm))
    # abc
    # acb
    # bac
    # bca
    # cab
    # cba
'''


# 🌐  ipaddress -- для сетей (№13)
'''
from ipaddress import ip_network

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


# 🎭  fnmatch -- для поиска по маске (№25)
'''
from fnmatch import fnmatch

if fnmatch('12345', '12?45'):
    print('Подходит')
'''


# 🔤 string -- готовые алфавиты
'''
from string import ascii_uppercase, digits, punctuation

print(ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(digits)           # 0123456789
print(punctuation)      # !"#$%&'()*+,-./:;<=>?@[|}~
'''

#  🔣  math -- математические функции
'''
from math import *

print(sqrt(225))    # 15.0
print(ceil(7 / 2))  # 4
print(factorial(5)) # 120
'''







