# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


print(is_prime(7))  # True
print(is_prime(8))  # False
print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(len(divisors(7)) == 0)  # True
print(len(divisors(8)) == 0)  # False
'''


# № 5477 (Уровень: Средний)
'''
def is_prime(x):
    if x <= 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True


cnt = 0
for x in range(600_000+1, 10**10):
    if x % 6 == 0:
        if is_prime(x-1) and is_prime(x+1):
            print(x-1, x+1)
            cnt += 1
            if cnt == 6:
                break
'''
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(600_000+1, 10**10):
    if x % 6 == 0:
        if len(divisors(x-1)) == 0 and len(divisors(x+1)) == 0:
            print(x-1, x+1)
            cnt += 1
            if cnt == 6:
                break
'''

# № 21903 Открытый вариант 2025 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3 and abs(x) % 100 == 15]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if ((x > 0) + (y > 0) + (z > 0) == 3) or ((x < 0) + (y < 0) + (z < 0) == 3):
        if min(x, y, z) * max(x, y, z) > min(A) ** 2:
            R.append(min(x, y, z) * max(x, y, z))
print(len(R), min(R))
'''




# № 21712 ЕГКР 19.04.25 (Уровень: Базовый)

M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4  and abs(x) % 10 == 6]
B = [x for x in A if x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: 22

# Первый пробник 21.12.24:
# Михаил 8/18 -> 46 вторичных баллов +[2, 4, 6, 12, 14, 15, 16, 23] -[1, 3, 5, 7, 8, 9, 11, 13, 17, 25]

# Второй пробник 28.02.25:
# Михаил 17/29 -> 70 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-16, 18, 19-20, 23, 25] -[5, 7, 10, 13, 17, 21, 22, 24]
# Егор 16/29 -> 68 вторичных баллов +[1-7, 9, 13, 14-18, 23, 25] -[8, 10, 11, 12, 19-21, 22, 24]

# Третий пробник 20.05.25:
# Михаил 19/29 -> 75 вторичных баллов +[1, 2, 5, 6, 7, 9-16, 18-20, 23-25] -[3, 4, 8, 17, 21, 22]