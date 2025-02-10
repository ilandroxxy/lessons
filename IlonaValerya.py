# region Домашка: ******************************************************************

'''
def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 100)):
        R.append(A)
print(min(R))
'''

'''
def F(x, a1, a2):
    P = 10 <= x <= 45
    Q = 35 <= x <= 78
    A = a1 <= x <= a2
    return ((not P) <= (Q)) and (not A)


R = []
M = [x / 4 for x in range(5 * 4, 90 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) == False for x in M):
            R.append(a2 - a1)
print(round(min(R)))
'''

'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not ((not P) <= (Q))) <= ((A) <= ((not Q) <= (P)))


R = []
M = [x / 4 for x in range(5 * 4, 30 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(round(max(R)))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# M = []
# for s in open('0. files/17.txt'):
#     M.append(int(s))
# print(M)

# Как надо открывать файл для 17 номера:
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []  # сюда будем складывать результаты
'''


# Рассмотрим три типа задач 17 номера:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается пара идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумевается пара различных элементов последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


# № 18957 (Уровень: Средний)
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    # if (str(x).count('0') == 0) + (str(y).count('0') == 0) + (str(z).count('0') == 0) >= 2:
    D = [str(p).count('0') == 0 for p in (x, y, z)]
    if sum(D) >= 2:
        if (x + y + z) < max(M) / 2:
            R.append(x + y + z)

print(len(R), max(R))
'''


# № 15333 Досрочная волна 2024 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
D = [x for x in M if x % 19 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x > max(D) or y > max(D):
        R.append(x + y)
print(len(R), max(R))
'''


# № 7819 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
D3 = [x for x in M if len(str(abs(x))) == 3 and x > 0]
A2 = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in D3) or (y in D3):
        if (x + y) % max(A2) == 0:
            R.append(x + y)
print(len(R), max(R))
'''


# № 8161 /dev/inf 05.23 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
D3 = [x for x in M if len(str(abs(x))) == 3]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in D3) + (y in D3) == 1:
        if (x + y) <= max(D3):
            R.append(x + y)
print(len(R), max(R))
'''


# № 6696 (Уровень: Базовый)
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x + y + z) % 2022 == 0:
        # if (x >= 0) or (y >= 0) or (z >= 0):
        if (x >= 0) + (y >= 0) + (z >= 0) >= 1:
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 6353 (Уровень: Средний)
'''
M = [int(s) for s in open('0. files/17.txt')]
D = [x for x in M if abs(x) % 118 == 0]
A = [x for x in M if abs(x) % 118 == 0 and str(x)[-1] != '8']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) or (y in D) or (z in D):
        if str(x)[-3:] == '118' or str(y)[-3:] == '118' or str(z)[-3:] == '118':
            if (x + y + z) > max(A):
                R.append((x + y + z)**2)
print(len(R), max(R))
'''

# № 7718 (Уровень: Средний)
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
