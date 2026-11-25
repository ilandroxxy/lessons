# region Домашка: ******************************************************************

# № 23756 Демоверсия 2026 (Уровень: Базовый)
'''
from functools import *

def F(n):
    return 2*(G(n-3)+8)

@lru_cache(None)
def G(n):
    if n < 10:
        return 2*n
    if n >= 10:
        return G(n-2)+1

for n in range(16000):
    G(n)

for n in range(16000):
    F(n)

print(F(15548))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# s - это кол-во камней в куче, которое мы ищем (путем перебора)
# n - это шаги нашей игры
'''
n = 1: Петя первый ход
n = 2: Ваня первый ход
n = 3: Петя второй ход
n = 4: Ваня второй ход
'''


# № 21714 ЕГКР 19.04.25(Уровень: Базовый)
# 1 куча: s+2, s+5, s*2 | s >= 128 | 1 < s < 127
'''
def F(s, n):
    if s >= 128:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+5, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(2, 127) if F(s, n=2)])
print(20, [s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
'''


# № 21418 Досрочная волна 2025(Уровень: Базовый)
# 1 куча: s-2, s/2 до меньшего | s <= 87 | s > 88
'''
from math import ceil, floor
def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 2, n-1), F(floor(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(89, 1000) if F(s, n=2)])
print(20, [s for s in range(89, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(89, 1000) if F(s, n=4) and not F(s, n=2)])
'''



# № 27631 Апробация 04.03.26(Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 211 | a = 17 | 1 < s <= 193

def F(a, s, n):
    if a+s >= 211:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(2, 193+1) if F(17, s, n=2)])
print(20, [s for s in range(2, 193+1) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(2, 193+1) if F(17, s, n=4) and not F(17, s, n=2)])




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [13, 15, 16, 23, 19-21]
# КЕГЭ = []
# todo на следующем уроке:
