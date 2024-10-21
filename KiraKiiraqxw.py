# region Домашка: ******************************************************************
'''
a = int(input())
b = int(input())
for x in range(a, b + 1):
    if (x % 20 == 0) or (x % 7 == 0 and x % 14 == 0) or (x % 10 == 9):
        print(x)
'''

'''
m = int(input())  # 1...24
total = 1
for j in range(1, m+1):
    if m % j == 0:
        total = total * j
print(total)
'''

'''
n = int(input())
cnt_1 = 0
cnt_2 = 0
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        cnt_2 += 1
    if x % 2 != 0:
        cnt_1 += 1
print(cnt_2)
print(cnt_1)
'''

# print(123 % 10)  # 3
# print(123 // 10)  # 12

'''
n = int(input())  # 21222344456
maxi = -10**9
mini = 10**9
while n > 0:
    x = n % 10

    if maxi < x:
        maxi = x

    mini = min(mini, x)

    n //= 10
print(maxi)
print(mini)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 2 №27228
# Логическая функция F задаётся выражением
# (¬x ∨ y ∨ z) ≡ (¬y ∧ z ∧ w)
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


# Тип 2 №16377
# Логическая функция F задаётся выражением
# ((x → y) ≡ (y → z)) ∧ (y ∨ w).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) == (y <= z)) and (y or w)
                if F == 1:
                    print(x, y, z, w)
'''


# ¬(y → x) ∨ (z → w) ∨¬z
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(y <= x)) or (z <= w) or (not z)
                if F == 0:
                    print(x, y, z, w)
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
