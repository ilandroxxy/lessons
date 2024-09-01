# region Домашка: ******************************************************************

'''
from itertools import *
cnt = 0
for p in product(sorted('СОТОЧКА'), repeat = 7):
    slovo = ''.join(p)
    slovo = slovo.replace('А', 'О')
    if 'ОО' in slovo:
        cnt += 1
print(cnt)
'''

'''
from itertools import *
cnt = set()
for p in permutations('СОТОЧКА'):
    slovo = ''.join(p)
    if 'ОО' in slovo or 'АО' in slovo or 'ОА' in slovo:
        cnt.add(slovo)
print(len(cnt))
'''
# 'СОТОЧКА' 'СОТОЧКА'

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import turtle as t
t.screensize(-10000, 10000)
t.tracer(0)
t.left(90)
l = 30

# Тут будет псевдокод
for i in range(9):
    t.forward(22 * l)
    t.right(90)
    t.forward(6 * l)
    t.right(90)
t.up()
t.fd(1 * l)
t.rt(90)
t.fd(5 * l)
t.lt(90)
t.down()
for i in range(9):
    t.fd(53 * l)
    t.rt(90)
    t.fd(75 * l)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(3, 'red')

t.done()
'''


# 12?34?5 -> 1233475
# 12*34 -> 1234 -> 12999934 -> 12000034
'''
from fnmatch import *
for x in range(1991, 10**10, 1991):
    if fnmatch(str(x), '1*4182?7'):
        print(x)

'''

# Функция поиска делителей
'''
import time
start = time.time()

# def divisors(x):
#     div = []
#     for j in range(1, x+1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)
# 2.884568929672241 -> 0.0005
'''


# № 6061 (Уровень: Средний)
'''
from fnmatch import *


def prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(10**7):
    if fnmatch(str(x), '34?8*9'):
        d = [i for i in divisors(x) if prime(i)]
        if len(d) > 4:
            print(x, max(d))
'''


# № 17879 Демоверсия 2025 (Уровень: Базовый)

def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


cnt = 0
for x in range(800_000+1, 10**10):
    d = divisors(x)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break

# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 12, 13, 14]
# КЕГЭ  = []
# на следующем уроке:
