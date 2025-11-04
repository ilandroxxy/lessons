# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Пример 23 номера
'''
def F(a, b):
    if a > b or a == 21:
        return 0
    elif a == b:
        return 1
    else:
        h = [F(a + 2, b), F(a + 3, b), F(a * 2, b)]
        return sum(h)

print(F(7, 14) * F(14, 32))
'''


# № 22437 (Уровень: Базовый)
# 1 куча: +4, +7, *4 | s >= 471 | 1 ≤ s ≤ 470

# s - это кол-во камней в куче
# n - это шаг игры:
# n = 1: Петя 1
# n = 2: Ваня 1
# n = 3: Петя 2
# n = 4: Ваня 2
'''
def F(s, n):
    if s >= 471:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+4, n-1), F(s+7, n-1), F(s*4, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 471) if F(s, n=2)])
print([s for s in range(1, 471) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 471) if F(s, n=4) and not F(s, n=2)])
'''


# № 21905 Открытый вариант 2025 (Уровень: Базовый)
# 1 куча: +1, +4, *3 | s >= 67 | 1 ≤ s ≤ 66
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 67) if F(s, n=2)])
print([s for s in range(1, 67) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 67) if F(s, n=4) and not F(s, n=2)])
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
    h = [F(s-3, n-1), F(s-5, n-1), F(floor(s/4), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(31, 1000) if F(s, n=2)])
print([s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''

# № 22066 (Уровень: Базовый)
# 2 кучи: a+3, s+3, a*2, s*2 | a + s >= 100 | a = 17 | 1 ≤ s ≤ 82
'''
def F(a, s, n):
    if a+s >= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+3, s, n-1), F(a, s+3, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 83) if F(17, s, n=2)])
print([s for s in range(1, 83) if F(17, s, n=3) and not F(17, s, n=1)])
print([s for s in range(1, 83) if F(17, s, n=4) and not F(17, s, n=2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 74) if F(7, s, n=2)])
print([s for s in range(1, 74) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 74) if F(7, s, n=4) and not F(7, s, n=2)])
'''


# № 19635 (Уровень: Базовый)
# 2 кучи: a-3 и s-3, a/2, s/2 (вниз) | a + s <= 100 | a = 48 | s > 52
'''
from math import floor, ceil
def F(a, s, n):
    if a+s <= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s-3, n-1), F(floor(a/2), s, n-1), F(a, floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(53, 1000) if F(48, s, n=2)])
print([s for s in range(53, 1000) if F(48, s, n=3) and not F(48, s, n=1)])
print([s for s in range(53, 1000) if F(48, s, n=4) and not F(48, s, n=2)])
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
