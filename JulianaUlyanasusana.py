# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

def F(a, b):
    if a >= b:
        return a == b
    h = [F(a+2, b), F(a+3, b), F(a*2, b)]
    return sum(h)


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
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 17682 Пересдача 04.07.24 (Уровень: Базовый)
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+3, n-1), F(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(1, 67) if F(s, 2)])
print([s for s in range(1, 67) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 67) if F(s, 4) and not F(s, 2)])
'''


def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0  # True/False
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if F(7, s, 2)])  # [19, 20, 21,
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 23, 25]
# КЕГЭ = []
# на следующем уроке: Разобрать досрочный вариант - повспоминать все задачки


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 34 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]

# Второй пробник 28.02.25:
# Ульяна 10/29 -> 51 вторичных баллов +[1-4, 6, 10, 13, 15, 16, 23] -[5, 8, 9, 12, 14, 17, 25]
