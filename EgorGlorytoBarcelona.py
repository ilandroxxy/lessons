# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 5924 (Уровень: Средний)
'''
def F(s, n):
    if s >= 56:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s + 2, n - 1)]
    if s % 3 == 0:
        h += [F(s*3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 56) if F(s, 2)])
print([s for s in range(1, 56) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 56) if F(s, 6) and not F(s, 4)])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 18, 19-21, 22, 23, 25]
# КЕГЭ  = []
# на следующем уроке: 9, 17

# Первый пробник 21.12.24:
# Egor 7/10 -> 40 вторичных баллов +[1, 4, 5, 10, 12, 13] -[2, 6, 8]

# Второй пробник 28.02.25:
# Egor 12/16 -> 56 вторичных баллов +[1-4, 6, 7, 11-14, 16, 23] -[5, 8, 10, 15]
