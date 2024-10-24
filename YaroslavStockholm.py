# region Домашка: ******************************************************************

'''
(x <= y) or (not(w <= z))

((x and (not y)) or (w <= z)) == (z == x)

((y or z) <= (z and w)) == (not((x and z) <= (w or y)))
'''


# № 18483 (Уровень: Базовый)
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w, int(F))
'''

'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) or (z == x)) and (w <= z)
                if F == 0:
                    print(x, y, z, w, int(F))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) or (z == x)) and (w <= z)
                if F == 1:
                    print(x, y, z, w, int(F))
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 6 №68507
# В начальный момент Черепаха находится B начале координат,
# её голова направлена вдоль положительного направления оси ординат, хвост опущен.

import turtle as t  # Подключаем библиотеку с коротким именем t
t.screensize(-2000, 2000)
t.tracer(0)  # Отключение анимации (мгновенная отрисовка)
t.left(90)
t.down()
l = 20

# Черепахе был дан для исполнения следующий алгоритм:
for i in range(2):  # Повтори 2 [Вперёд 21 Направо 90 Вперёд 27 Направо 90]
    t.forward(21 * l)
    t.right(90)
    t.forward(27 * l)
    t.right(90)
t.up()  # Поднять хвост
t.fd(9 * l)  # Вперёд 9 Направо 90 Вперёд 10 Налево 90
t.rt(90)
t.fd(10 * l)
t.lt(90)
t.down()  # Опустить хвост
for i in range(2):
    t.fd(86 * l)
    t.rt(90)
    t.fd(47 * l)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(3, 'red')

t.update()  # для корректной работы t.tracer(0)
t.done()  # Фиксирует окно отрисовки


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
