# region Домашка: ************************************************************

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
def F(a, b):
    if a >= b:
        return a == b  # True/False
    h = [F(a+2, b), F(a*2, b)]
    return sum(h)
'''

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# s - кол-во камней в куче
# n - шаг нашей игры

# n = 1: Петя первый шаг
# n = 2: Ваня первый шаг
# n = 3: Петя второй шаг
# n = 4: Ваня второй шаг
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
'''

# № 17682 Пересдача 04.07.24 (Уровень: Базовый)
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+3, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 67) if F(s, 2)])
print([s for s in range(1, 67) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 67) if F(s, 4) and not F(s, 2)])
'''

# № 17976 (Уровень: Базовый)
# 1 куча: -3, -5, /2 вниз | <= 17 | s >= 18
'''
from math import ceil, floor

def F(s, n):
    if s <= 17:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-5, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(18, 1000) if F(s, 2)])
print([s for s in range(18, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(18, 1000) if F(s, 4) and not F(s, 2)])
'''

# № 16330 Открытый вариант 2024 (Уровень: Базовый)
'''
def F(a, s, n):
    if a+s >= 59:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 54) if F(5, s, 2)])  # [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
print([s for s in range(1, 54) if F(5, s, 3) and not F(5, s, 1)])  # [24, 26]
print([s for s in range(1, 54) if F(5, s, 4) and not F(5, s, 2)])  # [23, 25]
'''
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [7, 11, 12, 17]
# на следующем уроке: 9, 10,


# Первый пробник 21.12.24:
# 4/8 -> 29 вторичных баллов +[1, 10, 16, 23] -[2, 4, 12, 15]

# Второй пробник 28.02.25:
# 10/29 -> 48 вторичных баллов +[1, 2, 4, 10, 12, 14, 15, 16, 23, 25] -[11]
