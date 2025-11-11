# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 22437 (Уровень: Базовый)
# 1 куча: +4, +7, *4 | s >= 471 | 1 ≤ s ≤ 470

# s - кол-во камней, которое ищем
# n - это шаг нашей игры

# шаг 1: Петя 1
# шаг 2: Ваня 1
# шаг 3: Петя 2
# шаг 4: Ваня 2
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


# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча: -2, /2 (вниз) | s <= 87 | s > 88
'''
from math import floor, ceil

def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(88, 1000) if F(s, n=2)])
print([s for s in range(88, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(88, 1000) if F(s, n=4) and not F(s, n=2)])
'''

# № 19635 (Уровень: Базовый)
# 2 кучи: a-3 s-3, a / 2, s / 2 (вниз) | a + s <= 100 | a = 48 | s > 52
'''
from math import floor, ceil

def F(a, s, n):
    if a + s <= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s-3, n-1), F(floor(a/2), s, n-1), F(a, floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(53, 1000) if F(48, s, n=2)])
print([s for s in range(53, 1000) if F(48, s, n=3) and not F(48, s, n=1)])
print([s for s in range(53, 1000) if F(48, s, n=4) and not F(48, s, n=2)])
'''


# № 19251 ЕГКР 21.12.24 (Уровень: Базовый)
# 1 куча: +3, +6, *3 | s >= 132 | 1 <= s <= 131
'''
def F(s, n):
    if s >= 132:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+3, n-1), F(s+6, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 132) if F(s, n=2)])
print([s for s in range(1, 132) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 132) if F(s, n=4) and not F(s, n=2)])
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 6, 8, 13, 14, 15, 16, 18, 19-21, 23]
# КЕГЭ = []
# на следующем уроке:
