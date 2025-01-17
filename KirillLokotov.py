# region Домашка: ************************************************************

# № 12797 (Уровень: Средний) 🌶
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if len(set(M)) == 3:
        copied = [x for x in M if M.count(x) == 2]
        not_copied = [x for x in M if M.count(x) == 1]
        if all(p % 2 != 0 for p in not_copied):
            if all(p % 2 == 0 for p in copied):
                cnt += 1
print(cnt)
'''


# and - Оба условия выполняются
# or - Хотя бы одно условие выполняется
# () != () - Только одно условие выполняется
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    if len(set(M)) != 6:
        flag += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''


# № 12795 (Уровень: Средний)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    avg = sum(M) // 7
    if any(x == avg for x in M):
        cnt += 1
print(cnt)
'''
# Ответ: 35


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 19233 ЕГКР 21.12.24 (Уровень: Базовый)
from itertools import *
print('1 2 3 4 5 6 7 8')
graph = 'BD DB BE EB BC CB CH HC HE EH HF FH FA AF FG GF AG GA GD DG DE ED'
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
for p in permutations('BCEHFAGD'):
    # ('D', 'G', 'A', 'F', 'H', 'B', 'C', 'E')
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ = []
# на следующем уроке:
