# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))


def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))


def F(a, b):
    if a >= b:
        return a == b
    h = [F(a+1, b), F(a+2, b), F(a+3, b)]
    return sum(h)

print(F(5, 7) * F(7, 11))
'''


# № 21905 Открытый вариант 2025 (Уровень: Базовый)
# 1 куча: +1, +4, *3 | s >= 67 | 1 ≤ s ≤ 66
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0  # True - победа Вани, False - победа Пети
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)
    # но при любом ходе Пети: else all(h)
    # после неудачного первого хода Пети: else any(h)

print([s for s in range(1, 67) if F(s, n=2)])
print([s for s in range(1, 67) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 67) if F(s, n=4) and not F(s, n=2)])
'''

# s - кол-во камней в куче
# n - это шаг нашей игры

# n = 1: Первый шаг Пети
# n = 2: Первый шаг Вани
# n = 3: Второй шаг Пети
# n = 4: Второй шаг Вани


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

print([s for s in range(2, 127) if F(s, n=2)])
print([s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
'''


# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча: -2, /2 (до меньшего) | s <= 87 | s > 88
'''
from math import ceil, floor
# ceil - округление вверх
# floor - округление вниз

def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(89, 1000) if F(s, n=2)])
print([s for s in range(89, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(89, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# В начальный момент в первой куче было семь камней
# 2 кучи: a+1, s+1, a*2, s*2 | a+s>=81 | 1 ≤ s ≤ 73 | a = 7
'''
def F(a, s, n):
    if a + s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    # return any(h) if (n - 1) % 2 == 0 else any(h) # после неудачного первого хода Пети

print([s for s in range(1, 74) if F(7, s, n=2)])  # 19
print([s for s in range(1, 74) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 74) if F(7, s, n=4) and not F(7, s, n=2)])
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: 12, 5, 14, 17, 9, 18, 25 и 7, 11 повторить 8 (возможно 15)


