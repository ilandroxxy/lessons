# region Домашка: ******************************************************************


# ctrl + alt + L
'''
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 20 == 0 and i % 10 == 9 and i % 14 == 0:
        print(i)
'''

'''
n = int(input())
maxi = -100000000
mini = 100000000
while n > 0:
    x = n % 10
    if maxi < x:
        maxi = x
    mini = min(mini, x)
    n //= 10
print(maxi)
print(mini)
'''

'''
n = int(input())
summa = 0
count = 0
total = 1
while n > 0:
    x = n % 10
    summa += x
    count += 1
    total *= x
    n //= 10
print(summa)
print(count)
print(total)
'''

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
                F = (x == (w or y)) or ((w <= z) and (y <= w))
                if F == 0:
                    print(x, y, z, w)

'''

# Тип 2 №27228
# Логическая функция F задаётся выражением (¬x ∨ y ∨ z) ≡ (¬y ∧ z ∧ w)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not x) or y or z) == ((not y) and z and w)
                if F == 1:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # (x ∨ ¬z) ∧ (x ≡ ¬w) ∧ (x → y)
                F = (x or (not z)) and (x == (not w)) and (x <= y)
                if F == 1:
                    print(x, y, z, w)
'''


# Тип 2 №52173
# Логическая функция F задаётся
# выражением: (z≡¬x)→((w→¬y)∧(y→x))
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                print(x, y, z, w, int(F))
'''


# Тип 2 №28538
# Логическая функция F задаётся выражением ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x and y) <= ((not z) or w)) and (((not w) <= x) or (not y))
                if F == 0:
                    print(x, y, z, w)
'''

# ¬(x→z)∨(y≡w)∨y
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not (x <= z)) or (y == w) or y
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
