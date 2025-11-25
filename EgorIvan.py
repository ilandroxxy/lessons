# region Домашка: ******************************************************************

# № 6268 Danov2302 (Уровень: Средний)
'''
def F(x, a1, a2):
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    A = a1 <= x <= a2
    return (not(((not B) <= (C)) <= (A)))

R = []
M = [x / 4 for x in range(10 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) == False for x in M):
            R.append(a2 - a1)
print(min(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Способ открывать 17.txt файлы
'''
M = [int(s) for s in open('files/17.txt')]
print(M)
'''

# Три прототипа 17 номера:
'''
#  i 0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента последовательности
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента последовательности
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумевается два различных элемента последовательности
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
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if x < 0 and len(str(abs(x))) == 4 and abs(x) % 9 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x**2 + y**2)
print(len(R), min(R))
'''


# № 22468 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if abs(x + y) > sum(M) / len(M):
        R.append(x + y)
print(len(R), abs(min(R)))
'''


# № 22469 (Уровень: Средний)
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if x % 2 != 0 and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (str(x)[-1] == str(sum(A))[-1]) + (abs(y) % 10 == abs(sum(A)) % 10) == 1:
        R.append(x * y)
print(len(R), max(R))
'''


# № 18582 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x < 0) + (y < 0) + (z < 0) >= 2:
        if abs(x + y + z) % 10 == abs(min(M)) % 10:
            R.append(abs(x + y + z))
print(len(R), max(R))
'''

# # endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 9, 27
