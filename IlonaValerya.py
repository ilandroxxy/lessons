# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 2 https://education.yandex.ru/ege/task/7f4398af-5c71-4cea-b491-3435c3279639
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (y == z) or (not w)
                if F == 0:
                    print(x, y, z, w)
'''


# Задание 2 https://education.yandex.ru/ege/task/fc4a8bdc-fdfe-4945-b982-30f68abee2d7
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w <= y) <= x) or (not z)
                if F == 0:
                    print(x, y, z, w)
'''

# Задание 2 https://education.yandex.ru/ege/task/c84e2709-a311-49ae-9a1d-7279bb7cf568
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = w and (y == (z <= (x or y)))
                if F == 1:
                    print(x, y, z, w)
'''

# Задание 2 https://education.yandex.ru/ege/task/18e677f8-5a13-4fdd-94d0-2b9de1950e2e
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not y)) and ((not x) or y) and w
                if F == 1:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w == y) or (((not x) <= z) and ((not z) <= y))
                if F == 0:
                    print(x, y, z, w)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ  = []
# на следующем уроке:
