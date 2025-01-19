# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

'''
from itertools import *
print('1 2 3 4 5 6 7')
table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
graph = 'AB BA AC CA AF FA BC CB CE EC EG GE ED DE GD DG DF FD'
for p in permutations('ABCEGDF'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7
# C G B E D A F
# E B G C A D F


'''
def convert(n ,b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 3)

    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s += convert(x, 3)

    r = int(s, 3)
    if r < 199:
        R.append(n)
print(max(R))
'''

'''
import turtle as t
t.tracer(0)
t.left(90)
size = 30

t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*size)
    t.right(45)

t.right(315)
t.forward(10*size)
for i in range(2):
    t.right(90)
    t.forward(10*size)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')

t.update()
t.done()
'''


'''
alphabeat = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = alphabeat[:16]
cnt = 0
s1 = alphabeat[1:16:2]
s2 = alphabeat[0:16:2]
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if a != '0':
                if len(set(num)) == len(num):
                    if a in s1 and b in s2 and c in s1:
                        cnt += 1
                    if a in s2 and b in s1 and c in s2:
                        cnt += 1
                    
print(cnt)
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 5, 8, 18, 19-21, 26
