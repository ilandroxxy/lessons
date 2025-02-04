# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)

# Вариант 1
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 10000):
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


R = []
for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))


# Вариант 2.2

print(min([A for A in range(1, 10000) if all(((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100))]))
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 17528 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


R = []
M = [x / 10 for x in range(5 * 10, 120 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
'''

# № 7846 Danov2304 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    # return not (not (P) <= (Q)) <= ((A) <= (not (Q) <= (P)))
    return (not((not P) <= Q)) <= (A <= ((not Q) <= P))


R = []
M = [x / 4 for x in range(10 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
