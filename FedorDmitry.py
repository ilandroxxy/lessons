# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
def F(a, b):
    if a > b or a == 16:
        return 0
    elif a == b:
        return 1
    h = [F(a+1, b), F(a+2, b), F(a*3, b)]
    return sum(h)

print(F(2, 9) * F(9, 18))
'''


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | s >= 51 | 1 <= s <= 50
'''
def F(s, n):
    """
    :param s: это кол-во камней в куче (перебираем и будем искать)
    :param n: это шаги нашей игры

    n = 1: Петин первый шаг
    n = 2: Ванин первый шаг
    n = 3: Петин второй шаг
    n = 4: Ванин второй шаг
    """
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 50+1) if F(s, n=2)])
print(20, [s for s in range(1, 50+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 50+1) if F(s, n=4) and not F(s, n=2)])
'''

# № 23278 Основная волна 11.06.25 (Уровень: Базовый)
# 1 куча: -3, -8, /3 (вниз) | s <= 16 | s >= 17
'''
from math import ceil, floor
def F(s, n):
    if s <= 16:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-8, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(17, 1000) if F(s, n=2)])
print(20, [s for s in range(17, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(17, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 23337 (Уровень: Средний)
# 2 кучи: a-3 s-4, a-8 s/2 (вниз), a/2 s-10 (вверх) | a + s <= 200 | a = 110 | s ≥ 100
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 200:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s-4, n-1), F(a-8, floor(s / 2), n-1), F(ceil(a / 2), s-10, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(100, 1000) if F(110, s, n=2)])
print(20, [s for s in range(100, 1000) if F(110, s, n=3) and not F(110, s, n=1)])
print(21, [s for s in range(100, 1000) if F(110, s, n=4) and not F(110, s, n=2)])
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14, 15, 16, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке:
