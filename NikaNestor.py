# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/inf/task/2d8f6e0c-c37b-4caa-b0b1-6584a5d0261f
'''
s = open('files/24.txt').readline()
while 'AHAHA' in s:
    s = s.replace('AHAHA', 'AHAH HAHA')
print(max([len(x) for x in s.split()]))
'''


# № 10105 Демоверсия 2024 (Уровень: Средний)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
s = s.split('T')
R = []
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    R.append(len(r))
print(max(R))
'''


# № 27634 Апробация 04.03.26 (Уровень: Базовый)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ Z встречается
# не менее 270 раз.
# Для выполнения этого задания следует написать. программу.
'''
s = open('files/24.txt').readline()
s = s.split('Z')
R = []
for i in range(len(s) - 268):
    r = 'Z' + 'Z'.join(s[i:i + 269]) + 'Z'
    R.append(len(r))
print(min(R))
'''

# № 17535 Основная волна 07.06.24 (Уровень: Средний)
# Текстовый файл состоит из символов A, B, C, D, E и F.
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых пара символов CD (в указанном порядке) встречается ровно 160 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('files/24.txt').readline()
s = s.split('CD')
R = []
for i in range(len(s)-160):
    r = 'D' + 'CD'.join(s[i:i+161]) + 'C'
    R.append(len(r))
print(max(R))


s = open('files/24.txt').readline()
s = s.split('XYZ')
R = []
for i in range(len(s)-160):
    r = 'YZ' + 'XYZ'.join(s[i:i+161]) + 'XY'
    R.append(len(r))
print(max(R))
'''


# https://education.yandex.ru/ege/inf/task/cee8176e-48b3-474f-b2ab-b410f608fa1a
'''
s = open('files/24.txt').readline()
s = s.replace('A', '*').replace('E', '*')
s = s.replace('B','+').replace('C','+').replace('D','+').replace('F','+')

s = s.split('*+')
print(s)
R = []
for i in range(len(s)-130):
    r = '+' + ''.join(s[i:i+131]) + '*'
    R.append(len(r))
print(max(R))
'''
# 645



# https://education.yandex.ru/ege/inf/task/301251e4-f9f7-4529-bbe2-446b0af1f949
'''
s = open('files/24.txt').readline()
s = s.replace('IT', '**').replace('TI', '**')
while '**' in s:
    s = s.replace('**', '* *')
m = [len(x) for x in s.split()]
print(max(m))
'''


# https://education.yandex.ru/ege/inf/task/4a723df3-ea35-4f64-bba3-afda2c8fb879
'''
from re import *
s = open('files/24.txt').readline()
pat = '[X]+|[Y]+|[Z]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''

# https://education.yandex.ru/ege/inf/task/543670ff-52fb-4d26-86f8-c82350ecb28b
'''
from re import *
s = open('files/24.txt').readline()
pat =  '((TXA)|(XA)|(XY))+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''

# https://education.yandex.ru/ege/inf/task/c215672a-d640-4947-a64f-85ea70c69346
'''
from re import *
s = open('files/24.txt').readline()
pat =  '[1-9][0-9]*[02468]'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([int(x) for x in M]))
'''


# https://education.yandex.ru/ege/inf/task/98ae80c8-1e05-4cad-b4cc-4adc1edcc487
'''
from re import *
s = open('files/24.txt').readline()
pat =  '((QRP)|(RP)|(P))(SQRP)+((SQR)|(SQ)|(S))'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [23]
# на следующем уроке: посмотреть 16 номера на лркуэш в какую сторону перебор и 15 номера ака ЕГКР
# С нуля 24 номера


# region Пробник 2

# Вероника
# Пробник №2
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17,
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных


# Нестор
# Пробник №2
# Дата: #Воскресенье #01Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных

# endregion Пробник 2
