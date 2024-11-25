# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 24 №27696
# Определите длину самой длинной последовательности, состоящей из символов L.
# Хотя бы один символ L находится в последовательности.
'''
# Вариант 1
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'L' and s[i+1] == 'L':
    if s[i:i+2] == 'LL':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)

# Ответ: 7


# Вариант 2

s = open('files/24.txt').readline()
s = s.replace('D', ' ').replace('R', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 3 - ctrl + F

s = open('files/24.txt').readline()
print(s)
'''


# Тип 24 №38602
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых нет идущих подряд символов P.
'''
s = open('files/24.txt').readline()
while 'PP' in s:
    s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))
'''

# Тип 24 №48472
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите максимальное количество идущих подряд групп символов вида:
'''
s = open('files/24.txt').readline()
s = s.replace('D', 'C').replace('F', 'C')
s = s.replace('O', 'A')
s = s.replace('AAC', '*')
s = s.replace('A', ' ').replace('C', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №68257
# Определите максимальную длину непрерывного фрагмента,
# который начинается и заканчивается одной и той же буквой из
# первой половины алфавита (от A до M) и не содержит эту букву внутри.
'''
from string import *
alphabet = ascii_uppercase
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

s = open('files/24.txt').readline()
maxi = 0
for x in alphabet[:13]:
    s = s.replace(f'{x}', '* *')
    maxi = max([len(x) for x in s.split()])
    s = s.replace('* *', f'{x}')
print(maxi)
'''


s = open('files/24.txt').readline()
cnt = 0
s = s.replace('A', '* *')

for x in s.split():
    if 'A' not in x and 'B' not in x and len(x) >= 10:
        cnt += 1

print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
