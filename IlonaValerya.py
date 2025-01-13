# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1, 10000):
    s = convert(n, 3)
    s = s.replace('2', '*')
    s = s.replace('0', '2')
    s = s.replace('*', '0')
    r = int(s, 3)
    res = abs(n - r)
    if res == 378:
        print(n)
        break
'''


# Черепаха выполнила следующую программу:
#
# Повтори 3 [Вперёд 11 Направо 90 Вперёд 24 Направо 90]
# Поднять хвост
# Вперёд 2 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 3 [Вперёд 6 Налево 90 Вперёд 9 Налево 90]
#
# Определите, сколько точек с целочисленными координатами
# будут находиться внутри объединения фигур, ограниченных
# заданными алгоритмом линиями,
# включая точки на границах этого объединения.
'''
import turtle as t
t.screensize(-2000, 2000)
t.left(90)
t.tracer(0)
size = 40


# тут будет псевдокод
for i in range(3):
    t.forward(11 * size)
    t.right(90)
    t.forward(24 * size)
    t.right(90)
t.up()
t.forward(2 * size)
t.right(90)
t.forward(5 * size)
t.left(90)
t.down()
for i in range(3):
    t.forward(6 * size)
    t.left(90)
    t.forward(9 * size)
    t.left(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')

t.update()
t.done()
'''

'''
s = '0123456789AB'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        num = a + b + c + d + e + f
                        if a != '0':
                            if num.count('B') == 1:
                                chet = [x for x in num if x in '02468A']
                                nechet = [x for x in num if x in '13579B']
                                if len(chet) == len(nechet):
                                    cnt += 1
print(cnt)
'''


#
# № 17862 Демоверсия 2025 (Уровень: Базовый)
'''
s = '0123456789AB'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if num.count('7') == 1:
                            D = [x for x in num if x > '8']
                            if len(D) <= 3:
                                cnt += 1
print(cnt)
'''


# № 18928 Новогодний вариант 2025 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('192.168.248.176/255.255.255.240', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') == s.count('0'):
        cnt += 1
print(cnt)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
