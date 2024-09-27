# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def divisors(x):
    div = []
    for j in range(1, int(x ** 0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


d = divisors(24)
print(d)  # [1, 2, 3, 4, 6, 8, 12, 24]


def prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x ** 0.5)+1):
        if x % j == 0:
            return False
    return True


print([x for x in range(1, 50) if prime(x)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


alphbaet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    r = ''
    while n > 0:
        r = alphbaet[n % b] + r
        n //= b
    return r


r = convert(123456789, 16)
print(r)  # 75BCD15
x = int('75BCD15', 16)
print(x)  # 123456789
'''


# Тип 15 №59756
# Для какого наименьшего целого неотрицательного числа А выражение
# (x<A)∨(y<A)∨(y>x−5)∨(y<2x−15) тождественно истинно?
'''
def F(x, y, A):
    return (x < A) or (y < A) or (y > x - 5) or (y < 2 * x - 15)


R = []
for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        R.append(A)
print(min(R))
 

# Вариант 2
print(min([A for A in range(0, 1000) if all(((x < A) or (y < A) or (y > x - 5) or (y < 2 * x - 15)) for x in range(100) for y in range(100))]))
'''


# Тип 15 №8666
# На числовой прямой даны два отрезка: P=[25; 50] и Q=[32; 47].
# Укажите наибольшую возможную длину промежутка A, для которого формула
# (¬ (x ∈ A) → (x ∈ P)) → ((x ∈ A) → (x ∈ Q))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x, a1, a2):
    P = 25 <= x <= 50
    Q = 32 <= x <= 47
    A = a1 <= x <= a2
    return ((not A) <= P) <= (A <= Q)


R = []
M = [x / 4 for x in range(20 * 4, 60 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(max(R))  # 15.0 -> 15, 15.5 -> 16
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
