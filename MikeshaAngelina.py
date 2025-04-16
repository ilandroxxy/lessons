# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# № 19712 (Уровень: Средний)
'''
def F(a, b, s):
    if a <= b:
        return a == b and 'AAA' not in s and 'BBB' not in s
    h = [F(a-2, b, s+'A')]
    if a % 2 == 0:
        h += [F(a/2, b, s+'B')]
    else:
        h += [F(a-7, b, s+'B')]
    return sum(h)

print(F(40, 1, ''))
'''


# https://education.yandex.ru/ege/task/1db660ae-e018-4537-be70-be01199dfa29
'''
from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]  
    if (max(M) + min(M)) % 3 == 0:
        if any(abs(p[0] - p[1]) == abs(p[2] - p[3]) for p in permutations(M)):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/7eeb5357-91a8-4e1a-b4ec-dafe92df2f09
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(uncopied) == 3:
        if (copied[0] ** 2) * 3 > (sum([x**2 for x in uncopied])):
            cnt += 1
print(cnt)
'''

'''
# [5, 5, 6, 7, 8]
# set([5, 5, 6, 7, 8]) = {5, 6, 7, 8}

# [5, 5, 5, 6, 7, 8]
# set([5, 5, 5, 6, 7, 8]) = {5, 6, 7, 8}

# [5, 5, 6, 6, 7, 8]
# set([5, 5, 6, 6, 7, 8]) = {5, 6, 7, 8}
'''


# https://education.yandex.ru/ege/task/d62dc568-941a-44da-870b-b8cc21faee9f
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if sum(nechet) > sum(chet):
        flag += 1
    if len(set(M)) == 4:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)



cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if (sum(nechet) > sum(chet)) + (len(set(M)) == 4) == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/0cee3383-2699-4e0d-a2f1-5f50a85ad086
'''
from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if max(M) < sum(M) - max(M):
    if max(M) < M[0] + M[1] + M[2]:  # sum(M[:3])
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# № 21421 Досрочная волна 2025 (Уровень: Базовый)
'''
from re import *
s = open('0. files/24.txt').readline()
# num = r'([123456789AB][0123456789AB]*[02468A])'
num = r'([1-B][0-B]*[02468A])'
M = [x.group() for x in finditer(num, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# № 20813 Апробация 05.03.25 (Уровень: Сложный)
'''
from re import *
s = open('0. files/24.txt').readline()
num = r'([789][0789]*|[0])'
reg = rf'{num}([*-]{num})*'
M = [x.group() for x in finditer(reg, s)]
maxi = 0
for x in M:
    maxi = max(maxi, len(x))
    print(x)
print(maxi)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [9, 13, 17, 19-21, 22, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 11, 24 - регулярки

# Первый пробник 5.02.25:
# Ангелина 11/29 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/29 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]

# Второй пробник 28.02.25:
# Ангелина 10/29 -> 51 вторичных баллов +[2, 3, 4, 7, 9, 10, 14, 18, 23, 25] -[1, 5, 6, 8, 12, 11, 13, 15, 17]
# Сергей 16/29 -> 67 вторичных баллов +[1, 2, 5, 6, 8, 11, 13-18, 19-21, 23, 25] -[3, 4, 7, 9, 10, 12, 22, 24]
