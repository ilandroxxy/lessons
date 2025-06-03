# region Домашка: ******************************************************************

'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


L = []
for n in range(1, 10000):
    s = convert(n, 4)
    print(s)
    if sum(map(int, s)) % 2 == 0:
        s = '31' + s + '02'
    else:
        s = '1' + s + convert(((n % 3) * 7), 4)

    r = int(s, 4)
    if r < 4528:
        L.append(n)
print(max(L))


def ch(x, b):
    s = ''
    while x > 0:
        s = str(x % b) + s
        x = x // b
    if s == '':
        return '0'
    return s

res = []
for n in range(1, 10000):
    s = ch(n, 4)
    if sum(int(e) for e in s) % 2 == 0:
        s = '31' + s + '02'
    else:
        s = '1' + s + ch((n % 3) * 7, 4)
    r = int(s, 4)
    if r < 4528:
        res.append(n)
print(max(res))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#8
'''
n = 0
from itertools import *
for p in product('012345678', repeat = 5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('3')==2:
            for x in '1357':
                num = num.replace(x, '*')
            if '*2' not in num and '2*' not in num and '*2*' not in num:
                n+=1
print(n)
'''



#6

print(21*21 + 21*25 - 11*15)

import turtle as t
t.screensize(2000, 2000)
size = 30
t.tracer(0)
t.left(90)


for i in range(4):
    t.fd(20*size)
    t.right(270)

t.up()
t.fd(6*size)
t.right(270)
t.fd(10 * size)
t.right(90)
t.down()

for i in range(2):
    t.fd(20*size)
    t.right(270)
    t.fd(24*size)
    t.right(270)
t.up()

for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*size, y*size)
        t.dot(3, 'red')

t.update()
t.done()

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Egor 7/10 -> 40 вторичных баллов +[1, 4, 5, 10, 12, 13] -[2, 6, 8]

# Второй пробник 28.02.25:
# Egor 12/16 -> 56 вторичных баллов +[1-4, 6, 7, 11-14, 16, 23] -[5, 8, 10, 15]
