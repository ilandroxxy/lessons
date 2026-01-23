# region Домашка: ******************************************************************


# № 23764 Демоверсия 2026 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
# Среди натуральных чисел, не превышающих 1010, найдите все числа, соответствующие маске 3?12?14*5, делящиеся на 1917 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце – соответствующие им
# результаты деления этих чисел на 1917.
'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x)

from re import *
for x in range(1917, 10**10, 1917):
    if fullmatch('3[0-9]12[0-9]14[0-9]+5', str(x)):
        print(x)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/inf/task/8337d1c9-9cbc-4ff8-ac40-ce04ba5dd256
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов Y.

# Вариант 1: ctrl + F
'''
s = open('files/24.txt').readline()
print(s)
print(len('YYYYYYYYYYY'))
'''

# Вариант 2: Как 17 номер
'''
s = open('files/24.txt').readline()
# s = 'xxxxxYYYYYYxxxYYxxxxYYYxxxYx'
cnt = 1
maxi = 0
for i in range(0, len(s)-1, 1):
    # if s[i] == 'Y' and s[i+1] == 'Y':
    if s[i:i+2] == 'YY':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''

# Вариант 3: Через замену replace()
'''
s = open('files/24.txt').readline()
# s = 'ZXZXZXYYYYYYXZXZXZYYZXXZXZYYYZXZYX'
s = s.replace('X', ' ').replace('Z', ' ')
print(max([len(x) for x in s.split()]))
'''

# Вариант 4: Через import re
'''
from re import *
s = open('files/24.txt').readline()
# s = 'ZXZXZXYYYYYYXZXZXZYYZXXZXZYYYZXZYX'
# print([x.group(0) for x in finditer('[Y]+', s)])  # ['YYYYYY', 'YY', 'YYY', 'Y']
print(max([len(x.group(0)) for x in finditer('[Y]+', s)]))
'''


# https://education.yandex.ru/ege/inf/task/4a723df3-ea35-4f64-bba3-afda2c8fb879
'''
s = open('files/24.txt').readline()
s = s.replace('X', ' ').replace('Z', ' ')
print(max([len(x) for x in s.split()]))

s = open('files/24.txt').readline()
s = s.replace('Y', ' ').replace('Z', ' ')
print(max([len(x) for x in s.split()]))

s = open('files/24.txt').readline()
s = s.replace('Y', ' ').replace('X', ' ')
print(max([len(x) for x in s.split()]))
'''

# https://education.yandex.ru/ege/inf/task/cd3c4d7c-cce1-4818-a4fc-b0f79a867e13
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)

s = open('files/24.txt').readline()
while 'XX' in s or 'YY' in s or 'ZZ' in s:
    s = s.replace('XX', 'X X').replace('YY', 'Y Y').replace('ZZ', 'Z Z')
print(max([len(x) for x in s.split()]))
'''

# https://education.yandex.ru/ege/inf/task/28e37b75-0bb5-41f6-a308-b8d391400eb2
'''
s = open('files/24.txt').readline()
s = s.replace('E', ' ').replace('F', ' ')
print(max([len(x) for x in s.split()]))
'''


# https://education.yandex.ru/ege/inf/task/dd3c7b28-6972-4dde-8d11-ef34db484b6d
'''
s = open('files/24.txt').readline()
s = s.replace('AB', 'A B')
print(max([len(x) for x in s.split()]))
'''

# https://education.yandex.ru/ege/inf/task/915c9534-1982-40ce-9f6b-f5c8cec6bdef
'''
s = open('files/24.txt').readline()
for x in 'LISENOK':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# https://education.yandex.ru/ege/inf/task/8fccd20b-438a-48a7-91f8-49e34350e04c
'''
s = open('files/24.txt').readline()
s = s.replace('A', 'B').replace('B', 'C')
while 'CC' in s:
    s = s.replace('CC', 'C C')
print(max([len(x) for x in s.split()]))
'''


# https://education.yandex.ru/ege/inf/task/98ae80c8-1e05-4cad-b4cc-4adc1edcc487

s = open('files/24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('SQRP', 'QRPS', 'RPSQ', 'PSQR'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 3
print(maxi)

# QRP RP P SQRPSQRPSQRPSQRP S SQ SQR


from re import *
s = open('files/24.txt').readline()
print([x.group(0) for x in finditer('(QRP|RP|P)(SQRP)+(S|SQ|SQR)', s)])
print(max([len(x.group(0)) for x in finditer('(QRP|RP|P)(SQRP)+(S|SQ|SQR)', s)]))



# https://education.yandex.ru/ege/inf/task/417b95a7-a644-43d9-b3f1-d1a1f753789a



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, 12, 24, 26
