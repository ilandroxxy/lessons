# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Как открывать файлы
'''
file = open('0. files/17.txt')
print(file)  # <_io.TextIOWrapper name='0. files/17.txt' mode='r' encoding='UTF-8'>

# print(file.read())
# print(file.readline())
# print(file.readlines())
file.close()

with open('0. files/17.txt', mode='r') as file:
    print(file.readline())
# Тут файл считается закрытым

M = []
with open('0. files/17.txt', mode='r') as file:
    for s in file:
        M.append(int(s))
print(M)
'''

# Как открывать файл для 17 номера
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
'''

# Три прототипа задач 17 номера:
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


# https://education.yandex.ru/ege/task/d5802159-70ca-4d5d-832c-9856d41c15a6
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if x > 0 and x % 100 == 17 and len(str(x)) == 5]
B = [x for x in M if abs(x) % 100 == 17]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    # if x in B or y in B or z in B:
    if (x in B) + (y in B) + (z in B) >= 1:
        if (abs(x) + abs(y) + abs(z)) <= max(D):
            R.append(x + y + z)
print(len(R), min(R))
'''


# https://education.yandex.ru/ege/task/8e1b9524-b73c-49fc-9fe4-36e27cc94449
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if x % 2025 == 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if x % min(D) == 0 or y % min(D) == 0 or z % min(D) == 0:
        if len(str((x + y + z))) == 6:
            R.append(x + y + z)
print(len(R), max(R))
'''

'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x % 16 == min(M) or y % 16 == min(M):
        R.append(x + y)
print(len(R), max(R))
'''


# https://education.yandex.ru/ege/task/de7994f7-d8fe-4848-a91b-b9e7f7490d67
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if abs(x) % 100 == 42]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) + (y in D) + (z in D) >= 2:
        if (x * y * z) > max(D) ** 2:
            R.append(x * y * z)
print(len(R), max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]
