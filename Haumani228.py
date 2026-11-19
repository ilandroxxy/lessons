


# Способы подключения библиотек:
'''
import math  # Самый стандартный способ подключения библиотеки
print(math.sqrt(16))
print(math.factorial(5))

import math as m  # Способ подключение библиотеки через короткое имя
print(m.sqrt(16))
print(m.factorial(5))

from math import sqrt, factorial, prod  # Подключаем самое необходимое из библиотеки
print(sqrt(16))
print(factorial(5))

from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(factorial(5))
print(prod([1, 2, 3, 4, 5]))

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
'''


# Условные операторы if, elif, else (ветвление)
'''
n = int(input())
if n > 0:  # если
    print('Число положительное')
elif n < 0:  # иначе если 
    print('Число отрицательное')
else:  # иначе 
    print('Число равно 0')
 '''


# Логические связки: and or
'''
a, b, c = 4, 5, 6

if a > 0 and b > 0 and c > 0:
    print('and - все условия верные')

if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно условие верное')
'''






