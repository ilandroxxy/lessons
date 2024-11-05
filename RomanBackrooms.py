# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = input()
cnt = 0
for i in set(s):
    if i in 'qwertyuiopasdfghjklzxcvbnm':
        cnt += 1
print(cnt)
'''


# Тип 2 №16431
# Логическая функция F задаётся выражением ((y → x) ≡ (x → w)) ∧ (z ∨ x).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= x) == (x <= w)) and (z or x)
                if F == 1:
                    print(x, y, z, w)
'''

# Тип 2 №27260
# Логическая функция F задаётся выражением ((x ∨ ¬y) ∧ (¬z ≡ w))→(y∧z)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x or (not y)) and ((not z) == w)) <= (y and z)
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 6 №63055
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 30

for i in range(4):
    t.forward(12 * size)
    t.right(90)

for i in range(5):
    t.forward(4 * size)
    t.right(45)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# Тип 6 №56506

import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
t.left(90)
size = 30

for i in range(3):
    t.forward(7 * size)
    t.right(90)
    
t.forward(10 * size)

for i in range(3):
    t.left(90)
    t.forward(6 * size)


t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
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
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
