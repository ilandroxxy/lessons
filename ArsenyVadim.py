# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 23555 Пересдача 03.07.25 (Уровень: Базовый)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied2) == 2 and len(copied1) == 2:
        if max(copied3 + copied2) > max(copied1):
            cnt += 1
print(cnt)
'''


# № 23268 Основная волна 11.06.25 (Уровень: Базовый)
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if sum(copied2) / 4 < max(copied1):
            print(n)
            break
'''


# № 23368 Резервный день 19.06.25 (Уровень: Базовый)
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    if len(M) == len(set(M)):  # - в строке все числа различны;
        if 2 * (min(M) + max(M)) == 3 * (sum(M) - max(M) - min(M)):
            print(n)

# Вариант 2

n = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    n += 1
    if len(M) == len(set(M)):  # - в строке все числа различны;
        if 2 * (M[0] + M[-1]) == 3 * (M[1] + M[2] + M[3]):
            print(n)
'''


# № 14661 Открытый курс "Слово пацана" (Уровень: Сложный)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) > 0 and len(nechet) > 0:
        if len(chet) % 2 == 0 and len(nechet) % 2 != 0:
            if max(chet) % 4 == 0:
                cnt += 1
print(cnt)
'''


'''
from itertools import permutations
M = [1, 2, 3, 4]
for p in permutations(M):
    print(p)
    # (1, 2, 3, 4)
    # (1, 2, 4, 3)
    # (1, 3, 2, 4)
    # (1, 3, 4, 2)
    # (1, 4, 2, 3)
    # (1, 4, 3, 2)
    # (2, 1, 3, 4)
    # (2, 1, 4, 3)
    # .....
'''

# № 24344 (Уровень: Средний)
'''
from itertools import permutations
n = 0
summa = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    n += 1
    if (min(M) + max(M)) ** 2 > (M[1] ** 3 + M[2] ** 3):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):
            summa += n
print(summa)
'''


# № 20070(Уровень: Средний)
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    flag = 0
    A = [x for x in M if len(str(x)) == 2]
    if len(A) == len(M):
        flag += 1
    if all(x % 5 != 0 for x in M):
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''

# № 25348 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке семь целых чисел.
# Определить количество строк таблицы, для которых выполнены оба условия:
# - в строке одно число повторяется трижды, остальные числа различны;
# - максимальное число строки не повторяется.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copy3 = [x for x in M if M.count(x) == 3]
    copy1 = [x for x in M if M.count(x) == 1]
    if len(copy3) == 3 and len(copy1) == 4:
        # if max(copy1) > max(copy3):
        if M.count(max(M)) == 1:
            cnt += 1
print(cnt)
'''


# № 19117 (Уровень: Средний)
# (В. Лашин) Откройте файл электронной таблицы, содержащей
# в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, содержащих числа,
# для которых выполнено хотя бы одно условие:

# – В строке одно число повторяется дважды, остальные различны;
# – Выполнены следующие два условия:
#     1. Сумма чётных чисел строки больше суммы нечётных;
#     2. В строке существуют как чётные числа, так и нечётные числа.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    ch = [x for x in M if x % 2 == 0]
    nch = [x for x in M if x % 2 != 0]
    print(M)
    flag = 0
    copy2 = [x for x in M if M.count(x) == 2]
    copy1 = [x for x in M if M.count(x) == 1]
    if len(copy2) == 2 and len(copy1) == 3:
        flag += 1
    if sum(ch) > sum(nch):
        if len(ch) > 0 and len(nch) > 0:
            flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 27
