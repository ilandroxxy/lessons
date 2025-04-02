# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 2491 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if hex(x)[-2:] == '0f']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 7 == 0) + (y % 7 == 0) == 1:
        if (x + y) % max(D) == 0:
            R.append(x + y)
print(len(R), max(R))
'''


# № 2491 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
avg = sum(M) / len(M)
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x < avg) or (y < avg) or (z < avg):
        if all('9' in str(p) for p in (x, y, z)):
            R.append(x + y + z)
print(len(R), max(R))
'''


# 1) Петя 1
# 2) Ваня 1
# 3) Петя 2
# 4) Ваня 2
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])


def F(a, s, n):
    if s + a >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if F(7, s, 2)])  # 19
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])  # 20
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])  # 20
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 23, 25]
# КЕГЭ = []
# на следующем уроке: ТИ на две/одну кучу кодом


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]

# Второй пробник 28.02.25:
# Матвей 14/29 -> 62 вторичных баллов +[1-4, 6, 7, 10, 11, 14, 15, 16, 18, 23, 25] -[5, 8, 12, 13]
