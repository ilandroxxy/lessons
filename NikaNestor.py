# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19251 ЕГКР 21.12.24 (Уровень: Базовый)
# 1 куча: +3, +6, *3 | s >= 132 | 1 ≤ s ≤ 131

# s - это кол-во камней в куче
# n - это шаг нашей игры

# n = 1: Петин первый шаг
# n = 2: Ванин первый шаг
# n = 3: Петин второй шаг
# n = 4: Ванин второй шаг
'''
def F(s, n):
    if s >= 132:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+3, n-1), F(s+6, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 132) if F(s, n=2)])
print(20, [s for s in range(1, 132) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 132) if F(s, n=4) and not F(s, n=2)])
'''

'''
def F(s, n):
    if s >= 301:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 3, n - 1), F(s * 5, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)


print(19, [s for s in range(1, 301) if F(s, n=2)])
print(20, [s for s in range(1, 301) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 301) if F(s, n=4) and not F(s, n=2)])
'''

# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (вниз) | s <= 30 | s ≥ 31
'''
from math import floor, ceil
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s -3, n - 1), F(s - 5, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(31, 1000) if F(s, n=2)])
print(20, [s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''

# № 22066 (Уровень: Базовый)
# 2 кучи: a+3, s+3, a*2, s*2 | a + s >= 100 | a = 17 | 1 ≤ s ≤ 82
'''
def F(a, s, n):
    if a+s >= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+3, s, n - 1), F(a, s+3, n - 1), F(a*2, s, n - 1), F(a, s*2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)


print(19, [s for s in range(1, 83) if F(17, s, n=2)])
print(20, [s for s in range(1, 83) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(1, 83) if F(17, s, n=4) and not F(17, s, n=2)])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 27
