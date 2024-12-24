# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задача 1
'''
from itertools import *
print('1 2 3 4 5 6 7')
table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
graph = 'GD DG GE EG DE ED DF FD FA AF AC CA AB BA BC CB CE EC'
for p in permutations('ABCDEFG'):
    new_table = table
    #   1    2    3    4    5    6    7
    # ('G', 'F', 'E', 'D', 'A', 'C', 'B')
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7
# C G B E D A F
# E B G C A D F


# Задача 6
'''
import turtle as t

t.tracer(0)  # подсмотрел t.tracer(0), но можно было бы решить без него
l = 40
t.left(90)
t.down()

t.right(90)
for _ in range(3):
    t.right(45)
    t.forward(l*10)
    t.right(45)

t.right(315)
t.forward(l*10)

for _ in range(2):
    t.right(90)
    t.forward(l*10)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(2, 'red')
t.update()
t.done()
'''

# Задача 8
'''
from itertools import *
n1 = '13579BDF'
n2 = '02468ACE'
cnt = 0
for i in permutations('0123456789ABCDEF', r=3):
    s = ''.join(i)
    if s[0] != '0':
        # if s[0] in n2 and s[1] in n1 and s[2] in n2:
        #     cnt += 1
        # if s[0] in n1 and s[1] in n2 and s[2] in n1:
        #     cnt += 1
        for x in n1:
            s = s.replace(x, '1')
        for x in n2:
            s = s.replace(x, '2')
        if '11' not in s and '22' not in s:
            cnt += 1

print(cnt)
'''


# Задача 9
'''
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if len(set(M)) == 5 and any(x for x in M if M.count(x) == 2):
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(not_copied) == 3 and len(copied) == 4:
        if M.count(max(M)) == 1:
            print(sum(M))
            break
'''

# Задача 11
'''
simb = 10
alph = 52  # alph = 2 ** i
i = 6  # кол-во бит на символ 
n = 65536
bit = simb * i
# минимально возможное целое число байт.
print(bit / 8)  # 7.5 -> 8
byte = 8

print((n*byte)/2**10)  # 512
'''


# Задача 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
d = []
for x in alphabet[:23]:
    A = int(f'7{x}38596', 23)
    B = int(f'14{x}36', 23)
    C = int(f'61{x}7', 23)
    if (A+B+C) % 22 == 0:
        print((A+B+C) // 22)
        # 47163321
'''

# 13, 17-21, 24, 25


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 9, 8, 11, 12, 13, 14, 15, 16, 17, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Стас 9/21 -> 48 вторичных баллов +[2, 3-5, 7, 10, 12, 16, 22] -[1, 6, 8, 9, 11, 13, 14, 15, 17-21, 24-25]
