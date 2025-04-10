# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21420 Досрочная волна 2024 (Уровень: Базовый)
# A. Прибавить 1
# B. Прибавить 2
# C. Умножить на 2
# Сколько существует программ, которые преобразуют число 7 в число 51,
# и при этом траектория вычислений содержит числа 13 и 15, но не содержит числа 35?

'''
def F(a, b):
    if a >= b or a == 35:
        return a == b  # True / False
    h = []
    h += [F(a+1, b)]
    h += [F(a+2, b)]
    h += [F(a*2, b)]
    return sum(h)

print(F(7, 13) * F(13, 15) * F(15, 51))
'''
# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ s ≤ 50

# s - кол-во камней в куче
# n - это шаг нашей игры

# n = 1: Петя первый шаг
# n = 2: Ваня первый шаг
# n = 3: Петя второй шаг
# n = 4: Ваня второй шаг

'''
def F(s, n):
    if s >= 51:  # условие
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]  # действия
    return any(h) if (n - 1) % 2 == 0 else all(h)  # all() / any()

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 17752 (Уровень: Базовый)
# 1 куча: +2, *2 | >= 54 | 1 ≤ S ≤ 53
'''
def F(s, n):
    if s >= 54:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 54) if F(s, 2)])
print([s for s in range(1, 54) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 54) if F(s, 4) and not F(s, 2)])
'''


# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча: -2, /2 вниз | <= 87 | S > 88
'''
from math import ceil, floor

def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(89, 1000) if F(s, 2)])
print([s for s in range(89, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(89, 1000) if F(s, 4) and not F(s, 2)])
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


# № 19750 (Уровень: Средний)
'''
def F(s, n):
    if s <= 19:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-5, n-1)]
    if s % 2 == 0:
        h += [F(s/2, n-1)]
    if s % 3 == 0:
        h += [F(s/3, n-1)]
    if s % 2 != 0 and s % 3 != 0:
        h += [F(s + 1, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(20, 1000) if F(s, 2)])
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])
'''


#19635
from math import *

def f(a, s, n):
    if a + s <= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [f(a - 3, s - 3, n - 1), f(floor(a / 2), s, n - 1), f(a, floor(s / 2), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(53, 1000) if f(48, s, 2)])  # 19
print([s for s in range(53, 1000) if f(48, s, 3) and not f(48, s, 1)])
print([s for s in range(53, 1000) if f(48, s, 4) and not f(48, s, 2)])



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [22, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 9, 11, 17, 19-21

# Первый пробник 5.02.25:
# Ангелина 11/29 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/29 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]

# Второй пробник 28.02.25:
# Ангелина 10/29 -> 51 вторичных баллов +[2, 3, 4, 7, 9, 10, 14, 18, 23, 25] -[1, 5, 6, 8, 12, 11, 13, 15, 17]
# Сергей 16/29 -> 67 вторичных баллов +[1, 2, 5, 6, 8, 11, 13-18, 19-21, 23, 25] -[3, 4, 7, 9, 10, 12, 22, 24]
