# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
'''

'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if F(x, A):
            k += 1
    if k == 999:
        print(A)
'''

'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''

'''
print(max([A for A in range(1, 1000) if all(((x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))) for x in range(1, 10000))]))
'''


# № 13082 (Уровень: Базовый)
'''
def F(x, y, A):
    return (3*x + y > 48) or (x > y) or (4*x + y < A)

for A in range(10000):
    if any(F(x, y, A) == False for x in range(100) for y in range(100)):
        print(A)
'''


# (x and y) <= z
'''
def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)


for A in range(1000000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 17528 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


R = []
M = [x/5 for x in range(100*5)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

# КЕГЭ № 12469 (Уровень: Базовый)
'''
def F(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


M = [i / 10 for i in range(110 * 10)]
R = []
for a1 in M:
    for a2 in M:
        if all(F(x) for x in M):
            R.append(a2-a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9
'''


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
'''
def F(a, b):  # a - start, b - stop
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))


def F(a, b):  # a - start, b - stop
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)


print(F(5, 7) * F(7, 11))
'''

# № 17534 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a-1, b) + F(a//2, b)

print(F(30, 8) * F(8, 1))
'''

'''
x = 152
print(x % 2 == 0)  # Четное, Делится ли на 2, Кратно ли 2
print(x % 10 == 2)  # Оканчивается на 2
print(x % 100 == 52)  # Оканчивается на 52
'''

'''
def F(a, b):
    if a > b or a == 16:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 18))
'''


# № 13830 (Уровень: Средний)

def F(a, b, c):
    if a > b:
        return 0
    elif a == b:
        return 1 and c != 'B'
    else:
        return F(a+2, b, 'A') + F(a+3, b, 'B') + F(a*2, b, 'C')


print(F(3, 20, ''))


'''
def F(a, b, c):
    if a > b:
        return 0
    elif a == b:
        print(c)
        return 1 and c[-1] != 'B'
    else:
        return F(a+2, b, c+'A') + F(a+3, b, c+'B') + F(a*2, b, c+'C')


print(F(3, 20, ''))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5*, 6, 7, 8*, 12*, 14*, 16, 18, 19-21]
# КЕГЭ  = [15, 23]
# на следующем уроке: 9, 11, 13, 25
