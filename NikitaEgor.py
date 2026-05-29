# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: *************************************************************


#  ¬x       |    (not x)
#  x ∧ y    |    x and y
# ¬(x ∧ y)  |  (not(x and y))
#  x ∨ y    |    x or y
#  x → y    |    x <= y
#  x ≡ y    |    x == y


# № 29953 Апробация 14.05.26 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((x <= w) <= (w == z))) and y
                if F == 1:
                    print(x, y, z, w)
'''


# 29334
# F=((z→x)→(x≡y))∨¬w
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z<=x)<=(x==y)) or (not w)  # +
                if F == 0:
                    print(x, y, z, w)
'''


# № 25341 ЕГКР 13.12.25 (Уровень: Базовый)
# F=(w≡z)∨¬(y→w)∨¬x
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w == z) or (not(y <= w)) or (not x)  # +
                if F == 0:
                    print(x, y, z, w)
'''


# 28923
#F=(x∧¬z∧¬w)∨(x∧¬z∧y)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not z) and (not w)) or (x and (not z) and y)  # +
                if F == 1:
                    print(x, y, z, w)
'''


# #28750
#F=(w≡z)∨¬(y→w)∨¬x
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w==z) or (not(y<=w)) or (not x)  # +
                if F == 0:
                    print(x, y, z, w)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 13, 14, 15, 16, 17, 18, 19-21, 22, 23]
# КЕГЭ = []
# на следующем уроке:
