# region Домашка: ******************************************************************

'''
import time
start = time.time()

# def Divisors(x):
#     div = []
#     for j in range(1, x + 1):
#         if x % j == 0:
#             div.append(j)
#     return div

def Divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


print(Divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(Divisors(16))  # [1, 2, 4, 8, 16]
print(Divisors(100_000_000))  # [1, 2, 4, 8, 16]

print(time.time() - start)  # 2.9306128 -> 0.00041
print(2.9306128 / 0.00041)   # 7147.83 раз
'''

'''
a = input()
summ = 0
mult = 1
for x in a:
    summ += int(x)
    mult *= int(x)
print(summ)
print(len(a))
print(mult)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №15939
# Логическая функция F задаётся
# выражением (z ∧ y) ∨ ((x → z ) ≡ (y → w)).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z and y) or ((x <= z) == (y <= w))
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 2 №68264
# Логическая функция F задаётся выражением:
# ((y ∨ z) → (z ∧ w)) ≡ ¬ ((x ∧ z) → (w ∨ y)).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y or z) <= (z and w)) == (not((x and z) <= (w or y)))
                if F == 1:
                    print(x, y, z, w)
'''


# Тип 2 №18483
# Логическая функция F задаётся выражением ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w).
'''
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
'''

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
