# region Домашка: ******************************************************************


# https://stepik.org/lesson/1309452/step/6?unit=1324568
'''
# i  0  1  2  3
L = [4, 5, 6, 9]
L[1] = 14
L.append(1)
L.append(2)
L.append(5)
del L[0]
L = L * 3
L.insert(4, 45)
print(L)
'''


# https://stepik.org/lesson/1309452/step/7?unit=1324568
'''
L = [3, 7, 1, 4, 9, 2]

x = L[0]
L[0] = L[-1]
L[-1] = x

# L[0], L[-1] = L[-1], L[0]
print(L)
'''


# https://stepik.org/lesson/1309452/step/8?unit=1324568
'''
n = int(input())
L = []
for i in range(n):
    x = int(input())
    L.append(x)
# [6, 7, 8, 3, 9]

L = sorted(L)
# [3, 6, 7, 8, 9]
print(L[-2])
'''
'''
n = int(input())
L = []
for i in range(n):
    x = int(input())
    L.append(x)
# [6, 7, 8, 3, 9]

L.remove(max(L))
# [3, 6, 7, 8]
print(max(L))
'''

# https://stepik.org/lesson/1309452/step/9?unit=1324568
'''
n = int(input())
L = []
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        L.append(x)
print(L)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
'''


# № 23548 Пересдача 03.07.25 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F = ((x∨y)→z)∨(y≡w)∨z
                F =((x or y) <= z) or (y == w) or z
                if F == 0:
                    print(x, y, z, w)
'''


# № 23361 Резервный день 19.06.25 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F=¬(y→(x≡z))∧(w→x)
                F =(not(y <= (x == z))) and (w <= x)
                if F == 1:
                    print(x, y, z, w)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ = []
# на следующем уроке:
