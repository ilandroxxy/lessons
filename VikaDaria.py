# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Чтение файла для 17 номера
'''
M = [int(x) for x in open('0. files/17.txt')]
'''

# Три прототипа 17 номера:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумеваются два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумеваются три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумеваются два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''

# № 24892 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if x < 0 and len(str(abs(x))) == 4 and abs(x) % 9 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x**2 + y**2)
print(len(R), min(R))
'''


# № 23563 Пересдача 03.07.25 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 35 == 0 and x > 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x != y:
        if abs(x - y) % min(A) == 0:
            R.append(x + y)
print(len(R), max(R))
'''


# № 21990 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    plus = [a for a in (x, y, z) if a > 0]
    minus = [a for a in (x, y, z) if a < 0]
    if abs(sum(minus)) <= sum(plus):
        if abs(x * y * z) % 10 == max(M) % 10:
            R.append(abs(x * y * z))
print(len(R), max(R))
'''

# № 10004 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if (x in A) + (y in A) == 1:
            if (abs(x + y) ** 0.5) == int((abs(x + y) ** 0.5)):
                R.append(x + y)
print(len(R), min(R))
'''


# № 23376 Резервный день 19.06.25 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
p = [x for x in M if len(str(abs(x))) == 5]
c = [x for x in p if abs(x) % 100 == 37]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (x in p) + (y in p) == 1:
        if (x + y) ** 2 > max(c) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''

# 23276
'''
M = [int(x) for x in open('files/17_23276.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if  abs(x) % 100 == 25]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) <= 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 13, 14, 15, 16, 17, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке: 9, 27
