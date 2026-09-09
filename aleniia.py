

# Что такое библиотеки
'''
from math import sqrt
print(f'Возведите число 2 в 4 степень: {2 ** 4}')
print(f'Возьмите квадратный корень от числа 16: {16 ** (1/2)}')
print(f'Возьмите квадратный корень от числа 16: {sqrt(16)}')
'''


# Способы взаимодейтсвия с библиотеками
'''
import math
print(math.sqrt(16))

import math as m  # Подключение библиотеки с другим (любым) именем
print(m.sqrt(16))

from math import sqrt, prod, factorial  #   Подключение конкретный функций из библиотеки
print(sqrt(16))
print(factorial(5))

from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(prod([1, 2, 3, 4]))
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

for perm in permutations('abc'):
    print(''.join(perm))


count = 1
from itertools import product
for p in product([1,2,3], repeat=2):
    print(count, p)
    count += 1

count = 1
from itertools import *
for p in product([1,2,3], repeat=2):
    print(count, p)
    count += 1
# TypeError: unsupported operand type(s) for +=: 'type' and 'int'
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
print(punctuation)      # !"#$%&'()*+,-./:;<=>?@[}~
'''

#  🔣  math -- математические функции
'''
from math import *

print(sqrt(225))    # 15.0
print(ceil(7 / 2))  # 4
print(factorial(5)) # 120
print(gcd(36, 60))  # 12
'''
# 📎 Важно: при использовании from < . . . > import * - может произойти конфликт имен, если вы используете у себя такие же названия переменных.
#
# 🛁 На экзамене from turtle import * и from math import * помогают писать код быстрее.
# 🛁 В остальных случаях лучше использовать точечный импорт: from module import func.





# Условные операторы (или ветвление): if, elif, else

# if - если
# elif - иначе если
# else - иначе
'''
# x, y = int(input('x: ')), int(input('y: '))
x, y = 5, 5
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
print('Продолжение программы')
'''


# Логические связки: and, or, not, in, not in
'''
a, b, c = 4, 5, -6
if a > 0 and b > 0 and c > 0:
    print('AND')
if a > 0 or b > 0 or c > 0:
    print('OR')

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все выполняются')
if (a > 0) + (b > 0) + (c > 0) == 0:
    print('Никто не выполняется')
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Выполняется только два')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно выполняется')


flag = True
print(not flag)  # False
print(not not flag)  # True

a = '23432675463254'
for x in a:
    print(x, end=' ')  # 2 3 4 3 2 6 7 5 4 6 3 2 5 4
print()

a = '23432675463254'
for x in a:
    if x in '02468':
        print(x, end=' ')  # 2 4 2 6 4 6 2 4
print()

a = '23432675463254'
for x in a:
    if x not in '02468':
        print(x, end=' ')  # 3 3 7 5 3 5
print()
'''
