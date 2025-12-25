# region Домашка: ******************************************************************

'''
n = 1234
summa1 = 0
while n > 0:
    summa1 += n % 10
    n //= 10
print(summa1)  # 10


n = 1234
s = str(n)
summa2 = 0
for x in s:
    summa2 += int(x)
print(summa2)

n = 1234
summa3 = sum([int(x) for x in str(n)])
print(summa3)

n = 1234
summa3 = sum(map(int, str(n)))
print(summa3)
'''


# № 8585 (Уровень: Базовый)
# 1. Вычти сумму всех цифр числа
# 2. Найди целую часть от деления на 2
# 3. Вычти 1
# Сколько существует программ, для которых при исходном
# числе 40 результатом является число 10,
# и при этом траектория вычислений содержит число 25?
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - sum(map(int, str(a))), b) + F(a // 2, b) + F(a-1, b)

print(F(40, 25) * F(25, 10))
'''

# endregion Домашка: ******************************************************************


# region Урок: *************************************************************


# № 25358 ЕГКР 13.12.25 (Уровень: Базовый)
# 1 куча: +2, +4, *2 | s >= 125 | 1 ≤ s ≤ 124
'''
def F(s, n):
    """
    :param s: - Кол-во камней в куче (их мы будем перебирать)
    :param n: - Это шаг нашей игры

    n = 1: Петя первый ход
    n = 2: Ваня первый ход
    n = 3: Петя второй ход
    n = 4: Ваня второй ход
    """
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n - 1), F(s + 4, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 124+1) if F(s, n=2)])
print([s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (вниз) | s <= 30 | s ≥ 31
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 5, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(31, 1000) if F(s, n=2)])
print([s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [5, 14, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке: 15, 2
