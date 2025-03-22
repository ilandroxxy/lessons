# region Домашка: ******************************************************************
from runpy import run_path

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Определите максимальное количество идущих подряд символов,
# среди которых символ T встречается не более 3 раз.

s = 'TxxxxxxTxxxTxxxxxxTxxxxTxxxxxTxxxxTxxxxxTxxxxxT'
# ['', 'xxxxxx', 'xxx', 'xxxxxx', 'xxxx', 'xxxxx', 'xxxx', 'xxxxx', 'xxxxx', '']
# 18 TxxxxxxTxxxTxxxxxx
# 22 xxxxxxTxxxTxxxxxxTxxxx
# 21 xxxTxxxxxxTxxxxTxxxxx
# 22 xxxxxxTxxxxTxxxxxTxxxx
# 21 xxxxTxxxxxTxxxxTxxxxx
# 22 xxxxxTxxxxTxxxxxTxxxxx
# 17 xxxxTxxxxxTxxxxxT
'''
s = s.split('T')
maxi = 0
for i in range(len(s) - 3):
    r = 'T'.join(s[i:i+3+1])
    maxi = max(maxi, len(r))
print(maxi)
'''


s = 'TxxxxxxTxxxTxxxxxxTxxxxTxxxxxTxxxxTxxxxxTxxxxxT'
# Определите минимальное количество идущих подряд символов,
# среди которых символ T встречается не более 3 раз.
# 9 TTxxxxxxT
# 12 TxxxxxxTxxxT
# 12 TxxxTxxxxxxT
# 13 TxxxxxxTxxxxT
# 12 TxxxxTxxxxxT
# 12 TxxxxxTxxxxT
# 12 TxxxxTxxxxxT
# 13 TxxxxxTxxxxxT
# 8 TxxxxxTT
'''
mini = 10**9
s = s.split('T')
for i in range(len(s) - (3-2)):
    r = 'T' + 'T'.join(s[i:i+3-2+1]) + 'T'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)
'''

# № 9753 Основная волна 19.06.23 (Уровень: Сложный)
# Определите максимальное количество идущих подряд символов,
# среди которых символ Y встречается не более 150 раз.
'''
s = open('0. files/24.txt').readline()
s = s.split('Y')
maxi = 0
for i in range(len(s) - 150):
    r = 'Y'.join(s[i:i+150+1])
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 11954 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
mini = 10**9
s = s.split('X')
for i in range(len(s) - (500-2)):
    r = 'X' + 'X'.join(s[i:i+500-2+1]) + 'X'
    if 'Y' not in r:
        mini = min(mini, len(r))
print(mini)
'''

s = open('0. files/24.txt').readline()
s = s.split('T')
mini = 0
for i in range(len(s)- 100):
    r ='T'.join(s[i:i+100+1])
    mini = max(mini, len(r))
print(mini)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = []
# на следующем уроке: 14

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


