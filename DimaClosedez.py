# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
s = 'xxxxxxxFxxxxxFxxxxFxxxxxxxxxFxxxxxFxxxxxxxFxxxxxx'
# ['xxxxxxx', 'xxxxx', 'xxxx', 'xxxxxxxxx', 'xxxxx', 'xxxxxxx', 'xxxxxx']
# 13 xxxxxxxFxxxxx
# 10 xxxxxFxxxx
# 14 xxxxFxxxxxxxxx
# 15 xxxxxxxxxFxxxxx
# 13 xxxxxFxxxxxxx
# 14 xxxxxxxFxxxxxx
s = s.split('F')
maxi = 0
for i in range(len(s)-1):
    r = 'F'.join(s[i:i+2])  # i, i+1
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)  # 15
'''

# № 14642 Открытый курс "Слово пацана" (Уровень: Базовый)
# Определите максимальное количество идущих подряд символов,
# среди которых символ F встречается не более одного раза.
'''
s = open('files/24.txt').readline()
s = s.split('F')
maxi = 0
for i in range(len(s)-1):
    r = 'F'.join(s[i:i+2])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 45


# xxxxxxXxxxxxYxxxxxxFxxxxxx

# № 13085 (Уровень: Средний)
# Определите максимальное количество идущих подряд символов,
# среди которых ровно по одному разу встречаются буквы X и Y.
'''
s = open('files/24.txt').readline()
s = s.replace('X', 'X ').replace('Y', 'Y ')
s = s.split()
maxi = 0
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]  # i, i+1, i+2
    if r.count('X') == 1 and r.count('Y') == 1:
        maxi = max(maxi, len(r))
print(maxi)
'''


# № 13100 (Уровень: Средний)
# Определите максимальное количество идущих подряд символов,
# среди которых каждая из букв C и D встречается не более двух раз.
'''
s = open('files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]  # i, i+1, i+2, i+3, i+4
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# № 14643 Открытый курс "Слово пацана" (Уровень: Базовы
# Определите максимальное количество идущих
# подряд символов, среди которых нет подстроки AXMM.
'''
s = open('files/24.txt').readline()
s = s.replace('AXMM', 'AXM XMM')
print(max([len(x) for x in s.split()]))
'''
# xxxxxAXMMxxxxxxxxxxxAXMMxxxxxxx
# xxxxx  xxxxxxxxxxx xxxxxxx  # 11
# xxxxxAXM XMMxxxxxxxxxxxAXM XMMxxxxxxx


# максимальное количество идущих подряд символов среди
# которых символ T встречается ровно 3 раза
'''
s = 'xxxxTxxxxxTxxxTxxxxTxxxTxxxxxxxxTxxxTxxxxxxxxxTxxxxTxxxxx'
# ['xxxx', 'xxxxx', 'xxx', 'xxxx', 'xxx', 'xxxxxxxx', 'xxx', 'xxxxxxxxx', 'xxxx', 'xxxxx']
# 19 xxxxTxxxxxTxxxTxxxx
# 18 xxxxxTxxxTxxxxTxxx
# 21 xxxTxxxxTxxxTxxxxxxxx
# 21 xxxxTxxxTxxxxxxxxTxxx
# 26 xxxTxxxxxxxxTxxxTxxxxxxxxx
# 27 xxxxxxxxTxxxTxxxxxxxxxTxxxx
# 24 xxxTxxxxxxxxxTxxxxTxxxxx
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])  # i, i+1, i+2, i+3
    print(len(r), r)
    maxi = max(maxi, len(r))
print(maxi)  # 27
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
# максимальное количество идущих подряд символов среди
# которых символ T встречается ровно 100 раз
'''
s = open('files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])   # i, i+1, i+2, ..., i+100
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 13715 (Уровень: Средний)
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых комбинация символов AB встречается ровно 50 раз.
'''
s = open('files/24.txt').readline()
s = s.split('AB')
maxi = 0
for i in range(len(s)-50):
    r = 'A' + 'AB'.join(s[i:i+51]) + 'B'  # i, i+1, i+2, ..., i+50
    maxi = max(maxi, len(r))
print(maxi)  # 10126 -> 10128
'''

# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов, среди которых подстрока FSRQ встречается ровно 80 раз.
'''
s = open('files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)  # 2373 -> 2379
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25, 26.1]
# КЕГЭ  = []
# на следующем уроке:
