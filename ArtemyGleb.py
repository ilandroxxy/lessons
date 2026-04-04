# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


#
# № 25358 ЕГКР 13.12.25 (Уровень: Базовый)
# 1 куча: +2, +4, *2 | s >= 125 | 1 ≤ s ≤ 124
'''
def F(s, n):
    """
    :param s: - кол-во камней в исходной куче (то, что будем искать)
    :param n: - это шаг нашей игры

    n = 1: Петя первый ход
    n = 2: Ваня первый ход
    n = 3: Петя второй ход
    n = 4: Ваня второй ход
    """
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n - 1), F(s + 4, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # any(h)

print(19, [s for s in range(1, 124+1) if F(s, n=2)])
print(20, [s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''

# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (вниз) | s <= 30 | s >= 31
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 5, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # any(h)

print(19, [s for s in range(31, 1000) if F(s, n=2)])
print(20, [s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 23203 Основная волна 10.06.25 (Уровень: Базовый)
# 1 куча: -3, -7, /3 (вниз) | s <= 11 | s > 11
'''
from math import ceil, floor
def F(s, n):
    if s <= 11:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 7, n - 1), F(floor(s / 3), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # any(h)

print(19, [s for s in range(12, 1000) if F(s, n=2)])
print(20, [s for s in range(12, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(12, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 27774 Апробация 04.03.26 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a + s >= 207 | a = 17 | 1 < s <= 189

def F(a, s, n):
    if a + s >= 207:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 1, s, n - 1), F(a, s + 1, n - 1), F(a * 2, s, n - 1), F(a, s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(2, 189+1) if F(17, s, n=2)])
print(20, [s for s in range(2, 189+1) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(2, 189+1) if F(17, s, n=4) and not F(17, s, n=2)])



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 9, 14, 15, 16, 17, 23, 19-21, 27]
# КЕГЭ = []
# на следующем уроке: