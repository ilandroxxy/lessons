# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print(f'Объединение фигур: {77 * 101 + 88 * 75 - 31*48} ')
print(f'Точки в объединение фигур: {78 * 102 + 89 * 76 - 32*49} ')

import turtle as t
t.screensize(10000,10000)
t.tracer(0)
t.left(90)
l = 13
for i in range(2):
    t.fd(77*l)
    t.rt(90)
    t.fd(101*l)
    t.rt(90)
t.up()
t.fd(29*l)
t.lt(90)
t.fd(44*l)
t.rt(90)
t.down()
for i in range(7):
    t.fd(88*l)
    t.rt(90)
    t.fd(75*l)
    t.rt(90)
t.up()
for x in range(-100,100):
    for y in range(-100,100):
        t.goto(x*l,y*l)
        t.dot(2, 'red')
t.update()
t.done()
'''


# 17736 (8)
'''
from itertools import *
n = 0
for p in product('0123456',repeat = 7):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] not in '35' and num.count('0') <= 1:
            for x in '0246':
                num = num.replace(x,'2')
            if num[-1] != '2':
                n+=1
print(n)
'''


# 18189 (19-21)
'''
from math import floor
def F(a,s,n):
    if a + s <= 63:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a - 1, s, n - 1), F(a, s - 1, n - 1), F(floor(a / 3), s, n - 1), F(a, floor(s / 3), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(7, 1000) if F(57, s, n=2)])
print([s for s in range(7, 1000) if F(57, s, n=3) and not F(57, s, n=1)])
print([s for s in range(7, 1000) if F(57, s, n=4) and not F(57, s, n=2)])
'''

# 18281 (12)
'''
M = []
for n in range(4, 100):
    s = '9' + '6'*n
    while '96' in s or '366' in s or '666' in s:
        if '96' in s:
            s = s.replace('96','6',1)
        if '366' in s:
            s = s.replace('366','69',1)
        if '666' in s:
            s = s.replace('666','3',1)
    sum_digits = [int(i) for i in s]
    M.append(sum(sum_digits))
print(max(M))
'''


def F(x,a1,a2):
   P = 17 <= x <= 61
   Q = 39 <= x <= 91
   A = a1 <= x <= a2
   return (Q and (not A)) and (A or (not P))
R = []
M = [x/4 for x in range(10*4, 110*4)]
for a1 in M:
   for a2 in M:
      if all(F(x,a1,a2) == False for x in M):
         R.append(a2 - a1)
print(min(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Николай 9/29 -> 48 вторичных баллов +[1, 2, 4, 7, 13, 14, 16, 23, 25] -[5, 6, 8, 9, 12, 15, 17, 24]

# Второй пробник 28.02.25:
# Николай 12/29 -> 56 вторичных баллов +[1-4, 8-10, 12, 13, 15, 16, 23] -[5, 6, 14, 17, 18-22, 24, 25]

# Третий пробник 20.05.25:
# Николай 17/29 -> 70 вторичных баллов # +[1, 2, 6, 7, 9, 10, 11, 13, 14, 15, 16, 18, 19-21, 23, 25] -[3, 4, 8, 12]



