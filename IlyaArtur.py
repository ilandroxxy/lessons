# region Домашка: ******************************************************************

'''
n = int(input())
max1 = -10**7
min1 = 10**7
while n > 0:
    x = n % 10
    max1 = max(max1, x)
    min1 = min(min1, x)
    n //= 10
print(max1)
print(min1)
'''


# Подсчет четных и нечетных чисел
'''
n = int(input())
chet = 0
nechet = 0
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(chet)
print(nechet)
'''

# Вывод таблицы умножения
'''
n = int(input())
for i in range(1, 10+1):
    print(f'{n} * {i} = {n * i}')
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
d1 = True
d0 = False  # bool (Boolean) 
'''


# Тип 2 №16878
# Логическая функция F задаётся выражением (x≡¬y)→(z≡(y∨w)).
'''
print('x y z w F')
for x in range(2):
    for y in [0, 1]:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == (not y)) <= (z == (y or w))
                if F == 0:
                    print(x, y, z, w)
'''


# Тип 2 №59707
# Миша заполнял таблицу истинности логической функции F:
# (x ∨ ¬y) ∧ ¬(y ≡ z) ∧ ¬w
'''
print('x y z w F')
for x in range(2):
    for y in [0, 1]:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F == 1:
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
