# region Домашка: ******************************************************************

'''
a = int(input())
maxi = 0
mini = 9
while a > 0:
    if a % 10 > maxi:
        maxi = a % 10
    if a % 10 < mini:
        mini = a % 10
    a //= 10
print(maxi)
print(mini)

a = int(input())
maxi = 0
mini = 9
while a > 0:
    maxi = max(a % 10, maxi)
    mini = min(a % 10, mini)
    a //= 10
print(maxi)
print(mini)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
d1 = True
print(not d1)  # False
print(not(not d1))  # True
'''


# Тип 2 №15787
# Логическая функция F задаётся выражением
# ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y)).
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) and (y <= w)) or (z == (x or y))
                if F == 0:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №33081
# Логическая функция F задаётся
# выражением (x ∨ ¬z) ∧ (x ≡ ¬w) ∧ (x → y).
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not z)) and (x == (not w)) and (x <= y)
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №59707
# Миша заполнял таблицу истинности логической функции F:
# (x ∨ ¬y) ∧ ¬(y ≡ z) ∧ ¬w
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №40977
# Логическая функция F задаётся
# выражением ((y → x) ∧ (z ∨ w)) → ((x ∧ ¬w) ∨ (y ≡ z))
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= x) and (z or w)) <= ((x and (not w)) or (y == z))
                if F == 0:
                    print(x, y, z, w, int(F))
'''



'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not (z == w)) <= (w and (not x))) or (x and (not y ))
                if F == 0:
                    print(x, y, z, w, int(F))
'''

'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w or x or (not z) or y) and (w or x or (not z) or (not y)) and ( w or (not x) or (not z) or (not y))
                if F == 0:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №52173
# Логическая функция F задаётся
# выражением: (z≡¬x)→((w→¬y)∧(y→x)).

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
# ФИПИ = [2]
# КЕГЭ  = []
# на следующем уроке:
