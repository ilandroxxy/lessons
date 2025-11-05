# region Домашка: ******************************************************************

# № 3376 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(21, 10**8, 21):
    if fnmatch(str(x), '1*5*9'):
        m2 = [j for j in range(len(str(x))-1)]
        m1 = [j for j in range(len(str(x))-1) if str(x)[j] < str(x)[j+1]]
        if len(m2) == len(m1):
            print(x, x//21)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



'''
def F(x, y, A):
    return (not((x < 7) or (y >= 5*x + A - 60) or (x >= 36) or (y < 225)))

for A in range(1000, 0, -1):
    if all(F(x, y, A) == False for x in range(0, 100) for y in range(0, 10000)):
        print(A)
        break
'''


# № 12483 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 79 != 0) and ((x & 31 == 0) <= (x & A != 0))

for A in range(0, 1000):
    if all(F(x, A) for x in range(90, 100+1)):
        print(A)
        break
'''


# № 12469 (Уровень: Базовый)
# На числовой прямой даны два отрезка: D = [7; 68] и C = [29; 100].
# Укажите наименьшую возможную длину
# такого отрезка A, для которого логическое выражение
# (x∈D) → ((¬(x∈C) ∧ ¬(x∈A)) → ¬(x∈D))
# истинно (т.е. принимает значение 1) при любом значении переменной х.
'''
def F(x, a1, a2):
    D = 7 <= x <= 68  # x∈D
    C = 29 <= x <= 100  # x∈C
    A = a1 <= x <= a2  # x∈A
    return (D) <= (((not C) and (not A)) <= (not D))

RES = []
M = [x / 10 for x in range(5*10, 120*10)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))  # 21.75 -> 21.8 -> 21.9
'''


# https://inf-ege.sdamgia.ru/problem?id=34541
'''
def F(x, a1, a2):
    P = 3 <= x <= 38
    Q = 21 <= x <= 57
    A = a1 <= x <= a2
    return ((Q) <= (P)) <= (not A)

res = []
M = [x / 5 for x in range(1 * 5, 100 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            res.append(a2 - a1)
print(max(res))  # 18.79999 -> 19
'''


'''
def F(x, y, A):
    return (3 * x + y > 48) or (x > y) or (4 * x + y < A)

for A in range(10000, -1, -1):
    if any(F(x, y, A) == 0 for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break
'''


def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


res = []
M = [x / 5 for x in range(5 * 5, 120 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            res.append(a2 - a1)
print(round(min(res)))


# https://stepik.org/lesson/1228673/step/12?unit=1242206
def F(x, A):
    return ((x in B) <= (x % 7 != 0)) or (A > 2 * x)


B = list(range(120, 130 + 1))

for A in range(1, 1000):
    if all(F(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 9, 13, 14, 15, 17, 25]
# КЕГЭ = []
# на следующем уроке: