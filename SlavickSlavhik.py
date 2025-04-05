# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20811 Апробация 05.03.25 (Уровень: Базовый)
# 1 куча: +1, +4, *2 | >= 51 | 1 ≤ S ≤ 50
'''
def F(s, h):
    if s >= 51:
        return h % 2 == 0    # True - Ваня победил / False - победил Петя
    if h == 0:
        return 0
    step = [F(s+1, h-1), F(s+4, h-1), F(s*2, h-1)]
    return any(step) if (h - 1) % 2 == 0 else all(step)


print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])
'''


# № 18144 (Уровень: Базовый)
'''
from math import ceil, floor

def F(s, h):
    if s <= 19:
        return h % 2 == 0    # True - Ваня победил / False - победил Петя
    if h == 0:
        return 0
    step = [F(s-4, h-1), F(s-6, h-1), F(ceil(s/2), h-1)]
    return any(step) if (h - 1) % 2 == 0 else all(step)


print([s for s in range(20, 1000) if F(s, 2)])
print([s for s in range(20, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(20, 1000) if F(s, 4) and not F(s, 2)])
'''


# № 20907 Апробация 05.03.25 (Уровень: Базовый)
'''
def F(a, s, h):
    if a+s >= 81:
        return h % 2 == 0    # True - Ваня победил / False - победил Петя
    if h == 0:
        return 0
    step = [F(a+1, s, h-1), F(a, s+1, h-1), F(a*2, s, h-1), F(a, s*2, h-1)]
    return any(step) if (h - 1) % 2 == 0 else all(step)


print([s for s in range(1, 74) if F(7, s, 2)])
print([s for s in range(1, 74) if F(7, s, 3) and not F(7, s, 1)])
print([s for s in range(1, 74) if F(7, s, 4) and not F(7, s, 2)])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ = [22, 25]
# на следующем уроке: повторить 22, 19-21, разобрать 3 с пробника

# Второй пробник 28.02.25:
# Славик 16/25 -> 67 вторичных баллов +[1, 2, 4-14, 16, 17, 18] -[3, 15, 19-21, 22-25]