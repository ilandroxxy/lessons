# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# Чтение файла для 17 номера
M = [int(x) for x in open('0. files/17.txt')]
R = []  # Сюда будем складывать результаты


# Рассмотрим три прототипа задач:
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумевается два различных элемента
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        print(f'{x}{y}', end=' ')
    print()
'''


# № 18142 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 10 == 8]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 16 == min(A)) + (y % 16 == min(A)) == 1:
        R.append(x + y)
print(len(R), max(R))
'''


# № 18045 (Уровень: Базовый)

M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 10) + (y % 10) == len(A):
        R.append(x + y)
print(len(R), min(R))

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 23, 25]
# КЕГЭ  = []
# на следующем уроке: 17 номер


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]

# Второй пробник 28.02.25:
# Матвей 14/29 -> 62 вторичных баллов +[1-4, 6, 7, 10, 11, 14, 15, 16, 18, 23, 25] -[5, 8, 12, 13]
