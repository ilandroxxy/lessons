# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 14642 Открытый курс "Слово пацана"(Уровень: Базовый)
# (М. Попков) Файл с текстом состоит не более чем из 10**6 символов D, E, F.
# Определите максимальное количество идущих подряд символов,
# среди которых символ F встречается не более одного раза.
'''
s = open('files/24.txt').readline()
s = s.split('F')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'F' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)
'''

'''
s = 'xxxxxxxxFxxxxxxxxFxxxxxxxxxxxxxxxFxxxxxxxxx'
maxi = 0
s = s.split('F')
for i in range(len(s)-1):
    r = s[i] + 'F' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)  # 25

# ['xxxxxxxx', 'xxxxxxxx', 'xxxxxxxxxxxxxxx', 'xxxxxxxxx']
# 17 xxxxxxxxFxxxxxxxx
# 24 xxxxxxxxFxxxxxxxxxxxxxxx
# 25 xxxxxxxxxxxxxxxFxxxxxxxxx
'''


# № 2251 (Уровень: Базовый)
# Текстовый файл содержит только заглавные буквы
# латинского алфавита(ABC…Z). Определите максимальное
# количество идущих подряд символов, среди которых
# не более двух букв D.
'''
s = open('files/24.txt').readline()
s = s.split('D')
maxi = 0
for i in range(len(s)-2):
    # r = s[i] + 'D' + s[i+1] + 'D' + s[i+2]
    r = 'D'.join(s[i:i+3])
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 13085 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых
# ровно по одному разу встречаются буквы X и Y.
'''
s = open('files/24.txt').readline()
s = s.replace('Y', 'Y ').replace('X', 'X ')
s = s.split()
maxi = 0
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]
    if r.count('X') == 1 and r.count('Y') == 1:
        maxi = max(maxi, len(r))
print(maxi)
'''


# 'BNPY', 'KBJBUY', 'QNIY', 'HHX', 'ELENZFPCRX'
# BNPYKBJBUYQNI Y
# KBJBUYQNIYHH X
# QNIYHHXELENZFPCR X


# № 13100 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых
# каждая из букв C и D встречается не более двух раз.
'''
s = open('files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# № 27634 Апробация 04.03.26(Уровень: Базовый)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих
# подряд символов (длину непрерывной подпоследовательности),
# среди которых символ Z встречается не менее 270 раз.
# Для выполнения этого задания следует написать. программу.
'''
s = open('files/24.txt').readline()
mini = 10**9
s = s.split('Z')
for i in range(len(s)-268):
    r = 'Z' + 'Z'.join(s[i:i+269]) + 'Z'
    mini = min(mini, len(r))
print(mini)  # 1058
'''


# № 21717 ЕГКР 19.04.25(Уровень: Средний)
# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в этом файле минимальное количество идущих подряд
# символов, среди которых подстрока RSQ встречается ровно 130 раз,
# при этом искомая последовательность не оканчивается символом Q.

s = open('files/24.txt').readline()
mini = 10**9
s = s.split('RSQ')
for i in range(len(s)-128):
    r = 'RSQ' + 'RSQ'.join(s[i:i+130]) + 'R'
    mini = min(mini, len(r))
print(mini)  # 497



# минимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.
'''
s = 'xxxxxTxxxTxxxxxxxxTxxTxxxxxTxxxxxxxxxxxxxxTxxxxxTxxTxxxx'
# ['xxxxx', 'xxx', 'xxxxxxxx', 'xx', 'xxxxx', 'xxxxxxxxxxxxxx', 'xxxxx', 'xx', 'xxxx']
mini = 10**9
s = s.split('T')
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
    print(len(r), r)

    # 14 TxxxTxxxxxxxxT
    # 13 TxxxxxxxxTxxT
    # 10 TxxTxxxxxT
    # 22 TxxxxxTxxxxxxxxxxxxxxT
    # 22 TxxxxxxxxxxxxxxTxxxxxT
    # 10 TxxxxxTxxT

print(mini)
'''

# максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 3 раза.
'''
s = 'xxxxxTxxxTxxxxxxxxTxxTxxxxxTxxxxxxxxxxxxxxTxxxxxTxxTxxxx'
# ['xxxxx', 'xxx', 'xxxxxxxx', 'xx', 'xxxxx', 'xxxxxxxxxxxxxx', 'xxxxx', 'xx', 'xxxx']
maxi = 0
s = s.split('T')
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
    print(len(r), r)
    # 21 xxxxxTxxxTxxxxxxxxTxx
    # 21 xxxTxxxxxxxxTxxTxxxxx
    # 32 xxxxxxxxTxxTxxxxxTxxxxxxxxxxxxxx
    # 29 xxTxxxxxTxxxxxxxxxxxxxxTxxxxx
    # 29 xxxxxTxxxxxxxxxxxxxxTxxxxxTxx
    # 28 xxxxxxxxxxxxxxTxxxxxTxxTxxxx
print(maxi)  # 32
'''

# максимальное количество идущих подряд символов,
# среди которых символ T встречается ровно 5 раза.
'''
s = 'xxxxxTxxxTxxxxxxxxTxxTxxxxxTxxxxxxxxxxxxxxTxxxxxTxxTxxxx'
maxi = 0
s = s.split('T')
for i in range(len(s)-5):
    r = 'T'.join(s[i:i+6])
    maxi = max(maxi, len(r))

print(maxi)  
'''


# № 10105 Демоверсия 2024(Уровень: Средний)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ T встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
maxi = 0
s = s.split('T')
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 13715 (Уровень: Средний)
# Текстовый файл состоит из символов A, B, C, D и E.
# Определите в прилагаемом файле максимальное количество идущих
# подряд символов, среди которых комбинация символов AB встречается ровно 50 раз.
'''
s = open('files/24.txt').readline()
maxi = 0
s = s.split('AB')
for i in range(len(s)-50):
    r = 'B' + 'AB'.join(s[i:i+51]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 20909 Апробация 05.03.25(Уровень: Средний)
# Текстовый файл состоит из заглавных букв латинского алфавита A, B, C, D, E и F.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов, среди которых пара AB (в указанном порядке) встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
maxi = 0
s = s.split('AB')
for i in range(len(s)-100):
    r = 'B' + 'AB'.join(s[i:i+101]) + 'A'
    maxi = max(maxi, len(r))
print(maxi)
'''

# № 19254 ЕГКР 21.12.24(Уровень: Базовый)
# Текстовый файл состоит из символов F, G, Q, R, S и W.
# Определите в прилагаемом файле максимальное количество идущих
# подряд символов, среди которых подстрока FSRQ встречается ровно 80 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('files/24.txt').readline()
maxi = 0
s = s.split('FSRQ')
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''


# № 23206 Основная волна 10.06.25(Уровень: Средний)
# Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
# Определите в прилагаемом файле последовательность из максимального количества
# идущих подряд символов, среди которых ровно 35 букв S, начинающуюся чётной цифрой,
# не содержащую других чётных цифр, кроме первой.

# todo Проверить задачку

s = open('files/24.txt').readline()
for x in '02468':
    s = s.replace(x, '*')
maxi = 0
s = s.split('S')
for i in range(len(s)-35):
    r = 'S'.join(s[i:i+36])

    if r.count('*') == 1 and r[0] == '*':
        print(len(r), r.count('S'), r.count('*'), r)
        maxi = max(maxi, len(r))
print(maxi)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# todo на следующем уроке:
