# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# максимальное количество идущих подряд символов,
# среди которых символ T встречается не более 3 раз.
# ['', 'xxxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxxx', 'xxxx', 'xxxxxx', 'xxxx', 'xxxx', 'xxxx', '']
# 16 TxxxxxTxxxTxxxxx
# 19 xxxxxTxxxTxxxxxTxxx
# 20 xxxTxxxxxTxxxTxxxxxx
# 21 xxxxxTxxxTxxxxxxTxxxx
# 22 xxxTxxxxxxTxxxxTxxxxxx
# 23 xxxxxxTxxxxTxxxxxxTxxxx
# 21 xxxxTxxxxxxTxxxxTxxxx
# 21 xxxxxxTxxxxTxxxxTxxxx
# 15 xxxxTxxxxTxxxxT
'''
s = 'TxxxxxTxxxTxxxxxTxxxTxxxxxxTxxxxTxxxxxxTxxxxTxxxxTxxxxT'
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    # print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 19717 (Уровень: Средний)
# Максимальное количество идущих подряд символов,
# среди которых символ M встречается не более 278 раз.
'''
s = open('0. files/24.txt').readline()
s = s.split('M')
maxi = 0
for i in range(len(s)-278):
    r = 'M'.join(s[i:i+279])
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


# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
'''
s = open('24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''


# https://education.yandex.ru/ege/task/764352cd-1971-4c8f-ac18-f74a63b9e5f2
'''
s = open('24.txt').readline()
for p in 'CDF':
    s = s.replace(p, 'B')
s = s.replace('O', 'A')
s = s.split('BA')

maxi = 0
for i in range(len(s)-5):
    r = 'B' + 'BA'.join(s[i:i+6]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)
'''

# Минимальное количество идущих подряд символов,
# среди которых символ T встречается не более 3 раз.
# ['', 'xxxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxxx', 'xxxx', 'xxxxxx', 'xxxx', 'xxxx', 'xxxx', '']
# 8 TTxxxxxT
# 11 TxxxxxTxxxT
# 11 TxxxTxxxxxT
# 11 TxxxxxTxxxT
# 12 TxxxTxxxxxxT
# 13 TxxxxxxTxxxxT
# 13 TxxxxTxxxxxxT
# 13 TxxxxxxTxxxxT
# 11 TxxxxTxxxxT
# 11 TxxxxTxxxxT
# 7 TxxxxTT
'''
s = 'TxxxxxTxxxTxxxxxTxxxTxxxxxxTxxxxTxxxxxxTxxxxTxxxxTxxxxT'
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)
'''

# Задача из пробника номер 2
# Минимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 210 раз.
'''
s = open('0. files/24.txt').readline()
s = s.split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [8, 14, 15, 23]
# на следующем уроке:

# Первый пробник 21.12.24:
# 24/25 -> 88 вторичных баллов +[1, 3-25] -[2]

# Второй пробник 10.02.25:
# 23/25 -> 86 вторичных баллов +[1-9, 11-23, 25] -[10, 24]
