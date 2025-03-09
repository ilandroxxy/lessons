# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not((not P) <= Q)) <= (A <= ((not Q) <= P))


R = []  # сюда складывать будем длины a2 - a1
M = [x / 4 for x in range(5 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(max(R))
'''

'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 70 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(int(min(R)))
'''


# 24  24 / 4 == 0   24 // 4 = 6
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(800_000+1, 10**10):
    d = [j for j in divisors(x) if j != x and j != 9 and j % 10 == 9]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


def divisors(x):
    div = []
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

print(divisors(24))

cnt = 0
for x in range(174457, 174506):
    d = [j for j in divisors(x)]
    if len(d) == 2:
        print(*d)
        cnt += 1

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ = [22, 25]
# на следующем уроке: повторить 22, 19-21, разобрать 3 с пробника

# Второй пробник 28.02.25:
# Славик 16/25 -> 67 вторичных баллов +[1, 2, 4-14, 16, 17, 18] -[3, 15, 19-21, 22-25]