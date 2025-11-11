# region Домашка: ******************************************************************


# № 8594 (Уровень: Базовый)
'''
def F(a,s, n):
    if a*s >= 455:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s, n-1), F(a,s+1, n-1), F(a*2,s, n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 91) if  F(5,s, n=2)])
print([s for s in range(1, 91) if  F(5,s, n=3) and not F(5,s, n=1) ])
print([s for s in range(1, 91) if F(5,s, n=4) and not F(5,s, n=2)] )
'''


# 1 куча: +1, +2, *2 | s >= 61 | 1 <= s <= 56
'''
def F(s, n, c):
    if s >= 61:
        return n % 2 == 0
    if n == 0:
        return 0
    if c == 'A':
        h = [F(s + 2, n - 1, 'B'), F(s * 2, n - 1, 'C')]
    elif c == 'B':
        h = [F(s + 1, n - 1, 'A'), F(s * 2, n - 1, 'C')]
    elif c == 'C':
        h = [F(s + 1, n - 1, 'A'), F(s + 2, n - 1, 'B')]
    else:
        h = [F(s + 1, n - 1, 'A'), F(s + 2, n - 1, 'B'), F(s * 2, n - 1, 'C')]
    return any(h) if (n - 1) % 2 == 0 else all(h)


print([s for s in range(1, 57) if F(s, 2, '')])
print([s for s in range(1, 57) if F(s, 3, '') and not F(s, 1, '')])
print([s for s in range(1, 57) if F(s, 4, '') and not F(s, 2, '')])
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
