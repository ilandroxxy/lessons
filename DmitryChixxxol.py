# region Домашка: ******************************************************************
from traceback import print_tb

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# 14642
'''
s = open('0. files/24.txt').readline()
s = s.split('F')
maxi = 0
for i in range(len(s)-1):
    r = 'F'.join(s[i:i+2])
    maxi = max(maxi, len(r))
print(maxi)
'''


# 2251
'''
s = open('0. files/24.txt').readline()
s = s.split('D')
maxi = 0
for i in range(len(s)-2):
    r = 'D'.join(s[i:i+3])
    maxi = max(maxi, len(r))
print(maxi)
'''

# 13100
'''
s = open('0. files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split(' ')
maxi = 0
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# Определите в прилагаемом файле максимальное количество идущих
# подряд символов, среди которых символ T встречается ровно 3 раз.
'''
s = 'TxxxxTxxxxTxxxxxxxTxxxTxxxxxTxxxxTxxxxxxxxxxxTxxxxxT'
# ['', 'xxxx', 'xxxx', 'xxxxxxx', 'xxx', 'xxxxx', 'xxxx', 'xxxxxxxxxxx', 'xxxxx', '']
# 18 TxxxxTxxxxTxxxxxxx
# 21 xxxxTxxxxTxxxxxxxTxxx
# 22 xxxxTxxxxxxxTxxxTxxxxx
# 22 xxxxxxxTxxxTxxxxxTxxxx
# 26 xxxTxxxxxTxxxxTxxxxxxxxxxx
# 28 xxxxxTxxxxTxxxxxxxxxxxTxxxxx
# 23 xxxxTxxxxxxxxxxxTxxxxxT

s = 'TxxxxTxxxxTxxxxxxxTxxxTxxxxxTxxxxTxxxxxxxxxxxTxxxxxT'
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''


# Определите в прилагаемом файле минимальное количество идущих
# подряд символов, среди которых символ T встречается ровно 3 раз.
'''
s = 'TxxxxTxxxxTxxxxxxxTxxxTxxxxxTxxxxTxxxxxxxxxxxTxxxxxT'
# 7 TTxxxxT
# 11 TxxxxTxxxxT
# 14 TxxxxTxxxxxxxT
# 13 TxxxxxxxTxxxT
# 11 TxxxTxxxxxT
# 12 TxxxxxTxxxxT
# 18 TxxxxTxxxxxxxxxxxT
# 19 TxxxxxxxxxxxTxxxxxT
# 8 TxxxxxTT
# ['', 'xxxx', 'xxxx', 'xxxxxxx', 'xxx', 'xxxxx', 'xxxx', 'xxxxxxxxxxx', 'xxxxx', '']
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''




# № 10105 Демоверсия 2024 (Уровень: Средний)
# Определите в прилагаемом файле максимальное количество идущих
# подряд символов, среди которых символ T встречается ровно 100 раз.
'''
s = open('0. files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 13715 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.split('AB')
maxi = 0
for i in range(len(s)-50):
    r = 'B' + 'AB'.join(s[i:i+51]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 21717 ЕГКР 19.04.25 (Уровень: Средний)

s = open('0. files/24.txt').readline()
s = s.split('RSQ')
mini = 10**9
for i in range(len(s)-128):
    r = 'RSQ' + 'RSQ'.join(s[i:i+129]) + 'RSQ'
    mini = min(mini, len(r))
print(mini)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.2, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]

# Второй пробник 28.02.25:
# Dmitry 13/16 -> 58 вторичных баллов +[1-5, 7, 8, 12, 14-16, 23, 25] -[6, 9, 13, 17]
