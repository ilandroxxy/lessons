# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 12254 ЕГКР 16.12.23 (Уровень: Базовый)
'''
from re import *

s = open('0. files/24.txt').readline()
reg = rf'([Q]|(SQ))(RSQ)*([R]|(RS))'
reg = rf'(?=({reg}))'

M = [x.group(1) for x in finditer(reg, s)]

maxi = 0
for x in M:
    print(x)
    maxi = max(len(x), maxi)
print(maxi)


s = open('0. files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(0, len(s)-2, 1):
    if s[i:i+3] in ('RSQ', 'SQR', 'QRS'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)
'''


'''
s = 'TxxxxTxxxTxxxxxxxTxxxxTxxxxxxTxxxxTxxxxxxxTxxxTxxxxxxT'
# ['', 'xxxx', 'xxx', 'xxxxxxx', 'xxxx', 'xxxxxx', 'xxxx', 'xxxxxxx', 'xxx', 'xxxxxx', '']
# 17 TxxxxTxxxTxxxxxxx
# 21 xxxxTxxxTxxxxxxxTxxxx
# 23 xxxTxxxxxxxTxxxxTxxxxxx
# 24 xxxxxxxTxxxxTxxxxxxTxxxx
# 24 xxxxTxxxxxxTxxxxTxxxxxxx
# 23 xxxxxxTxxxxTxxxxxxxTxxx
# 23 xxxxTxxxxxxxTxxxTxxxxxx
# 19 xxxxxxxTxxxTxxxxxxT

# Максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''

s = 'TxxxxTxxxTxxxxxxxTxxxxTxxxxxxTxxxxTxxxxxxxTxxxTxxxxxxT'
# 7 TTxxxxT
# 10 TxxxxTxxxT
# 13 TxxxTxxxxxxxT
# 14 TxxxxxxxTxxxxT
# 13 TxxxxTxxxxxxT
# 13 TxxxxxxTxxxxT
# 14 TxxxxTxxxxxxxT
# 13 TxxxxxxxTxxxT
# 12 TxxxTxxxxxxT
# 9 TxxxxxxTT

# Минимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.

s = s.split('T')
mini = 9999
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
print(mini)




# № 10105 Демоверсия 2024 (Уровень: Средний)
# Максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 100 раз.



'''
s = open('0. files/24.txt').readline()
s = s.split('X')
mini = 99999
for i in range(len(s)-498):
    r = 'X' + 'X'.join(s[i:i+499]) + 'X'
    if 'Y' not in r:
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
# КЕГЭ = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Стас 9/29 -> 48 вторичных баллов +[2, 3-5, 7, 10, 12, 16, 22] -[1, 6, 8, 9, 11, 13, 14, 15, 17-21, 24-25]

# Второй пробник 28.02.25:
# Стас 18/29 -> 72 вторичных баллов +[1-5, 7, 8, 10, 11, 13-16, 18-21, 23] -[6, 9, 12, 17, 22, 24, 25]
