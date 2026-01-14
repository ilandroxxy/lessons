# region Домашка: ******************************************************************

# № 19157 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(6437, 10**10, 6437):
    if fnmatch(str(x), '1?3*5*954'):
        print(x)

from re import *
for x in range(6437, 10**10, 6437):
    if fullmatch('1[0-9]3[0-9]*5[0-9]*954', str(x)):
        print(x)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 24 №27691
# Определите максимальное количество идущих подряд символов A.
'''
# s = open('files/24.txt').readline()
# B C A C AA BBB AAAA BBBBB CC BB AA CCCCC

# Вариант 1: ctrl + F - (поиск по выводу)
s = open('files/24.txt').readline()
# print(s)
print(len('AAAAAAA'))


# Вариант 2
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] == 'A' and s[i+1] == 'A':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)


# Вариант 3
s = open('files/24.txt').readline()
s = s.replace('B', 'C').replace('C', ' ')
print(max([len(x) for x in s.split()]))


# Вариант 4
from re import *
s = open('files/24.txt').readline()
print([x.group(0) for x in finditer(r'[A]+', s)])
print(max([len(x.group(0)) for x in finditer(r'[A]+', s)]))
'''


# Тип 24 №27695
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
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


#  Определите максимальную длину цепочки вида **A   ABAB...
#  (составленной из фрагментов AB, последний фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if cnt == 1 and s[i:i+2] == 'BA':
        continue
    if s[i:i+2] in ('AB', 'BA'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''

'''
s = open('files/24.txt').readline()
s = s.replace('AB', '**').replace('**A', '**+')
s = s.replace('A', 'B').replace('B', 'C').replace('C', ' ')
s = s.replace('+*', '+ *')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27699
# Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(len(s)-1):
    if cnt == 1 and s[i:i+3] in ('DRL', 'RLD'):
        continue
    if s[i:i+3] in ('LDR', 'DRL', 'RLD'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)
'''


# Тип 24 №36037
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

# AAAAAAXZZYBBBBBBBBB
# AAAAAA    BBBBBBBBB
# AAAAAAXZZ    ZZYBBBBBBBBB
'''
s = open('files/24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №37159
# Найдите максимальную длину подстроки, в которой
# символы a и d не стоят рядом.
'''
s = open('files/24.txt').readline()
s = s.replace('ad', 'a d').replace('da', 'd a')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №79737
# Определите в этом файле последовательность идущих
# подряд символов, представляющих собой запись
# максимального чётного 14-ричного числа.
# В ответе запишите количество символов
# (значащих цифр в записи числа) в этой последовательности.

s = open('files/24.txt').readline()
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[14:]:
    s = s.replace(x, ' ')
print(max([[len(x), x] for x in s.split()]))


M = sorted([[len(x), x] for x in s.split()])
for x in M:
    print(*x)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке:
