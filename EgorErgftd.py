# region Домашка: ******************************************************************

# Проверка "число оканчивается на 9":
M = [int(x) for x in open('17.txt')]
D = [x for x in M if abs(x) % 10 == 9]
B = [x for x in M if str(x)[-1] == '9']

# abs() - взять модуль числа

'''
a = int(input())
b = int(input())

for i in range(a, b+1):
    if i % 20 == 0 or (i % 7 == 0 and i % 14 == 0) or abs(i) % 10 == 9:
        print(i)
'''

# Это условие лежит в основе 25 номера (поиск делителей)
'''
a = int(input())

b = 1
for i in range(1, a + 1):
    if a % i == 0:
        b *= i
print(b)
'''


"""
import time
start = time.time()

'''
def divisors(num: int) -> list:
    res = []
    for j in range(1, num + 1):
        if num % j == 0:
            res.append(j)
    return res
'''


def divisors(num: int) -> list:
    '''
    Функция поиска делителей числа num
    :param num: Принимает целое (int) число.
    :return: Возвращает список делителей от 1 до числа num
    '''
    res = []
    for j in range(1, int(num**0.5) + 1):
        if num % j == 0:
            res += [j, num // j]
            # res.append(j)
            # res.append(num // j)
    return sorted(set(res))


print(divisors(100_000_000))  # 2.9338 -> 0.00040

print(time.time() - start)

div = divisors(24)
print(div)  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
help(divisors)

# divisors(num: int) -> list
#     Функция поиска делителей числа num
#     :param num: Принимает целое (int) число.
#     :return: Возвращает список делителей от 1 до числа num
"""

'''
n = int(input())
summa = 0
count = 0
prodd = 1
while n > 0:
    summa += n % 10
    count += 1
    prodd *= n % 10
    n //= 10
print(summa, count, prodd, sep='\n')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import turtle as t
t.tracer(0)  # Отключает анимацию, то есть мгновенная отрисовка
t.left(90)  # t.lt(90) - изначально повернули голову по оси ординат (вверх)
t.down()  # Опустили перо, чтобы начать рисовать
l = 20  # Сами задаем и регулируем масштаб


# Тут пишем псевдокод алгоритма


# Тут мы пробегаем координаты x, y (учитывая масштаб) и рисуем точки .dot() красного цвета
t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''


# Тип 6 №69884
'''
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 28 Направо 90 Вперёд 26 Направо 90]
# Поднять хвост
# Вперёд 8 Направо 90 Вперёд 7 Налево 90
# Опустить хвост
# Повтори 4 [Вперёд 67 Направо 90 Вперёд 98 Направо 90].
# Определите площадь пересечения фигур, нарисованных при помощи алгоритма.

import turtle as t
t.tracer(0)
t.left(90)
t.down()
l = 20


# Тут пишем псевдокод алгоритма
for _ in range(4):
    t.forward(28 * l)  # t.fd(28 * l)
    t.rt(90)
    t.forward(26 * l)
    t.rt(90)

t.up()
t.forward(8 * l)
t.rt(90)
t.forward(7* l)
t.lt(90)
t.down()

for _ in range(4):
    t.forward(67 * l)
    t.rt(90)
    t.forward(98 * l)
    t.rt(90)


t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''


# № 17547 Основная волна 08.06.24 (Уровень: Средний)
# Повтори 3 [Вперёд 7 Направо 90 Вперёд 12 Направо 90]
# Поднять хвост
# Вперёд 4 Направо 90 Вперёд 6 Налево 90
# Опустить хвост
# Повтори 4 [Вперёд 83 Направо 90 Вперёд 77 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри
# объединения фигур, ограниченных заданными алгоритмом линиями, включая точки на
# границах этого объединения.
'''
import turtle as t
t.screensize(10000, 10000)
t.tracer(0)
t.left(90)
t.down()
l = 10


# Тут пишем псевдокод алгоритма
for _ in range(3):
    t.fd(7 * l)
    t.rt(90)
    t.fd(12 * l)
    t.rt(90)

t.up()
t.fd(4 * l)
t.rt(90)
t.fd(6 * l)
t.lt(90)
t.down()

for _ in range(4):
    t.fd(83 * l)
    t.rt(90)
    t.fd(77 * l)
    t.rt(90)


t.up()
for x in range(-80, 50):
    for y in range(-80, 50):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ  = []
# на следующем уроке:
