# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# 5
'''
R = []
for n in range(1,100):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r >= 76:
        R.append(n)
print(min(R))
'''


# 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:22]:
    A = int(f'63{x}59685', 22)
    B = int(f'17{x}53', 22)
    С = int(f'36{x}5', 22)
    if (A + B + С) % 21 == 0:
        M.append((A + B + С) // 21)
print(min(M))
'''


# 12
'''
R = []
for n in range(4, 10000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
      if '12' in s:
        s = s.replace('12', '2', 1)
      if '322' in s:
        s = s.replace('322', '21', 1)
      if '222' in s:
        s = s.replace('222', '3', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    R.append(summa)
    print(max(R))
'''

# 23
'''
def F(a, b):
    if a <= b or a == 13:
        return a == b
    return F(a - 1, b) + F(a - 2, b) + F(a // 3, b)
print(F(18, 8) * F(8, 3))
'''

# 2
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y <= x) and w and (not z)
                if F == 1:
                    print(x, y, z, w)
'''


# 6

print(21*21 + 21*25 - 15*11)
print(20*20 + 20*24 - 14*10)

import turtle as t
t.tracer(0)
size = 15
for i in range (4):
    t.forward(20*size)
    t.right(270)
t.up()
t.backward(6*size)
t.right(270)
t.forward(10*size)
t.right(90)
t.down()
for i in range(2):
    t.forward(20*size)
    t.right(270)
    t.forward(24*size)
    t.right(270)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [5, 8, 17]
# на следующем уроке:


# Второй пробник 10.02.25:
# 7/29 -> 42 вторичных баллов +[1, 4, 6, 12, 14, 15, 16] -[3, 5, 8, 23, 25]
