# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# Открыть файл 17 номера
'''
M = [int(x) for x in open('files/17.txt')]


# Рассмотрим три прототипа задач:
M = [1, 2, 3, 4, 5]

# 1. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

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
'''


# № 14952 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if str(x)[-3:] == '121']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    D = [p for p in (x, y, z) if p % 2 == 0 and len(str(abs(p))) == 4]
    if len(D) <= 1:
        if (x + y + z) <= max(A):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 16383 ЕГКР 27.04.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if abs(x) % 100 == 21 and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) != (y in A):
        if (x**2 + y ** 2) >= max(A) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''

'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) < 100]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x + y) / 2 > len(D):
        R.append(x + y)  # добавляет элемент в конец списка
print(len(R), max(R))
'''

# https://education.yandex.ru/ege/task/1add80bc-628c-4b17-888f-7b04f3b4b4e0
# 234789012 % 10 == 2
# 234789012 % 100 == 12
# str(234789012)[-2:] == '12'
# 1234789012 % 100 == 88
#
# len(str(abs(-200))) == 3
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 100 == 13]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x + y + z) <= max(D):
        if len([p for p in (x, y, z) if len(str(abs(p))) == 3]) == 2:
            R.append(x + y + z)
print(len(R), max(R))
'''


# https://education.yandex.ru/ege/task/8ed78924-577d-436c-97f2-32c324afa788
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 4 and abs(x) % 100 == 42]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in D) + (y in D) + (z in D) >= 2:
        if (x + y + z) > max(D):
            R.append(x + y + z)
print(len(R), max(R))
'''

# https://education.yandex.ru/ege/task/f3c2ea76-84dc-43cd-a8b8-3855a737e358
'''
M = [int(x) for x in open('files/17.txt')]
D = sorted([x for x in M if len(str(abs(x))) == 3])
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x + y) < D[1] ** 2:
        R.append(x + y)
print(len(R), max(R))
'''
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12]
# на следующем уроке: 7, 9, 10,
