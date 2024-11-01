# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
for s in open('files/17.txt'):
    print(int(s))

file = open('files/17.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='files/17.txt' mode='r' encoding='UTF-8'>
file.close()

with open('files/17.txt', mode='r') as file:
    print(file)
# Тут файл уже считается закрытым


with open('files/17.txt', mode='r') as file:
    M = [int(x) for x in file]
'''

'''
# Способ открытия файла для 17 номера:
M = [int(x) for x in open('files/17.txt')]

# Разберем три типа задач 17 номера:
M = [1, 2, 3, 4, 5]

# 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]


# 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        print(f'{x}{y}', end=' ')
    print()
'''

# Тип 17 №51986
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 10 == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if abs(min(x, y)) % 10 == 5:
        if (x**2 + y**2) < min(D) ** 2:
            R.append(x**2 + y**2)
print(len(R), max(R))
'''


# Тип 17 №37360
'''
M = [int(x) for x in open('files/17.txt')]
print(M)
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if (x + y) % 120 == 0:
            R.append(x + y)
print(len(R), max(R))
'''


# Тип 17 №39764
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = sorted((M[i], M[i+1], M[i+2]))
    if x ** 2 + y ** 2 == z ** 2:
        R.append(x + y + z)
print(len(R), max(R))
'''


# https://inf-ege.sdamgia.ru/problem?id=68279
# Тип 17 №68279
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 1000 == 562]
R = []
for i in range(len(M)-3):
    # x, y, z, w = M[i], M[i+1], M[i+2], M[i+3]
    x, y, z, w = M[i:i+4]
    M_5 = [p for p in M[i:i+4] if len(str(abs(p))) == 5]
    M_not_5 = [p for p in M[i:i+4] if len(str(abs(p))) != 5]
    if len(M_5) >= 1 and len(M_not_5) >= 2:
        krat_3 = [p for p in M[i:i+4] if abs(p) % 3 == 0]
        krat_7 = [p for p in M[i:i+4] if abs(p) % 7 == 0]
        if len(krat_3) < len(krat_7):
            if max(D) < (x + y + z + w) < 2 * max(D):
                R.append(x + y + z + w)
print(len(R), max(R))
'''


# Тип 17 №46975
'''
M = [int(x) for x in open('files/17.txt')]
chet = [x for x in M if x % 2 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 3 == 0 and y < sum(chet) / len(chet)) or (y % 3 == 0 and x < sum(chet) / len(chet)):
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
