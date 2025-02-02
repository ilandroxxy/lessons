# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Пару слов про работу с файлами
'''
file = open('files/17.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='files/17.txt' mode='r' encoding='UTF-8'>


# print(file.read())  # Прочитать/Вывести сразу все содержимое файла
# print(file.readline())  # Вывести только первую строку файла (Заголовки)
# print(file.readlines())  # Вывести все строки файла в виде списка строк

file.close()  # Закрыли файл
'''

# Хороший патерн работы с файлами:
'''
with open('files/17.txt', mode='r') as file:
    M = []
    for x in file:
        M.append(int(x))
print(M)
# Считается, что выходя из with файл уже закрыт
'''

# Лучший способ открытия файла для 17 номера:
'''
M = [int(x) for x in open('files/17.txt')]
'''

# Разберем три прототипа задач 17 номера:
'''
# Пример тестовых данных
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


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 100 == 43 and 10000 <= abs(x) <= 99999]
# D = [x for x in M if str(x)[-2:] == '43' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    # if x in D or y in D or z in D:
    if (x in D) + (y in D) + (z in D) >= 1:
        if (x**2 + y**2 + z**2) <= max(D)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''


# № 19119 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x % 43 == min(M) and y % 43 == min(M):
        R.append(abs(x - y))
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



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 17, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Тимур 6/14 -> 40 вторичных баллов +[12, 14, 16, 19, 23, 25] -[4, 5, 6, 7, 8, 10, 11, 13]
