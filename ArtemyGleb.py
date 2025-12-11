# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17684 Пересдача 04.07.24 (Уровень: Базовый)
# A. Вычти 2
# B. Найти целую часть от деления на 2
# Сколько существует программ, для которых при исходном
# числе 38 результатом является число 2 и при этом траектория
# вычислений содержит число 10?
'''
def F(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    h = [F(a-2, b), F(a//2, b)]
    return sum(h)

print(F(38, 10) * F(10, 2))
'''


# № 22437 (Уровень: Базовый)
# 1 куча: +4, +7, *4 | s >= 471 | 1 ≤ s ≤ 470
'''
def F(s, n):
    """
    :param s: - это кол-во камней, которое мы ищем (будем перебирать)
    :param n: - это шаги нашей игры

    n = 1: Петя первый ход
    n = 2: Ваня первый ход
    n = 3: Петя второй ход
    n = 4: Ваня второй ход
    """
    if s >= 471:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+4, n-1), F(s+7, n-1), F(s*4, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 470+1) if F(s, n=2)])
print(20, [s for s in range(1, 470+1) if F(s, n=3) and not F(s, n=1) ])
print(21, [s for s in range(1, 470+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 21418 Досрочная волна 2025 (Уровень: Базовый)
# 1 куча: -2, /2 (вниз) | s <= 87 | s > 88
'''
from math import ceil, floor
def F(s, n):
    if s <= 87:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(89, 1000) if F(s, n=2)])
print(20, [s for s in range(89, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(89, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 22066 (Уровень: Базовый)
# 2 кучи: a+3, s+3, a*2, s*2 | a+s >= 100 | a = 17 | 1 ≤ s ≤ 82
'''
def F(a, s, n):
    if a+s >= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+3, s, n-1), F(a, s+3, n-1), F(a*2, s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print(19, [s for s in range(1, 82+1) if F(17, s, n=2)])
print(20, [s for s in range(1, 82+1) if F(17, s, n=3) and not F(17, s, n=1) ])
print(21, [s for s in range(1, 82+1) if F(17, s, n=4) and not F(17, s, n=2)])
'''


# № 18268 (Уровень: Базовый)
# 2 кучи : a-3, s-3 , a/3 , s/3 | a+s<=72 | a=50 | s > 22

from math import ceil, floor
def F (a,s,n):
    if a+s<=72:
        return n%2==0
    if n==0:
        return 0
    h=[F(a-3,s,n-1),F(a,s-3,n-1),F(ceil(a/2),s,n-1),F(a,ceil(s/2),n-1)]
    return any(h) if (n-1)%2==0 else any(h)

print(19, [s for s in range(23,1000) if F(50,s,n=2)])
print(20, [s for s in range(23,1000) if F(50,s,n=3) and not F(50,s,n=1)])
print(21, [s for s in range(23,1000) if F(50,s,n=4) and not F(50,s,n=2)])





# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
