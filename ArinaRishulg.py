# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


'''
def divisors(x):
    x = 24
    div = []
    for j in range(1, int(x**0.5)+1):  # 1 2 3 4 5
        if 24 % j == 0:  # 1 2 3 4
            div += [j, 24 // j]
            #       1     24
            #       2     12
            #       3      8
            #       4      6
            #
    div = [1, 24, 2, 12, 3, 8, 4, 6]
    return sorted(set(div))
    # [1, 2, 3, 4, 6, 8, 12, 24]

divisors(24)



def divisors(x):
    x = 24
    div = []
    for j in range(2, int(x**0.5)+1):  # 1 2 3 4 5
        if 24 % j == 0:  # 2 3 4
            div += [j, 24 // j]
            #       2     12
            #       3      8
            #       4      6
            #
    div = [1, 24, 2, 12, 3, 8, 4, 6]
    return sorted(set(div))
    # [1, 2, 3, 4, 6, 8, 12, 24]

divisors(24)
'''


'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

# не считая единицы и самого числа.
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))
'''


# № 20814 Апробация 05.03.25 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(500_001, 10**10):
    div = divisors(x)
    R = sum(div)
    if R % 10 == 9:
        print(x, R)
        input()
'''


# № 17564 Основная волна 08.06.24 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(700_001, 10**10):
    d = [j for j in divisors(x)]
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(x, M)
            input()
'''


# № 17642 Основная волна 19.06.24 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(800_001, 10**10):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9]
    if len(d) > 0:
        print(x, min(d))
        input()
'''
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16, 17, 18, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 17, 22, 25


# Первый пробник 7.03.25:
# Арина 12/29 -> 56 вторичных баллов +[1, 2, 3, 4, 5, 8, 9, 11, 12, 14, 15, 23] -[7, 13, 17, 19-21, 18, 25]
