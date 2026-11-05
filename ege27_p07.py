# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# a - кол-во камней в первой куче
# s - кол-во камней во второй куче
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход

# № 31516 Демоверсия 2027(Уровень: Базовый)
# 2 кучи: a+4, s+4, a*2, s*2 | a + s >= 133 | a = 17 | 1 <= s <= 115
'''
def F(a, s, n):
    if a + s >= 133:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 4, s, n-1), F(a, s + 4, n-1), F(a * 2, s, n-1), F(a, s * 2, n-1)]
    # return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)


print(19, [s for s in range(1, 115+1) if F(17, s, n=2)])
print(20, [s for s in range(1, 115+1) if F(17, s, n=3) and not F(17, s, n=1)])
print(21, [s for s in range(1, 115+1) if F(17, s, n=4) and not F(17, s, n=2)])
'''



# № 31227 Резерв 22.06.26(Уровень: Базовый)
# 2 кучи: a-3, s-3, a/3, s/3  a+s <= 53 a = 19  s >= 35
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 53:
        return n % 2 ==0
    if n ==0:
        return 0
    h = [F(a -3, s, n-1), F(a, s-3,n-1), F(floor(a/3),s,n-1), F(a, floor(s/3),n-1)]
    return any(h) if (n-1 ) %2==0 else all(h)
    return any(h) if (n-1 ) %2==0 else any(h)

print(19, [s for s in range(35+1, 1000) if F(19, s, n=2)])
print(20, [s for s in range(35+1, 1000) if F(19, s,n=3) and not F(19, s,n=1)])
print(21, [s for s in range(35+1, 1000) if F(19,s,n=4) and not F(19, s, n=2)])
'''


# № 31157 Основная волна 19.06.26(Уровень: Базовый)
# 2 кучи: а + 1, s + 1, а * 2, s * 2 | а+s >= 171| а = 25| 1 <= s <= 171
'''
def F(a, s, n):
    if a + s >= 171:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 1, s, n - 1), F(a, s + 1, n - 1), F(a * 2, s, n - 1), F(a, s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 145 + 1) if F(25, s, n = 2)])
print(19, [s for s in range(1, 145 + 1) if F(25, s, n = 3) and not F(25, s, n = 1)])
print(19, [s for s in range(1, 145 + 1) if F(25, s, n = 4) and not (F(25, s, n = 2))])
'''


# № 28940 ЕГКР 18.04.26(Уровень: Базовый)
# 1 куча: s + 1, s + 5, s * 3,   s >= 124      1 <= s <= 123
'''
def F(s, n):
    if s >= 124:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s + 5, n - 1), F(s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else all(h)


print(19, [s for s in range(1, 123 + 1) if F(s, n=2)])
print(20, [s for s in range(1, 123 + 1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 123 + 1) if F(s, n=4) and not (F(s, n=2))])
'''





# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 13, 14, 15, 16, 18, 19-21, 22]
# КЕГЭ = []
# todo на следующем уроке:
