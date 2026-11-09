# region Домашка: ******************************************************************

# Исполнитель преобразует число на экране.
# 1. Вычти 2
# 2. Найди целую часть от деления на 2
# Сколько существует программ, для которых при
# исходном числе 28 результатом является число 1,
# и при этом траектория вычислений содержит число 10?
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - 2, b) + F(a // 2, b)

print(F(28, 10) * F(10, 1))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# n - это шаг игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 31126 Основная волна 18.06.26(Уровень: Базовый)
# 2 кучи: a+1, s+1, a*3, s*3 | a + s >= 155 | a = 15 | 1 <= s <= 139
'''
def F(a, s, n):
    if a + s >= 155:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*3, s, n-1), F(a, s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 139+1) if F(15, s, n=2)])
print([s for s in range(1, 139+1) if F(15, s, n=3) and not F(15, s, n=1)])
print([s for s in range(1, 139+1) if F(15, s, n=4) and not F(15, s, n=2)])
'''


# № 28940 ЕГКР 18.04.26(Уровень: Базовый)
'''
#1 кучи: s+1, s+5, s*3  s >= 124  1<=s<=123
def F(S,n):
    if S >= 124:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(S+1,n-1), F(S+5,n-1), F(S*3,n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print(19, [S for S in range(1,123+1) if F(S,n=2)])
print(20, [S for S in range(1,123+1) if F(S,n=3) and not F(S,n=1)])
print(21, [S for S in range(1,123+1) if F(S,n=4) and not F(S,n=2)])
'''

# № 29974 Апробация 14.05.26(Уровень: Базовый)
# 1 куча: s-3, s-7, s / 4, | s <= 15 | s > 15 |
'''
from math import ceil, floor

def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 7, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(16, 1000) if F(s, n=2)])
print([s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 27774 Апробация 04.03.26(Уровень: Базовый)
#2 кучи: a+1, S+1, a*2, S*2  a + S >= 207  a = 17  1<=S<=189
'''
def F(a,S,n):
    if a + S >= 207:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1,S,n-1), F(a,S+1,n-1), F(a*2,S,n-1), F(a,S*2,n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)
    return any(h) if (n-1) % 2 == 0 else any(h)

print(19, [S for S in range(1,189+1) if F(17,S,n=2)])
print(20, [S for S in range(1,189+1) if F(17,S,n=3) and not F(17,S,n=1)])
print(21, [S for S in range(1,189+1) if F(17,S,n=4) and not F(17,S,n=2)])
'''


# № 29351 Открытый вариант 2026(Уровень: Базовый)
# 2 кучи: a + 4, s + 4, a * 3, s * 3 | a + s >= 154 | a = 11 | 1 ≤ S ≤ 142
def F(a, s, n):
    if a + s >= 154:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 4, s, n - 1), F(a, s + 4, n - 1), F(a * 3, s, n - 1), F(a, s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)


print([s for s in range(1, 142 + 1) if F(11, s, n=2)])
print([s for s in range(1, 142 + 1) if F(11, s, n=3) and not F(11, s, n=1)])
print([s for s in range(1, 142 + 1) if F(11, s, n=4) and not F(11, s, n=2)])



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [10, 13, 15, 16, 19-21]
# КЕГЭ = []
# todo на следующем уроке:
