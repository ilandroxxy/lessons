# region Домашка: ******************************************************************


# № 23368 Резервный день 19.06.25 (Уровень: Базовый)
'''
n = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    n += 1
    # copied1 = [x for x in M if M.count(x) == 1]
    # if len(copied1) == 5:
    if len(set(M)) == 5:
            if 2 * (max(M) + min(M)) == 3 * (M[1] + M[2] + M[3]):
                print(n)
'''
# 13412


# № 5627 (Уровень: Средний) 🌶
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied = [x for x in M if M.count(x) > 1]
    flag = 0
    if len(copied) > 0:
        flag += 1
    a, b, c, d, e, f = M
    if (b - a) == (c - b) == (d - c) == (e - d) == (f - e):
        flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 23547 Пересдача 03.07.25 (Уровень: Базовый)

print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 14 21 23 24 32 36 37 41 42 45 54 57 63 67 73 75 76'
graph = 'AF FA AG GA FG GF FC CF CB BC CD DC DB BD BE EB EG GE'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # A F C G E D B
        # D C F B E A G

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 8, 9, 13, 14, 15, 16, 17, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке:
