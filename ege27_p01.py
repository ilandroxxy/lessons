# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 1975 Демоверсия 2022(Уровень: Базовый)
# Текстовый файл состоит из символов P, Q, R и S.
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых нет идущих подряд символов P.

# Вариант 1
'''
s = open('files/24.txt').readline()
while 'PP' in s:
    s = s.replace('PP', 'P P')

print(max([len(x) for x in s.split()]))
'''

# Вариант 2
'''
s = open('files/24.txt').readline()
cnt = 0
maxi = 0
for i in range(len(s)-1):
    if s[i:i+2] == 'PP':
        if cnt > maxi:
            maxi = cnt
        cnt = 0
    cnt += 1
print(maxi)
'''

# Вариант 3
'''
from re import *
s = open('files/24.txt').readline()
pat = '(P)+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
'''


# № 2419 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского
# алфавита A, B, C длиной не более 106 символов.
# Найдите длину самой длинной подцепочки, состоящей из символов C
'''
# Вариант 1

s = open('files/24.txt').readline()
s = s.replace('A', 'B').replace('B', ' ')
print(max([len(x) for x in s.split()]))


# Вариант 2


s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i:i+2] == 'CC':
        cnt += 1
    else:
        if cnt > maxi:
            maxi = cnt
        cnt = 1
print(maxi)


# Вариант 3

from re import *
s = open('files/24.txt').readline()
pat = '[C]+'
M = [x.group(0) for x in finditer(pat, s)]
print(max([len(x) for x in M]))
'''


# № 19887 (Уровень: Базовый)
# (М. Попков) Во входном файле в строчку записаны
# арабские цифры от 0 до 9 включительно.
# Требуется найти самую длинную последовательность,
# в которой чётные и нечётные цифры чередуются.
'''
# Вариант 2

s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if (s[i] in '13579' and s[i+1] in '02468') or (s[i+1] in '13579' and s[i] in '02468'):
        cnt += 1
    else:
        maxi = max(cnt, maxi)
        cnt = 1
print(maxi)


# Вариант 1

s = open('files/24.txt').readline()
for x in '02468':
    s = s.replace(x, '2')
for x in '13579':
    s = s.replace(x, '1')
while '22' in s or '11' in s:
    s = s.replace('11', '1 1')
    s = s.replace('22', '2 2')
print(max([len(x) for x in s.split()]))


# Вариант 3
from re import *
s = open('files/24.txt').readline()
pat = '([13579][02468])+|([02468][13579])+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''


# № 2426 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов 1, 2, 3, A, B, C.
# Определите максимальное количество идущих подряд цифр.
'''
s = open('files/24.txt').readline()
for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))

from re import *
s = open('files/24.txt').readline()
pat = '[123]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''



# № 16333 Открытый вариант 2024(Уровень: Базовый)
# Текстовый файл состоит из заглавных букв латинского алфавита Q, R, W и цифр 1, 2, 4.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых ни одна буква не стоит рядом с буквой, а цифра – с цифрой.

'''
from re import *
s = open('files/24.txt').readline()
pat = '([QRW][124])+[QRW]|([124][QRW])+[124]'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))


s = open('files/24.txt').readline()
s = s.replace('Q', 'W').replace('W', 'R')
s = s.replace('1', '4').replace('4', '2')
while '22' in s or 'RR' in s:
    s = s.replace('22', '2 2')
    s = s.replace('RR', 'R R')
print(max([len(x) for x in s.split()]))
'''



# № 2942 Апробация 19.02.2022(Уровень: Базовый)
# Текстовый файл состоит из символов А, В и С.
# Определите максимальное количество идущих подряд пар
# символов АВ или АС в прилагаемом файле.

s = open('files/24.txt').readline()
s = s.replace('AB', '+').replace('AC', '*')
s = s.replace('A', 'B').replace('B', 'C').replace('C', ' ')
print(max([len(x) for x in s.split()]))


from re import *
s = open('files/24.txt').readline()
pat = '((AB)|(AC))+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]) / 2)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# todo на следующем уроке:
