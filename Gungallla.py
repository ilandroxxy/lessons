# region Домашка: ******************************************************************

# (x and (not y)) or (y == z) or w
# ((y <= x) == (x <= w)) and (z or x)
# (((not x) or z) == (y and (not w))) <= (z and y)

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import turtle as t  # подключение библиотеки
t.screensize(-2000, 2000)
t.left(90)
t.tracer(0)  # отключает анимацию отрисовки
size = 20  # вводим переменную для масштаба

for i in range(8):
    t.forward(16 * size)  # движение вперед на 100 пикселей
    t.right(90)
    t.forward(22 * size)
    t.right(90)
t.up()  # поднять хвост, то есть перестать рисовать
t.forward(5 * size)
t.right(90)
t.forward(5 * size)
t.left(90)
t.down()  # опустить хвост
for i in range(8):
    t.fd(52 * size)
    t.rt(90)
    t.fd(77 * size)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)  # прыгнуть в координату
        t.dot(3, 'red')

t.update()  # для корректной работы t.tracer()
t.done()  # фиксировать окно после отрисовки
'''


# № 20817 Апробация 05.03.25 (Уровень: Средний)
'''
print(6552 + 364 - 168)  # 6748

import turtle as t
t.left(90)
t.screensize(-2000, 2000)
t.tracer(0)
size = 20

# Тут пишем псевдокод
for i in range(3):
    t.forward(27 * size)
    t.right(90)
    t.forward(12 * size)
    t.right(90)
t.up()
t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for i in range(4):
    t.forward(83 * size)
    t.right(90)
    t.forward(77 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
size = 20
t.left(90)

t.fd(25 * size)
t.rt(45)
t.fd(50 * size)

t.up()
t.bk(50 * size)
t.rt(45)
t.fd(15 * size)
t.lt(90)
t.fd(30 * size)
t.down()

t.rt(180)
t.fd(60 * size)
t.bk(5 * size)
t.rt(90)
t.fd(31 * size)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')

t.update()
t.done()


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
