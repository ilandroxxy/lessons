# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def f(c, e):
    if c < e or c == 7:
        return 0
    if c == e:
        return 1
    h = [f(c-1 , e), f(c - 4, e), f(c // 3, e)]
    return sum(h)

print(f(19, 13) * f(13, 2))
'''

# s - это кол-во камней в куче
# n - это шаг нашей игры
# n = 1: первый шаг Пети
# n = 2: первый шаг Вани
# n = 3: второй шаг Пети
# n = 4: второй шаг Вани

# № 21714 ЕГКР 19.04.25 (Уровень: Базовый)
# 1 куча: +2, +5, *2 | s >= 128 | 1 < s < 127
'''
def F(s, n):
    if s >= 128:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+5, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(2, 127) if F(s, n=2)])
print(20, [s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
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


# № 18268 (Уровень: Базовый)
# 2 кучи: a-3, s-3, a/2, s/2 (вверх) | a + s <= 72 | a = 50 | s > 22
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 72:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s, n - 1), F(a, s-3, n - 1), F(ceil(a/2), s, n - 1), F(a, ceil(s/2), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)


print(19, [s for s in range(23, 1000) if F(50, s, n=2)])
print(20, [s for s in range(23, 1000) if F(50, s, n=3) and not F(50, s, n=1)])
print(21, [s for s in range(23, 1000) if F(50, s, n=4) and not F(50, s, n=2)])
'''


# +3, *3| 1 <= S <= 64 | a + s >= 77 | a = 12

def f(a, s, n):
    if a + s >= 77:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(a + 3, s, n - 1), f(a, s + 3, n - 1), f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print(19, [s for s in range(1, 64 + 1) if f(12, s, n=2)])
print(20, [s for s in range(1, 64 + 1) if f(12, s, n=3) and not f(12, s, n=1)])
print(21, [s for s in range(1, 64 + 1) if f(12, s, n=4) and not f(12, s, n=2)])


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: