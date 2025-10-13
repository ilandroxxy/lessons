# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21716 ЕГКР 19.04.25 (Уровень: Базовый)
# A. Прибавь 3
# B. Прибавь 7
# C. Умножь на 3
# Сколько существует таких программ, которые исходное
# число 12 преобразуют в 89, и при этом траектория вычислений
# программы содержит числа 40 и 72 и не содержит 56?

def F(a, b):
    if a >= b or a == 56:
        return a == b
    h = [F(a+3, b), F(a+7, b), F(a*3, b)]
    return sum(h)
print(F(12, 40) * F(40, 72) * F(72, 89))



# s - это кол-во камней в куче
# n - это шаг нашей игры
# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 21714 ЕГКР 19.04.25 (Уровень: Базовый)
# 1 куча: s+2, s+5, s*2 | s >= 128 | 1 < s < 127
'''
def F(s, n):
    if s >= 128:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+5, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(2, 127) if F(s, n=2)])
print([s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
'''


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: s+1, s+4, s*2 | s >= 51 | 1 ≤ s ≤ 50
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    # при любом ходе Пети Ваня может выиграть своим первым ходом
    return any(h) if (n - 1) % 2 == 0 else all(h) 
    
    # Ваня выиграл своим первым ходом после неудачного первого хода Пети
    """return any(h) if (n - 1) % 2 == 0 else any(h)"""

print([s for s in range(1, 50+1) if F(s, n=2)])
print([s for s in range(1, 50+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 50+1) if F(s, n=4) and not F(s, n=2)])
'''


# floor - округление до меньшего
# ceil - округление до большего

# № 23278 Основная волна 11.06.25 (Уровень: Базовый)
# 1 куча: s-3, s-8, s/3 (до меньшего) | s <= 16 | s ≥ 17
'''
from math import floor, ceil
def F(s, n):
    if s <= 16:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-8, n-1), F(floor(s/3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(17, 1000) if F(s, n=2)])
print([s for s in range(17, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(17, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | a = 7 | 1 ≤ s ≤ 73
'''
def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 73+1) if F(7, s, n=2)])
print([s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])
'''


# № 19635 (Уровень: Базовый)
# 2 кучи: a - 3 и s - 3, a / 2, s / 2 (меньше) | a + s <= 100 | a = 48 | s > 52
'''
from math import floor
def F(a, s, n):
    if a + s <= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s-3, n-1), F(floor(a / 2), s, n-1), F(a, floor(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(53, 1000) if F(48, s, n=2)])
print([s for s in range(53, 1000) if F(48, s, n=3) and not F(48, s, n=1)])
print([s for s in range(53, 1000) if F(48, s, n=4) and not F(48, s, n=2)])
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 16, 23, 25]
# КЕГЭ = []
# на следующем уроке: В идеале на выходные взять повторение всех номером
