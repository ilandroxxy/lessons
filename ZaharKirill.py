# region Домашка: ******************************************************************

# № 9149 (Уровень: Базовый)
# Логическая функция F задаётся выражением:
# F = ((x → y) ∨ (z ≡ x)) ∧ (w → z)
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) or (z == x)) and (w <= z)
                print(x, y, z, w, int(F))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 70

# Тут пишем псевдокод:


# Тут перебираем точки:
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')


t.update()
t.done()
'''


# Задание 6 https://education.yandex.ru/ege/task/f66464da-e0e7-410b-80b2-e82b651747e1
'''
import turtle as t  # Импортируем библиотеку с коротким именем t
t.screensize(-2000, 2000)  # Позволяет добавить ползунки масштаба
t.tracer(0)  # Отключает анимацию отрисовки
t.left(90)  # Поворачиваем налево, по условию задачи
size = 70  # Задаем масштаб отрисовки

# Тут пишем псевдокод:
t.forward(9 * size)  # Вперед 3 * size пикселей
t.right(90)  # Поворот на 90 градусов
for i in range(2):
    t.forward(3 * size)
    t.right(90)
    t.forward(3 * size)
    t.right(270)
for i in range(2):
    t.forward(3 * size)
    t.right(90)
t.forward(9 * size)

# Тут перебираем точки:
t.up()  # Поднять перо
for x in range(-50, 50):  # Перебираем координаты точек
    for y in range(-50, 50):
        t.goto(x * size, y * size)  # Прыгнуть в координату x, y
        t.dot(3, 'red')  # Рисуем точку толщины 3 и красного цвета


t.update()  # Для корректной работы t.tracer(0)
t.done()  # Фиксирует окно отрисовки
'''


# Задание 6 https://education.yandex.ru/ege/task/0c1968f6-ce78-40ac-991c-a4f080b9e66e
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 70

# Тут пишем псевдокод:
for i in range(6):
    t.forward(7 * size)
    t.right(120)
t.up()
t.forward(3 * size)
t.right(90)
t.down()
for i in range(8):
    t.forward(5 * size)
    t.right(90)

# Тут перебираем точки:
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')


t.update()
t.done()
'''


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
