# region Домашка: ******************************************************************
from http.cookiejar import join_header_words

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Минимальное количество идущих подряд символов,
# среди которых символ M встречается не более 3 раз.

# 7 MMxxxxM
# 10 MxxxxMxxxM
# 12 MxxxMxxxxxxM
# 12 MxxxxxxMxxxM
# 13 MxxxMxxxxxxxM
# 15 MxxxxxxxMxxxxxM
# 15 MxxxxxMxxxxxxxM
# 15 MxxxxxxxMxxxxxM
# 14 MxxxxxMxxxxxxM
# 9 MxxxxxxMM
'''
s = 'MxxxxMxxxMxxxxxxMxxxMxxxxxxxMxxxxxMxxxxxxxMxxxxxMxxxxxxM'
s = s.split('M')
mini = 10**9
for i in range(len(s)-1):
    r = 'M' + 'M'.join(s[i:i+2]) + 'M'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)
'''

# Максимальное количество идущих подряд символов,
# среди которых символ M встречается не более 3 раз.

# MxxxxMxxxMxxxxxx 16
# xxxxMxxxMxxxxxxMxxx 19
# xxxMxxxxxxMxxxMxxxxxxx 22
# xxxxxxMxxxMxxxxxxxMxxxxx 24
# xxxMxxxxxxxMxxxxxMxxxxxxx 25
# xxxxxxxMxxxxxMxxxxxxxMxxxxx 27
# xxxxxMxxxxxxxMxxxxxMxxxxxx 26
# xxxxxxxMxxxxxMxxxxxxM 21
'''
s = 'MxxxxMxxxMxxxxxxMxxxMxxxxxxxMxxxxxMxxxxxxxMxxxxxMxxxxxxM'
s = s.split('M')
maxi = 0
for i in range(len(s)-3):
    r = 'M'.join(s[i:i+4])
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 19717 (Уровень: Средний)
# (М. Попков) Текстовый файл состоит из символов A, E, G, I, L, M и R.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ M встречается не более 278 раз.
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


# № 17535 Основная волна 07.06.24 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.split('CD')
maxi = 0
for i in range(len(s)-160):
    r = 'D' + 'CD'.join(s[i:i+161]) + 'C'
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 11954 (Уровень: Средний)
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
                    cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ = []
# на следующем уроке: регулярные выражения, 26, 27


# Первый пробник 21.12.24:
# Лиза 11/29 -> 54 вторичных баллов +[1-2, 4, 5, 10, 12-14, 16, 23, 25] -[3, 6, 8]

# Второй пробник 28.02.25:
# Лиза 17/29 -> 70 вторичных баллов +[1-17, 23, 25] -[]
