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
                F = (x and (not y)) or (x == z) or w
                if F == 0:
                    print(x, y, z, w)
'''

# Тип 2 №38936
# Логическая функция F задаётся выражением (x ≡ ¬y) → ((x ∧ w) ≡ (z ∧ ¬w))
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == (not y)) <= ((x and w) == (z and (not w)))
                if F == 0:
                    print(x, y, z, w)
'''

# Тип 2 №52173
# Логическая функция F задаётся выражением: (z≡¬x)→((w→¬y)∧(y→x))

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 1:
                    print(x, y, z, w, int(F))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
