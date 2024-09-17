# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
file = open(file='9.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='9.txt' mode='r' encoding='UTF-8'>
file.close()


with open(file='9.txt', mode='r') as file:
    print(file)
    # Когда мы выходим из with, то файл считается закрытым


# print(file.read()) - Все содержимое файла сразу

# print(file.readline()) - Возвращает только лишь первую строку файла

# print(file.readlines()) - Возвращает сразу все строки файла в виде списка

file = open('9.txt')

print(file)  # <_io.TextIOWrapper name='9.txt' mode='r' encoding='UTF-8'>

# for s in open('9.txt'):
#     print(s)
'''


'''
with open(file='9.txt', mode='r') as file:
    for s in file:
        M = [int(x) for x in s.split()]
        print(M)
'''


# № 17863 Демоверсия 2025 (Уровень: Средний)
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – в строке только одно число повторяется трижды, остальные числа различны;
# – квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех её неповторяющихся чисел.
'''
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
'''
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        if sum(copied) ** 2 > sum(not_copied) ** 2:
            cnt += 1
print(cnt)
'''


# № 17770 (Уровень: Средний)
'''
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if (M[-1] + M[-2]) * 2 > (sum(M[:-2]) * 3):
        N = [x for x in M if abs(x) % 10 == 5]
        if len(N) >= 2:
            cnt += 1
print(cnt)
'''

# № 17522 Основная волна 07.06.24 (Уровень: Базовый)
'''
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if max(M) < sum(M[:-1]):
        if len(set(M)) == 3:
            cnt += 1
print(cnt)
'''

'''
from itertools import *
M = [1, 2, 3, 4]
for p in permutations(M):
    print(p)
'''


# № 16320 Открытый вариант 2024 (Уровень: Базовый)

'''
from itertools import *
cnt = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''
'''
from itertools import *
cnt = 0
num = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        num += 1
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(num - cnt)
'''

'''
s = input('Введите строку: ')
if len(set(s)) == len(s):
    print('Нет копий')
else:
    print('Копии есть')
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# todo: № 12797 Открытый курс "Слово пацана" (Уровень: Средний)

cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(not_copied) == 2:
        if all(str(x) in '02468' for x in copied):
            if all(str(x) in '13579' for x in not_copied):
                cnt += 1
print(cnt)

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

