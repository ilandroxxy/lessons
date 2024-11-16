# region Домашка: ******************************************************************

# № 12918
'''
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 4 and len(not_copied) == 2:
        # if M[-1] != M[-2]:
        if M.count(max(M)) == 1:
            if M[0] * M[5] > M[1] + M[2] + M[3] + M[4]:
                print(sum(M))
                break
'''


# № 5627 (Уровень: Средний)
# https://stepik.org/lesson/1038670/step/9?unit=1062777
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(M) != len(set(M)) or all(M[1] - M[0] == M[i+1] - M[i] for i in range(len(M)-1)):
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
from itertools import permutations
print('1 2 3 4 5 6 7')
table = '12 13 14 15 16 17 21 27 31 35 37 41 45 46 51 53 54 61 64 71 72 73'
graph = 'BC CB DB BD DC CD DE ED EC CE EF FE FC CF FG GF CG GC GA AG CA AC'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# Задание 1 https://education.yandex.ru/ege/task/ec7525ac-28c3-46ad-b08e-3dd50971a444
'''
from itertools import permutations
print('1 2 3 4 5 6 7 8')
table = '13 14 15 23 25 31 32 38 41 45 46 51 52 54 64 67 68 76 78 83 86 87'
graph = 'аб ба ав ва бв вб бд дб дг гд вг гв де ед же еж зж жз ез зе аз за'
for p in permutations('абвгджзе'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i - 1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# Задание 1 https://education.yandex.ru/ege/task/54850221-13b8-42db-99b4-4f96f1734932
'''
from itertools import permutations
print('1 2 3 4 5 6 7')
table = '12 13 15 21 24 25 31 34 36 42 43 46 47 51 52 56 57 63 64 65 74 75'
graph = 'AF FA AG GA AD DA DE ED DG GD EC CE FE EF FC CF FB BF BG GB GC CG'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
