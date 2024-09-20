# region Домашка: ************************************************************


# Произведение делителей
'''
m = int(input())
my_prod = 1
for j in range(1, m+1):
    if m % j == 0:
        my_prod *= j
print(my_prod)
'''

'''
from math import prod
m = int(input())
div = []
for j in range(1, m+1):
    if m % j == 0:
        div.append(j)
# print(div)
print(prod(div))
'''

# Max и Min
'''
n = int(input())
M = [int(x) for x in str(n) if x in '02468']
print(max(M))
print(min(M))


n = int(input())
M = str(n)
print(max(M))
print(min(M))
'''

# Анализ числа
'''
n = int(input())  # 1234
summa = 0
count = 0
my_prod = 1
while n > 0:
    ostat = n % 10
    summa += ostat
    count += 1
    my_prod *= ostat
    n //= 10
print(summa)
print(count)
print(my_prod)
'''

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        print(x, y)
'''


# Тип 2 №16431
# ((y → x) ≡ (x → w)) ∧ (z ∨ x)
'''
print('x y z w')
for x in [0, 1]:
    for y in range(2):
        for z in 0, 1:
            for w in (0, 1):
                F = ((y <= x) == (x <= w)) and (z or x)
                if F == 1:
                    print(x, y, z, w)
'''


# Тип 2 №33747
# (¬(z ≡ w) → (w ∧ ¬x)) ∨ (x ∧ ¬y)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not(z == w)) <= (w and (not x))) or (x and (not y))
                if F == 0:
                    print(x, y, z, w)
'''

# Тип 2 №68264
# ((y ∨ z) → (z ∧ w)) ≡ ¬ ((x ∧ z) → (w ∨ y))

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y or z) <= (z and w)) == (not((x and z) <= (w or y)))
                if F == 1:
                    print(x, y, z, w)


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ = []
# на следующем уроке:
