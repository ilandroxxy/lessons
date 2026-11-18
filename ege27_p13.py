# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21907 Открытый вариант 2025(Уровень: Базовый)
# A. Прибавить 1
# B. Прибавить 2
# C. Умножить на 2

# Сколько существует программ, для которых при исходном числе 3 результатом
# является число 18, при этом траектория вычислений содержит число 14 и не содержит 8?
'''
def F(a, b):
    if a > b or a == 8:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2, b) + F(a * 2, b)

print(F(3, 14) * F(14, 18))

# Вариант 2

def F(a, b):
    if a >= b or a == 8:
        return a == b
    return F(a + 1, b) + F(a + 2, b) + F(a * 2, b)

print(F(3, 14) * F(14, 18))
'''


# № 20967 (Уровень: Базовый)
# A. вычти 2
# B. вычти 3
# C. найди целую часть от деления на 3

# Сколько существует таких программ, которые исходное число 48 преобразуют
# в число 4, и при этом траектория вычислений содержит числа 17 и 25 и не содержит числа 15?
'''
def F(a, b):
    if a <= b or a == 15:
        return a == b
    return F(a - 2, b) + F(a - 3, b) + F(a // 3, b)

print(F(48, 25) * F(25, 17) * F(17, 4))
'''


# № 19711 (Уровень: Базовый)
# А. Прибавить 1
# В. Умножить на 2
# C. Возвести в квадрат
# Сколько существует последовательностей команд, для которых при исходном
# числе 3 результатом является число 48 и при этом траектория вычислений не содержит число 36?
'''
def F(a, b):
    if a >= b or a == 36:
        return a == b
    return F(a + 1, b) + F(a * 2, b) + F(a ** 2, b)

print(F(3, 48))
'''



# № 31367 Пересдача 08.07.26(Уровень: Средний)
# A. Прибавь 1
# B. Измени цифру
# Вторая команда применяется только к числу, у которого в записи
# присутствует хотя бы одна цифра 1, и действует, заменяя число
# на экране числом, в котором каждая цифра 1 заменена на цифру 3.

# Сколько существует программ, для которых при исходном числе 11 результатом является число 94?
'''
def F(a, b):
    if a >= b:
        return a == b

    s = str(a)
    if s.count('1') >= 1:
        s = s.replace('1', '3')
        return F(a + 1, b) + F( int(s) , b)
    else:
        return F(a + 1, b)

print(F(11, 94))
'''

'''
a = 11 -> 33
a = 21 -> 23
a = 20 -> 20
'''


# № 31128 Основная волна 18.06.26(Уровень: Средний)
# A. Прибавь 1
# B. Поменяй местами
# Вторая команда применяется только к числу, у которого цифра
# в разряде десятков по значению меньше цифры, стоящей в разряде
# единиц, и действует, заменяя число на экране числом, в котором
# цифры двух младших разрядов поменялись местами.

# Сколько существует программ, для которых при исходном числе 100 результатом является число 150?
'''
def F(a, b):
    if a >= b:
        return a == b

    s = str(a)
    if s[1] < s[2]:
        return F(a + 1, b) + F(int(s[0] + s[2] + s[1]), b)
    else:
        return F(a + 1, b)

print(F(100, 150))
'''


# № 4596 Основная волна 2022(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = 1 при n<3;
# F(n)=F(n−1)+n−1 если n>2 и при этом n чётно;
# F(n)=F(n−2)+2×n−2 если n>2 и при этом n нечётно.
# Чему равно значение функции F(34)?
'''
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n-1) + n-1
    if n > 2 and n % 2 != 0:
        return F(n-2) + 2*n - 2

print(F(34))
'''

# № 9747 Основная волна 19.06.23(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=n при n<11;
# F(n)=n+F(n–1), если n≥11.
# Чему равно значение выражения: F(2024)−F(2021)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n - 1)

print(F(2024) - F(2021))
'''
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded




# № 17557 Основная волна 08.06.24(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=1 при n=1;
# F(n)=2×n×F(n–1), если n>1.
# Чему равно значение выражения: (F(2024)/16−F(2023))/F(2022)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)

print( (F(2024) // 16 - F(2023)) // F(2022) )
#     print( (F(2024) / 16 - F(2023)) / F(2022) )
#              ~~~~~~~^~~
# OverflowError: integer division result too large for a float
'''


# № 23275 Основная волна 11.06.25(Уровень: Базовый)
# Алгоритм вычисления значения функции
# F(n) и G(n), где n – целое число, задан следующими соотношениями:
# F(n)=2×(G(n−3)+8);
# G(n)=2×n, если n<10.
# G(n)=G(n−2)+1, если n≥10.
# Чему равно значение выражения F(15548)?
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return 2 * (G(n - 3) + 8)

def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

print(F(15548))
'''

# Вариант 2
'''
from functools import *

def F(n):
    return 2 * (G(n - 3) + 8)

@lru_cache(None)
def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

for n in range(16000):
    G(n)

print(F(15548))
'''


# № 25355 ЕГКР 13.12.25(Уровень: Базовый)
# Алгоритм вычисления функций
# F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n)=F(n−4)+3580, если n≥19;
# F(n)=6×(G(n−7)−36), если n<19;

# G(n)=n/20+28, если n≥248045;
# G(n)=G(n+9)−4, если n<248045.
# Чему равно значение функции F(673)?
'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 19:
        return F(n-4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4

for n in range(250_000-1, -1, -1):
    G(n)

for n in range(700):
    F(n)

print(F(673))
'''




# № 21905 Открытый вариант 2025(Уровень: Базовый)
# 1 куча: s+1, s+4, s*3 | s >= 67 | 1 ≤ s ≤ 66
'''
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 66+1) if F(s, n=2)])
print([s for s in range(1, 66+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 66+1) if F(s, n=4) and not F(s, n=2)])
'''

# № 21714 ЕГКР 19.04.25(Уровень: Базовый)
# 1 куча: s+2, s+5, s*2 | s >= 128 | 1 < s < 127
'''
def F(s, n):
    if s >= 128:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+5, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(2, 127) if F(s, n=2)])
print([s for s in range(2, 127) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(2, 127) if F(s, n=4) and not F(s, n=2)])
'''


# № 31516 Демоверсия 2027(Уровень: Базовый)
# 2 кучи: a+4, s+4, a*2, s*2 | a + s >= 133 | a = 17 | 1 ≤ s ≤ 115
'''
def F(a, s, n):
    if a + s >= 133:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+4, s, n-1), F(a, s+4, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 115+1) if F(17, s, n=2)])
print([s for s in range(1, 115+1) if F(17, s, n=3) and not F(17, s, n=1)])
print([s for s in range(1, 115+1) if F(17, s, n=4) and not F(17, s, n=2)])
'''


# № 21418 Досрочная волна 2025(Уровень: Базовый)
# 1 куча: s-2, s/2 до меньшего | s <= 87 | s > 88
'''
from math import ceil, floor
def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(floor(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(89, 1000) if F(s, n=2)])
print([s for s in range(89, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(89, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 23759 Демоверсия 2026(Уровень: Базовый)
# 1 куча: a-3, s-5, s/4 до меньшего | s <= 30 | s >= 31
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-5, n-1), F(floor(s/4), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(31, 1000) if F(s, n=2)])
print([s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 25358 ЕГКР 13.12.25(Уровень: Базовый)
# 1 куча: s+2, s+4, s*2 | s >= 125 | 1 <= s <= 124
'''
def F(s, n):
    if s>= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+2, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 125) if F(s, n=2)])
print([s for s in range(1, 125) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 125) if F(s, n=4) and not F(s, n=2)])
'''



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [13, 16, 19-21, 23]
# КЕГЭ = []
# todo на следующем уроке: 19-21, 15

