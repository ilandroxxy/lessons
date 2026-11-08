# region Домашка: ******************************************************************

# № 2152 (Уровень: Базовый)
# 1. Прибавить 4
# 2. Прибавить 10
# 3. Сделать нечётное
#
# Третья команда преобразует число n в число 2n+1.
# Сколько существует программ, которые исходное число 2 преобразуют в число 27?
'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a + 4, b) + F(a + 10, b) + F(2 * a + 1, b)

print(F(2, 27))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# s - это кол-во камней в куче, то есть именного его мы и ищем
# n = это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 25358 ЕГКР 13.12.25(Уровень: Базовый)
# 1 куча: s+2, s+4, s*2 | s >= 125 | 1 <= s <= 124
'''
def F(s, n):
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n-1), F(s + 4, n-1), F(s * 2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print(19, [s for s in range(1, 124+1) if F(s, n=2)])
print(20, [s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 21905 Открытый вариант 2025(Уровень: Базовый)
# 1 куча: s+1, s+4, s*3 | s >= 67 | 1 <= s <= 66
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n-1), F(s + 4, n-1), F(s * 3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 66+1) if F(s, n=2)])
print(20, [s for s in range(1, 66+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 66+1) if F(s, n=4) and not F(s, n=2)])
'''



# № 23203 Основная волна 10.06.25(Уровень: Базовый)
# 1 куча: s-3, s-7, s/3 до меньшего | s <= 11 | s > 11
'''
from math import ceil, floor
def F(s, n):
    if s <= 11:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n-1), F(s - 7, n-1), F(floor(s / 3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(11+1, 1000) if F(s, n=2)])
print(20, [s for s in range(11+1, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(11+1, 1000) if F(s, n=4) and not F(s, n=2)])
'''
# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход



# № 31516 Демоверсия 2027(Уровень: Базовый)
# 2 кучи: a+4, s+4, a*2, s*2 | a+s >= 133 | a = 17 | 1 <= s <= 115

def F(a, s, n):
    if a + s >= 133:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 4, s, n-1), F(a, s + 4, n-1), F(a * 2, s, n-1), F(a, s * 2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 115+1) if F(17, s, n=2)])
print(20, [s for s in range(1, 115+1) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(1, 115+1) if F(17, s, n=4) and not F(17, s, n=2)])



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [10, 13, 15, 16, 19-21]
# КЕГЭ = []
# todo на следующем уроке:
