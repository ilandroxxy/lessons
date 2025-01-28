# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Пару слов про работу с файлами
'''
file = open('files/17.txt')
print(file.readline())
file.close()

with open('files/17.txt', mode='r') as file:
    print(file.readline())
# Здесь файл считается закрытым

M = []
for x in open('files/17.txt'):
    M.append(int(x))
print(M)
'''

# Идеальное чтение файла для 17 номера:
'''
M = [int(x) for x in open('files/17.txt')]
R = []
'''

# Разберем три прототипа 17 номера:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]


# 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Назовём парой два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if str(x)[-2:] == '43' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    # if x in D or y in D or z in D:
    # if any(p in D for p in (x, y, z)):
    if (x in D) + (y in D) + (z in D) >= 1:
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''


# № 18582 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if x < 0]  # отрицательные числа
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) + (y in D) + (z in D) >= 2:
        if str(x + y + z)[-1] == str(min(M))[-1]:
            R.append(abs(x + y + z))
print(len(R), max(R))
'''


# № 7718 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))
'''


#
# № 4416 (Уровень: Базовый)

M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if (x + y) % 60 == 0:
            if (x % 40 == 0) + (y % 40 == 0) >= 1:
                R.append(x + y)
print(len(R), max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Лиза 11/14 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

