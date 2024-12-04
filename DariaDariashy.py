# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038670/step/14?unit=1062777
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]

    nechet = [x for x in M if x % 2 != 0]

    k = (len(M) != len(set(M))) + (len(nechet) == 3)
    if k == 1:
        cnt += 1
print(cnt)
'''


# https://stepik.org/lesson/1038670/step/15?unit=1062777
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    # if (sum(M) // 7) in M:
    if any(x == (sum(M) // 7) for x in M):
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://inf-ege.sdamgia.ru/problem?id=27688
# Определите длину самой длинной последовательности, состоящей из символов Z.
# Хотя бы один символ Z находится в последовательности.
'''
# Вариант 1
s = open('files/24.txt').readline()
count = 1  # Будем считать промежуточные последовательности
maxi = 0  # Будем хранить длину самой большой последовательности
for i in range(len(s)-1):
    # x, y = s[i], s[i+1]
    # if x+y == 'ZZ':

    # if s[i] == 'Z' and s[i+1] == 'Z':

    if s[i:i+2] == 'ZZ':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# Вариант 2
'''
s = open('files/24.txt').readline()
s = s.replace('X', ' ').replace('Y', ' ')
print(max([len(x) for x in s.split()]))
'''

# Вариант 3 использовать просто ctrl + F в консоли
'''
s = open('files/24.txt').readline()
print(s)
'''


# https://inf-ege.sdamgia.ru/problem?id=47228
'''
s = open('files/24.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('DA', '*')
s = s.replace('D', 'A')
print(max([len(x) for x in s.split('A')]))
'''


# rrrrrXZZYrrr
# rrrrr rrr  # 5
# rrrrrXZZ ZZYrrr  # 8


# https://inf-ege.sdamgia.ru/problem?id=36037
# Определите максимальное количество идущих подряд символов,
# среди которых нет подстроки XZZY.
'''
s = open('files/24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
print(max([len(x) for x in s.split()]))
'''


# https://inf-ege.sdamgia.ru/problem?id=38602
'''
s = open('files/24.txt').readline()
s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))
'''

# https://inf-ege.sdamgia.ru/problem?id=27690
'''
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# https://inf-ege.sdamgia.ru/problem?id=58326
'''
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] > s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке:
