# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 14642 Открытый курс "Слово пацана" (Уровень: Базовый)
# (М. Попков) Файл с текстом состоит не более чем из 106 символов D, E, F.
# Определите максимальное количество идущих подряд символов, среди которых
# символ F встречается не более одного раза.

s = 'xxxxxxFxxxxxxFxxxxxxxFxxxxxxxx'
# ['xxxxxx', 'xxxxxx', 'xxxxxxx', 'xxxxxxxx']
# 13 xxxxxxFxxxxxx
# 14 xxxxxxFxxxxxxx
# 16 xxxxxxxFxxxxxxxx
'''
s = open('files/24.txt').readline()
s = s.split('F')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'F' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)  # 45
'''

# № 13085 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов,
# среди которых ровно по одному разу встречаются буквы X и Y.

# aaaaaX aaaaaY aaaaaY
# aaaaaXaaaaaYaaaaaY
# aaaaaXaaaaaYaaaaa
'''
s = open('files/24.txt').readline()
s = s.replace('X', 'X ').replace('Y', 'Y ')
s = s.split()
maxi = 0
for i in range(len(s)-2):
    r = s[i] + s[i+1] + s[i+2][:-1]
    if r.count('X') == 1 and r.count('Y') == 1:
        maxi = max(maxi, len(r))
print(maxi)
'''


# № 13100 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов,
# среди которых каждая из букв C и D встречается не более двух раз.

# xxxxxC xxxxxD xxxxxC xxxxxD xxxxxD
# xxxxxCxxxxxDxxxxxCxxxxxDxxxxx
'''
s = open('files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    # r = s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4][:-1]
    r = ''.join(s[i:i+5])[:-1]
    if r.count('D') == 2 and r.count('C') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 3 раз.
'''
s = 'xxxxxTxxTxxxxTxxxxxxxxxxTxxxxTxxxxxxTxxx'
# ['xxxxx', 'xx', 'xxxx', 'xxxxxxxxxx', 'xxxx', 'xxxxxx', 'xxx']

# 24 xxxxxTxxTxxxxTxxxxxxxxxx
# 23 xxTxxxxTxxxxxxxxxxTxxxx
# 27 xxxxTxxxxxxxxxxTxxxxTxxxxxx
# 26 xxxxxxxxxxTxxxxTxxxxxxTxxx

s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    # print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''


# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 5 раз.
'''
s = 'xxxxxTxxTxxxxTxxxxxxxxxxTxxxxTxxxxxxTxxx'
# ['xxxxx', 'xx', 'xxxx', 'xxxxxxxxxx', 'xxxx', 'xxxxxx', 'xxx']

# 36 xxxxxTxxTxxxxTxxxxxxxxxxTxxxxTxxxxxx
# 34 xxTxxxxTxxxxxxxxxxTxxxxTxxxxxxTxxx

s = s.split('T')
maxi = 0
for i in range(len(s)-5):
    r = 'T'.join(s[i:i+6])
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 20909 Апробация 05.03.25 (Уровень: Средний)
# Текстовый файл состоит из заглавных букв латинского алфавита A, B, C, D, E и F.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых пара AB (в указанном порядке) встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
s = s.split('AB')
maxi = 0
for i in range(len(s)-100):
    r = 'B' + 'AB'.join(s[i:i+101]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)
'''
# ABxxxABxxxABxxxABxxxxAB
#  BxxxABxxxABxxxABxxxxA


# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в прилагаемом файле максимальное
# количество идущих подряд символов,
# среди которых подстрока FSRQ встречается ровно 80 раз.
'''
s = open('files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''


# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди
# которых символ T встречается ровно 3 раз.

s = 'xxxxxTxxTxxxxTxxxxxxxxxxTxxxxTxxxxxxTxxx'
# ['xxxxx', 'xx', 'xxxx', 'xxxxxxxxxx', 'xxxx', 'xxxxxx', 'xxx']

# 9 TxxTxxxxT
# 17 TxxxxTxxxxxxxxxxT
# 17 TxxxxxxxxxxTxxxxT
# 13 TxxxxTxxxxxxT
'''
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)
'''


# № 11954 (Уровень: Средний)
# (PRO100 ЕГЭ) Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ X встречается не менее 500 раз, а символ Y не встречается совсем.
'''
s = open('files/24.txt').readline()
s = s.split('X')
mini = 10**9
for i in range(len(s)-498):
    r = 'X' + 'X'.join(s[i:i+499]) + 'X'
    if 'Y' not in r:
        mini = min(mini, len(r))
print(mini)
'''

s = open('files/24.txt').readline()
s = s.split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: 10, 12, 24, 26
