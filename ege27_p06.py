# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# s - это кол-во камней в куче которое мы ищем
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 21418 Досрочная волна 2025(Уровень: Базовый)
# 1 куча: s-2, s/2 меньшего | s <= 87 | s > 88
'''
from math import ceil, floor
def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 2, n - 1), F(floor(s / 2), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(88+1, 10000) if F(s, n=2)])
print([s for s in range(88+1, 10000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(88+1, 10000) if F(s, n=4) and not F(s, n=2)])
'''


# № 31365 Пересдача 08.07.26(Уровень: Базовый)
# 2 кучи: a-2, s-2, a/3, s/3 меньшего | a + s <= 47 | a = 16 | s >= 32
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 47:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a - 2, s, n-1), F(a, s - 2, n-1), F(floor(a / 3), s, n-1), F(a, floor(s / 3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(32, 1000) if F(16, s, n=2)])
print([s for s in range(32, 1000) if F(16, s, n=3) and not F(16, s, n=1)])
print([s for s in range(32, 1000) if F(16, s, n=4) and not F(16, s, n=2)])
'''


# № 31157 Основная волна 19.06.26(Уровень: Базовый)
'''
def f(a, s, n):
    if a + s >= 171:
        return 0
    if n == 0:
        return 0
    h = [f(a + 1, s, n - 1), f(a * 2, s, n - 1), f(a, s + 1, n - 1), f(a, s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)


print([s for s in range(1, 145 + 1) if f(25, s, n=2)])
print([s for s in range(1, 145 + 1) if f(25, s, n=3) and not f(25, s, n=1)])
print([s for s in range(1, 145 + 1) if f(25, s, n=4) and not f(25, s, n=2)])
'''

# № 29974 Апробация 14.05.26(Уровень: Базовый)
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 7, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(15 + 1, 10000) if F(s, n=2)])
print([s for s in range(15 + 1, 10000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(15 + 1, 10000) if F(s, n=4) and not F(s, n=2)])
'''


# № 23378 Резервный день 19.06.25(Уровень: Базовый)
from math import ceil, floor
def F(s, n):
    if s <= 27:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 6, n - 1), F(floor(s / 3), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(27 + 1, 10000) if F(s, n=2)])
print([s for s in range(27 + 1, 10000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(27 + 1, 10000) if F(s, n=4) and not F(s, n=2)])


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 13, 15, 16, 19-21]
# КЕГЭ = []
# todo на следующем уроке:
