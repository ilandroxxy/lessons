# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
def F(a, b):
    if a >= b:
        return a == b
    h = [F(a+1, b), F(a+2, b), F(a*2, b)]
    return sum(h)
'''

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1 +4 *2 | >=51 | 1 ≤ S ≤ 50
'''
# n = 1: Первый Петин ход
# n = 2: Первый Ванин ход
# n = 3: Второй Петин ход
# n = 4: Второй Ванин ход

def F(s, n):
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    # if (n - 1) % 2 == 0:
    #     return any(h)
    # else:
    #     return all(h)
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 17638 Основная волна 19.06.24 (Уровень: Базовый)
'''
def F(s, n):
    if s >= 39:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+3, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 39) if F(s, 2)])
print([s for s in range(1, 39) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 39) if F(s, 4) and not F(s, 2)])
'''


# № 18144 (Уровень: Базовый)
# 1 куча: -4, -6, /2 вверх | <= 19 | s >= 20
'''
from math import ceil, floor

def F(s, n):
    if s <= 19:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-4, n-1), F(s-6, n-1), F(ceil(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

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
    return any(h) if (n - 1) % 2 == 0 else all(h)  # any(h) - для 19 номера

print([s for s in range(1, 74) if F(7, s, 2)])  # [19,
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = [9, 13, 22, 24, 25]
# на следующем уроке:


# Первый пробник 21.12.24:
# Ефим 12/25 -> 56 вторичных баллов +[1-4, 7, 8, 11, 14-18] -[5, 6, 9, 10, 12, 19-21, 22, 23, 24, 25]
