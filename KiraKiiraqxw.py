# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (x == z) or w
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 6 №47301
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления
# оси ординат, хвост опущен.
# Повтори 5 [Вперёд 7 Направо 120].

# Определите, сколько точек с целочисленными координатами
# будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом.
# Точки на линии учитывать не следует.
'''
import turtle as t  # Импортируем библиотеку с коротким именем t
t.tracer(0)  # Отключает анимацию отрисовки (мгновенная отрисовка)
size = 70  # Переменная для регулирования масштаба отрисовки
t.left(90)

for i in range(5):  # Повтори 5
    t.forward(7 * size)  # Вперёд 7
    t.right(120)  # Направо 120

t.up()  # Поднять хвост перед перебором точек
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()  # Для корректной работы t.tracer(0)
t.done()  # Фиксирует окно отрисовки
'''


# Тип 6 №47406
'''
import turtle as t  
t.tracer(0)  
size = 80
t.left(90)

# тут пишем псевдокод
for i in range(4):
    t.forward(12 * size)
    t.right(90)

for i in range(3):
    t.forward(12 * size)
    t.right(120)

# тут перебираются точки
t.up()  
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')

t.update()  
t.done()
'''


# https://education.yandex.ru/ege/task/9cf4b3b6-bed0-4c41-99fe-c1f6b8c80b19
'''
import turtle as t
t.tracer(0)
size = 40

t.left(40)
for i in range(5):
    t.left(95)
    t.forward(12 * size)
    t.left(45)
    t.forward(8 * size)
    t.left(40)

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
