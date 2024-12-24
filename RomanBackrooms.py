# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задача 5
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(10000, 0, -1):

    s = convert(n, 3)

    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        a = (n % 3) * 4
        s = s + convert(a, 3)

    r = int(s, 3)

    if r < 199:
        print(n)
        break
'''


# Задача 6
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 40

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
        t.dot(2, 'red')

t.update()
t.done()
'''

# Задача 8
'''
from itertools import *
cnt = 0
for p in permutations('0123456789ABCDEF', r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in '02468ACE':
            num = num.replace(x, '2')
        for x in '13579BDF':
            num = num.replace(x, '1')
        if '22' not in num and '11' not in num:
            cnt += 1

print(cnt)
'''

# № 231 (Уровень: Базовый)
'''
n = 8**820 - 2**760 + 14
print(bin(n))
print(bin(n)[2:].count('0'))
print(f'{n:b}'.count('0'))
'''


# № 306 Джобс 28.09.2020 (Уровень: Базовый)
'''
n = 36**27 + 6**18 - 19
R = []
while n > 0:
    R.append(n % 6)
    n //= 6
R.reverse()
print(R.count(0))


# Вариант 2
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


n = 36**27 + 6**18 - 19
print(convert(n, 6).count('0'))
'''


# № 17633 Основная волна 19.06.24 (Уровень: Базовый)
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for x in range(2030):
    n = 6**260 + 6**160 + 6**60 - x
    s = convert(n, 6)
    if s.count('0') == 202:
        print(x)
        break

# Вариант 2

for x in range(2030):
    n = 6**260 + 6**160 + 6**60 - x
    R = []
    while n > 0:
        R.append(n % 6)
        n //= 6
    R.reverse()
    if R.count(0) == 202:
        print(x)
        break
'''


# № 17973 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUOIPASDFGHJKLZXCVBNM')
for x in alphabet[:24]:
    A = int(f'12{x}734 ', 24)
    B = int(f'8{x}95{x}3', 24)
    C = int(f'24{x}796', 24)
    if (A + B + C) % 23 == 0:
        print((A + B + C) // 23)
'''

'''
alphabet = sorted('0123456789QWERTYUOIPASDFGHJKLZXCVBNM')
for x in alphabet[:12]:
    for y in alphabet[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            print((A + B) // 99)
'''
# 41428


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке: устанавливаем Pycharm


# Первый пробник 21.12.24:
# Стас 2/5 -> 14 вторичных баллов +[2, 12] -[5, 6, 8]
