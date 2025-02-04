# region Домашка: ******************************************************************

# № 7846 (Уровень: Базовый)
'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))


R = []
M = [x / 4 for x in range(10 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(round(max(R)))
'''


# № 2356 (Уровень: Базовый)
'''
def f(x, a1, a2):
    q = 35 <= x <= 78
    p = 10 <= x <= 45
    a = a1 <= x <= a2
    return ((not p) <= q) and (not a)


r = []
m = [x for x in range(0, 80)]
for a1 in m:
    for a2 in m:
        if all(f(x, a1, a2) == False for x in m):
            r.append(a2 - a1)

print(min(r))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


from itertools import *
print('1 2 3 4 5 6 7')
table = '13 17 23 26 27 31 32 35 45 46 53 54 62 64 67 71 72 76'  # тут
graph = 'AB BA AD DA AF FA FB BF FC CF CG GC GE EG EB BE ED DE'  # тут
for p in permutations('ABCDEGF'):  # тут
    new_table = table
    for i in range(1, 7+1):  # тут
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

print(13 + 21 + 8 + 53 + 5)

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 5, 6, 8, 12, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]
