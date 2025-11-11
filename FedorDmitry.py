# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23561 Пересдача 03.07.25 (Уровень: Базовый)
# Для какого наибольшего натурального числа А выражение
# ДЕЛ(х,128)→(¬ДЕЛ(х,А)→¬ДЕЛ(х,80))
# истинно (т.е. принимает значение 1) при любом натуральном значении переменной х?
'''
# Вариант 1
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        # if F(x, A) == False:
        if not F(x, A):
            flag = False
            break
    if flag == True:
        print(A)

# Вариант 2
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

for A in range(1, 1000):
    cnt = 0
    for x in range(1, 10000):
        # if F(x, A) == True:
        if F(x, A):
            cnt += 1
    if cnt == 9999:
        print(A)

# Вариант 3
def F(x, A):
    return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))

# Вариант 4
print(max([A for A in range(1, 1000) if all( ((x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))) for x in range(1, 10000))]))
'''


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)
# Для какого наименьшего целого положительного числа А выражение
# (x<A)∧(y<3A)∨(2x+y>128)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
def F(x, y, A):
    return (x < A) and (y < 3*A) or (2*x + y > 128)

RES = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''

# № 20823 (Уровень: Базовый)
# Найдите минимальное натуральное значение А, при котором значение выражения
# (x&A=0)→((x&77=0)∧(x&44=0))
# тождественно истинно, то есть принимает значение 1 при
# любом натуральном значении х.
'''
def F(x, A):
    return (x&A==0) <= ((x&77==0) and (x&44==0))

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
# Пусть на числовой прямой дан отрезок B = [60,80].
# Для какого наибольшего натурального числа А логическое выражение
# ДЕЛ(x,А)∨((x∈B)→¬ДЕЛ(x,22))
# истинно (т.е. принимает значение 1) при любом целом
# положительном значении переменной х?
'''
def F(x, A):
    B = 60 <= x <= 80  # (x∈B)
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 12469 (Уровень: Базовый)
# На числовой прямой даны два отрезка: D = [7; 68] и C = [29; 100].
# Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
# (x∈D)→((¬(x∈C)∧¬(x∈A))→¬(x∈D))
# истинно (т.е. принимает значение 1) при любом значении переменной х.
'''
def F(x, a1, a2):
    D = 7 <= x <= 68  # (x∈D)
    C = 29 <= x <= 100  # (x∈C)
    A = a1 <= x <= a2  # (x∈A)
    return  (D) <= (((not C) and (not A)) <= (not D))

R = []
M = [x / 4 for x in range(5 * 4, 120 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
print(round(min(R)))
'''


# 17528
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return  (P) <= (((Q) and (not A)) <= (not P))

R = []
M = [x / 4 for x in range(10 * 4, 60 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
print(round(min(R)))
'''

# 16833
'''
def F(x, a1, a2):
    Q = 75 <= x <= 118  # (x∈q)
    P = 25 <= x <= 73  # (x∈p)
    A = a1 <= x <= a2  # (x∈A)
    return  ((A) and (not Q)) <= ((P) or (Q))

R = []
M = [x / 4 for x in range(5 * 4, 120 * 4)]
#print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
#print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
print(round(max(R)))
'''



# 18266
'''
for A in range(1, 10**5):
    k = True
    for x in range(1, 10**5):
        if ((x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))) == False:
            k = False
            break
    if k == True:
        print(A)
        break

# Вариант 2
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))

for A in range(1, 10**5):
    if all(F(x, A) for x in range(1, 10**5)):
        print(A)
        break
'''


# 14352
'''
def F(x, A):
    B = 120 <= x <= 180  # (x∈B)
    return (x % A == 0) or ((B) <= ((x % 16 != 0 ) or (x+A<=204)))

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14, 15, 25]
# КЕГЭ = []
# на следующем уроке:
