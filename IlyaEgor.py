# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)
# Для какого наименьшего целого положительного числа А выражение
# (x<A) ∧ (y<3A) ∨ (2x+y>128)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?

# Вариант 1
'''
def F(x, y, A):
    return (x < A) and (y < 3 * A) or (2 * x + y > 128)

RES = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        RES.append(A)
print(min(RES))
'''

# Вариант 2
'''
def F(x, y, A):
    return (x < A) and (y < 3 * A) or (2 * x + y > 128)

RES = []
for A in range(1, 1000):
    cnt = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == True:
                cnt += 1
    if cnt == 9801:
        RES.append(A)
print(min(RES))
'''

# Вариант 3
'''
def F(x, y, A):
    return (x < A) and (y < 3 * A) or (2 * x + y > 128)

RES = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''


# Вариант 4
'''
print(min([A for A in range(1, 1000) if all( ((x < A) and (y < 3 * A) or (2 * x + y > 128)) for x in range(1, 100) for y in range(1, 100))]))
'''


# № 23561 Пересдача 03.07.25 (Уровень: Базовый)
# Для какого наибольшего натурального числа А выражение
# ДЕЛ(х,128)→(¬ДЕЛ(х,А)→¬ДЕЛ(х,80))
# истинно (т.е. принимает значение 1) при любом натуральном значении переменной х?
'''
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 21901 Открытый вариант 2025 (Уровень: Базовый)
# Для какого наименьшего неотрицательного целого числа А логическое выражение
# ((x&52 !=0)∧(x&48=0))→¬(x&А=0)
# истинно (т.е. принимает значение 1) при любом неотрицательном целом значении переменной х?
'''
def F(x, A):
    return ((x & 52 != 0) and (x & 48 == 0)) <= (x & A != 0)

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''

# 20580
'''
def F(x,y,A):
    return (9* x + y > A) or (x >= 36) or (y >= 18)
m = []
for A in range(1,1000):
    if all(F(x,y,A) for x in range(1,100) for y in range(1,100)):
        m.append(A)
print(max(m))
'''


# 21414
'''
def F(x, y, A):
    return (5<y) or (x>32) or (x+2*y<A)

M = []
for A in range(1,1000):
    if all(F(x, y, A) for x in range(1,100) for y in range(1,100)):
        M.append(A)
print(min(M))
'''
# Ответ: 43


# 17556
'''
def F(x,A):
    B = 70 <= x <= 90
    return (x % A == 0) or ((B) <=(x %22 !=0))
m = []
for A in range(1,1000):
    if all(F(x,A) for x in range(1,100)):
        m.append(A)
print(max(m))
'''

# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

M = []
for A in range(1,1000):
    if all(F(x, A) for x in range(1,10000)):
        M.append(A)
print(max(M))
'''



# № 17528 Основная волна 07.06.24 (Уровень: Базовый)
# На числовой прямой даны два отрезка:
# P=[15;40] и Q=[21;63]. Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
# (x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P)) истинно (т.е. принимает значение 1)
# при любом значении переменной х.
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


RES = []
M = [x / 4 for x in range(10 * 4, 70 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''


# № 16833 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = a1 <= x <= a2
    return ((A) and (not Q)) <= ((P) or (Q))


RES = []
M = [x / 4 for x in range(20 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(max(RES)) #48# 
'''


def F(x, a1, a2):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return (C) <= (((not A) and (B)) <= (not C))


RES = []
M = [x / 4 for x in range(20 * 4, 120 * 4)]
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
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 25]
# КЕГЭ = []
# на следующем уроке: 16, 23, 19-21
