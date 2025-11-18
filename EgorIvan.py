# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21414 Досрочная волна 2025 (Уровень: Базовый)

# Вариант 1
'''
def F(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

RES = []
for A in range(0, 5000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
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
    return (5 < y) or (x > 32) or (x + 2*y < A)

RES = []
for A in range(0, 5000):
    cnt = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if F(x, y, A) == True:
                cnt += 1
    if cnt == 10000:
        RES.append(A)
print(min(RES))
'''

# Вариант 3
'''
def F(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

RES = []
for A in range(0, 5000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        RES.append(A)
print(min(RES))
'''

# № 20584 (Уровень: Базовый)
'''
def F(x, A):
    return ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)

RES=[]
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''

# № 20577 (Уровень: Базовый)
'''
def F(x, A):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))

RES=[]
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES=[]
for A in range(1, 5000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# 20823
'''
def F(x, A):
    return (x & A == 0) <= ((x & 77 == 0) and (x & 44 == 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1,10000)):
        RES.append(A)
print(min(RES))
'''

# 18266
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range(1,10000)):
        RES.append(A)
print(min(RES))
'''


# 18140
'''
def F(x, y, A):
    return (x - y >= 39) or (y <= x) or (y >= A - 20)


RES = []
for A in range(1, 5000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(max(RES))
'''

# № 18044 (Уровень: Базовый)
'''
def F(x, a1, a2):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2
    return (not((M) or (N)) == (not A))

RES=[]
M = [x / 4 for x in range(20*4, 90*4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''
# 44.0 -> 44
# 44.45 -> 44
# 44.50 -> 45
# 44.75 -> 45


# 12469
'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return (D) <= (((not C) and (not A)) <= (not D))

RES=[]
M = [x / 5 for x in range(5*5, 110*5)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))
'''
# 21.75 -> 22


# # endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
