# region Домашка: ******************************************************************

'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                print(x, y, z, w, int(F))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Шпаргалка для решения 6 номера
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 20

# Тут пишем псевдокод:


# Тут рисуем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# Задание 6 https://education.yandex.ru/ege/task/010affd8-27b2-4067-87d8-4496e10c2627
'''
import turtle as t  # Импортировали библиотеку с коротким именем t
t.screensize(-2000, 2000)  # Добавляем ползунки регулировки масштаба окна
t.tracer(0)  # Отключает анимацию отрисовки
t.left(90)  # Поворачиваем на 90 градусов налево, по условию
size = 20  # Переменная отвечающая за масштаб отрисовки


# Тут пишем псевдокод:
for i in range(2):
    t.forward(12 * size)
    t.right(90)
    t.forward(19 * size)
    t.right(90)
t.up()
t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for i in range(2):
    t.forward(12 * size)
    t.right(90)
    t.forward(6 * size)
    t.right(90)

# Тут рисуем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):  # Перебираем координаты точек
        t.goto(x * size, y * size)  # Прыгаем в определенную точку
        t.dot(3, 'red')  # Рисуем точку толщины 3 красного цвета

t.update()  # Для корректной работы t.tracer(0)
t.done()  # Зафиксировать окно отрисовки
'''


# Задание 6 https://education.yandex.ru/ege/task/a5a6fe7c-3e0b-4e9c-9dbf-10560a973262
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 20

# Тут пишем псевдокод:
for i in range(2):
    t.forward(5 * size)
    t.right(90)
    t.forward(11 * size)
    t.right(90)
t.up()
t.backward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for i in range(2):
    t.forward(42 * size)
    t.right(90)
    t.forward(63 * size)
    t.right(90)

# Тут рисуем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

print(5 * 2 + 11 * 2 + 42 * 2 + 63 * 2 - 20)

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
