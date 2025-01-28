# region Домашка: ******************************************************************


'''
def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    else:
        return f(a - sum([int(x) for x in str(a)]), b) + f(a // 2, b) + f(a - 1, b)


print(f(40, 25) * f(25, 10))
'''


# № 2152 (Уровень: Базовый)
'''
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return f(a + 4, b) + f(a + 10, b) + f(2*a + 1, b)


print(f(2, 27))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)

# Вариант 1
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not F(x, y, A):
                flag = False
                break
    if flag == True:
        print(A)
        break
'''

# Вариант 2
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


R = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))

# Вариант 2.1

print(min([A for A in range(1, 1000) if all(((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100))]))
'''


# print(14 & 5)  # 4
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

#
# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


#
# № 15330 Досрочная волна 2024 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= (((not A) and B) <= (not C))


R = []
M = [x for x in range(20, 120)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


def F(x, a1, a2):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))


R = []
M = [x / 10 for x in range(60 * 10, 120 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))

# 22.75 -> 22.799 -> 22.9000 -> 23


# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]
