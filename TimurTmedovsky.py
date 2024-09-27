# region Домашка: ******************************************************************

# Max и Min
'''
b = input()
maxi, mini = max(b), min(b)
print(maxi, mini, sep='\n')

a = int(input())
maxi, mini = 0, 10**9
while a > 0:
    x = a % 10
    maxi = max(maxi, x)
    mini = min(mini, x)
    a //= 10
print(maxi, mini, sep='\n')
'''


# Анализ числа
'''
a = int(input())
b = 0
c = 0
d = 1
while a:
    b += a % 10
    c += 1
    d *= a % 10
    a //= 10
print(b)
print(c)
print(d)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №59707
# Миша заполнял таблицу истинности логической функции F:
# (x ∨ ¬y) ∧ ¬(y ≡ z) ∧ ¬w
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
'''


# Тип 2 №35976
# Логическая функция F задаётся выражением ((x ∧ ¬y) ≡ (z ∨ ¬w)) → (x ∧ z).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x and (not y)) == (z or (not w))) <= (x and z)
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 2 №48423
# Логическая функция F задаётся выражением:
# (x → (y ≡ w)) ∧ (y ≡ (w → z))
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (y == w)) and (y == (w <= z))
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (y == w)) and (y == (w <= z))
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №40977
# Логическая функция F задаётся выражением ((y → x) ∧ (z ∨ w)) → ((x ∧ ¬w) ∨ (y ≡ z))

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
