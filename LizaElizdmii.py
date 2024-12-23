# region Домашка: ******************************************************************

# Задача 6
'''
import turtle as t
t.tracer(0)
t.screensize(-2000,2000)
l=40
t.left(90)


t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*l)
    t.right(45)
t.right(315)
t.forward(10 * l)
for i in range(2):
    t.right(90)
    t.forward(10*l)


t.up()
for x in range(-50,50):
    for y in range(-50, 50):
        t.goto(x*l,y*l)
        t.dot(4,'red')
t.update()
t.done()
'''


# Задача 8
'''
from itertools import *

cnt = 0
chet = '02468ACE'
nechet = '13579BDF'
for x in permutations('0123456789ABCDEF', 3):
    a = ''.join(x)
    if a[0] != '0':
        # if a[0] in chet and a[1] in nechet and a[2] in chet:
        #     cnt += 1
        # if a[0] in nechet and a[1] in chet and a[2] in nechet:
        #     cnt += 1
        for z in chet:
            a = a.replace(z, '2')
        for z in nechet:
            a = a.replace(z, '1')
            
        if '22' not in a and '11' not in a:
            cnt += 1

print(cnt)
'''

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
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Лиза 11/14 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

