# region Домашка: ******************************************************************

# № 11954 (Уровень: Средний) 🌶
'''
s = open('0. files/24.txt').readline()
s = s.split('X')
mini = 10**9
for i in range(len(s)-498):
    r = 'X' + 'X'.join(s[i:i+499]) + 'X'
    if 'Y' not in r:
        mini = min(mini, len(r))
print(mini)
'''


# № 8475 (Уровень: Средний)
'''
s = [int(x) for x in open('0. files/17.txt')]
f = [x for x in s if len(str(abs(x))) == 3 and abs(x) % 10 == 8]
R = []
for i in range(len(s) - 2):
    a, b, c = s[i:i + 3]
    v = [x for x in (a, b, c) if x ** 2 > min(f) ** 2]
    w = [x for x in (a, b, c) if len(str(abs(x))) == 3]
    if len(v) == 2 and len(w) >= 1:
        R.append(a + b + c)
print(len(R), max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 6757 Апробация 10.03.23 (Уровень: Базовый)
'''
s = open('0. files/24.txt').readline()
s = s.replace('CFE', '*').replace('FCE', '*')
for x in 'CDEF':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# № 7012 (Уровень: Средний)
'''
f = open('0. files/24.txt').readlines()
cnt = 0
for s in f:
    for x in 'UIOPASDFGHJKLZXCVBNM0123456789':
        s = s.replace(x, '')
    flag = ''
    bflag = 'QWERTY'
    for i in range(len(s)):
        if flag == 'QWERTY':
            cnt += 1
            break
        if s[i] == bflag[0]:
            flag += s[i]
            bflag = bflag[1:]

print(cnt)
'''


# № 9791 Основная волна 20.06.23 (Уровень: Средний)
'''
from string import *
alphabet = digits + ascii_uppercase
s = open('0. files/24.txt').readline()
for x in alphabet[16:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# № 12476 PRO100 ЕГЭ 29.12.23 (Уровень: Сложный)
'''
s = open('0. files/24.txt').readline()
s = s.split('RO')
maxi = 0
for i in range(len(s)-21):
    r = 'O' + 'RO'.join(s[i:i+22]) + 'R'
    if 'ROR' in r or 'ORO' in r:
        r = r.replace('ROR', 'RO OR')
        r = r.replace('ORO', 'OR RO')
        maxi = max(maxi, max([len(x) for x in r.split()]))
print(maxi)
'''

'''
s = open('files/24_9753.txt').readline()
s = s.split('Y')
maxi = 0
for i in range(len(s) - 150):
    d = 'Y'.join(s[i:i + 151])
    maxi = max(maxi, len(d))
print(maxi)
'''


# № 18029 (Уровень: Базовый)
'''
s = open('0. files/24.txt').readline()
s = s.replace('X', 'X X').split()
maxi_y = 0
R = []
for x in s:
    if maxi_y <= x.count('Y'):
        maxi_y = x.count('Y')
        R.append([maxi_y, len(x)])
for elem in R:
    print(elem)
'''


# № 14512 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.replace('1', '1 1').replace('8', '8 8')
maxi = 0
for x in s.split():
    if x.count('1') == 1:
        if x.count('B') == x.count('C'):
            maxi = max(maxi, len(x))
print(maxi)
# print(max([len(x) for x in s.split() if x.count('1') == 1 and x.count('B') == x.count('C')]))
'''


# № 14513 (Уровень: Базовый)
'''
from string import *
maxi = 0
s = open('0. files/24.txt').readline()
for x in digits:
    s = s.replace(x, '&')
for x in ascii_uppercase:
    s = s.replace(x, '#')
s = s.replace('&#', '& #')
s = s.split()
for i in range(len(s)-1):
    r = ''.join(s[i:i+2])

    while r[-1] == '&':
        r = r[:-1]
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 19719 (Уровень: Базовый)
'''
s = open('0. files/24.txt').readline()
while any(p in s for p in ('**', '--', '-*', '*-')):
    for x in ('**', '--', '-*', '*-'):
        s = s.replace(x, ' ')


maxi = 0
s = s.split()
for x in s:
    try:
        eval(x)  # эта функция считает арифметическое действие от строки
        maxi = max(maxi, len(x))
    except Exception as e:
        continue
print(maxi)
'''


# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************



# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
