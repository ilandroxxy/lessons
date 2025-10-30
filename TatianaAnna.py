# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23561 Пересдача 03.07.25 (Уровень: Базовый)
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуралиное число m».
# Для какого наибольшего натурального числа А выражение ДЕЛ(х,128)→(¬ДЕЛ(х,А)→¬ДЕЛ(х,80))
# истинно (т.е. принимает значение 1) при любом натуральном значении переменной х?
'''
# Вариант 1
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 5000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        RES.append(A)
print(max(RES))


# Вариант 2
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 5000):
    cnt = 0
    for x in range(1, 10000):
        if F(x, A) == True:
            cnt += 1
    if cnt == 9999:
        RES.append(A)
print(max(RES))

# Вариант 3
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))


# Вариант 4
print(max([A for A in range(1, 5000) if all(((x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))) for x in range(1, 10000))]))
'''


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x < A) and (y < 3*A) or (2*x + y > 128)

RES = []
for A in range(1, 5000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''


# № 21901 Открытый вариант 2025 (Уровень: Базовый)
'''
def F(x, A):
    return ((x & 52 != 0) and (x & 48 == 0)) <= (x & A != 0)

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
# Пусть на числовой прямой дан отрезок B = [60,80].
# Для какого наибольшего натурального числа А логическое выражение
# ДЕЛ(x,А) ∨ ((x∈B) → ¬ДЕЛ(x,22))
# истинно (т.е. принимает значение 1) при любом целом положительном значении переменной х?
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 21710 ЕГКР 19.04.25 (Уровень: Базовый)
# На числовой прямой даны два отрезка: B = [36; 75] и C = [60; 110].
# Укажите наименьшую возможную длину такого отрезка A, что логическое выражение
# ¬(x∈A) → ((x∈B) ≡ (x∈C))
#  истинно (т.е. принимает значение 1) при любом значении переменной х.
'''
def F(x, a1, a2):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= (B == C)

RES = []
M = [x / 4 for x in range(20*4, 130*4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''

# 20577
'''
def F(x, A):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))


RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''

# 9247
'''
def F(x, y, A):
    return (x - 3 * y < A) or (y > 400) or (x > 56)


RES = []
for A in range(1, 5000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''

# 17528
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


RES = []
M = [x / 4 for x in range(10 * 4, 100 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''

# 17871
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


RES = []
M = [x / 4 for x in range(10 * 4, 100 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
