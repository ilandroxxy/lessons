# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************


#5
'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'

    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'

    r = int(s, 2)
    if n > 27:
       R.append(r)
print(min(R))
'''
from typing import is_protocol

#6
'''
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
size = 15
for i in range (4):
    t.forward(19*size)
    t.right(90)
    t.forward(30*size)
    t.right(90)
t.up()
t.forward(2*size)
t.right(90)
t.forward(8*size)
t.left(90)
t.down()
for i in range(4):
    t.forward(93*size)
    t.right(90)
    t.forward(97*size)
    t.right(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

#12
'''
s = '9' * 134
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1)
    else:
        s = s.replace('9999', '2', 1)
print(s)
'''


#16
'''
import sys
sys.setrecursionlimit(100000)
def F(n):
    if n == 1:
        return n 
    if n > 1:
        return (n - 1) * F(n - 1)
print((F(2024)//7 - F(2023))/F(2022))
'''

# 11

alp = 10+26+450  # 486
i = 9

byte = 100 * 1024 / 575
print(byte)  # 178.086 -> 179

bit = 179 * 8
sym = bit / i
print(sym)  # 159.1111


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [5, 8, 17]
# на следующем уроке:


# Второй пробник 10.02.25:
# 7/29 -> 42 вторичных баллов +[1, 4, 6, 12, 14, 15, 16] -[3, 5, 8, 23, 25]
