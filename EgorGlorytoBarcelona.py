# region Домашка: ******************************************************************

# Числа с условиями
'''
a = int(input())
b = int(input())

for i in range(a, b+1):
    if (i % 20 == 0) or (i % 7 == 0 and i % 14 == 0) or (i % 10 == 9):
        print(i)
'''

'''
n = int(input())
maxi = 0
mini = 10**9
while n > 0:
    mini = min(mini, n % 10)
    maxi = max(maxi, n % 10)
    n //= 10
print(maxi)
print(mini)

n = int(input())
summa = 0
count = 0
total = 1
while n > 0:
    summa += n % 10
    count += 1  # count = count + 1
    total *= n % 10
    n = n // 10
print(summa)
print(count)
print(total)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №15970
# Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z ) ∨ w.
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (y == z) or w
                if F == 0:
                    print(x, y, z, w)
'''

# Тип 2 №16805
# Логическая функция F задаётся выражением
# (¬x ≡ z) → (y ≡ (w ∨ x))
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not x) == z) <= (y == (w or x))
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 2 №33472
# Логическая функция F задаётся выражением
# (w → x) ∧ ((y → z) ≡ (x → y))

# (w → x) ∧ ((y → z) ≡ (x → y))
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w <= x) and ((y <= z) == (x <= y))
                if F == 1:
                    print(x, y, z, w)
'''

# Тип 2 №18483
# Логическая функция F задаётся выражением
# ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w).
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
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
