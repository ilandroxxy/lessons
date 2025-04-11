# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 4741 (Уровень: Средний)
'''
import sys
sys.setrecursionlimit(6000)

from math import sqrt
def f(n):
    # if sqrt(n) == int(sqrt(n)):  # sqrt(16) == 16
    if (n ** 0.5).is_integer():
        return n ** 0.5
    else:
        return f(n + 1) + 1
print(int(f(4850) + f(5000)))
'''


# № 4739 (Уровень: Средний)
'''
from functools import *
import sys
sys.setrecursionlimit(400000)

@lru_cache(None)
def f(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return f(n + 1) + f(n + 2)

for i in range(13000, 1, -1):
    f(i)

print(f(12345) * (f(10) - f(12))//f(11) + f(10101))
'''


'''
def f(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return f(n + 1) + f(n + 2)


print(f(12345) * 1 + f(10101))
'''
# f(10) = f(11) + f(12)


# № 8474 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def f(n):
    if n > 3456:
        return n + 1
    if n <= 3456 and n % 3 == 0:
        return f(n + 1) + f(n + 2)
    if n <= 3456 and n % 3 != 0:
        return f(n + n % 3) + 2

print(f(12) - f(17))
'''


# № 10659 (Уровень: Средний)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n + F(n - 1)

cnt = 0
for n in range(1, 100+1):
    if  F(2023) // F(n) % 2 == 0:
        cnt += 1
print(cnt)
'''


# № 8585 (Уровень: Базовый)
# 1. Вычти сумму всех цифр числа
# 2. Найди целую часть от деления на 2
# 3. Вычти 1
#
# Сколько существует программ, для которых при исходном числе 40
# результатом является число 10, и при этом траектория
# вычислений содержит число 25?
'''
def F(a, b):
    if a <= b:
        return a == b
    h = [F(a - sum(map(int, str(a))), b), F(a // 2, b), F(a-1, b)]
    return sum(h)


print(F(40, 25) * F(25, 10))  # 247
'''


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50

# s - это кол-во камней в куче
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя Второй ход
# n = 4: Ваня Второй ход
'''
def F(s, n):
    if s >= 51:
        return n % 2 == 0  # True - Ваня победил / False - Петя победил
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 19251 ЕГКР 21.12.24 (Уровень: Базовый)
# 1 куча: +3, +6, *3 | >= 132 | 1 ≤S≤ 131
'''
def F(s, n):
    if s >= 132:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+3, n-1), F(s+6, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 132) if F(s, 2)])
print([s for s in range(1, 132) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 132) if F(s, 4) and not F(s, 2)])
'''


# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча: -2, /2 вниз | <= 87 | S > 88
'''
from math import sqrt, ceil, floor

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
# 2 куча: a+1, s+1, a*2, s*2 | a + s >= 81 | 1 ≤ S ≤ 73 | a = 7

def F(a, s, n):
    if a+s >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    # return any(h) if (n - 1) % 2 == 0 else all(h) # при любом ходе Пети
    return any(h) if (n - 1) % 2 == 0 else any(h) # после неудачного первого хода Пети


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
# ФИПИ = [15, 16, 23]
# КЕГЭ  = []
# на следующем уроке: 5, 7, 8, 9, 13, 25

# Первый пробник 21.12.24:
# Анастасия 9/29 -> 48 вторичных баллов +[1, 2, 4, 12, 16, 14, 15, 23, 20-21] -[3, 8, 10, 11, 18, 19]
