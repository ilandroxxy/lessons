# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# КЕГЭ № 5491 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 10 == 3]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    # а сумма квадратов элементов пары меньше, чем квадрат наименьшего из элементов последовательности
    if x < y and abs(x) % 10 == 3 and (x ** 2 + y ** 2) < min(D) ** 2:
        R.append(x ** 2 + y ** 2)
    if y < x and abs(y) % 10 == 3 and (x ** 2 + y ** 2) < min(D) ** 2:
        R.append(x ** 2 + y ** 2)
print(len(R), max(R))


M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if abs(x) % 10 == 3]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if abs(min(x, y)) % 10 == 3 and (x ** 2 + y ** 2) < min(D) ** 2:
        R.append(x ** 2 + y ** 2)
print(len(R), max(R))
'''


# Открываем 9 номер .txt файл:
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
'''


# Тип 9 №52180
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):  # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(chet) > len(nechet):
            if sum(chet) < sum(nechet):
                cnt += 1
print(cnt)
'''


# Тип 9 №63025
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) != len(set(M)):
        if M.count(max(M)) == 1:  # — максимальное число в строке не повторяется;
            copied = [x for x in M if M.count(x) > 1]
            if sum(copied) > max(M):
                cnt += 1
print(cnt)
'''


# № 8946 (Уровень: Базовый)
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[4] ** 2 > M[0] * M[1] * M[2] * M[3]:
        if (M[4] + M[3]) > (2 * (M[0] + M[1] + M[3])):
            cnt += 1
print(cnt)
'''


# Тип 9 №69914
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        if copied[0] >= sum(not_copied) / 3:
            cnt += 1
print(cnt)
'''

# Тип 9 №39238
# Определите, сколько среди заданных троек чисел таких,
# которые могут быть сторонами прямоугольного треугольника.
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[0] ** 2 + M[1] ** 2 == M[2] ** 2:
        cnt += 1
print(cnt)
'''


# № 17522 Основная волна 07.06.24 (Уровень: Базовый)

cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[3] < M[0] + M[1] + M[2]:
        if len(set(M)) == 3:
            cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
