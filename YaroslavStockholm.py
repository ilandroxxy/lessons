# region Домашка: ******************************************************************


# № 17564 Основная волна 08.06.24 (Уровень: Средний)
# https://stepik.org/lesson/1038816/step/14?unit=1062780
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div.append(j)
            div.append(x//j)
    return sorted(set(div))


k = 0
for x in range(700000+1, 1000000):
    d = divisors(x)
    if len(d) >= 2:
        M = max(d) + min(d)
        if M % 10 == 4:
            print(x, M)
            k += 1
            if k == 5:
                break
'''


# № 5477 (Уровень: Средний) 🌶
# https://stepik.org/lesson/1038816/step/15?unit=1062780
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div.append(j)
            div.append(x//j)
    return sorted(set(div))


k = 0
for x in range(600_000+1, 10**10):
    if x % 6 == 0:
        if len(divisors(x-1)) == 0 and len(divisors(x+1)) == 0:
            print(x-1, x+1)
            k += 1
            if k == 6:
                break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
'''
def F(x, y, A):
    return (x - 3*y < A) or (y > 400) or (x > 56)


for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# № 18877 (Уровень: Базовый)
'''
def F(x, y, A):
    return (not((x < 7) or (y >= 5*x + A - 60) or (x >= 36) or (y < 225)))


for A in range(10000, 1, -1):
    if all(F(x, y, A) == False for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
'''


# № 18266 (Уровень: Базовый)
'''
def F(x, A):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''

# 14 & 5
# 14 -> 1100_2
# 5  -> 0101_2

# Побитовая конъюнкция%


# 1110
# 0101
# 0100 -> 4


# 18175 (Уровень: Базовый)
'''
def F(x, A):
    return ((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''

# print(max([A for A in range(1, 1000) if all( (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) for x in range(1, 10000))]))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 10, 12, 13, 14, 15, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Женя 5/7 -> 34 вторичных баллов +[2, 5, 8, 12, 14] -[6, 10]
# Ярослав 2/7 -> 14 вторичных баллов +[2, 12] -[5, 6, 8, 10, 14]
