# region Домашка: ******************************************************************


# № 8426 (Уровень: Средний)
# https://stepik.org/lesson/1038709/step/4?unit=1062775
'''
def F(n):
    if n > 1_000_000:
        return n
    if n <= 1_000_000:
        return n + F(2 * n)


def G(n):
    return F(n) / n


cnt = 0
r = G(2000)
for n in range(1, 100000):
    if G(n) == r:
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 15 №68516


# Вариант 1 - Решение через флаги
'''
def F(x, A):
    return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))


R = []
for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        R.append(A)
        
print(max(R))
'''

# Вариант 2 - Решение через счетчик
'''
def F(x, A):
    return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))


R = []
for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if F(x, A):
            k += 1
    if k == 999:
        R.append(A)

print(max(R))
'''

# Вариант 3 - Решение через all()
'''
def F(x, A):
    return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''

# Вариант 4 - Решение через all() в одну строку
'''
print(max([A for A in range(1, 1000) if all((x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0)) for x in range(1, 10000))]))
'''


# Тип 15 №60257
# Для какого наименьшего целого неотрицательного числа А выражение
# (x + 2y < A) ∨ (y > x) ∨ (x > 60)
# тождественно истинно (то есть принимает значение 1) при любых целых неотрицательных х и y?
'''
def F(x, y, A):
    return (x + 2*y < A) or (y > x) or (x > 60)


R = []
for A in range(1, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        R.append(A)
print(min(R))
'''


'''
def F(x, A):
    return ((x & 41 != 0) <= ((x & 33 == 0) <= (x & A != 0)))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(min(R))
'''


# Тип 15 №34521
'''
def F(x, A):
    return (x & 51 == 0) or ((x & 41 == 0) <= (x & A == 0))


R = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(10000)):
        R.append(A)
print(max(R))
'''


# Тип 15 №34543
# На числовой прямой даны два отрезка: P=[3, 13] и Q=[12, 22].
# Какова наибольшая возможная длина интервала A, что формула
# ((х ∈ A) → (х ∈ Р)) ∨ (х ∈ Q)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

'''
def F(x, a1, a2):
    P = 3 <= x <= 13
    Q = 12 <= x <= 22
    A = a1 <= x <= a2
    return (A <= P) or Q

R = []
M = [x / 4 for x in range(0 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))
'''


# Тип 15 №34547
'''
def F(x, a1, a2):
    P = 8 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P or A) <= (Q or A)


R = []
M = [x / 4 for x in range(0 * 4, 60 * 4)]
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
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 25]
# КЕГЭ  = []
# на следующем уроке:
