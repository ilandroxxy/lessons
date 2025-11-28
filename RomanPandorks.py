# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 5
'''
RES = []
for n in range(1, 10000):
    s = f'{n:b}'
    if n % 5 == 0:
        s = s + '11'
    else:
        s = s + f'{(n // 5):b}'
    r = int(s, 2)
    if n % 2 == 0 and r > 896:
        RES.append(n)
print(min(RES))
'''
from runpy import run_path

# Номер 6
'''
# Посчитать площадь объединения фигур
print(17 * 26 + 278 * 345 - 20 * 13)

# Посчитать точки на площади объединения фигур
print(18 * 27 + 279 * 346 - 21 * 14)

import turtle as t
t.tracer(0)
t.screensize(5000, 5000)
t.left(90)
size = 15

for i in range(7):
    t.forward(17 * size)
    t.right(90)
    t.forward(26 * size)
    t.right(90)
t.up()
t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for i in range(7):
    t.forward(278 * size)
    t.right(90)
    t.forward(345 * size)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# Номер 13
'''
from ipaddress import *
net = ip_network('127.204.113.250/255.255.254.0', 0)
cnt = 0
for ip in net:
    print(ip)
    cnt += 1
    if cnt == 5:
        break

# 127.204.112.1
print(127 + 204 + 112 + 1)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 6, 8, 13, 14, 15, 16, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
