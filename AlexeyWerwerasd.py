# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# Задание 17 https://education.yandex.ru/ege/task/75f1504f-3de9-4807-94ca-b08cea796a26


# Способ открытия файла
'''
M = [int(x) for x in open('files/17.txt')]
'''


# Рассмотрим три прототипа задач:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    # x, y = M[i], M[i+1]
    #                  ~^^^^^
    # IndexError: list index out of range


# 2. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
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


# Задание 17 https://education.yandex.ru/ege/task/75f1504f-3de9-4807-94ca-b08cea796a26
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x % 3 == 0 or y % 3 == 0:
        R.append(x+y)
print(len(R), max(R))
'''


# Задание 17 https://education.yandex.ru/ege/task/ac407c00-8ed4-46fb-b78c-45b5ebcd9b6d
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 3]
print(D)
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    summa_x = sum([int(i) for i in str(x) if i.isdigit()])
    summa_y = sum([int(i) for i in str(y) if i.isdigit()])
    if (summa_x % 5 == 0) != (summa_y % 5 == 0):
        if abs(x**2 - y**2) >= max(D)**3:
            R.append(x+y)
print(len(R), max(R))
'''


'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 4]
A = [x for x in M if abs(x) % 100 == 25]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) + (y in D) + (z in D) <= 2:
        if (x + y + z) <= max(A):
            R.append(x + y + z)
print(len(R), max(R))
'''

M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        R.append(x+y)
print(len(R), max(R))
sum([int(i) for i in str(x) + str(y)])

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ = []
# на следующем уроке:
