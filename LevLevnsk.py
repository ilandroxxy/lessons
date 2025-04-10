# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

def gameOver(pos):
    return sum(pos) >= 77


def moves(pos):
    x, y = pos
    return (x + 1, y), (2 * x, y), (x, y + 1), (x, 2 * y)


def win(pos, M):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return False
    r = [win(move, M - 1)
         for move in moves(pos)]
    return any(r) if M % 2 != 0 else \
        all(r)


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# M = 1: Петя первый ход
# M = 2: Ваня первый ход
# M = 3: Петя Второй ход
# M = 4: Ваня Второй ход
'''
def F(s, m):
    if s >= 51:  # условие победы
        return m % 2 == 0
    if m == 0:
        return 0
    h = [F(s+1, m-1), F(s+4, m-1), F(s*2, m-1)]  # действия
    return any(h) if (m - 1) % 2 == 0 else all(h)  # all / any

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])

'''
# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча | -2, /2 вниз | <= 87 | s > 88
'''
from math import ceil, floor
def F(s, m):
    if s <= 87:  # условие победы
        return m % 2 == 0
    if m == 0:
        return 0
    h = [F(s-2, m-1), F(floor(s/2), m-1)]  # действия
    return any(h) if (m - 1) % 2 == 0 else all(h)  # all / any

print([s for s in range(89, 1000) if F(s, 2)])
print([s for s in range(89, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(89, 1000) if F(s, 4) and not F(s, 2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | 1 ≤ S ≤ 73
'''
def F(a, s, m):
    if a+s >= 81:  # условие победы
        return m % 2 == 0
    if m == 0:
        return 0
    h = [F(a+1, s, m-1), F(a, s+1, m-1), F(a*2, s, m-1), F(a, s*2, m-1)]  # действия
    return any(h) if (m - 1) % 2 == 0 else all(h)  # all / any

print([s for s in range(1, 74) if F(7, s, 2)])
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
# ФИПИ = [5, 8, 9, 14, 15]
# КЕГЭ = []
# на следующем уроке: 12, 23, 25, 26/27, 19-21


# Первый пробник 7.03.25:
# Лев 8/46 -> _ вторичных баллов +[2, 5, 15, 16, 19, 20, 23, 25] -[8, 9, 12, 21]
