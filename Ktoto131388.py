



# Условные операторы: if, elif, else
'''
n = int(input('n: '))
if n > 0:  # если
    print('Число положительное')
elif n < 0:  # иначе если
    print('Число отрицательное')
else:  # иначе
    print('Число равно 0')
'''
from os import times_result

'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, -6
if x > 0 and y > 0:
    print('Перавя четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
print('Конец программы')
'''


# Логические связки: and, or, not, in, not in, ==, !=
'''
a, b, c = 5, 6, 5

print(a == b)  # False
print(a == c)  # True

print(a != b)  # True
print(a != c)  # False

print(True + True + False + True)  # 3

if a > 0 and b > 0 and c > 0:
    print('AND - выполняются все условия')
if a > 0 or b > 0 or c > 0:
    print('OR - выолняется хотя бы одно условие')

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('выполняются все 3 условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('выолняется хотя бы одно условие')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('выолняется только одно условие')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('выолняется не более двух условий')



flag = True
print(not flag)  # False
print(not(not flag))  # True


s = 'ags12d3b43q2w534g6tvb'

for x in s:
    print(x, end=' ')  # a g s 1 2 d 3 b 4 3 q 2 w 5 3 4 g 6 t v b
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 1 2 3 4 3 2 5 3 4 6
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # a g s d b q w g t v b
print()


s = '8943132384'
print(sum([int(x) for x in s]))  # 45

s = 'ags12d3b43q2w534g6tvb'
print(sum([int(x) for x in s if x in '0123456789']))  # 33


s = 'ags12d3b43q2w534g6tvb'
# print(sum([int(x) for x in s]))  # 45
# ValueError: invalid literal for int() with base 10: 'a'
'''



# Библиотеки в Python
'''
print(f'Взять квадратный корень от числа 16: {16 ** (1/2)}')  # 4.0

import math
print(f'Взять квадратный корень от числа 16: {math.sqrt(16)}')  # 4.0
'''


# Способы подключения библиотек
'''
import math
print(math.sqrt(16))
print(math.factorial(5))


import math as m  # Подключение библиотеки с коротким именем 
print(m.sqrt(16))
print(math.factorial(5))


from math import sqrt, factorial, prod  # Подключаем определенные функции из библиотеки 
print(sqrt(16))
print(factorial(5))


from math import *  # Подключаем сразу все содержимое библиотеки 
print(sqrt(16))
print(factorial(5))
print(prod([1, 2, 3, 4]))
'''









