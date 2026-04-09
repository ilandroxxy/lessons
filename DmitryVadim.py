#
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 28764 Досрочная волна 2026 (Уровень: Базовый)
#
# Исполнитель преобразует число на экране. У исполнителя есть три команды,
# которые обозначены латинскими буквами:
# A. Прибавить 1
# B. Прибавить 3
# C. Умножить на 2
# Программа для исполнителя – это последовательность команд.
# Сколько существует программ, для которых при исходном числе 2 результатом
# является число 25, и при этом траектория вычислений содержит число 15 и не содержит 7?
'''
def F(a, b):
    if a > b or a == 7:
        return 0
    elif a == b:
        return 1
    h = [F(a + 1, b), F(a + 3, b), F(a * 2, b)]
    return sum(h)

print(F(2, 15) * F(15, 25))
'''


# № 25358 ЕГКР 13.12.25 (Уровень: Базовый)
# 1 куча: +2, +4, *2 | s >= 125 | 1 ≤ s ≤ 124

# n = 1: Первый ход Пети
# n = 2: Первый ход Ваня
# n = 3: Второй ход Пети
# n = 4: Второй ход Вани
'''
def F(s, n):
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n - 1), F(s + 4, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)


print(19, [s for s in range(1, 124+1) if F(s, n=2)])
print(20, [s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 18958 (Уровень: Базовый)
# 1 куча: +3, *3, + s**2 | s >= 666 | s < 666
'''
def F(s, n):
    if s >= 666:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 3, n - 1), F(s * 3, n - 1), F(s + (s ** 2), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 666) if F(s, n=2)])
print(20, [s for s in range(1, 666) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 666) if F(s, n=4) and not F(s, n=2)])
'''


# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 до меньшего | s <= 30 | s >= 31
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 5, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)


print(19, [s for s in range(31, 1000) if F(s, n=2)])
print(20, [s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 28704 (Уровень: Базовый)
# 2 кучи: a + 3, s + 3, a + 13, s + 13 | a * s >= 516 | a = 7 | 1 ≤ s ≤ 73
'''
def F(a, s, n):
    if a * s >= 516:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 3, s, n - 1), F(a, s + 3, n - 1), F(a + 13, s, n - 1), F(a, s + 13, n - 1)]
    # return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)


print(19, len([s for s in range(1, 73+1) if F(7, s, n=2)]))
print(20, [s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print(21, [s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])
'''


# № 27774 Апробация 04.03.26 (Уровень: Базовый)
# 2 кучи: a*2, a+1, s*2, s+1  |  a+s >= 207 | a=17 |  1 < s =< 189
'''
def F(a, s, n):
    if a+s >= 207:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a, s*2, n-1), F(a, s+1, n-1), F(a + 1, s, n-1), F(a*2, s, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)
    #return any(h) if (n-1) % 2 == 0 else any(h)

print([s for s in range(2, 189 +1) if F(17,s, n=2)])
print([s for s in range(2, 189 +1) if F(17,s, n=3) and not F(17, s, n=1)])
print([s for s in range(2, 189 +1) if F(17,s, n=4) and not F(17, s, n=2)])
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [4, 5, 13, 19-21]
# на следующем уроке:



