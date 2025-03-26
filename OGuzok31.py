# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Определите максимальное количество идущих подряд символов A.
'''
# Вариант 1
s = open('0. files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'A' and s[i+1] == 'A':
    if s[i:i+2] == 'AA':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)

# Вариант 2
s = open('0. files/24.txt').readline()
s = s.replace('B', ' ').replace('C', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №59848
# Необходимо найти самую длинную подстроку,
# которая может являться числом в 24-ричной системе счисления.
'''
from string import *
alphabet = digits + ascii_uppercase
s = open('0. files/24.txt').readline()
for x in alphabet[24:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split() if x[0] != '0']))
'''

# Тип 24 №27690
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.

s = open('0. files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2? сопоставление, 3, 4, 5, 7, 8, 9-, 11-, 12-, 13, 14, 15, 16, 18, 19-21-, 22, 23]
# КЕГЭ = []
# на следующем уроке:


# Второй пробник 28.02.25:
# Селим 18/29 -> 72 вторичных баллов +[1-5, 8, 10-16, 19-21, 23, 25] -[6, 7, 9, 17, 22, 24]
