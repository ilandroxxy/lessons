# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def F(a, b):
    if a <= b or a == 7:
        return a == b
    h = [F(a - 1, b), F(a - 4, b), F(a // 3, b)]
    return sum(h)

print(F(19, 13) * F(13, 2))
'''

#  № 21905 Открытый вариант 2025 (Уровень: Базовый)
# 1 куча: +1, +4, *3 | s >= 67 | 1 ≤ s ≤ 66

# s - это кол-во камней в куче (то что ищем)
# n - это шаг нашей игры

# n = 1 - Петя первый ход
# n = 2 - Ваня первый ход
# n = 3 - Петя второй ход
# n = 4 - Ваня второй ход
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n-1), F(s + 4, n-1), F(s * 3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 66+1) if F(s, n=2)])
print([s for s in range(1, 66+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 66+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (до меньшего) | s <= 30 | s ≥ 31
'''
from math import ceil, floor

def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3 , n-1), F(s - 5 , n-1), F(floor(s / 4) , n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(31, 1000) if F(s, n=2)])
print([s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | a=7 | 1 ≤ s ≤ 73
'''
def F(a, s, n):
    if a + s >= 81 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s , n-1), F(a, s+1, n-1), F(a*2, s , n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 73+1) if F(7, s, n=2)])
print([s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])
'''


# № 18268 (Уровень: Базовый)
# 2 кучи: a-3, s-3, a/2, s/2 (в большее) | a+s <= 72 | a = 50 | s > 22

from math import ceil
def F(a, s, n):
    if a + s <= 72:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s , n-1), F(a, s-3, n-1), F(ceil(a / 2), s , n-1), F(a, ceil(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(23, 1000) if F(50, s, n=2)])
print([s for s in range(23, 1000) if F(50, s, n=3) and not F(50, s, n=1)])
print([s for s in range(23, 1000) if F(50, s, n=4) and not F(50, s, n=2)])


# № 21714 ЕГКР 19.04.25 (Уровень: Базовый)
# 1 куча: +2, +5, *2 | s >= 128 | 1 < s < 127
'''
def F(s, n):
    if s >= 128 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2 , n-1), F(s + 5 , n-1), F(s * 2 , n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(2, 127) if F(s, n=2)])
print([s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
