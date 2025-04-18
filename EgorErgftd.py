# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a+2, b) + F(a*2, b)
'''

# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# s - это кол-во камней в куче
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0  # True - победа Ваня / False - победа Пети
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
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
# 2 кучи: a+1, s+1, a*2, s*2 | a + s >= 81 | 1 ≤ S ≤ 73 | a = 7

def F(a, s, n):
    if a + s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

# else all(h) - при любой игре Пети
# else any(h) - после неудачного первого хода Пети

print([s for s in range(1, 74) if F(7, s, 2)])
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 7, 11, 19-21, 22, 24

# Первый пробник 21.12.24:
# Михаил 8/18 -> 46 вторичных баллов +[2, 4, 6, 12, 14, 15, 16, 23] -[1, 3, 5, 7, 8, 9, 11, 13, 17, 25]

# Второй пробник 28.02.25:
# Михаил 17/29 -> 70 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-16, 18, 19-20, 23, 25] -[5, 7, 10, 13, 17, 21, 22, 24]
# Егор 16/29 -> 68 вторичных баллов +[1-7, 9, 13, 14-18, 23, 25] -[8, 10, 11, 12, 19-21, 22, 24]
