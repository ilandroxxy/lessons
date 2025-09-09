# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
'''


# № 23548 Пересдача 03.07.25 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x or y) <= z) or (y == w) or z
                if F == 0:
                    print(x, y, z, w)
'''
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not (w <= (x == y))) and (z <= x)
                if F == 1:
                    print(x, y, z, w)
'''

# № 13799 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F = (not((x == y) or (y == w) or (w == z))) or (x and (not y))
                F = (((not x) and w) <= y) and (y <= (z and (not y)))
                if F == 1:
                    print(x, y, z, w)
'''


# № 13800 (Уровень: Базовый)

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((x == y) or (y == w) or (w == z))) or (x and (not y))
                if F == 1:
                    print(x, y, z, w)



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ = []
# на следующем уроке: Генераторы списков, строки


