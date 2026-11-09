# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************




# Способы подключения библиотек
'''

print(f'Возведение в степень: {2 ** 4}')  # 16
print(f'Взятие квадратного корня: {16 ** (1 / 2)}')  # 4.0
print(f'Взятие кубического корня: {27 ** (1 / 3)}')  # 3.0



import math  # Самое стадратное подключение библиотеки в python
print(math.sqrt(16))


import math as m  # Подключили библиотеку с коротким именем m
print(m.sqrt(16))


from math import sqrt, factorial, prod  # Мы подключили только часть функций из библиотеки
print(sqrt(16))
print(factorial(5))


from math import *  # Подключение сразу всего содержимого
print(sqrt(16))
print(factorial(5))
print(prod([1, 2, 3, 4, 5]))
'''


# Пример конфликта имен
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


# 🔥 Очень полезные библиотеки Python для ЕГЭ по информатике

# 🐢 turtle - графика (№6)
# Позволяет рисовать траекторию исполнителя, перемещаться по координатной плоскости и отмечать точки.
'''
import turtle as t

t.tracer(0)
t.fd(100)
t.rt(90)
t.goto(50, 30)
t.dot(5, 'red')
t.update()
t.done()
'''

# 🔄 itertools - комбинаторика (№8/1/9/17/24/25)
# product() перебирает последовательности с повторениями, а permutations() - перестановки без повторений.
'''
from itertools import product, permutations

for x in product('123', repeat=10):
    print(''.join(x))
# 11, 12, 13, 21, 22, 23, 31, 32, 33

for x in permutations('ABC', r=3):
    print(''.join(x))
# ABC, ACB, BAC, BCA, CAB, CBA
'''

# ⚠️ Важно! При использовании from itertools import * можно случайно перезаписать переменную count.
# ⠀
# 📎 Подробно разбирал эту ошибку в отдельном посте (https://t.me/informatika_kege_itpy/1213).



# 🌐 ipaddress - компьютерные сети (№10)
# Позволяет определить адрес сети, маску подсети и количество IP-адресов.
'''
from ipaddress import ip_network

net = ip_network('192.168.1.64/26', strict=False)

print(net)                # 192.168.1.64/26
print(net.netmask)        # 255.255.255.192
print(net.num_addresses)  # 64
'''


# 🤔 sys + functools - рекурсия (№16)

# setrecursionlimit()
# Увеличивает допустимую глубину рекурсии.
# ⠀
# lru_cache()
# Запоминает результаты вычислений, чтобы не считать одно и то же повторно.
'''
from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10000)

@lru_cache(None)
def F(n):
    if n <= 3:
        return n
    return F(n - 1) + F(n - 3)
'''

# 🎭 fnmatch и re - поиск по маске (№24, №25)⠀
# Библиотека fnmatch позволяет искать числа по маске. Символ ? обозначает один произвольный символ,
# а * - любую последовательность символов, в том числе пустую.

# Пример: найдём числа до 10⁸, соответствующие маске 1234*54 и делящиеся на 21.
'''
from fnmatch import fnmatch
for x in range(21, 10**8, 21):
    if fnmatch(str(x), '1234*54'):
        print(x, x // 21)
'''
# 📎 Альтернативный вариант через re:
'''
from re import fullmatch
for x in range(21, 10**8, 21):
    if fullmatch(r'1234[0-9]*54', str(x)):
        print(x, x // 21)
'''
# Библиотека re даёт больше возможностей для составления шаблонов и особенно полезна в №24.


# 🔤 string - готовые алфавиты (№5, №14)
# Не нужно вручную выписывать цифры и буквы. В Python уже существуют готовые наборы символов.
'''
from string import digits, ascii_uppercase, punctuation

alp = digits + ascii_uppercase

print(alp[:2])  # 01
print(alp[:8])  # 01234567
print(alp)      # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(ascii_uppercase)  # ABC...XYZ
print(digits)           # 0123456789
print(punctuation)      # Знаки пунктуации
'''


# 🔣 math - математические функции
# ⠀
# Библиотека содержит полезные функции для округления чисел, вычисления произведений и расстояний между точками.
'''
from math import ceil, floor, prod, dist

print(ceil(7 / 2))   # 4
print(floor(7 / 2))  # 3

print(sum([1, 2, 3, 4, 5]))   # 15
print(prod([1, 2, 3, 4, 5]))  # 120

print(dist((0, 0), (3, 4)))   # 5.0
'''
# 📎 Обратите внимание на несколько моментов:
# ⠀
# 1️⃣ ceil() округляет вверх, а floor() вниз.
# ⠀
# 2️⃣ prod() вычисляет произведение элементов, а sum() их сумму.
# ⠀
# 3️⃣ dist() вычисляет расстояние между точками. Особенно полезно в №27 при работе с кластерами.
# ⠀
# ⚠️ Не путайте round() с обычным округлением половины вверх!
# Например, round(2.5) вернёт 2, а round(3.5) вернёт 4.



# Условные операторы if, elif, else
'''
n = int(input('n: '))
if n > 0:  # ЕСЛИ 
    print('Число положительное')
elif n < 0:  # ИНАЧЕ ЕСЛИ 
    print('Число отрицательное')
else:  # ИНАЧЕ
    print('Число равно нулю')
'''

'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Число лежит на осях')
'''


# Логические связки: and, or, not, in, not in, ==, !=

a, b, c = 4, 5, -4  # = - присваивание значения элементам

# == - сравнение (равны ли элементы)
print(a == b)  # False
print(a == c)  # True

# != - сравнение (не равны ли элементы)
print(a != b)  # True
print(a != c)  # False

if a > 0 and b > 0 and c > 0:
    print('and - проверяет, что все перечисленные элементы верные')
if a > 0 or b > 0 or c > 0:
    print('or - проверяет, что хотя бы одно условие верное')

if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Выполняется только два условия')
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Выполняются все условия')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Выполняются хотя бы одно условие')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Выполняются не более двух условий')

print(True + True + True + False)  # 3
print( 1   +   1  +   1  +    0)  # 3


s = 'k3j4h3kjh34jh5'

for x in s:
    print(x, end=' ')  # k 3 j 4 h 3 k j h 3 4 j h 5
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 3 4 3 3 4 5
print()


for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # k j h k j h j h
print()


s = '42378'
summa = 0
for x in s:
    summa += int(x)
print(summa)  # 24

s = '42f 37.8'
summa = 0
for x in s:
    if x in '0123456789':
        summa += int(x)
print(summa)  # 24



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [18]
# КЕГЭ = []
# todo на следующем уроке: циклы while и for 
