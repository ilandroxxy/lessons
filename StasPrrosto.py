# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 20218 кегэ
'''
from itertools import *

cnt = 1
for i in product(sorted('СИНЕРГЯ'), repeat=6):
    s = ''.join(i)
    if 'ГИРЯ' in s:
        print(cnt, s)
    cnt += 1
'''


# 20071 кегэ
'''
from math import prod
def f(n):
    if n > 2000:
        return 16
    if n <= 2000:
        return 2*f(n+3)

n = f(50)//f(110)
N = [int(x) for x in str(n) if x != '0']
print(prod(N))
'''

# 19892
'''
from math import *
s = 1920*1080
N = 65536
i = ceil(log2(N))


# X - сколько вмещает одна карта
print(512 - 52)  # 460

for j in range(1, 15):
    if 460 %j == 0:
        print(j, 460 % j)
print(460 / 5)  # 92 - фотографии на одной флешке
I = s*i  # бит
print(I*92 / 2**23)
'''
# 363.867 -> 364


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(s, n):
    """

    :param s: кол-во камней в куче (которое ищем)
    :param n: n - шаг игры
    n = 1: Петя 1 ход
    n = 2: Ваня 1 ход
    n = 3: Петя 2 ход
    n = 4: Ваня 2 ход
    :return: Подходящие s - из них мы уже будем выбирать минимальные/максимлаьные
    """
    if s >= 51:
        return n % 2 == 0  # Если ход четны, то это ход Вани
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])  # 19
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])  # 20
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])  # 21
'''

# № 18144 (Уровень: Базовый)
'''
from math import ceil, floor

def F(s, n):
    if s <= 19:
        return n % 2 == 0  # Если ход четны, то это ход Вани
    if n == 0:
        return 0
    h = [F(s-4, n-1), F(s-6, n-1), F(ceil(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(20, 1000) if F(s, 2)])  # 19
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])  # 20
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])  # 21
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(a, s, n):
    if s + a >= 81:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a, s+1, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 74) if F(7, s, 2)])  # 19
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])  # 20
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])  # 20
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке: 27 номера

# Первый пробник 21.12.24:
# Стас 9/29 -> 48 вторичных баллов +[2, 3-5, 7, 10, 12, 16, 22] -[1, 6, 8, 9, 11, 13, 14, 15, 17-21, 24-25]

# Второй пробник 28.02.25:
# Стас 18/29 -> 72 вторичных баллов +[1-5, 7, 8, 10, 11, 13-16, 18-21, 23] -[6, 9, 12, 17, 22, 24, 25]
