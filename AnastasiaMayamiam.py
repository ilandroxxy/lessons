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
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
'''

'''
from itertools import*
n = 0
for i in product(sorted('БИКНОСР'), repeat = 6):
    a = ''.join(i)
    n += 1
    if a[0] != 'Р' and a.count('Б') == 2 and a.count('К') < 2:
        print(n)
'''

'''
from sys import*
setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 1 + f(n - 1)
print(f(2024) - f(2022))
'''

'''
for x in '0123456789ABCDEFGHI':
    s1 = '83' + x + '916'
    s2 = '123' + x + '45'
    s3 = '67' + x + '89'
    s = int(s1, 19) + int(s2, 19) + int(s3, 19)
    if s % 17 == 0:
        print(s // 17)


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''


'''
for n in range(4, 10000):
    s = '5' + '2' * n
    while('52' in s or '1122' in s or '2222' in s):
        if('52' in s):
            s = s.replace('52', '11', 1)
        if('2222' in s):
            s = s.replace('2222', '5', 1)
        if('1122' in s):
            s = s.replace('1122', '25', 1)
    if sum([int(x) for x in s]) == 64:
        print(n)
'''

'''
from turtle import*
tracer(0)
left(90)
k = 20
screensize(3000, 3000)
down()
for i in range(4):
    fd(10 * k)
    rt(270)
up()
fd(3 * k)
rt(270)
fd(5 * k)
rt(90)
down()
for i in range(2 * k):
    fd(10 * k)
    rt(270)
    fd(12 * k)
    rt(270)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'red')
update()
done()
'''

'''
sym = 32
alp = 16
i = 4
bit = sym * i
print(bit / 8)
byte = bit / 8
print((byte * 16384) / 2**10)
'''

'''
def f(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

for n in range(1, 1000):
    s = f(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + f(x, 3)
    r = int(s, 3)
    if r > 150:
        print(n)
        break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке: 5, 7, 8, 9, 13, 15, 16, 19-21 (2 кучи + убывание), 25

# Первый пробник 21.12.24:
# Анастасия 9/29 -> 48 вторичных баллов +[1, 2, 4, 12, 16, 14, 15, 23, 20-21] -[3, 8, 10, 11, 18, 19]
