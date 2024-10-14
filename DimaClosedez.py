# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def divisors(x):  # 24
    div = []
    for j in range(1, x+1):
        if x % j == 0:
            div.append(j)
    return div


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
'''


'''
def nod(a, b):  # Функция поиска НОД
    div = []
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            div.append(j)
    return max(div)


print(nod(12, 24))
'''


# Тип 15 №33517
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число
# n делится без остатка на натуральное число m».
#
# Для какого наибольшего натурального числа А формула
# ДЕЛ(70, A) ∧ (ДЕЛ(x, 28) → (¬ДЕЛ(x, А) → ¬ДЕЛ(x, 21)))
#
# тождественно истинна (то есть принимает значение 1 при любом
# натуральном значении переменной x)?

# Вариант 1
'''
def F(x, A):
    return (70 % A == 0) and ((x % 28 == 0) <= ((x % A != 0) <= (x % 21 != 0)))


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

# Вариант 2
'''
def F(x, A):
    return (70 % A == 0) and ((x % 28 == 0) <= ((x % A != 0) <= (x % 21 != 0)))


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

# Вариант 3
'''
def F(x, A):
    return (70 % A == 0) and ((x % 28 == 0) <= ((x % A != 0) <= (x % 21 != 0)))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))


# Вариант 4

print(max([A for A in range(1, 1000) if all(((70 % A == 0) and ((x % 28 == 0) <= ((x % A != 0) <= (x % 21 != 0)))) for x in range(1, 10000))]))
'''


# Тип 15 №18594
# Для какого наименьшего целого неотрицательного числа A выражение
# (2m + 3n > 43) ∨ (m < A) ∨ (n ≤ A)
# тождественно истинно при любых целых неотрицательных m и n?
'''
def F(m, n, A):
    return (2*m + 3*n > 43) or (m < A) or (n <= A)


for A in range(0, 1000):
    if all(F(m, n, A) for m in range(100) for n in range(100)):
        print(A)
        break
'''

# Тип 15 №39244
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Для какого наименьшего неотрицательного целого числа А формула
# (x & 105 = 0) → ((x & 58 ≠ 0) → (x & А ≠ 0))
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

'''
def F(x, A):
    return (x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))

for A in range(0, 1000):
    if all(F(x, A) for x in range(0, 1000)):
        print(A)
        break
'''


# Тип 15 №7763
# На числовой прямой даны два отрезка: P=[5, 30] и Q=[14, 23].
# Укажите наибольшую возможную длину промежутка A, для которого формула
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''
def F(a1, a2, x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = a1 <= x <= a2
    return (P == Q) <= (not A)


R = []
M = [x / 10 for x in range(2 * 10, 40 * 10)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) for x in M):
            R.append(a2 - a1)
print(max(R))  # 8.75 -> 8.8 -> 8.9 -> 9
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 25]
# КЕГЭ  = []
# на следующем уроке:
