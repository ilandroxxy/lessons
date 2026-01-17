# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 5223 (Уровень: Базовый)
'''
c = 1
maxi = 0
k = ''
s = open('files/24.txt').readline()
for i in range(len(s) - 1):
    if s[i] + s[i + 1] != 'DD':
        c += 1
        k += s[i]
        if 'FE' in k:
            maxi = max(maxi, c)
    else:
        c = 1
        k = ''
print(maxi)
'''

'''
maxi = 0
k = '0'
s = open('files/24.txt').readline()
for i in range(len(s) - 1):
    if s[i] + s[i + 1] != 'DD':
        k += s[i]
        if 'FE' in k:
            maxi = max(maxi, len(k))
    else:
        k = '0'
print(maxi)
'''

# LLONDDDBKTIACOQFJYMTS
# LLOND DDBKTIACOQFJYMTS

# LLONDDDDBKTIACOQFJYMTS
# LLOND DD DBKTIACOQFJYMTS
'''
s = open('files/24.txt').readline()
while 'DD' in s:
    s = s.replace('DD', 'D D')

print([x for x in s.split() if 'FE' in x])
print(max([len(x) for x in s.split() if 'FE' in x]))
'''


# № 2426 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов 1, 2, 3, A, B, C.
# Определите максимальное количество идущих подряд цифр.
'''
c = 0
res = []
s = open('files/24.txt').readline()
for i in range(len(s)):
    if s[i] in '123':
        c += 1
    else:
        res.append(c)
        c = 0
print(max(res))


c = 0
maxi = 0
s = open('files/24.txt').readline()
for i in range(len(s)):
    if s[i] in '123':
        c += 1
        maxi = max(maxi, c)
    else:
        c = 0
print(max(res))


c = 0
maxi = 0
s = open('files/24.txt').readline()
for x in s:
    if x in '123':
        c += 1
        maxi = max(maxi, c)
    else:
        c = 0
print(max(res))

# Вариант 2
s = open('files/24.txt').readline()
s = s.replace('A', 'B').replace('B', 'C').replace('C', ' ')
print(max([len(x) for x in s.split()]))
'''



# КЕГЭ № 16388 ЕГКР 27.04.24 (Уровень: Базовый)
# Текстовый файл состоит из символов K, L, M и N.
# В прилагаемом файле определите максимальное количество символов
# в непрерывной подпоследовательности, состоящей из идущих подряд
# групп символов KLMN в указанном порядке, при этом в начале и
# в конце искомой последовательности группа символов KLMN может
# быть неполной.

# i 0123456789
#   KLMNKLMNKLMNKLMN
'''
c = 3
maxi = 0
s = open('files/24.txt').readline()
for i in range(len(s) - 3):
    if (s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'KLMN'
            or s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'MNKL'
            or s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'NKLM'
            or s[i] + s[i + 1] + s[i + 2] + s[i + 3] == 'LMNK'):
        c += 1
    else:
        maxi = max(maxi, c)
        c = 3
print(maxi)

c = 3
maxi = 0
s = open('files/24.txt').readline()
for i in range(len(s) - 3):
    if s[i:i + 4] in ('KLMN', 'MNKL', 'NKLM', 'LMNK'):
        c += 1
    else:
        maxi = max(maxi, c)
        c = 3
print(maxi)
'''


'''
s = open('files/24.txt').readline()
s = s.replace('KLMN', '****')
for x in 'KLMN':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

# todo почему не хватает элементов
'''
from re import *
s = open('files/24.txt').readline()
print([x.group(0) for x in finditer('(N|MN|LMN)(KLMN)+(K|KL|KLM)', s)])
print(max([len(x.group(0)) for x in finditer('(N|MN|LMN)(KLMN)+(K|KL|KLM)', s)]))
'''


# № 13939 (Уровень: Средний)
# (Д. Бахтиев) Текстовый файл состоит из цифр 0, 1, 2, 3, 4
# и букв A, B, C, D, E.
# Определите в прилагаемом файле количество подстрок, которые
# могут представлять запись натурального числа в троичной системе
# счисления без незначащих нулей.
'''
s = open('files/24.txt').readline()
s = '444400122104444'
for x in 'ABCDE34':
    s = s.replace(x, ' ')

R = []
for x in s.split():
    while len(x) > 0 and x[0] == '0':
        if x[0] == '0':
            x = x[1:]
    R.append(len(x))
print(max(R))
'''


# № 10724 (Уровень: Базовый)
# Определите в прилагаемом файле максимальное количество
# идущих подряд символов, которые могут представлять запись
# числа в шестнадцатеричной системе счисления.
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('files/24.txt').readline()
for x in alp[16:]:
    s = s.replace(x, ' ')

R = []
for x in s.split():
    while len(x) > 0 and x[0] == '0':
        if x[0] == '0':
            x = x[1:]
    R.append(len(x))
print(max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке:
