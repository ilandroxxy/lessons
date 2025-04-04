# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
def F(a, b):
    if a >= b:
        return a == b  # True/False
    h = [F(a + 1, b), F(a + 2, b), F(a * 3, b)]
    return sum(h)
'''

# n = 1: Петин первый ход
# n = 2: Ванин первый ход
# n = 3: Петин второй ход
# n = 4: Венин второй ход

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 16385 ЕГКР 27.04.24 (Уровень: Базовый)
'''
def F(s, n):
    if s >= 435:
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(s+5, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 435) if F(s, 2)])
print([s for s in range(1, 435) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 435) if F(s, 4) and not F(s, 2)])
'''

# № 17875 Демоверсия 2025 (Уровень: Базовый)
# 1 куча: -2, -5, /3 вниз | <= 19 | S ≥ 20
'''
from math import ceil, floor
def F(s, n):
    if s <= 19:
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(s-5, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h) # при любом ходе Пети Ваня может выиграть своим первым ходом
    # return any(h) if (n - 1) % 2 == 0 else any(h) # Ваня может выиграть после неудачного хода Пети

print([s for s in range(20, 1000) if F(s, 2)])
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 74) if F(7, s, 2)])  # [19,
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ = []
# на следующем уроке:

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


