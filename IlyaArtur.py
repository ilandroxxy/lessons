# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
# Вариант 1
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not F(x, y, A):  # F(x, y, A) == False
                flag = False
                break
    if flag == True:
        print(A)
        break


# Вариант 2

def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    k = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == True:
                k += 1
    if k == 9801:
        print(A)
        break


# Вариант 3

def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


R = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))


# Вариант 3.2

R = []
for A in range(1, 1000):
    if all(((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))


# Вариант 4

print(min([A for A in range(1, 1000) if all(((x - 3*y < A) or (y > 400) or (x > 56)) for x in range(1, 100) for y in range(1, 100))]))
'''


# Пример с функциями all, any:
'''
N = [2, 4, 5, 8, 10, 12, 16, 20]
if all(x % 2 == 0 for x in N):
    print('all N')
if any(x % 2 != 0 for x in N):
    print('any N')  # any N


M = [2, 4, 14, 8, 10, 12, 16, 20]
if all(x % 2 == 0 for x in M):
    print('all M')  # Yes M
if any(x % 2 != 0 for x in M):
    print('any M')  # all M
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


# № 11234 (Уровень: Базовый)
'''
def F(x, A):
    B = 120 <= x <= 130  # (x ∈ B) B = [120; 130]
    return (B <= (x % 7 != 0)) or (A > 2*x)


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(min(R))
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(min(R))
'''


# № 18044 (Уровень: Базовый)
'''
def F(x, a1, a2):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2
    return (not(M or N)) == (not A)


R = []
M = [x / 4 for x in range(20 * 4, 100 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 44.9 -> 45
'''


# Тип 15 №36028
# На числовой прямой даны два отрезка:
# P=[17,54] и Q=[37,83].
# Какова наименьшая возможная длина интервала A, что формула
# (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
'''
def F(x, a1, a2):
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

R = []
M = [x / 4 for x in range(10 * 4, 100 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 17.0
'''


# Тип 15 №61395
'''
def F(x, y, A):
    return (3*x + y > 48) or (x > y) or (4*x + y < A)


R = []
for A in range(1, 1000):
    if any(F(x, y, A) == False for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 15, 16, 23]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
