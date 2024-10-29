# region Домашка: ******************************************************************
'''
summ = 0
for i in range(12):
    if i % 2 == 0:
        print(i, end=' ')  # 0 2 4 6 8 10
        summ += i
print(summ)
'''

'''
tоtаl = 1
fоr i in range(2, 6):  # 2 3 4 5  # 5! = 1 * 2 * 3 * 4 * 5
    total *= i
рrint(total)
'''

# Max и Min
'''
n = int(input())
maxi = -10**9
mini = 10**9
while n > 0:
    if mini > n % 10:
        mini = n % 10
    maxi = max(maxi, n % 10)
    n //= 10
print(maxi)
print(mini)
'''

# Анализ числа
'''
n = int(input())  # 23
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

# Подсчет четных и нечетных чисел
'''
chet = 0
nechet = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(chet)
print(nechet)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №59707
# Миша заполнял таблицу истинности логической функции F:
# (x∨¬y)∧¬(y≡z)∧¬w
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


# Тип 2 №19051
# Миша заполнял таблицу истинности функции
# (x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (x == z) or (not w)
                if F == 0:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №40977
# Логическая функция F задаётся выражением
# ((y → x) ∧ (z ∨ w)) → ((x ∧ ¬w) ∨ (y ≡ z))
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


# Тип 2 №51971
# Логическая функция F задаётся выражением:
# (x≡¬y)→((z→¬w)∧(w→y))

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == (not y)) <= ((z <= (not w)) and (w <= y))
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
