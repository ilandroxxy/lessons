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
                F = ((w == (not x)) <= (not(z <= w)) or (not y))
                if F == 0:
                    print(x, y, z, w)
'''


# № 31214 Резерв 22.06.26 (Уровень: Базовый)
'''
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
size = 20

for i in range(2):
    t.forward(21 * size)
    t.right(90)
    t.forward(27 * size)
    t.right(90)
t.up()
t.forward(9 * size)
t.right(90)
t.forward(10 * size)
t.left(90)
t.down()
t.color('blue')
for i in range(2):
    t.forward(86 * size)
    t.right(90)
    t.forward(47 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')
t.update()
t.done()

print(22 * 28 + 87 * 48 - 18 * 13)  # 4558 - Найдите точки на площади фигуры
print(21 * 27 + 86 * 47 - 17 * 12)  # 4405 - Найдите площадь фигуры
'''

'''
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
size = 20

for i in range(7):
    t.forward(12 * size)
    t.right(90)
    t.forward(20 * size)
    t.right(90)
t.up()
t.forward(1 * size)
t.right(90)
t.forward(10 * size)
t.left(90)
t.down()
t.color('blue')
for i in range(7):
    t.forward(66 * size)
    t.right(90)
    t.forward(92 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')
t.update()
t.done()
'''


# № 29959 Апробация 14.05.26 (Уровень: Базовый)
'''
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
size = 20

for _ in range(3):
    t.forward(32 * size)
    t.right(90)
    t.forward(38 * size)
    t.right(90)
t.up()
t.fd(25 * size)
t.rt(90)
t.fd(21 * size)
t.lt(90)
t.down()
t.color('blue')
for _ in range(3):
    t.forward(29 * size)
    t.right(90)
    t.backward(18 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')
t.update()
t.done()

print ((33 * 39) + (30* 19)-( 19*8 ))
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке:

