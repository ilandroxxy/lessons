# region Домашка: ******************************************************************

# № 7718 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if ((x * y) % 18 == 0) != ((x + y) % 18 == 0):
            R.append(x + y)
print(len(R), max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 24 №27697
# Текстовый файл состоит не более чем из 10*6 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов D.
# Хотя бы один символ D находится в последовательности.

# Вариант 1
'''
s = open('files/24.txt').readline()
cnt = 1  # Хранить длину промежуточной
maxi = 0  # Хранить длину максимальной подпоследовательности
for i in range(len(s)-1):
    # if s[i] == 'D' and s[i+1] == 'D':
    if s[i:i+2] == 'DD':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''

# Вариант 2
'''
s = open('files/24.txt').readline()
s = s.replace('L', ' ').replace('R', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №59817
# Текстовый файл состоит из символов, обозначающих прописные
# буквы латинского алфавита. Определите максимальное количество
# идущих подряд символов, среди которых никакие две буквы из набора
# букв A, B и C (с учетом повторений) не записаны подряд.
'''
s = open('files/24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27694
# Текстовый файл состоит не более чем из 10**6 символов A, B и C.
# Определите максимальную длину цепочки вида ABABABA...
# (составленной из фрагментов AB, последний фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    # if (s[i] == 'A' and s[i+1] == 'B') or (s[i] == 'B' and s[i+1] == 'A')
    if s[i:i + 2] in ('AB', 'BA'):
        if cnt == 1 and s[i] == 'B':
            continue
        cnt += 1
        maxi = max(cnt, maxi)
    else:
        cnt = 1
print(maxi)
'''


s = open('files/24.txt').readline()
print(s)
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 9, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
