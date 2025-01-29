
# Определите максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.


s = 'xxxxxxTxxxTxxxxxTxxxTxxxxxxTxxTxxxxxxxTxxxxxxxxxxTxxxTxxxx'
# ['xxxxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxxx', 'xx', 'xxxxxxx', 'xxxxxxxxxx', 'xxx', 'xxxx']
# 20 xxxxxxTxxxTxxxxxTxxx
# 20 xxxTxxxxxTxxxTxxxxxx
# 19 xxxxxTxxxTxxxxxxTxx
# 21 xxxTxxxxxxTxxTxxxxxxx
# 28 xxxxxxTxxTxxxxxxxTxxxxxxxxxx
# 25 xxTxxxxxxxTxxxxxxxxxxTxxx
# 27 xxxxxxxTxxxxxxxxxxTxxxTxxxx
'''
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
# Определите максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 133


# № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
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
# Ответ: 2379


# Определите минимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.


s = 'xxxxxxTxxxTxxxxxTxxxTxxxxxxTxxTxxxxxxxTxxxxxxxxxxTxxxTxxxxxxxx'
# ['xxxxxx', 'xxx', 'xxxxx', 'xxx', 'xxxxxx', 'xx', 'xxxxxxx', 'xxxxxxxxxx', 'xxx', 'xxxx']
# 20 xxxxxxTxxxTxxxxxTxxx
# 20 xxxTxxxxxTxxxTxxxxxx
# 19 xxxxxTxxxTxxxxxxTxx
# 21 xxxTxxxxxxTxxTxxxxxxx
# 28 xxxxxxTxxTxxxxxxxTxxxxxxxxxx
# 25 xxTxxxxxxxTxxxxxxxxxxTxxx
# 27 xxxxxxxTxxxxxxxxxxTxxxTxxxx
'''
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''
# 5*, 8, 9, 13, 18, 19-21, 22, 24


# № 11954 (Уровень: Средний)
# Определите в прилагаемом файле минимальное количество идущих подряд символов,
# среди которых символ X встречается не менее 500 раз, а символ Y не встречается совсем.
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

# print(max(map(len, s)))
'''

