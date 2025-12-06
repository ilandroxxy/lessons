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
from multiprocessing.pool import worker
from wsgiref.simple_server import software_version

# № 17638 Основная волна 19.06.24 (Уровень: Базовый)
# 1 куча: +1, +3, *2 | s >= 39 | 1 ≤ s ≤ 38
'''
def F(s, n):
    """
    :param s: - это кол-во камней в куче, которое мы ищем
    :param n: - это шаги нашей игры

    n = 1: Петя первый ход
    n = 2: Ваня первый ход
    n = 3: Петя второй ход
    n = 4: Ваня второй ход
    """
    if s >= 39:
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+3, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 38+1) if F(s, n=2)])
print(20, [s for s in range(1, 38+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 38+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 23278 Основная волна 11.06.25 (Уровень: Базовый)
# 1 куча: -3, -8, /3 (вниз) | s <= 16 | s ≥ 17
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


# № 22066 (Уровень: Базовый)
# 2 кучи: a+3, s+3, a*2, s*2 | a+s >= 100 | a=17 | 1 ≤ s ≤ 82
'''
def F(a, s, n):
    if a+s >= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+3, s, n-1), F(a, s+3, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 82+1) if F(17, s, n=2)])
print(20, [s for s in range(1, 82+1) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(1, 82+1) if F(17, s, n=4) and not F(17, s, n=2)])
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 13, 14, 15, 16, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
