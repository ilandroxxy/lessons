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


'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F = ((x or y)<=z) or (y == w) or z  #  23548
                # F = y and (z == (w <= (x or z)))  # 20567
                # F = (not(((not x) or y) and (not w)) or (not(z and (not(y and w)))))  # 19234
                # F = (not((x == y) or (y == w) or ( w == z))) or (x and (not y))  # 13800
                F = (((not x) and w) <= y) and (y <= (z and (not y)))  # 13799
                if F == 1:
                    print(x, y, z, w)
'''


# F=((w→z)≡(x→¬y))∧(x∨z)

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w <= z) == (x <= (not y))) and (x or z)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w <= z) == (x <= (not y))) and (x or z)
                if F == 1:
                    print(x, y, z, w, int(F))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 9, 17]
# КЕГЭ = []
# на следующем уроке: