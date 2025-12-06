# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    h = [F(a+1, b), F(a+2, b), F(a+3, b)]
    return sum(h)

print(F(5, 7) * F(7, 11))
'''

# № 21714 ЕГКР 19.04.25 (Уровень: Базовый)
# 1 куча: +2, +5, *2 | s >= 128 | 1 < s < 127
"""
def F(s, n):
    '''
    :param s: - Это кол-во камней в куче (то, что будем искать)
    :param n: - Это шаг нашей игры

    n = 1: Петя первый шаг
    n = 2: Ваня первый шаг
    n = 3: Петя второй шаг
    n = 4: Ваня второй шаг
    '''
    if s >= 128:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+5, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(2, 127) if F(s, n=2)])
print(20, [s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
"""


# № 23565 Пересдача 03.07.25 (Уровень: Базовый)
# 1 куча: -3, -8, /3 (вниз) | s <= 15 | s ≥ 16
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-8, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(16, 1000) if F(s, n=2)])
print(20, [s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | a = 7 | 1 ≤ s ≤ 73

def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 73+1) if F(7, s, n=2)])
print(20, [s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print(21, [s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
