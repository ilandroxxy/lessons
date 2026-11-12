# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(x, y)
    # 1 2
    # 2 3
    # 3 4
    # 4 5
'''

# Под парой подразумевается два идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
'''

# Под тройкой подразумевается три идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
'''


# № 31514 Демоверсия 2027(Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
cnt = 0
maxi = 0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 33 == min(M)) or (y % 33 == min(M)):
        cnt += 1
        maxi = max(maxi, x + y)
print(cnt, maxi)

# Вариант 2
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 33 == min(M)) or (y % 33 == min(M)):
        R.append(x + y)
print(len(R), max(R))
'''


# № 31363 Пересдача 08.07.26(Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 4]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) > max(A):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 31155 Основная волна 19.06.26(Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if abs(x) % 100 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) or (y < 0):
        if (x + y) < len(A):
            R.append(x + y)
print(len(R), max(R))
'''


# Три прототипа 17 номера
'''
M = [1, 2, 3, 4, 5]

# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()
'''


# Тип 17 №37358
# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000. Определите и запишите в ответе
# сначала количество пар элементов последовательности, у которых сумма
# элементов кратна 10, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента
# последовательности. Порядок элементов в паре не важен.
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if (x + y) % 10 == 0:
            R.append(x + y)
print(len(R), max(R))  # 4999742 19990
'''


# № 25356 ЕГКР 13.12.25(Уровень: Базовый)
# Определите количество троек элементов последовательности,
# в которых ни один из трёх элементов не является четырёхзначным числом,
# а сумма элементов тройки больше максимального элемента последовательности,
# оканчивающегося на 30. В ответе запишите количество найденных троек чисел,
# затем максимальную из сумм элементов таких троек.
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# № 21712 ЕГКР 19.04.25(Уровень: Базовый)

M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
B = [x for x in A if x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [13, 16, 17, 19-21]
# КЕГЭ = []
# todo на следующем уроке: 9, 15,
