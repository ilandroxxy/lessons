# region Домашка: ************************************************************


'''
def G(n):
    return F(n) / n


def F(n):
    if n > 1_000_000:
        return n
    if n <= 1_000_000:
        return n + F(2 * n)


cnt = 0
r = G(2000)
for n in range(1, 10**6+1):
    if G(n) == r:
        cnt += 1
print(cnt)
'''


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 18175 (Уровень: Базовый)

# Вариант 1
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


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
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 1000):
    cnt = 0
    for x in range(1, 10000):
        if F(x, A) == True:
            cnt += 1
    if cnt == 9999:
        R.append(A)
print(max(R))
'''

# Вариант 3
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))


# Вариант 4
print(max([A for A in range(1, 1000) if all( (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) for x in range(1, 10000))]))
'''


# № 17678 Пересдача 04.07.24 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x + y <= 24) or (y <= x - 2) or (y >= A)


R = []
for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        R.append(A)

print(max(R))
'''


# № 17556 Основная волна 08.06.24 (Уровень: Базовый)

'''
def F(x, A):
    B = 70 <= x <= 90
    return (x % A == 0) or (B <= (x % 22 != 0))

R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(10000)):
        R.append(A)
print(max(R))
'''

# № 14348 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 47 == 0) or ((x & 13 == 0) <= (x & A != 0))


for A in range(0, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

'''
def F(x, a1, a2):
    B = 34 <= x <= 72
    C = 32 <= x <= 61
    A = a1 <= x <= a2
    return (B <= A) and ((not C) or A)


R = []
M = [x / 5 for x in range(30 * 5, 80 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 40.0 -> 40, 40.7 -> 41, 40.2 -> 40
'''


'''
def F(x, a1, a2):
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    A = a1 <= x <= a2
    return C <= ((B and (not A)) <= (not C))


R = []
M = [x / 5 for x in range(50 * 5, 160 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# № 15330 Досрочная волна 2024 (Уровень: Базовый)

def F(x, a1, a2):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= (((not A) and B) <= (not C))


R = []
M = [x / 5 for x in range(20 * 5, 120 * 5)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))




# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ = []
# на следующем уроке:
