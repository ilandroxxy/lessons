# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 6
'''
from turtle import *
screensize(-5000, 5000)
tracer(0)
l = 20

for i in range(4):
    fd(10 * l)
    rt(270)
up()
fd(3 * l)
rt(270)
fd(5 * l)
rt(90)
down()
for i in range(2):
    fd(10 * l)
    rt(270)
    fd(12 * l)
    rt(270)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * l, y * l)
        dot(3, 'red')
update()
done()
'''
from struct import iter_unpack

# Номер 12
'''
for n in range(4, 10001):
    s = '5' + '2' * n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    e = [int(i) for i in s]
    if sum(e) == 64:
        print(n)
        break
'''


# Номер 5
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)
    r = int(s, 3)
    if r > 150:
        print(n)
        break
'''

# # i   0    1    2    3    4
# M = ['a', 'b', 'c', 'd', 'e']
# # -i -5   -4   -3   -2   -1

# Номер 8
'''
from itertools import *
n = 0
for p in product(sorted('СБОРНИК'), repeat=6):
    word = ''.join(p)
    n += 1
    if word[0] != 'Р' and word.count('Б') == 2 and word.count('К') <= 1:
        print(n, word)
'''

# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 22, 25 повторять

# Второй пробник 28.02.25:
# Дарья 10/29 -> 51 вторичных баллов +[1, 2, 4, 7, 10, 11, 13, 15, 16, 18] -[3, 6, 12, 22]

