


# Условные операторы: if, elif, else (ветвление)
'''
n = int(input('n: '))
if n > 0:  # если
    print('Число положительное')
elif n < 0:  # иначе если
    print('Число отрицательное')
else:  # иначе
    print('Число равно нулю')
   '''
from tkinter import image_names

'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, -5
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторя четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Лежит на осях')
print('Конец программы')
'''



# Логические связки: and, or, not, in, not in, ==, !=
'''
a, b, c = 5, 6, 5

print(a == c)  # True
print(a == b)  # False

print(a != b)  # True
print(a != c)  # False

print(72 % 2 == 0)  # True
print(73 % 2 == 0)  # False

if a > 0 and b > 0 and c > 0:
    print('AND - выполняются все условия')
if a > 0 or b > 0 or c > 0:
    print('OR - выполняется хотя бы одно из условий')

print(b > 0)  # True
print(True + True + False + True)  # 3

if (a > 0) + (b > 0) + (c > 0) == 1:
    print("Только одно условие выполняется")
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Выполняются все условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Выполняется хотя бы одно из условий')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Выполняется не больше двух условий')


flag = True
print(not flag)  # False
print(not(not flag))  # True


s = '2iu34hj23ui4h2'

for x in s:
    print(x, end=' ')  # 2 i u 3 4 h j 2 3 u i 4 h 2
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 2 3 4 2 3 4 2
print()

for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # i u h j u i h
print()



s = '43290384092'
print(sum([int(x) for x in s]))  # 44

s = '43sd2903few8409wte2'
# print(sum([int(x) for x in s]))  # ValueError: invalid literal for int() with base 10: 's'
print(sum([int(x) for x in s if x in '0123456789']))  # 44
'''


print(f'Квадратный корень от числа 16: {16 ** (1/2)}')

import math
print(f'Квадратный корень от числа 16: {math.sqrt(16)}')


# Способы подключения библиотек
'''
# Вариант 1
import math
print(math.pi)
print(math.sqrt(16))


# Вариант 2
import math as m  # Подключение библиотеки через короткое имя
print(m.pi)
print(m.sqrt(16))


# Вариант 3
from math import sqrt, pi, factorial  # Подключил опредленные функции из библиотеки
print(pi)
print(sqrt(16))


# Вариант 4
from math import *  # Подключение сразу всего содержимого
print(pi)
print(sqrt(16))
print(factorial(5))
'''








