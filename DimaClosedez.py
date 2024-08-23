# region Домашка: ******************************************************************
'''
maxi = 0
mini = 10**9
n = int(input())  # 3267
while n > 0:
    x = n % 10
    if maxi < x:
        maxi = x
    if mini > x:
        mini = x
    n //= 10
print(maxi)
print(mini)
'''

'''
maxi = 0
mini = 10**9
n = int(input())  # 3267
while n > 0:
    x = n % 10
    maxi = max(maxi, x)
    mini = min(mini, x)
    n //= 10
print(maxi)
print(mini)
'''

'''
n = int(input())
print(max(str(n)))
print(min(str(n)))
'''

'''
n = int(input())
total = 1  # произведение
summa = 0
count = 0
while n > 0:
    x = n % 10
    total *= x
    summa += x
    count += 1
    n //= 10
print(summa)
print(count)
print(total)
'''

'''
from math import prod

n = int(input())
N = [int(x) for x in str(n)]
print(sum(N))
print(len(N))
print(prod(N))
'''

'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# M = [1, 2, 3, 2, 3, 4]
# print(set(M))  # {1, 2, 3, 4}


# № 17547 Основная волна 08.06.24 (Уровень: Средний)
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат, хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 3 [Вперёд 7 Направо 90 Вперёд 12 Направо 90]
# Поднять хвост
# Вперёд 4 Направо 90 Вперёд 6 Налево 90
# Опустить хвост
# Повтори 4 [Вперёд 83 Направо 90 Вперёд 77 Направо 90]
'''
import turtle as t
t.tracer(0)  # Отключаем анимацию отрисовки
t.screensize(-10000, 10000)
t.left(90)
l = 40

# Тут мы будем писать псевдокод:

for i in range(3):
    t.forward(7 * l)
    t.right(90)
    t.forward(12 * l)
    t.right(90)

t.up()  # Поднять хвост

t.fd(4 * l)
t.rt(90)
t.fd(6 * l)
t.lt(90)

t.down()  # Опустить хвост

for i in range(4):
    t.fd(83 * l)
    t.rt(90)
    t.fd(77 * l)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(2, 'red')

t.update()
t.done()
'''


# № 17625 Основная волна 19.06.24 (Уровень: Базовый)
# Повтори 10 [Вперёд 22 Направо 90 Вперед 16 Направо 90]
# Поднять хвост
# Вперед 1 Направо 90 Вперёд 1 Налево 90
# Опустить хвост
# Повтори 10 [Вперёд 72 Направо 90 Вперёд 79 Направо 90]

import turtle as t
t.tracer(0)  # Отключаем анимацию отрисовки
t.screensize(-10000, 10000)
t.left(90)
l = 40

# Тут мы будем писать псевдокод:
for i in range(10):
    t.fd(22*l)
    t.rt(90)
    t.fd(16 * l)
    t.rt(90)
t.up()
t.fd(1*l)
t.rt(90)
t.fd(1 * l)
t.lt(90)
t.down()
t.color('green')
for i in range(10):
    t.fd(72*l)
    t.rt(90)
    t.fd(79 * l)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(4, 'red')

t.update()
t.done()



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


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
