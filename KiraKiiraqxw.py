# region Домашка: ******************************************************************


# https://stepik.org/lesson/1038667/step/3?unit=1062772
'''
from itertools import *
cnt = 0
for p in permutations('ЯРОСЛАВ', r=5):
    word = ''.join(p)
    sogl = [x for x in word if x in 'РСЛВ']
    glas = [x for x in word if x in 'ЯОА']

    if len(sogl) > len(glas):
        if all(x not in word for x in 'ЯА АЯ АО ОА ОЯ ЯО'.split()):
            cnt += 1

print(cnt)
'''


# https://stepik.org/lesson/1038667/step/4?unit=1062772
'''
from itertools import *
M = []
n = 0
for p in product(sorted('МАРКСЛ'), repeat = 6):
    word = ''.join(p)
    n += 1
    if 'КС' not in word and 'СК' not in word:
        # copied = [x for x in word if word.count(x) == 3]
        # not_copied = [x for x in word if word.count(x) == 1]
        # if len(copied) == 3 and len(not_copied) == 3:
        if len(set(word)) == 4 and any(word.count(x) == 3 for x in word):
            M.append(n)

print(max(M))
'''


# https://stepik.org/lesson/1038667/step/5?unit=1062772
'''
from itertools import *
cnt = 0
for p in product('0123456789ABCDE', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            D = [x for x in num if x > '9']
            if len(D) >= 2:
                cnt += 1
print(cnt)
'''


# https://stepik.org/lesson/1038667/step/10?unit=1062772
'''
from itertools import *
N = []
n = 0
for p in product(sorted('ФОКУС'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('Ф') == 0 and word.count('У') == 2:
        N.append(n)
print(max(N))
'''

# Задача 6
'''
import turtle as t
t.tracer(0)
t.left(90)
size = 40

t.right(90)
for i in range (3):
    t.right(45)
    t.forward(10*size)
    t.right(45)
t.right(315)
t.forward(10*size)
for i in range (2):
    t.right(90)
    t.forward(10*size)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# Задача 12
'''
for n in range(4, 10000):
    s = '1' + '8' * n
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)

    if s.count("1") == 3:
        print(n)
        break
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (z == w)) or (not (y <= w))
                if F == 0:
                    print(x, y, z, w)
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
# ФИПИ = [2, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Кира 2/6 -> 54 вторичных баллов +[7, 10] -[2, 6, 8, 12]
