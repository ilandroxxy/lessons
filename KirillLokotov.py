# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
for x in open('files/17.txt'):
    print(x)

# Строчка, чтобы прочитать содержимое файла для 17 номера
M = [int(x) for x in open('files/17.txt')]

# Рассмотрим три типа задач 17 номера:

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

# 3. Под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


# № 17873 Демоверсия 2025 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
R = []  # сюда складываем результаты
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    # остаток от деления хотя бы одного из элементов
    # на 16 равен минимальному элементу последовательности
    if x % 16 == min(M) or y % 16 == min(M):
        R.append(x + y)
print(len(R), max(R))
'''

# № 18176 (Уровень: Средний)

M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if x > 0 and str(x)[-1] == '4']
print(min(D))  # 54
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    s = ''.join([str(abs(p)) for p in (x, y, z)])
    summa = sum([int(p) for p in s])  # sum(map(int, s))
    # (3487, 908, -54) -> ['3487', '908', '54'] -> '348790854'
    if summa == min(D):
        R.append(x + y + z)
print(len(R), max(R))





# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ = []
# на следующем уроке:
