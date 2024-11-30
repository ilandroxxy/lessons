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
                F = ((w <= y) <= x) or ((not z) and (x <= y))
                if F == 0:
                    print(x, y, z, w)
'''

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]

'''
for n in range(1, 10000):
    s = convert(n, 4)
    summa = sum([int(x) for x in s])
    if summa % 2 == 0:
        s = '31' + s + '02'
    else:
        s = '1' + s + convert((n % 3) * 7, 4)
    r = int(s, 4)
    if r < 4528:
        print(n)
'''

'''
print(135 * 122 + 149 * 75 - 9 * 94)
print(149 * 75)
print(9 * 94)

import turtle as t
t.screensize(-5000, 5000)
t.tracer(0)
t.left(90)
size = 10

for i in range(4):
    t.forward(135 * size)
    t.right(90)
    t.forward(122 * size)
    t.right(90)
t.up()
t.fd(41 * size)
t.lt(90)
t.forward(66*size)
t.right(90)
t.down()
for i in range(4):
    t.forward(149 * size)
    t.right(90)
    t.forward(75 * size)
    t.right(90)

# Тут перебираем точки

t.up()
for x in range(-30, 30):
    for y in range(-30, 150):
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
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
