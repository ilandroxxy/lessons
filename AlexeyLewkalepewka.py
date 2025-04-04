# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20811 Апробация 05.03.25 (Уровень: Базовый)

def f(s, n):
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s+1, n-1), f(s+4, n-1), f(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( [s for s in range(1, 51) if f(s, 2)] ) # 19
print( [s for s in range(1, 51) if f(s, 3) and not f(s, 1)] ) # 20
print( [s for s in range(1, 51) if f(s, 4) and not f(s, 2)] ) # 21


# № 18144 (Уровень: Базовый)
'''
from math import ceil

def f(s, n):
    if s <= 19: return n % 2 == 0
    if n == 0: return 0
    h = [f(s-4, n-1), f(s-6, n-1), f(ceil(s/2), n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(20, 1000) if f(s, 2)]) # 19 - 39
print([s for s in range(20, 1000) if f(s, 3) and not f(s, 1)]) # 20 - 43 44
print([s for s in range(20, 1000) if f(s, 4) and not f(s, 2)]) # 21 - 88
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
'''
def f(a, s, n):
    if s + a >= 81: return n % 2 == 0
    if n == 0: return 0
    h = [f(a+1, s, n-1), f(a, s+1, n-1), f(a*2, s, n-1), f(a, s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if f(7, s, 2)]) # 19 - 19
print([s for s in range(1, 74) if f(7, s, 3) and not f(7, s, 1)]) # 20
print([s for s in range(1, 74) if f(7, s, 4) and not f(7, s, 2)]) # 21
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [8, 14, 15, 23]
# на следующем уроке:

# Первый пробник 21.12.24:
# 24/25 -> 88 вторичных баллов +[1, 3-25] -[2]

# Второй пробник 10.02.25:
# 23/25 -> 86 вторичных баллов +[1-9, 11-23, 25] -[10, 24]
