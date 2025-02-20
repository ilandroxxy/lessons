# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 12 (19244)
'''
for n in range(4, 10000):
    s = '1' + '2' * n

    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)

    summa = sum(map(int, s))
    if summa == 15:
        print(n)
        break
'''


# Номер 8 (19240)
'''
s = sorted('ЯНВАРЬ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if a != 'Я':
                        if word.count('Ь') <= 1:
                            if 'ЯЯ' not in word:
                                print(n)
'''


# Номер 6 (19238)
'''
import turtle as t
t.screensize(-2000, 2000)
t.left(90)
t.tracer(0)
size = 20

# тут описываем псевдокод
for i in range(8):
    t.forward(16 * size)
    t.right(90)
    t.forward(22 * size)
    t.right(90)
t.up()
t.forward(5 * size)
t.right(90)
t.forward(5 * size)
t.left(90)
t.down()
for i in range(8):
    t.forward(52 * size)
    t.right(90)
    t.forward(77 * size)
    t.right(90)

# тут рисуем точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')

t.update()
t.done()
'''


# Номер 5 (19237)
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        summa = sum(map(int, s))
        s = s + convert(summa, 3)
    r = int(s, 3)  # в десятичную
    if r > 220 and r % 2 == 0:
        R.append(r)
print(min(R))
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(((not x) or y) and (not w)) or (not(z and (not(y and w)))))
                if F == 0:
                    print(x, y, z, w)
'''

# № 18482 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x ==(y <= (z or x))) and w
                if F == 1:
                    print(x, y, z, w)
'''


# № 18126 (Уровень: Базовый)

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z == x) <= w) and (w <= (y and x))
                if F == 1:
                    print(x, y, z, w)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
