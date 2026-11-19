# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 28940 ЕГКР 18.04.26(Уровень: Базовый)
# 1 куча: s+1, s+5, s*3 | s >= 124 | 1 ≤ s ≤ 123
'''
def F(s, n):
    if s >= 124:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+5, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 123+1) if F(s, n=2)])
print([s for s in range(1, 123+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 123+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 25358 ЕГКР 13.12.25(Уровень: Базовый)
# 1 куча: s+2, s+4, s*2 | s >= 125 | 1 <= s <= 124
'''
def F(s, n):
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 124+1) if F(s, n=2)])
print([s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''


# 1 куча: s-2, s-7, s / 3 до меньшего | s <= 20007 | s > 20007
'''
from math import floor, ceil
def F(s, n):
    if s <= 20007:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(s-7, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(20007+1, 100000) if F(s, n=2)])
print([s for s in range(20007+1, 100000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(20007+1, 30000) if F(s, n=4) and not F(s, n=2)])
'''


# № 31516 Демоверсия 2027(Уровень: Базовый)
# 2 куча: a+4, s+4, a*2, s*2 | a+s>=133 | a=17 | 1 ≤ s ≤ 115
'''
def F(a, s, n):
    if a+s >= 133:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+4, s, n - 1), F(a, s+4, n - 1), F(a*2, s, n - 1), F(a, s*2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

a = 17
print([s for s in range(1, 115 + 1) if F(a, s, n=2)])
print([s for s in range(1, 115 + 1) if F(a, s, n=3) and not F(a, s, n=1)])
print([s for s in range(1, 115 + 1) if F(a, s, n=4) and not F(a, s, n=2)])
'''

'''
from math import floor, ceil
def f(s, n):
    if s <= 11:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s - 3, n-1), f(s - 7, n-1), f(floor(s / 3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(11 + 1, 1000) if f(s, n=2)])
print([s for s in range(11 + 1, 1000) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(11 + 1, 1000) if f(s, n=4) and not f(s, n=2)])
'''


# № 23278 Основная волна 11.06.25(Уровень: Базовый)
# s-3|  s - 8 | s / 3
from math import floor, ceil
def f(s, n):
    if s <=  16:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(s -3, n-1), f(s - 8, n-1) , f(floor(s / 3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    #return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(17+1, 1000) if f(s, n=2)])
print([s for s in range(17+1, 1000) if f(s, n=3) and not f(s, n=1)])
print([s for s in range(17+1, 1000) if f(s, n=4) and not f(s, n = 2)])




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [8, 13, 15, 16, 19-21, 23]
# КЕГЭ = []
# todo на следующем уроке:
#  5, 14 - что-то смотрели