# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(1, 5000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s += convert(x, 3)
    r = int(s, 3)

    if r < 199:
        print(n)
'''


'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
t.down()
l = 40
t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10*l)
    t.right(45)
t.right(315)
t.forward(10*l)
for i in range(2):
    t.right(90)
    t.forward(10*l)
t.up()
for x in range(-50,50):
    for y in range(-50,50):
        t.goto(x*l,y*l)
        t.dot(5,'red')
t.update()
t.done()
'''

'''
from itertools import permutations

alphabet = sorted('0123456789ABCDEF')
cnt = 0
for i in permutations(alphabet, r=3):
    a = ''.join(i)
    if a[0] != '0':
        # if a[0] in b and a[1] in c and a[2] in b:
        #     cnt += 1
        # if a[0] in c and a[1] in b and a[2] in c:
        #     cnt += 1
        for x in '02468ACE':
            a = a.replace(x, '2')
        for x in '13579BDF':
            a = a.replace(x, '1')
        if '11' not in a and '22' not in a:
            cnt += 1
print(cnt)
'''


M = []
alphabet = sorted('0123456789ABCDEFGHIJKLM')
for x in alphabet:
    A = int(f'7{x}38596', 23)
    B = int(f'14{x}36', 23)
    C = int(f'61{x}7', 23)
    if (A + B + C) % 22 == 0:
        M.append((A + B + C) // 22)
print(min(M))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 14]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]
