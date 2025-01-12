# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# Задача 5
'''
def ter(n):
    t = ''
    while n > 0:
        t = str(n % 3) + t
        n //= 3
    return t


A = []
for n in range(1, 10000):
    s = ter(n)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        s = s + ter((n % 3) * 4)
    if int(s, 3) < 199:
        A.append(n)
print(max(A))
'''


# Задач 6
'''
from turtle import *
screensize(-2000, 2000)
tracer(0)
m = 50
left(90)
right(90)
for i in range(3):
    right(45)
    forward(10 * m)
    right(45)
right(315)
forward(10 * m)
for i in range(2):
    right(90)
    forward(10 * m)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(2, 'red')
update()
done()
'''
# Ответ: 203


# Задача 8
'''
from itertools import permutations

k = 0
c = '02468ACE'
n = '13579BDF'
for i in permutations(c + n, r=3):
    a = ''.join(i)
    if a[0] == '0':
        continue
    for x in c:
        a = a.replace(x, '2')
    for x in n:
        a = a.replace(x, '1')
    if '11' not in a and '22' not in a:
        k = k + 1
    # if a[0] in c and a[1] in n and a[2] in c:
    #     k = k + 1
    # if a[0] in n and a[1] in c and a[2] in n:
    #     k = k + 1
print(k)
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
    if s.count('1') == 3:
        print(n)
        break
'''

'''
s = '13231231323123121'
s = s.replace('2', '*')
print(s)  # 13*31*313*31*31*1

s = s.replace('*', '2', 3)
print(s)  # 132312313231*31*1
'''


# Задача 23
'''
def f(a, b):
    if a < b or a == 7:  # не содержит числа 7
        return 0
    if a == b:
        return 1
    return f(a - 1, b) + f(a - 3, b) + f(a // 2, b)


print(f(19, 10) * f(10, 3))
'''


# Задача 25
'''
from fnmatch import *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x // 2025)
'''


# Задача 24
'''
s = open('files/24.txt').readline()
s = s.replace('9', '8').replace('B', 'A').replace('C', 'A')
while 'AA' in s or '88' in s:
    s = s.replace('AA', 'A A')
    s = s.replace('88', '8 8')
print(max([len(x) for x in s.split()]))
'''


# Задача 9
'''
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M.count(M[-1]) == 1:
        # if len(set(M)) == 5 and any(M.count(x) == 2 for x in M):
        copied = [x for x in M if M.count(x) == 2]
        not_copied = [x for x in M if M.count(x) == 1]
        if len(not_copied) == 3 and len(copied) == 4:
            print(sum(M))
            break
'''

# 22.


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = [22]
# на следующем уроке: 25, 24


# Первый пробник 21.12.24:
# Ефим 12/25 -> 56 вторичных баллов +[1-4, 7, 8, 11, 14-18] -[5, 6, 9, 10, 12, 19-21, 22, 23, 24, 25]
