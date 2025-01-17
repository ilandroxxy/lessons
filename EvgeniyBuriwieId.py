# region Домашка: ************************************************************

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F=¬((¬x∨y)∧¬w)∨¬(z∧¬(y∧ w))
                F = (not(((not x) or y) and (not w)) or (not(z and (not (y and w)))))
                if F == 0:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F= ¬(w→(x≡y∨y))∧(z→x)
                F = (not(w <= (x == (y or y)))) and (z <= x)
                if F == 1:
                    print(x, y, z, w)
'''


print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F =  ((z == x)<=w) and (w<=(y and x))
                if F == 1:
                    print(x, y, z, w)


from itertools import *
print('1 2 3 4 5 6 7 8')
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'BD DB BE EB BC CB CH HC HE EH FH HF FA AF FG GF AG GA GD DG DE ED'
for p in permutations('BCHFAGED'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12, 17]
# на следующем уроке: 7, 9, 10,


# Первый пробник 21.12.24:
# 4/8 -> 27 вторичных баллов +[1, 10, 16, 23] -[2, 4, 12, 15]


