# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#
# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
# Вариант 1
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break

# Вариант 2
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    cnt = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == True:
                cnt += 1
    if cnt == 9801:
        print(A)
        break
   '''

# Вариант 3
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


R = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))

# Вариант 4
print(min([A for A in range(1, 1000) if all(((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100))]))
'''


# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 15330 Досрочная волна 2024 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 24 <= x <= 90  # (x∈B) B=[24;90]
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= (((not A) and B) <= (not C))


R = []
M = [x / 4 for x in range(20 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 43.0 -> 43
'''
# Ответ: 43

'''
def F(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))

M = [i / 4 for i in range(1 * 4, 110 * 4)]
R = []
for a1 in M:
    for a2 in M:
        if all(F(x) for x in M):
            R.append(a2-a1)
print((min(R)))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]
