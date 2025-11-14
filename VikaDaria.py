# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# s - это кол-во камней в куче (будем искать - перебирать)
# n - это шаг нашей игры

# n = 1: Петя 1
# n = 2: Ваня 1
# n = 3: Петя 2
# n = 4: Ваня 2

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

print(19, [s for s in range(1, 66+1) if F(s, n=2)])
print(20, [s for s in range(1, 66+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 66+1) if F(s, n=4) and not F(s, n=2)])
'''


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


# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (вниз) | s <= 30 | s >= 31
'''
from math import floor, ceil
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

# № 20825 (Уровень: Базовый)
# 2 кучи: a-5 s+2, a+2 s-5, a/2, s/2 вниз | a+s <= 69 | a = 35 | s > 50
'''
from math import floor
def F(a, s, n):
    if a+s <= 69:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(floor(a / 2), s, n-1), F(a, floor(s / 2), n-1), F(a-5, s+2, n-1), F(a+2, s-5, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(51, 1000) if F(35, s, n=2)])
print(20, [s for s in range(51, 1000) if F(35, s, n=3) and not F(35, s, n=1)])
print(21, [s for s in range(51, 1000) if F(35, s, n=4) and not F(35, s, n=2)])
'''


# 23203
'''
from math import floor
def F(s, n):
    if s <= 11:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3 , n-1), F(s - 7 , n-1), F(floor(s / 3) , n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(12, 1000) if F(s, n=2)])
print([s for s in range(12, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(12, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# 20811
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s + 4, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 50 + 1) if F(s, n=2)])
print([s for s in range(1, 50 + 1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 50 + 1) if F(s, n=4) and not F(s, n=2)])
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 13, 14, 15, 16, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке:
