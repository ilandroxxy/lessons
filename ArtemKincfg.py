# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 17748 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x <= 19) or (y < 2*x + A - 50) or (y > 17)


for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break
'''

# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(10000)):
        R.append(A)
print(max(R))
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(10000)):
        print(A)
        break
'''


# № 14352 (Уровень: Базовый)
'''
def F(x, A):
    B = 120 <= x <= 180
    return (x % A == 0) or (B <= ((x % 16 != 0) or (x + A <= 204)))

for A in range(1, 1000):
    if all(F(x, A) for x in range(10000)):
        print(A)
'''


# № 14349 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    A = a1 <= x <= a2
    return C <= ((B and (not A)) <= (not C))


R = []
M = [x / 4 for x in range(50 * 4, 155 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# № 13895 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 34 <= x <= 72
    C = 32 <= x <= 61
    A = a1 <= x <= a2
    return (B <= A) and ((not C) or A)


R = []
M = [x / 4 for x in range(30 * 4, 75 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15]
# КЕГЭ  = []
# на следующем уроке:
