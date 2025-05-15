# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 20808 Апробация 05.03.25 (Уровень: Средний)
'''
alp = '0123456'
def f(n, b):
    res = ''
    while n > 0:
        res += alp[n % b]
        n //= b
    return res[::-1]


R = []
for x in range(1, 2030):
    n = 7 ** 170 + 7 ** 100 - x
    s = f(n, 7)
    R.append([s.count('0'), x])
    if s.count('0') == 73:
        print(s.count('0'), x)
print(max(R))  # [73, 1715]
'''


# № 17558 Основная волна 08.06.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
otrich = [x for x in M if x < 0]
S = [x for x in M if abs(x) % 32 == 0]
R = []
for i in range(len(M) - 1):
    a, b = M[i], M[i + 1]
    if (a in otrich) + (b in otrich) >= 1:
        if (a + b) < len(S):
            R.append(a + b)
print(len(R), max(R))
'''

# № 20896 Апробация 05.03.25 (Уровень: Базовый)
'''
R = []
for n in range(0, 1000):
    s = f'{n:b}'
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if r > 19:
        R.append(n)
print(min(R))
'''


'''
from itertools import *
cnt = 0
for s in product('012345678', repeat=5):
    sl = ''.join(s)
    if sl[0] != '0':
        for a in '1357':
            sl = sl.replace(a, '*')
        if sl.count('0') == 1 and '*0' not in sl and '0*' not in sl:
            cnt += 1
print(cnt)
'''


# № 18445 Сергей Горбачев
'''
from ipaddress import *
net = ip_network('140.116.194.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b[:8][-1] == '0':
        if b[8:16][-1] == '0':
            if b[16:24][-1] == '0':
                if b[24:][-1] == '0':
                    print(ip, b, b[:8], b[8:16], b[16:24], b[24:])
                    cnt += 1
print(cnt)
'''

# № 18450 Сергей Горбачев
'''
def F(a, b):
    if a > max(b) or a == 23:
        return 0
    if a in b:
        return 1
    else:
        return F(a+3, b) + F(a+4, b) + F(a*2, b)

print(F(11, [50, 51, 52, 53, 54]))
'''


# № 18318 Сергей Горбачев
'''
from fnmatch import *
cnt = 0
for x in range(111, 10**8, 111):
    if x % 2 == 0:
        if fnmatch(str(x), '3*4?5*6?'):
            cnt += 1
print(cnt)


from re import *
cnt = 0
for x in range(111, 10**8, 111):
    if x % 2 == 0:
        if fullmatch('3[0-9]*4[0-9]5[0-9]*6[0-9][13579]', str(x)):
            cnt += 1
print(cnt)
'''

# № 9553 Джобс 14.06.23 (Уровень: Базовый)
'''
from re import *
for x in range(13, 10**9, 13):
    if fullmatch('24[02468]*68[39]35', str(x)):
        print(x, x // 13)
'''
# 24268335 1866795
# 24868935 1912995
# 240068335 18466795
# 240668935 18512995
# 242668335 18666795
# 248468935 19112995


# № 18116 Сергей Горбачев
'''
cnt = 0
summa = 0
R = []
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    A = [x for x in M if x % 2 == 0 and M.count(x) == 3]
    B = [x for x in M if x % 2 != 0 and M.count(x) == 1]
    if len(A) == 3 and len(B) == 3:
        if sum(A) ** 2 > sum(B) ** 2:
            cnt += 1
            R.append(n)
            summa += n
print(f'Кол-во подходящих строк: {cnt}')
print(f'Наименьший номер строки: {min(R)}')
print(f'Наибольший номер строки: {max(R)}')
print(f'Сумма номеров: {summa}')


summa = 0
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    A = [x for x in M if x % 2 == 0 and M.count(x) == 3]
    B = [x for x in M if x % 2 != 0 and M.count(x) == 1]
    if len(A) == 3 and len(B) == 3:
        if sum(A) ** 2 > sum(B) ** 2:
            summa += n
print(summa)
'''


# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: ********************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = [5, 9, 14, 15, 16, 17, 22, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]

# Второй пробник 28.02.25:
# Александр 24/25 -> 88 вторичных баллов +[1-10, 12-25] -[11]
# Саша 10/25 -> 51 вторичных баллов +[1, 2, 4, 12, 14-16, 19, 23, 25] -[3, 5, 6-10, 11, 13, 17, 18, 20-22, 24]
