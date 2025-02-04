# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 24 №27691
# Текстовый файл состоит не более чем из 10**6 символов A, B и C.
# Определите максимальное количество идущих подряд символов A.


# Вариант 1 - ctrl + F
'''
s = open('0. files/24.txt').readline()
print(s)
'''


# Вариант 2 - aka 17 номер
'''
s = open('0. files/24.txt').readline()
count = 1  # длина промежуточной последовательности
count_max = 0
for i in range(len(s)-1):
    # if s[i] == 'A' and s[i+1] == 'A':
    if s[i:i+2] == 'AA':
        count += 1
        count_max = max(count_max, count)
    else:
        count = 1
print(count_max)
'''


# Вариант 3
'''
s = open('0. files/24.txt').readline()
s = s.replace('B', ' ').replace('C', ' ')
count_max = 0
for x in s.split():
    count_max = max(count_max, len(x))
print(count_max)


s = open('0. files/24.txt').readline()
s = s.replace('B', ' ').replace('C', ' ')
print(max([len(x) for x in s.split()]))


print(max([len(x) for x in open('0. files/24.txt').readline().replace('B', ' ').replace('C', ' ').split()]))
'''


# Тип 24 №40740
# Определите максимальное количество идущих подряд символов,
# среди которых нет ни одной буквы A и при этом не менее трёх букв E.
'''
s = open('0. files/24.txt').readline()
print(max([len(x) for x in s.split('A') if x.count('E') >= 3]))
'''


# Тип 24 №37159
# Найдите максимальную длину подстроки,
# в которой символы a и d не стоят рядом.
'''
s = open('0. files/24.txt').readline()
s = s.replace('ad', 'a d').replace('da', 'd a')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27689
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).

s = open('0. files/24.txt').readline()
count = 2
count_max = 0
for i in range(len(s) - 2):
    if s[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
        if count == 2 and s[i:i+3] != 'XYZ':
            continue
        count += 1
        count_max = max(count, count_max)
    else:
        count = 2
print(count_max)


# Тип 24 №27690
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
'''
s = open('0. files/24.txt').readline()
count = 1
count_max = 0
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        count += 1
        count_max = max(count_max, count)
    else:
        count = 1
print(count_max)


s = open('0. files/24.txt').readline()
while 'AA' in s or 'BB' in s or 'CC' in s:
    s = s.replace('AA', 'A A')
    s = s.replace('BB', 'B B')
    s = s.replace('CC', 'C C')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №59849
# Необходимо найти самую длинную подстроку,
# содержащую символы из алфавита 26-ричной системы счисления.
'''
s = open('0. files/24.txt').readline()
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[26:]:
    s = s.replace(x, ' ')

print(sorted([len(x) for x in s.split()])[-1])
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №47021
# Определите количество групп из идущих подряд не менее 10 символов,
# которые начинаются и заканчиваются буквой A и не содержат других
# букв A (кроме первой и последней) и букв B.
'''
s = open('0. files/24.txt').readline()
s = s.replace('A', 'A A')
print(len([x for x in s.split() if 'B' not in x and len(x) >= 10]))
'''


# Тип 24 №47228
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида:
# согласная + гласная.
'''
s = open('0. files/24.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'F').replace('F', 'D')
while 'AA' in s or 'DD' in s:
    s = s.replace('DD', 'D D').replace('AA', 'A A')
print(max([len(x) for x in s.split()]) / 2)
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]
