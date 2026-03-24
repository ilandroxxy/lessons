# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 2419 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского алфавита A, B, C длиной
# не более 106 символов. Найдите длину самой длинной подцепочки, состоящей из символов C
'''
s = open('files/24.txt').readline()
s = s.replace('B', 'A').replace('A', ' ')
print(max([len(x) for x in s.split()]))
'''

# № 1975 Демоверсия 2022 (Уровень: Базовый)
# Текстовый файл состоит из символов P, Q, R и S.
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых нет идущих подряд символов P.
'''
s = open('files/24.txt').readline()
s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))
'''


# № 2426 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов 1, 2, 3, A, B, C.
# Определите максимальное количество идущих подряд цифр.
'''
s = open('files/24.txt').readline()
for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

# № 2942 Апробация 19.02.2022 (Уровень: Базовый)
# Текстовый файл состоит из символов А, В и С.
# Определите максимальное количество идущих подряд пар символов АВ или АС в прилагаемом файле.
'''
s = open('files/24.txt').readline()
s = s.replace('AB', '*').replace('AC', '+')
for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

# № 1302 Открытый вариант КЕГЭ (Уровень: Базовый)
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
'''
s = open('files/24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
print(max([len(x) for x in s.split()]))
'''

# № 5237 (Уровень: Средний)
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов, среди которых
# нет символов Z, а остальные символы чередуются.
'''
s = open('files/24.txt').readline()
s = s.replace('Z', ' ')

for x in 'XYZ':
    while x*2 in s:
        s = s.replace(x*2, f'{x} {x}')
print(max([len(x) for x in s.split()]))
'''


# № 14642 Открытый курс "Слово пацана" (Уровень: Базовый)
# (М. Попков) Файл с текстом состоит не более чем из 106 символов D, E, F.
# Определите максимальное количество идущих подряд символов, среди которых
# символ F встречается не более одного раза.
'''
s = open('files/24.txt').readline()
s = s.replace('F', 'F ')
s = s.split()
R = []
for i in range(len(s)-1):
    r = ''.join(s[i:i+2])[:-1] 
    R.append(len(r))
print(max(R))
'''


# № 2251 (Уровень: Базовый)
# Текстовый файл содержит только заглавные буквы латинского алфавита(ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых не более двух букв D.
'''
s = open('files/24.txt').readline()
s = s.replace('D', 'D ')
s = s.split()
R = []
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]
    R.append(len(r))
print(max(R))
'''

'''
xxxxxD xxxxD xxxxxD xxxD xxxxxD xxD xxxxD 
# xxxxxDxxxxDxxxxx [D]
# xxxxDxxxxxDxxx [D]
# xxxxxDxxxDxxxxx [D]
# xxxxxDxxDxxxx [D]
'''


# № 13085 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых ровно
# по одному разу встречаются буквы X и Y.
'''
s = open('files/24.txt').readline()
s = s.replace('X', 'X ').replace('Y', 'Y ')
s = s.split()
R = []
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]
    if r.count('X') == 1 and r.count('Y') == 1:
        R.append(len(r))
print(max(R))
'''

# № 13100 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых каждая
# из букв C и D встречается не более двух раз.
'''
s = open('files/24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ')
s = s.split()
R = []
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        R.append(len(r))
print(max(R))
'''
# xxxxxCxxxxxCxxxxDxxxxDxxxxx


# Определите в прилагаемом файле максимальное количество идущих подряд
# символов, среди которых символ T встречается ровно 3 раз.

# s = open('files/24.txt').readline()
s = 'xxxxxTxxxxTxxxxxTxxxxxTxxxTxxxxxxxxxTxxxTxxxxxxxTxxxxxx'
# ['xxxxx', 'xxxx', 'xxxxx', 'xxxxx', 'xxx', 'xxxxxxxxx', 'xxx', 'xxxxxxx', 'xxxxxx']
# 22 xxxxxTxxxxTxxxxxTxxxxx
# 20 xxxxTxxxxxTxxxxxTxxx
# 25 xxxxxTxxxxxTxxxTxxxxxxxxx
# 23 xxxxxTxxxTxxxxxxxxxTxxx
# 25 xxxTxxxxxxxxxTxxxTxxxxxxx
# 28 xxxxxxxxxTxxxTxxxxxxxTxxxxxx
'''
s = s.split('T')
R = []
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    print(len(r), r)
    R.append(len(r))
print(max(R))
'''


# № 10105 Демоверсия 2024 (Уровень: Средний)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ T встречается ровно 100 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('files/24.txt').readline()
s = s.split('T')
R = []
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    R.append(len(r))
print(max(R))
'''

# № 13715 (Уровень: Средний)
# Текстовый файл состоит из символов A, B, C, D и E.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых комбинация символов AB встречается ровно 50 раз.
'''
s = open('files/24.txt').readline()
s = s.split('AB')
R = []
for i in range(len(s)-50):
    r = 'B' + 'AB'.join(s[i:i+51]) + 'A'
    R.append(len(r))
print(max(R))
'''
# A BxxxxABxxxxxABxxxxxABxxxA B


# Определите в прилагаемом файле МИНИМАЛЬНОЕ количество идущих подряд
# символов, среди которых символ T встречается ровно 3 раз.

# s = open('files/24.txt').readline()
s = 'xxxxxTxxxxTxxxxxTxxxxxTxxxTxxxxxxxxxTxxxTxxxxxxxTxxxxxx'
# ['xxxxx', 'xxxx', 'xxxxx', 'xxxxx', 'xxx', 'xxxxxxxxx', 'xxx', 'xxxxxxx', 'xxxxxx']
# 12 TxxxxxTxxxxT
# 12 TxxxxTxxxxxT
# 13 TxxxxxTxxxxxT
# 11 TxxxxxTxxxT
# 15 TxxxTxxxxxxxxxT
# 15 TxxxxxxxxxTxxxT
# 13 TxxxTxxxxxxxT
# 16 TxxxxxxxTxxxxxxT
'''
s = s.split('T')
R = []
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(len(r), r)
    R.append(len(r))
print(min(R))
'''

# № 27634 Апробация 04.03.26 (Уровень: Базовый)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ Z встречается не менее 270 раз.
# Для выполнения этого задания следует написать. программу.

s = open('files/24.txt').readline()
s = s.split('Z')
R = []
for i in range(len(s)-268):
    r = 'Z' + 'Z'.join(s[i:i+269]) + 'Z'
    R.append(len(r))
print(min(R))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.2, 25, 27]
# КЕГЭ = [11]
# на следующем уроке: 7, 24 номера через замену, 24 номера через замену + split()


# region 📖 Пробник (Вариант 2)

# Студент #Арсений
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 3, 9, 17, 22, 27
# ❔ Без ответа: 6, 24, 25, 26
# Итог: 19/29 первичных балла ~ 75 вторичных

# endregion 📖 Пробник (Вариант 2)

