
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 2419 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского алфавита A, B, C
# Найдите длину самой длинной подцепочки, состоящей из символов C
'''

# Вариант 1: ctrl + F
s = open('files/24.txt').readline()
print(s)
print(len('CCCCCCCCCCC'))  # 11


# Вариант 2: Через .replace() замену
s = open('files/24.txt').readline()
s = s.replace('B', 'A').replace('A', ' ')
print(max([len(x) for x in s.split()]))


# Вариант 3: Решение Ака 17 номер (пары/тройки/четверки)
s = open('files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(len(s)-1):
    if s[i] == 'C' and s[i+1] == 'C':
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)


# Вариант 4: Решение через import re

from re import *
s = open('files/24.txt').readline()
pat = '[C]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''


# № 1975 Демоверсия 2022 (Уровень: Базовый)
'''
s = open('files/24.txt').readline()
s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))


s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i:i+2] != 'PP':
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)
'''


# № 864 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Найдите длину самой длинной подцепочки, не содержащей гласных букв.
'''
s = open('files/24.txt').readline()
s = s.replace('A', 'E').replace('E', ' ')
print(max([len(x) for x in s.split()]))

from re import *
s = open('files/24.txt').readline()
pat = '[BCDF]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''

# № 1039 100 базовых задач Е. Джобс (Уровень: Базовый)
# В файле записана последовательность символов.
# Укажите длину самой длинной последовательности, состоящей из одинаковых символов.
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)


from re import *
s = open('files/24.txt').readline()
pat = '([a]+|[b]+|[c]+|[d]+|[e]+|[f]+|[g]+|[h]+)'  # ...
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''



# № 1302 Открытый вариант КЕГЭ (Уровень: Базовый)
'''
s = open('files/24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] != 'XZZY':
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 3
print(maxi)

s = open('files/24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
print(max([len(x) for x in s.split()]))
'''

# № 21 Демоверсия 2021 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)
'''


# № 2250 (Уровень: Базовый)
'''
from re import *
s = open('files/24.txt').readline()
pat = '[B-Z]+[A][B-Z]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))


s = open('files/24.txt').readline()
s = s.replace('A', 'A ').split()
maxi = 0
for i in range(len(s)-1):
    r  = ''.join(s[i:i+2])[:-1]
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 2251 (Уровень: Базовый)
# Текстовый файл содержит только заглавные буквы латинского алфавита(ABC…Z). Определите
# максимальное количество идущих подряд символов, среди которых не более двух букв D.
'''
s = open('files/24.txt').readline()
s = s.replace('D', 'D ').split()
maxi = 0
for i in range(len(s)-2):
    r  = ''.join(s[i:i+3])[:-1]
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 13100 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых каждая
# из букв C и D встречается не более двух раз.
'''
s = open('files/24.txt').readline()
s = s.replace('D', 'D ').replace('C', 'C ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    r  = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# № 10105 Демоверсия 2024 (Уровень: Средний)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ T встречается ровно 100 раз.
# Для выполнения этого задания следует написать программу.


s = open('files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)





# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [12, 13, 19-21, 24.1, 27]
# КЕГЭ = []
# на следующем уроке:

# Получаются: 1, 2, 3, 4, 6, 10, 11, 15, 17, 18, 23
# 50 / 50: 5, 7, 9, 16,
# Не получаются: 8, 14, 22, 25
# Не разбирали: 24, 26


# region 📖 Пробник (Вариант 2)

# Студент #Эллина
# Дата: #Понедельник #16Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17, 18, 22, 27
# ❔ Без ответа: 6, 14, 24, 26
# Итог: 20/29 первичных балла ~ 78 вторичных

# endregion 📖 Пробник (Вариант 2)



