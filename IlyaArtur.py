# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 6 https://education.yandex.ru/ege/task/0c1968f6-ce78-40ac-991c-a4f080b9e66e
'''
import turtle as t  # Подключаем библиотеку черепахи с коротким именем t
t.screensize(-2000, 2000)  # Добавляет ползунки для масштаба
t.tracer(0)  # Отключает анимацию отрисовки
t.left(90)  # По условию задачи поворачиваем голову на 90 градусов (вверх)
size = 60  # Задаем масштаб отрисовки самостоятельно

# Тут пишем псевдокод
for _ in range(6):
    t.forward(7 * size)  #
    t.right(120)
t.up()  # Поднять хвост
t.fd(3 * size)
t.rt(90)
t.down()  # Опустить хвост
for _ in range(8):
    t.fd(5 * size)
    t.rt(90)

# Тут перебираем точки
t.up()  # Перед тем как рисовать точки, уместно поднять перо
for x in range(-30, 30):  # Перебираем координаты точек x, y
    for y in range(-30, 30):
        t.goto(x * size, y * size)  # Прыгаем в координату с соблюдением масштаба size
        t.dot(3, 'red')  # Рисуем точку толщины 3 и красного цвета

t.update()  # Для корректной работы функции t.tracer(0)
t.done()  #  Фиксирует окно отрисовки, чтобы оно не закрывалось
'''


# Задание 6
# https://education.yandex.ru/ege/task/af4de739-ab1c-423f-a382-8d0a8ff7bc61
'''
print(8 * 15 + 12)

import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 60

# Тут пишем псевдокод
for _ in range(2):
    t.forward(7 * size)
    t.left(90)
    t.forward(14 * size)
    t.left(90)
t.right(225)
for _ in range(4):
    t.forward(5 * size)
    t.right(90)

# Тут перебираем точки
t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# № 17547 Основная волна 08.06.24 (Уровень: Средний)
'''
print(13 * 8 + 84 * 78 - 7 * 4)

import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 60

# Тут пишем псевдокод
for _ in range(3):
    t.forward(7 * size)
    t.right(90)
    t.forward(12 * size)
    t.right(90)
t.up()
t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for _ in range(4):
    t.forward(83 * size)
    t.right(90)
    t.forward(77 * size)
    t.right(90)

# Тут перебираем точки
t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

# № 17669 Пересдача 04.07.24 (Уровень: Базовый)

print(13 * 8 + 84 * 78 - 7 * 4)

import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 40

# Тут пишем псевдокод
for _ in range(4):
    t.forward(19 * size)
    t.right(90)
    t.forward(30 * size)
    t.right(90)
t.up()
t.forward(2 * size)
t.right(90)
t.forward(8 * size)
t.left(90)
t.down()
for _ in range(4):
    t.forward(93 * size)
    t.right(90)
    t.forward(97 * size)
    t.right(90)

# Тут перебираем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
