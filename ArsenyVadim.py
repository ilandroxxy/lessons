# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 23561 Пересдача 03.07.25 (Уровень: Базовый)

# Вариант 1
'''
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        RES.append(A)
print(max(RES))
'''

# Вариант 2
'''
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 10000):
    cnt = 0
    for x in range(1, 10000):
        if F(x, A) == True:
            cnt += 1
    if cnt == 9999:
        RES.append(A)
print(max(RES))
'''

# Вариант 3
'''
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 20905 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    return (x & A == 0) <= ((x & 77 == 0) and (x & 44 == 0))

RES = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''


# № 21414 Досрочная волна 2025 (Уровень: Базовый)
'''
def F(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

RES = []
for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))

# Вариант 2
print(min([A for A in range(1, 10000) if all(((5 < y) or (x > 32) or (x + 2*y < A)) for x in range(1, 100) for y in range(1, 100))]))
'''

# № 17748 (Уровень: Базовый)
'''
def f(x, y, A):
    return ((x <= 19) or (y < 2 * x + A - 50) or (y > 17))

RES = []
for A in range(0, 5000):
    flag = True
    for x in range(100):
        for y in range(100):
            if f(x, y, A) == False:
                flag = False
                break
    if flag == True:
        RES.append(A)
print(min(RES))
'''
'''
def f(x, y, A):
    return ((x <= 19) + (y < 2 * x + A - 50) + (y > 17))

RES = []
for A in range(0, 5000):
    if all(f(x, y, A) for x in range(100) for y in range(100)):
        RES.append(A)
print(min(RES))
'''


'''
# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)

def F(x, y, A):
    return(x - 3*y < A) or (y > 400) or (x > 56)

RES=[]
for A in range(1, 10000):
    if all(F(x,y, A)for x in range(1,100) for y in range(1,100)):
        RES.append(A)
print(min(RES))
'''


# 16381
'''
RES = []
def f(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))
for A in range(1, 5000):
    if all(f(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 17556 Основная волна 08.06.24 (Уровень: Базовый)
'''
def F(x, A):
    B = 70 <= x <= 90
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)

print(max(RES))
'''


# № 17528 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 15 <= x <= 40  # (x∈P)
    Q = 21 <= x <= 63  # (x∈Q)
    A = a1 <= x <= a2  # (x∈A)
    return (P) <= (((Q) and (not A)) <= (not P))

RES = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''
# 19.0 -> 19
# 19.45 -> 19
# 19.75 -> 20


# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68  # (x∈P)
    C = 29 <= x <= 100  # (x∈Q)
    A = a1 <= x <= a2  # (x∈A)
    return (D) <= (((not C) and (not A)) <= (not D))

RES = []
M = [x / 10 for x in range(1 * 10, 120 * 10)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))  # 21.75 -> 21.8 -> 21.9 -> 22
'''


# № 17528 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

RES = []
M = [x / 5 for x in range(10 * 5, 80 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 13, 14, 15, 25]
# КЕГЭ  = []
# на следующем уроке: 16, 23, 19-21
