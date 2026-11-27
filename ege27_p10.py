# region Домашка: ******************************************************************

# № 8585 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - sum(map(int, str(a))), b) + F(a // 2, b) + F(a-1, b)

print(F(40, 25) * F(25, 10))


n = 34253456
summa = 0
while n > 0:
    summa += n % 10
    n //= 10
print(summa)  # 32

summa = 0
n = str(34253456)
for x in n:
    summa += int(x)
print(summa)

summa = 0
n = str(34253456)
for i in range(1, 10):
    summa += n.count(str(i)) * i
print(summa)

s = '101010101'
summa = s.count('1')
print(summa)

s = '34253456'
print(sum([int(x) for x in s]))
print(sum(map(int, s)))


s = '34253456 d.'
print(sum([int(x) for x in s if x in '0123456789']))
print(sum([int(x) for x in s if x.isdigit()]))

def syma(n):
    return sum(int(i) for i in str(n))

s = '9428'
print([int(x) for x in s])  # [9, 4, 2, 8]
print(int(x) for x in s)  # <generator object <genexpr> at 0x100498820>

print(sum([int(x) for x in s]))  # [9, 4, 2, 8]
print(sum(int(x) for x in s))  # <generator object <genexpr> at 0x100498820>
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# s - это кол-во камней в куче (мы его ищем)

# n - это шаг нашей игры
# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 28940 ЕГКР 18.04.26(Уровень: Базовый)
# 1 куча: s+1, s+5, s*3 | s >= 124 | 1 ≤ s ≤ 123
'''
def F(s, n):
    if s >= 124:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+5, n-1), F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 123+1) if F(s, n=2)])
print(20, [s for s in range(1, 123+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 123+1) if F(s, n=4) and not F(s, n=2)])
'''


#  29974 Апробация 14.05.26(Уровень: Базовый)
# 1 куча: a-3, s-7, s/4 до меньшего | s <= 15 | s > 15
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-7, n-1), F(floor(s / 4), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(16, 1000) if F(s, n=2)])
print(20, [s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 23565 Пересдача 03.07.25(Уровень: Базовый)
# 1 куча: s-3, s-8, s/3 до меньшего | s <= 15 | s >= 16
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(s-8, n-1), F(floor(s / 3), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(16, 1000) if F(s, n=2)])
print(20, [s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# № 31516 Демоверсия 2027(Уровень: Базовый)
# 2 кучи: a+4, s+4, a*2, s*2 | a+s >= 133 | a = 17 | 1 <= s <= 115

def F(a, s, n):
    if a+s >= 133:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+4, s, n-1), F(a, s+4, n-1), F(a*2, s, n-1), F(a, s*2, n-1),]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 115+1) if F(17, s, n=2)])
print(20, [s for s in range(1, 115+1) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(1, 115+1) if F(17, s, n=4) and not F(17, s, n=2)])




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [8, 10, 15, 16, 23, 19-21]
# КЕГЭ = []
# todo на следующем уроке: 13

# 2, 5, 18