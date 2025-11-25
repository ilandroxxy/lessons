# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 23 (типовое решение)
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        h = [F(a+1, b), F(a+2, b), F(a+3, b)]
        return sum(h)

print(F(5, 7) * F(7, 11))
'''

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | s >= 51 | 1 ≤ s ≤ 50
'''
def F(s, n):
    """
    :param s: Кол-во камней в куче (будем перебирать и искать)
    :param n: Это шаги нашей игры!!

    n = 1: Первый ход Пети
    n = 2: Первый ход Вани
    n = 3: Второй ход Пети
    n = 4: Второй ход Вани
    """

    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 51) if F(s, n=2)])
print(20, [s for s in range(1, 51) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 51) if F(s, n=4) and not F(s, n=2)])
'''


# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (вниз) | s <= 30 | s ≥ 31
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-5, n-1), F(floor(s/4), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(31, 1000) if F(s, n=2)])
print(20, [s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''



# № 18268 (Уровень: Базовый)
# 2 кучи: a-3, s-3, a/2, s/2 (вверх) | a + s <= 72 | a = 50 | s > 22
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 72:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s, n-1), F(a, s-3, n-1), F(ceil(a / 2), s, n-1), F(a, ceil(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(23, 1000) if F(50, s, n=2)])
print(20, [s for s in range(23, 1000) if F(50, s, n=3) and not F(50, s, n=1)])
print(21, [s for s in range(23, 1000) if F(50, s, n=4) and not F(50, s, n=2)])
'''


# endregion Урок: *************************************************************
#
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
