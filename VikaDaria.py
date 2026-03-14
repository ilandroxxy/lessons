# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 3, 6, 7, 10

# 25
'''
from fnmatch import *
for x in range(0, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2024)

from re import *
for x in range(0, 10**8, 2023):
    if fullmatch('2[0-9]*1[0-9]71', str(x)):
        print(x, x // 2024)
'''


# 17
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied2) == 4 and len(copied1) == 3:
        if sum(copied2) / 4 < sum(copied1) / 3:
            cnt += 1
print(cnt)
'''


s = 'xxxxTxxxxxxTxxxxTxxTTxxxxTxxxxxxxxxTxxxxTxxxxxx'



# Определите максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раз.
'''
s = 'xxxxTxxxxxxxxxTxxxxTxxxxxx'.split('T')
print(s)  # ['xxxx', 'xxxxxxxxx', 'xxxx', 'xxxxxx']
# r = 'T'.join(s[i:i+4])  # 'xxxxTxxxxxxxxxTxxxxTxxxxxx'
'''

s = 'xxxxTxxxxxxTxxxxTxxTTxxxxTxxxxxxxxxTxxxxTxxxxxx'
# xxxxTxxxxxxTxxxxTxx 19
# xxxxxxTxxxxTxxT 15
# xxxxTxxTTxxxx 13
# xxTTxxxxTxxxxxxxxx 18
# TxxxxTxxxxxxxxxTxxxx 20
# xxxxTxxxxxxxxxTxxxxTxxxxxx 26
'''
s = s.split('T')
maxi = 0
for i in range(len(s) - 3):
    r = 'T'.join(s[i:i + 4])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Определите минимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раз.
'''
s = 'TxxxxxxxxxTxxxxT'.split('T')
print(s)  # ['xxxxxxxxx', 'xxxx']
r = 'T' + 'T'.join(s[i:i+2]) + 'T'  # 'TxxxxxxxxxTxxxxT'
'''

s = 'xxxxTxxxxxxTxxxxTxxTTxxxxTxxxxxxxxxTxxxxTxxxxxx'
# TxxxxTxxxxxxT 13
# TxxxxxxTxxxxT 13
# TxxxxTxxT 9
# TxxTT 5
# TTxxxxT 7
# TxxxxTxxxxxxxxxT 16
# TxxxxxxxxxTxxxxT 16
# TxxxxTxxxxxxT 13
'''
s = s.split('T')
mini = 10**8
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i + 2]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''


# 24

# Текстовый файл содержит заглавные буквы латинского алфавита.
# Определите минимальное количество идущих подряд символов, среди которых символ T
# встречается ровно 210 раз.
'''
s = open('files/24.txt').readline()
s = s.split('T')
mini = 10**8
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i + 209]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 25]
# на следующем уроке:


# region 📖 Пробник (Вариант 2)

# Студент #Дарья сдал ответы на пробник, вот результаты:
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 4, 5, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27
# ⛔️ Неверно: 3, 6, 7, 10, 24, 26
# ❔ Без ответа: Нет
# Итог: 22/29 первичных балла ~ 83 вторичных


# Студент #Маша сдал ответы на пробник, вот результаты:
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 21, 23
# ⛔️ Неверно: 10, 18
# ❔ Без ответа: 9, 17, 22, 24, 25, 26, 27
# Итог: 18/29 первичных балла ~ 72 вторичных

# endregion 📖 Пробник (Вариант 2)

