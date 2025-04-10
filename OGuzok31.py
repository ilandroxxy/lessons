# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# s - это кол-во камней
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0  # True - если победа Вани / False - победа Пети
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 19251 ЕГКР 21.12.24 (Уровень: Базовый)
'''
def F(s, n):
    if s >= 132:
        return n % 2 == 0  # True - если победа Вани / False - победа Пети
    if n == 0:
        return 0
    h = [F(s+3, n-1), F(s+6, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 132) if F(s, 2)])
print([s for s in range(1, 132) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 132) if F(s, 4) and not F(s, 2)])
'''


# № 19120 (Уровень: Базовый)
'''
from math import ceil, floor

def F(s, n):
    if s <= 12:
        return n % 2 == 0  # True - если победа Вани / False - победа Пети
    if n == 0:
        return 0
    h = [F(s-1, n-1), F(s-2, n-1), F(s-3, n-1), F(s-4, n-1), F(s-5, n-1), F(floor(s/5), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(20, 1000) if F(s, 2)])
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if F(7, s, 2)])
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2? сопоставление, 3, 4, 5, 7, 8, 9-, 11-, 12-, 13, 14, 15, 16, 18, 19-21-, 22, 23]
# КЕГЭ = []
# на следующем уроке:


# Второй пробник 28.02.25:
# Селим 18/29 -> 72 вторичных баллов +[1-5, 8, 10-16, 19-21, 23, 25] -[6, 7, 9, 17, 22, 24]
