# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20580 (Уровень: Базовый)
'''
def F(x, y, A):
    return (9*x + y > A) or (x >= 36) or (y >= 18)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
'''


# № 20584 (Уровень: Базовый)
'''
def F(x, A):
    return ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

# № 20809 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, A):
    B = 60 <= x <= 80
    return (x % A == 0) or ((B) <= (x % 22 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 20577 (Уровень: Базовый)
'''
def F(x, A):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''


# № 21710 ЕГКР 19.04.25 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= ((B) == (C))


R = []
M = [x / 4 for x in range(30 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# № 20905 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# № 21413 Досрочная волна 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        print(x, (A + B + C) // 20)
'''



# № 19562 (Уровень: Базовый)
'''
n = 16807**35 + 2401**2 * 343**9 - 49**52 + 7**3 - 2005
R = []
while n > 0:
    R.append(n % 49)
    n //= 49
R.reverse()
print(len([x for x in R if x > 9]))
'''


# № 19484 (Уровень: Базовый)
'''
n = 5 * 729 ** 2024 + 3*243**1413 - 7 * 81**169 - 2*9**107 + 3017
R = []
while n > 0:
    R.append(n % 27)
    n //= 27
R.reverse()
print(sum([x for x in R if x <= 25 and x % 2 == 0]))
'''


# № 21900 Открытый вариант 2025 (Уровень: Базовый)
'''
for x in range(1, 2300):
    n = 7**350 + 7**150 - x
    R = []
    while n > 0:
        R.append(n % 7)
        n //= 7
    R.reverse()
    if R.count(0) == 200:
        print(x)
'''

'''
# M = []
for x in range(1, 3000):
    n = 4**210 + 4**110 - x
    R = []
    while n > 0:
        R.append(n % 4)
        n //= 4
    R.reverse()
    if R.count(0) == 105:
        print(x)
#   M.append(R.count(0))
# print(max(M))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ  = [13, 14, 15, 16, 23]
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]

# Второй пробник 28.02.25:
# Захар 7/13 -> 43 вторичных баллов +[1, 2, 10, 12, 14, 15, 16] -[4, 5, 6, 8, 13, 17, 23, 25]
# Kirill 6/13 -> 40 вторичных баллов +[2, 10, 13, 14, 15, 16] -[5, 6, 8, 12, 17, 23, 25]