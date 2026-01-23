# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
n = 234
s = str(n)
summa = 0
for x in s:
    summa += int(x)
print(summa)


print(sum([int(x) for x in str(n)]))

print(sum(map(int, str(n))))
'''


# № 8585 (Уровень: Базовый)
'''
def F(a,b):
    if a == b:
        return 1
    elif a < b:
        return 0
    else:
        return F(a - sum(map(int, str(a))), b) + F(a // 2, b) + F(a-1, b)

print(F(40, 25) * F(25, 10))
'''


# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 25358 (Уровень: Базовый)
# 1 куча: +2, +4, *2 | s >= 125 | 1 ≤ s ≤ 124
'''
def F(s, n):
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n - 1), F(s + 4, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 124+1) if F(s, n=2)])
print(20, [s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 23565 Пересдача 03.07.25(Уровень: Базовый)
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 8, n - 1), F(floor(s / 3), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print(19, [s for s in range(16, 1000) if F(s, n=2)])
print(20, [s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 23759 Демоверсия 2026(Уровень: Базовый)
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 5, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print(19, [s for s in range(31, 1000) if F(s, n=2)])
print(20, [s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: s1+1, s2+1, s1*2, s2*2 | s1 + s2 >= 81 | s1 = 7 | 1 <= s <= 73
'''
def F(s1, s2, n):
    if s1 + s2 >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s1+1, s2, n - 1), F(s1, s2+1, n - 1), F(s1*2, s2, n - 1), F(s1, s2*2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)


print(19, [s for s in range(1, 73+1) if F(7, s, n=2)])
print(20, [s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print(21, [s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])
'''


# № 17532 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(s1, s2, n):
    if s1 + s2 >= 65:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s1 + 1 , s2, n - 1), F(s1, s2 + 1, n - 1), F(s1 * 3 , s2, n - 1), F(s1, s2 * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 58+1) if F(6, s, n=2)])
print(20, [s for s in range(1, 58+1) if F(6, s, n=3) and not F(6, s, n=1)])
print(21, [s for s in range(1, 58+1) if F(6, s, n=4) and not F(6, s, n=2)])
'''

# № 18268 (Уровень: Базовый)

from math import ceil, floor
def F(s1, s2, n):
    if s1 + s2 <= 72:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s1 - 3, s2, n - 1), F(s1, s2 - 3, n - 1), F(ceil(s1 / 2), s2, n - 1), F(s1, ceil(s2 / 2), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)


print(19, [s for s in range(23, 1000) if F(50, s, n=2)])
print(20, [s for s in range(23, 1000) if F(50, s, n=3) and not F(50, s, n=1)])
print(21, [s for s in range(23, 1000) if F(50, s, n=4) and not F(50, s, n=2)])


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 13, 14, 15, 16, 18, 19-21, 23, 25, 27.1]
# КЕГЭ = [5, 8, 14, 15, 16, 23, 19-21]
# на следующем уроке:
