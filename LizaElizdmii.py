# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# Тип 24 №27687

# Вариант 1
'''
# s = 'xxxYYYYxxxYYYYYYxYYxxx'

s = open('0. files/24.txt').readline()
cnt = 1  # длина промежуточных последовательностей
maxi = 0  # длина самой большой последовательности
for i in range(len(s)-1):
    # if s[i] == 'Y' and s[i+1] == 'Y':
    if s[i:i+2] == 'YY':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''

# Вариант 2
'''
s = open('0. files/24.txt').readline()
s = s.replace('X', ' ').replace('Z', ' ')
print([x for x in s.split()])
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27421
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
'''
s = open('0. files/24.txt').readline()
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


# Тип 24 №27689
# Определите максимальную длину цепочки вида XYZXYZXY...
# (составленной из фрагментов XYZ,
# последний фрагмент может быть неполным).
'''
s = open('0. files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(len(s)-2):
    if s[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)
'''


# Тип 24 №58329
# Определите максимальное количество идущих подряд цифр,
# среди которых сумма двух
# идущих подряд цифр больше числа следующего за ними.
'''
s = open('0. files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(len(s)-2):
    if int(s[i]) + int(s[i+1]) > int(s[i+2]):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)
'''

# Тип 24 №58326
# Определите максимальное количество идущих подряд цифр,
# расположенных в строгом убывающем порядке.
'''
s = open('0. files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if int(s[i]) > int(s[i+1]):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''


# Тип 24 №37159
# Найдите максимальную длину подстроки,
# в которой символы a и d не стоят рядом.

# xxxxAAxxxxx
# xxxxA AxxxxxA
# xxxx  xxxxx
'''
s = open('0. files/24.txt').readline()
s = s.replace('ad', 'a d').replace('da', 'd a')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №48445
# Определите максимальное количество идущих подряд
# групп символов вида: A, C, D, F, O
# согласная + согласная + гласная
'''
s = open('0. files/24.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('DDA', '*')
s = s.replace('D', ' ').replace('A', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №55820
# Определите максимальное количество идущих подряд символов,
# среди которых символы Q, R, S в различных комбинациях
# (с учётом повторений) не стоят рядом.
'''
s = open('0. files/24.txt').readline()
s = s.replace('R', 'Q').replace('S', 'Q')
s = s.replace('QQ', 'Q Q')
print(max([len(x) for x in s.split()]))
'''



# Тип 24 №39253
# Определите максимальное количество идущих подряд символов,
# среди которых не более одной буквы D.

# ['YEKUWM', 'EKHABHHPE'] = 'YEKUWMDEKHABHHPE'
'''
s = open('0. files/24.txt').readline()
s = s.split('D')
maxi = 0
for i in range(len(s)-1):
    r = 'D'.join(s[i:i+2])
    maxi = max(maxi, len(r))
print(maxi)
'''


# Тип 24 №61370
'''
s = open('0. files/24.txt').readline()
s = s.replace('A', 'A ').replace('B', 'B ')
s = s.split()
maxi = 0
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]
    if r.count('A') == 1 and r.count('B') == 1:
        maxi = max(maxi, len(r))
print(maxi)
'''
# 'CWYB', 'OA', 'XTQVHDA' -> 'CWYBOAXTQVHDA'

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: 26, 27


# Первый пробник 21.12.24:
# Лиза 11/29 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

# Второй пробник 28.02.25:
# Лиза 17/29 -> 70 вторичных баллов +[1-17, 23, 25] -[]
