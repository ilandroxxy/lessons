# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18175 (Уровень: Базовый)
'''
# Вариант 1

def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

RES = []
for A in range(1, 5000):
    flag = True
    for x in range(1, 10000):
        # if F(x, A) == False:
        if not F(x, A):
            flag = False
            break
    if flag == True:
        RES.append(A)
print(max(RES))


# Вариант 2

def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

RES = []
for A in range(1, 5000):
    cnt = 0
    for x in range(1, 10000):
        # if F(x, A) == True:
        if F(x, A):
            cnt += 1
    if cnt == 9999:
        RES.append(A)
print(max(RES))


# Вариант 3

def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))


# Вариант 3.1

RES = []
for A in range(1, 5000):
    if all( (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))

# Вариант 3.2

print(max([A for A in range(1, 5000) if all( (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) for x in range(1, 10000))]))
'''


# № 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
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

# № 20580 (Уровень: Базовый)
'''
def f(x, y, A):
    return (9*x + y > A) or (x >= 36) or (y >= 18)
res = []
for A in range(1, 5000):
    if all(f(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        res.append(A)
print(max(res))
'''


# № 20577 (Уровень: Базовый)
'''
def f(x, A):
    return ((x&A != 0) <= ((x&698 == 0) <= (x&321 != 0)))

res = []
for A in range(1, 5000):
    if all(f(x, A) for x in range(1, 10000)):
        res.append(A)
print(max(res))
'''

# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
def f(x, y, a):
    return (x - 3*y < a) or (y > 400) or (x > 56)
res = []
for a in range(1, 10000):
    if all(f(x,y,a) for x in range(1, 100) for y in range(1, 100)):
        res.append(a)
print(min(res))
'''

# № 20584 (Уровень: Базовый)
'''
def f(x, A):
    return ((405 % x == 0) <= (81 % x == 0) or (A - x > 162 ))

res = []
for A in range(1, 5000):
    if all(f(x, A) for x in range(1, 10000)):
        res.append(A)
print(min(res))
'''


# Функции all() и any()
'''
M = [2, 4, 6, 8, 2, 4, 8, 0]
print(all(x % 2 == 0 for x in M))  # True

M = [5, 2, 4, 6, 8, 2, 4, 8, 0, 5]
print(all(x % 2 == 0 for x in M))  # False

M = [5, 2, 4, 6, 8, 2, 4, 8, 0, 5]
print(any(x % 2 != 0 for x in M))  # True
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or (B <= (x % 22 != 0))

res = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        res.append(A)
print(max(res))
'''


# № 20905 Апробация 05.03.25 (Уровень: Базовый)

def F(x, a1, a2):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

RES = []
M = [x / 4 for x in range(10 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))  # 29.0 -> 29


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 14, 15, 17, 25]
# КЕГЭ = []
# на следующем уроке: 16, 23, 19-21
