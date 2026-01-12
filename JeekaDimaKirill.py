# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Как можно открывать файлы
'''
file = open('files/17.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='files/17.txt' mode='r' encoding='UTF-8'>

M = []
for s in file:
    s = int(s)
    M.append(s)
print(M)

file.close()
'''


# Как надо открывать файлы
'''
with open('files/17.txt', mode='r') as file:
    M = []
    for s in file:
        s = int(s)
        M.append(s)
    print(M)
'''

# Как будем делать мы
'''
M = [int(s) for s in open('files/17.txt')]
print(M)
'''


# Три прототипа 17 номера
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


# № 25356 (Уровень: Базовый)
# Определите количество троек элементов последовательности,
# в которых ни один из трёх элементов не является четырёхзначным числом,
# а сумма элементов тройки больше максимального элемента последовательности, оканчивающегося на 30
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 24892 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if x < 0 and len(str(abs(x))) == 4 and abs(x) % 9 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x**2 + y**2)
print(len(R), min(R))
'''


# № 23376 Резервный день 19.06.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in A if abs(x) % 100 == 37]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) ** 2 > max(B) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''


# № 21712 ЕГКР 19.04.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
B = [x for x in A if x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 7718 (Уровень: Средний)

M = [int(s) for s in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))



# endregion Урок: *************************************************************
#
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 9, 27
