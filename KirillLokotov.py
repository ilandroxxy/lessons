# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Четыре вариант подключения библиотеки:
'''
M = [1, 2, 3, 4, 5]

import math
print(math.sqrt(16))

import math as m
print(m.sqrt(16))

from math import sqrt, prod, pow
print(sqrt(16))

from math import *
print(sqrt(16))
print(prod(M))
'''


'''
import turtle as t
t.left(90)  # t.lt(90)
t.forward(100)  # t.fd(100)
t.done()
'''

# Тип 6 №47315
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат, хвост опущен.
# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 6 [Вперёд 7 Направо 90 Вперёд 7 Направо 90].
#
# Определите количество точек с целочисленными координатами, лежащих внутри
# или на границе области, которую ограничивает заданная алгоритмом линия.

'''
import turtle as t  # Подключаем библиотеку с именем t
t.screensize(-5000, 5000)
t.tracer(0)  # Отключаем анимацию отрисовки (мгновенная отрисовка)
t.left(90)  # Удовлетворяем условию, чтобы повернуть голову строго вверх
l = 40  # Переменная l отвечает за масштаб отрисовки: forward, backward, goto

# Тут будем писать псевдокод
for i in range(6):
    t.forward(7 * l)
    t.right(90)
    t.forward(7 * l)
    t.right(90)

t.up()  # Поднимаем перо, чтобы не было лишний линий на рисунке
for x in range(-50, 50):  # Перебираем координаты точек (x, y)
    for y in range(-50, 50):
        t.goto(x * l, y * l)  # Прыгаем в выбранную координату учитывая масштаб l
        t.dot(3, 'red')  # Ставим точку толщины 3 и красного цвета

t.update()  # Обновляем экран для корректной работы t.tracer(0)
t.done()  # Фиксирует окно отрисовки
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ = []
# на следующем уроке:
