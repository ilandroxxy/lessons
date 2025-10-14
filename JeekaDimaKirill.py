# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23374 Резервный день 19.06.25 (Уровень: Базовый)
# Для какого наименьшего целого положительного числа А выражение
# (x<A)∧(y<3A)∨(2x+y>128)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
# Вариант 1
def F(x, y, A):
    return (x<A) and (y<3*A) or (2*x+y>128)

for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):  # 9801
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break

# Вариант 2
def F(x, y, A):
    return (x<A) and (y<3*A) or (2*x+y>128)

for A in range(1, 1000):
    cnt = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == True:
                cnt += 1
    if cnt == 9801:
        print(A)
        break

# Вариант 3

def F(x, y, A):
    return (x<A) and (y<3*A) or (2*x+y>128)

RES = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''

# Вариант 4
'''
print(min([A for A in range(1, 1000) if all( ((x<A) and (y<3*A) or (2*x+y>128)) for x in range(1, 100) for y in range(1, 100))]))
'''


# № 23561 Пересдача 03.07.25 (Уровень: Базовый)
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
'''
def F(x, A):
    return ((x & 52 != 0) and (x & 48 == 0)) <= (x & A != 0)

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(min(RES))
'''

# 23374
# Для какого наименьшего целого положительного числа А выражение (x < A) ∧ (y < 3A) ∨ (2x + y > 128)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
RES = []
def F(x, y, A):
    return (x < A) and (y < 3*A) or (2*x + y > 128)
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        RES.append(A)
print(min(RES))
'''


# 20577
#(x & A ≠ 0) → ((x & 698 = 0) → (x & 321 ≠ 0))
'''
def F (x , A):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))

RES = []
for A in range(1, 5000):
    if all(F(x, A) for x in range (1, 10000)):
        RES.append(A)
print (max(RES))
'''


# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or ((B) <= (x % 22 != 0))

RES = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        RES.append(A)
print(max(RES))
'''


# № 20905 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

RES = []
M = [x / 4 for x in range(10 * 4, 90 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            RES.append(a2 - a1)
print(min(RES))

# 29.0 -> 29
# 29.4 -> 30
# 29.5 -> 29.75 -> 29.80 -> 30
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 13, 14, 15]
# КЕГЭ = []
# на следующем уроке: 16, 23, 19-21, 25
