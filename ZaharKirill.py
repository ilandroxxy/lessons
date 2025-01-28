# region Домашка: ******************************************************************

# № 2152 (Уровень: Базовый)
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+4, b) + F(a+10, b) + F(2*a + 1, b)

print(F(2, 27))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 15 №37150
'''
def F(x, y, A):
    return (2*x + y != 70) or (x < y) or (A < x)


for A in range(1, 10000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
'''

# Вариант 2
'''
def F(x, y, A):
    return (2*x + y != 70) or (x < y) or (A < x)

R = []
for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(max(R))

# Вариант 3

print(max([A for A in range(1, 10000) if all(((2*x + y != 70) or (x < y) or (A < x)) for x in range(1, 100) for y in range(1, 100))]))
'''


# Тип 15 №69925
'''
def F(x, A):
    B = 70 <= x <= 90
    return (x % A == 0) or ((B) <= (not(x % 22 == 0)))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

# Тип 15 №38949
'''
def F(x, A):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(F(x, A)  for x in range(1, 10000)):
        print(A)
        break
'''


# Тип 15 №36028
'''
def F(x, a1, a2):
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 100 * 4)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 17.0 -> 17
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 13, 14, 15, 16, 23]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]
