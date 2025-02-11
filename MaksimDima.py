# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Определите максимальное количество идущих подряд символов
# среди которых символ M встречается не более (ровно) 3 раз(а).

s = 'MxxxxMxxxxxMxxxMxxxxxxMxxxxMxxxxxxxMxxxxxMxxxxMxxxxxxM'
# ['', 'xxxx', 'xxxxx', 'xxx', 'xxxxxx', 'xxxx', 'xxxxxxx', 'xxxxx', 'xxxx', 'xxxxxx', '']
# 15 MxxxxMxxxxxMxxx
# 21 xxxxMxxxxxMxxxMxxxxxx
# 21 xxxxxMxxxMxxxxxxMxxxx
# 23 xxxMxxxxxxMxxxxMxxxxxxx
# 25 xxxxxxMxxxxMxxxxxxxMxxxxx
# 23 xxxxMxxxxxxxMxxxxxMxxxx
# 25 xxxxxxxMxxxxxMxxxxMxxxxxx
# 18 xxxxxMxxxxMxxxxxxM
'''
s = s.split('M')
maxi = 0
for i in range(len(s)-3):
    r = 'M'.join(s[i:i+4])
    # print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 19717 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.split('M')
maxi = 0
for i in range(len(s)-278):
    r = 'M'.join(s[i:i+279])
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых подстрока FSRQ встречается ровно 80 раз.
'''
s = open('0. files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''



# 17535 Основная волна 07.06.24 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.split('CD')
maxi = 0
for i in range(len(s)-160):
    r = 'D' + 'CD'.join(s[i:i+161]) + 'C'
    maxi = max(maxi, len(r))
print(maxi)
'''

'''
s = open('0. files/24.txt').readline()
s = s.split('CD')
maxi = 0
for i in range(len(s)-140):
    r = 'D' + 'CD'.join(s[i:i+141]) + 'C'
    maxi = max(maxi, len(r))
print(maxi)
'''


# Определите минимальную подстроку, содержащую 3 символа M.
'''
s = 'MxxxxMxxxxxMxxxMxxxxxxMxxxxMxxxxxxxMxxxxxMxxxxMxxxxxxM'
# ['', 'xxxx', 'xxxxx', 'xxx', 'xxxxxx', 'xxxx', 'xxxxxxx', 'xxxxx', 'xxxx', 'xxxxxx', '']
# 7 MMxxxxM
# 12 MxxxxMxxxxxM
# 11 MxxxxxMxxxM
# 12 MxxxMxxxxxxM
# 13 MxxxxxxMxxxxM
# 14 MxxxxMxxxxxxxM
# 15 MxxxxxxxMxxxxxM
# 12 MxxxxxMxxxxM
# 13 MxxxxMxxxxxxM
# 9 MxxxxxxMM
s = s.split('M')
mini = 10**9
for i in range(len(s)-1):
    r = 'M' + 'M'.join(s[i:i+2]) + 'M'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)
'''


# Определите минимальную подстроку, содержащую 100 символов Т.
'''
s = open('0. files/24.txt').readline()
s = s.split('T')
mini = 10**9
for i in range(len(s)-98):
    r = 'T' + 'T'.join(s[i:i+99]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''


# Тип 24 №39253
# Определите максимальное количество идущих подряд символов,
# среди которых не более одной буквы D.
'''
s = open('0. files/24.txt').readline()
s = s.split('D')
maxi = 0
for i in range(len(s)-1):
    r = 'D'.join(s[i:i+2])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Тип 24 №63073
# Определите максимальное количество идущих подряд символов,
# среди которых каждая из букв C и D встречается не более двух раз.
'''
s = open('0. files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''
# ['C', 'YC', 'HD', 'YEKUWMD', 'EKHABHHPED']


# № 19970 (Уровень: Сложный)

s = open('0. files/24.txt').readline()
for x in '++ ** +* *+'.split():
    s = s.replace(x, ' ')
maxi = 0
for x in s.split():
    try:
        r = eval(x)
        if len(str(r)) > 1 and r % 5 == 0:
            if maxi < len(x):
                maxi = len(x)
                print(maxi, r, x)
    except:
        continue
print(maxi)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo разобрать задачку Тип 24 №59847
'''
s = open('0. files/24.txt').readline()
s = s.replace('WW', ' ')
s = s.split()
maxi = 0
for i in range(len(s)-100):
    r = 'W' + 'WW'.join(s[i:i+101]) + 'W'
    maxi = max(maxi, len(r))
print(maxi)
'''

from turtle import *
print(bk)

# зацепка может быть тут https://inf-ege.sdamgia.ru/problem?id=59729
# В строке TTTT пара символов встречается ровно 3 раза.

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]
