# region Домашка: ******************************************************************

# № 17535 Основная волна 07.06.24 (Уровень: Средний)
'''
s = open('files/24.txt').readline()
s = s.replace('CD', 'C D').split()
maxi = -1
for i in range(len(s)-160):
    r = ''.join(s[i:i+161])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Максимальное количество идущих подряд символов
# среди которых символ * встречается ровно 3 раза.
'''
maxi = 0
s = 'XXXXX*XXXXX*XXX*XXXX*XXXXXX*XXX*XXX'.split('*')
# ['XXXXX', 'XXXXX', 'XXX', 'XXXX', 'XXXXXX', 'XXX', 'XXX']
for i in range(len(s)-3):
    r = '*'.join(s[i:i+4])
    maxi = max(maxi, len(r))
    # XXXXX*XXXXX*XXX*XXXX
    # XXXXX*XXX*XXXX*XXXXXX
    # XXX*XXXX*XXXXXX*XXX
    # XXXX*XXXXXX*XXX*XXX
print(maxi)
'''

# № 858 (Уровень: Базовый)
'''
import time
start = time.time()

from string import *
alphabet = digits + ascii_uppercase
cnt = 0
for s in open('files/24.txt').readlines():
    if any(f'F{x}O' in s for x in alphabet):
        cnt += 1
print(cnt)

print(time.time() - start)
'''

'''
a = int(input())
b = int(input())
summa = 0
for num in range(a, b + 1):
    if num % 2 == 0:
        print(num)
        summa += num

if summa == 0:
    print('Нет чётных чисел')
else:
    print(summa)
'''

'''
s = input()

a = int(input())
b = int(input())
M = [num for num in range(a, b + 1) if num % 2 == 0]
if sum(M) == 0:
    print('Нет чётных чисел')
else:
    print(*sorted(M), sum(M), sep='\n')
'''


# Логическая функция F задаётся выражением
# ((x ≡ z) ∨ ¬(x ≡ w)) ∧ ((y → x) ∨ ¬z)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x == z) or (not(x == w))) and ((y <= x) or (not z))
                if F == 0:
                    print(x, y, z, w)


print('x y z w')
from itertools import *
for x, y, z, w in product([0, 1], repeat=4):
    F = ((x == z) or (not(x == w))) and ((y <= x) or (not z))
    if F == 0:
        print(x, y, z, w)
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 24 №27696
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов L.
# Хотя бы один символ L находится в последовательности.

# Вариант 1
'''
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
'''

# Вариант 1
'''
s = open('files/24.txt').readline()
s = s.replace('R', ' ').replace('D', ' ')
print(max([len(x) for x in s.split()]))
# ['LLL', 'LLLLL', 'LLLLL', 'LLLLLLL', 'LLLLLLLLLL', 'LLLL', 'LLLLLLL', 'LLLL']
# [3, 5, 5, 7, 10, 4, 7, 4]
'''


# Тип 24 №27695
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)


s = open('files/24.txt').readline()
s = s.replace('LL', 'L L').replace('DD', 'D D').replace('RR', 'R R')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27689
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
count = 2
maxi = 0
for i in range(len(s) - 2):
    if s[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''


# Тип 24 №47228
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида:
# согласная  + гласная.
'''
s = open('files/24.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'D').replace('F', 'D')
while 'DD' in s or 'AA' in s:
    s = s.replace('AA', 'A A').replace('DD', 'D D')
R = []
for x in s.split():
    if x[0] == 'A':
        R.append(x[1:])
    else:
        R.append(x)

print(max([len(x) / 2 for x in R]))
'''


# Тип 24 №37131
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.

# s = 'FEWUYHFEIUWDFKEK LOEWKRL KEWRJEWIOJR'
# print(max([len(x) for x in s.split()]))
'''
s = open('files/24.txt').readline()
s = s.replace('KL', 'K L').replace('LK', 'L K')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №59817
# Текстовый файл состоит из символов, обозначающих прописные буквы латинского
# алфавита. Определите максимальное количество идущих подряд символов, среди
# которых никакие две буквы из набора букв A, B и C
# (с учетом повторений) не записаны подряд.
'''
s = open('files/24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №59849
# Текстовый файл состоит не более чем из 10**6 символов латинского алфавита.
# Необходимо найти самую длинную подстроку, содержащую символы из
# алфавита 26-ричной системы счисления. В ответ записать длину
# последовательности символов, которая может являться числом в 26-ричной
# системе счисления.

# Всегда можно посмотреть содержимое библиотеки через ctrl + B
'''
from string import *  # Из библиотеки string импортируем сразу все содержимое
alphabet = digits + ascii_uppercase  # Используем цифры и большие буквы
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ


s = open('files/24.txt').readline()
# s = '1100190001101109'
cnt = ''
r = ''
maxi = 0
for i in range(len(s)):
    if s[i] in alphabet[:26]:
        cnt += s[i]
    else:
        if len(cnt) > 0:
            while cnt[0] == '0':
                cnt = cnt[1:]
        if maxi < len(cnt):
            maxi = len(cnt)
        cnt = ''
print(maxi)
'''

# Вариант 2
'''
from string import *
alphabet = digits + ascii_uppercase
s = open('files/24.txt').readline()

for x in alphabet[26:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №46982
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество групп из идущих подряд не менее 12 символов, которые
# начинаются и заканчиваются буквой E и не содержат других букв E
# (кроме первой и последней) и букв F.
'''
s = open('files/24.txt').readline()
s = s.replace('E', 'E E')
print(len([x for x in s.split() if 'F' not in x and len(x) >= 12]))
'''


# Тип 24 №45258
# Текстовый файл состоит из символов A, B и C.
# Определите максимальное количество идущих подряд пар символов AB или CB
# в прилагаемом файле.
# Искомая подпоследовательность должна состоять только из пар AB, или только
# из пар CB, или только из пар AB и CB
# в произвольном порядке следования этих пар.
'''
s = open('files/24.txt').readline()
s = s.replace('AB', '*').replace('CB', '+')

for x in 'ABC':
    s = s.replace(x, ' ')

print(max([len(x) for x in s.split()]))
print(len(max(s.split(), key=len)))

M = ['df', 'ert', 'errt', 'e', 'erw']
print(len(max(M, key=len)))  # 4 - 'errt'
'''


# Тип 24 №68257
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальную длину непрерывного фрагмента, который начинается и
# заканчивается одной и той же буквой из первой половины алфавита (от A до M)
# и не содержит эту букву внутри.
'''
# ABCDEFGHIJKLM
s = open('files/24.txt').readline()
maxi = 0
for x in 'ABCDEFGHIJKLM':
    s = s.replace(x, f'{x} {x}')
    lenght = max([len(x) for x in s.split()])
    if maxi < lenght:
        maxi = lenght
    s = s.replace(f'{x} {x}', x)
print(maxi)
'''


# Тип 24 №27699
# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(0, len(s)-2, 1):
    if s[i:i+3] in ('LDR', 'DRL', 'RLD'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)
'''
# Тип 24 №38958


# Тип 24 №38958
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых
# не более одной буквы A.
'''
s = open('files/24.txt').readline().split('A')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'A' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 863 (Уровень: Базовый)
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
'''


# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается не более 3 раз.

s = '*****T*****T******T*T********T***T****T*******T**'.split('T')
# ['*****', '*****', '******', '*', '********', '***', '****', '*******', '**']
# 20 *****T*****T******T*
# 23 *****T******T*T********
# 21 ******T*T********T***
# 19 *T********T***T****
# 25 ********T***T****T*******
# 19 ***T****T*******T**
'''
maxi = 0
for i in range(len(s)):
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Тип 24 №59702
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ Y встречается не более 150 раз.
'''
s = open('files/24.txt').readline().split('Y')
maxi = 0
for i in range(len(s)):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)
'''


# Определите минимальную подстроку, содержащую 3 символов Т
s = '********T*****T******T*T********T***T****T*******T*********'.split('T')
# ['*****', '*****', '******', '*', '********', '***', '****', '*******', '**']
# 16 T********T*****T
# 14 T*****T******T
# 10 T******T*T
# 12 T*T********T
# 14 T********T***T
# 10 T***T****T
# 14 T****T*******T
# 19 T*******T*********T
# 11 T*********T
'''
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)  # 10
'''


# Тип 24 №59792
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 100 символов Т
'''
s = open('files/24.txt').readline().split('T')
mini = 10**9
for i in range(len(s)-98):
    r = 'T' + 'T'.join(s[i:i+99]) + 'T'
    mini = min(mini, len(r))
print(mini)  # 1523
'''


# Крайний символ среза не учитывается
'''
s = '01234'
print(s[1:4])
print(s[1:8])


M = [0, 1, 2, 3, 4]
print(M[1:4])
print(M[1:8])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
