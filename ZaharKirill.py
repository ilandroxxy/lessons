# region Домашка: ******************************************************************
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (z == w)) or (not(y <= w))
                if F == 0:
                    print(x, y, z, w)
'''


'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        print(n)
'''

'''
import turtle as t
t.screensize(-2000, 2000)
t.left(90)
t.tracer(0)
size = 70

t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10 * size)
    t.right(45)
t.right(315)
t.forward(10 * size)
for i in range(2):
    t.right(90)
    t.forward(10 * size)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')


t.update()
t.done()
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# номер 13
'''
from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'213.168.83.190/{mask}', 0)
    if '213.168.64.0' in str(net):
        print(net, mask, 32-mask)
'''
# Ответ: 14


# номер 16
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2*n + 5 + F(n - 2)

print(F(3027) - F(3023))
# RecursionError: maximum recursion depth exceeded
'''
# Ответ: 12114

# № 17635 Основная волна 19.06.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(2025)

def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n + 1) * F(n - 1)

print((F(2024) - 3 * F(2023)) // F(2022))
'''

'''
import time
start = time.time()

def F(n):
    if n > 1_000_000:
        return n
    if n <= 1_000_000:
        return n + F(2 * n)

def G(n):
    return F(n) / n

cnt = 0
x = G(2000)
for n in range(1, 10**6):
    if G(n) == x:
        cnt += 1
print(cnt)

print(time.time() - start)
'''


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))


def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))
'''


# № 17877 Демоверсия 2025 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - 2, b) + F(a // 2, b)


print(F(38, 16) * F(16, 2))
'''


#
# № 13881 (Уровень: Базовый)
'''
def f(a, b):
    if a >= b or a == 20:
        return a == b
    return f(a + 1, b) + f(a + 3, b) + f(a * a, b)


print(f(3, 23) * f(23, 25))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 13, 14, 16, 23]
# КЕГЭ  = []
# на следующем уроке: Разбираем пробный вариант. Будет 1.5 часовое занятие


# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]
