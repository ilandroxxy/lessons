# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# print((28 * 13) + (84 * 78) - (7 * 24))  # 6748

'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 30

for i in range(3):
    t.fd(27 * size)
    t.rt(90)
    t.fd(12 * size)
    t.rt(90)
t.up()
t.fd(4 * size)
t.rt(90)
t.fd(6 * size)
t.lt(90)
t.down()
for i in range(4):
    t.fd(83 * size)
    t.rt(90)
    t.fd(77 * size)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

'''
from turtle import *
screensize(-5000, 5000)
tracer(0)
l = 10
up()

rt(270)
fd(350 * l)
rt(270)
fd(50 * l)
rt(180)
down()
for i in range(20):
    fd(530 * l)
    rt(90)
    fd(380 * l)
    rt(90)
up()
rt(90)
fd(10 * l)
rt(90)
fd(20 * l)
rt(270)
down()
for i in range(32):
    fd(830 * l)
    rt(270)
    fd(530 * l)
    rt(270)
up()

for x in range(-50, 50):
    for y in range(-50,50):
        goto(x * l, y * l)
        dot(3, 'red')
update()
done()
'''


# № 19889 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(902714+1, 10**10):
    d = [j for j in divisors(x) if j != 5 and j % 10 == 5]
    if len(d) > 0:
        print(x, min(d))
        input()
'''


# № 19779 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(55_000_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0 and j % 1000 == 777]
    if len(d) > 0:
        print(x, min(d))
        input()
'''


# № 18591 (Уровень: Средний)
# – символ «Н» означает ровно одну нечётную цифру;
# – символ «Ч» означает ровно одну чётную цифру.
# Ч9?23?*23НЧ
'''
from fnmatch import *
for x in range(1984, 10**10, 1984):  # делящиеся на 1984 без остатка.
    if fnmatch(str(x), '?9?23?*23??'):
        if str(x)[0] in '2468' and str(x)[-1] in '02468':
            if str(x)[-2] in '13579':
                print(x, x // 1984)
'''
# 491234 2336
# ?9?23?*23??

# ?: 0123456789
# *: 00008 0000 00 _


# № 5642 (Уровень: Средний)
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

for x in range(500_000+1, 10**10):
    d = [j for j in divisors(x) if fnmatch(str(j), '*1?3')]
    if len(d) == 3:
        print(x, max(divisors(x)))
        input()
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 22, 24.1 повторять

# Второй пробник 28.02.25:
# Дарья 10/29 -> 51 вторичных баллов +[1, 2, 4, 7, 10, 11, 13, 15, 16, 18] -[3, 6, 12, 22]

