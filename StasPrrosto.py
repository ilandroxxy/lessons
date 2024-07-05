# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17625 Основная волна 19.06.24 (Уровень: Базовый)
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления
# оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 10 [Вперёд 22 Направо 90 Вперед 16 Направо 90]
# Поднять хвост
# Вперед 1 Направо 90 Вперёд 1 Налево 90
# Опустить хвост
# Повтори 10 [Вперёд 72 Направо 90 Вперёд 79 Направо 90]
'''
import turtle as t
t.screensize(-100000, 100000)  # Добавляем ползунки для регулирования положениря окна
t.tracer(0)  # Отключаем анимацию отрисовки
t.left(90)  # t.lt(90) - повернуть налево 90 градусов
l = 20  # Наша локальная переменная для масштаба

t.color('blue')
for _ in range(10):
    t.fd(22*l)
    t.rt(90)
    t.fd(16*l)
    t.rt(90)
t.up()
t.fd(1*l)
t.rt(90)
t.fd(1*l)
t.lt(90)

t.down()
t.color('green')  # Меняем цвет отрисовки
for _ in range(10):
    t.fd(72*l)
    t.rt(90)
    t.fd(79*l)
    t.rt(90)

t.up()  # Прежде чем наносить точки, нужно поднять перо
for x in range(-50, 50):  # Перебираем значения с координатами x и y для точек
    for y in range(-50, 50):
        t.goto(x * l, y * l)  # Прыгаем в конкретную координату с масштабом l
        t.dot(2, 'red')  # Рисуем точку толщины 2 и красного цвета

t.update()  # Обновляем анимацию (окно) для .tracer(0)
t.done()  # Зафиксировать окно отрисовки, чтобы оно не закрывалось
'''


import turtle as t
t.tracer(0)
t.left(90)
l = 30
x, y = 0, 0

for _ in range(10):
    x += 6
    y += 15
    t.goto(x * l, y * l)
    x += 4
    y += -6
    t.goto(x * l, y * l)
    x = 2
    y = 2
    t.goto(x * l, y * l)
    x += 3
    y += 9
    t.goto(x * l, y * l)

t.up()  # Прежде чем наносить точки, нужно поднять перо
for x in range(-50, 50):  # Перебираем значения с координатами x и y для точек
    for y in range(-50, 50):
        t.goto(x * l, y * l)  # Прыгаем в конкретную координату с масштабом l
        t.dot(5, 'red')  # Рисуем точку толщины 2 и красного цвета

t.update()  # Обновляем анимацию (окно) для .tracer(0)
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
