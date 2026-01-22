# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Зимний гроб
'''
A = []
for s in open('files/9.csv'):
    M = [str(int(x)) for x in s.split(';')]
    A += M

maxi = 0
n = 0
for x in set(A):
    if A.count(x) > maxi:
        maxi = A.count(x)
        n = x
print(maxi, n)
print(n)

cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]

    flag = 0
    copied = [x for x in M if M.count(x) > 1]

    if sum(M) >= sum(copied) ** 2:
        flag += 1

    if len(M) == len(set(M)):
        flag += 1

    if int(n) in M:
        flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)
'''


# № 7094 OpenFIPI (Уровень: Базовый)
# Текстовый файл состоит из символов A, C, D, F и U.
# Определите максимальное количество идущих подряд пар символов вида согласная + гласная в прилагаемом файле.
'''
s = open('files/24.txt').readline()
cnt = 0
maxi = 0
s = s.replace('D', 'F').replace('F', 'C').replace('C', '*')
s = s.replace('A', 'U').replace('U', '#').replace('*#', '0')
for p in s:
    if p == '0':
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 0
print(maxi)


s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if cnt == 1 and (s[i] in 'AU' and s[i+1] in 'CDF'):
        continue
    if (s[i] in 'AU' and s[i+1] in 'CDF') or (s[i] in 'CDF' and s[i+1] in 'AU'):
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi // 2)


s = open('files/24.txt').readline()
s = s.replace('D', 'F').replace('F', 'C').replace('C', '*')
s = s.replace('A', 'U').replace('U', '#').replace('*#', '0')
s = s.replace('#', ' ').replace('*', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №47021
# Определите количество групп из идущих подряд не менее 10 символов,
# которые начинаются и заканчиваются буквой A и не содержат других
# букв A (кроме первой и последней) и букв B.
'''
# A AxxxxxA AxxxA AxxxxxxxA A
# AxxxxxA
# AxxxA
# AxxxxxxxA

s = open('files/24.txt').readline()
s = s.replace('A', 'A A')
print(len([len(x) for x in s.split() if len(x) >= 10 and 'B' not in x]))
'''


# Тип 24 №40999
# Определите максимальное количество идущих подряд символов,
# среди которых нет ни одной буквы E и при этом не менее трёх букв A.
'''
s = open('files/24.txt').readline()
s = s.replace('E', ' ')
print(max([len(x) for x in s.split() if x.count('A') >= 3]))
'''




# Тип 24 №61370
# Определите максимальное количество идущих подряд символов,
# среди которых ровно по одному разу встречаются буквы A и B.
'''
s = open('files/24.txt').readline()
s = s.replace('A', 'A ').replace('B', 'B ')
s = s.split()
maxi = 0
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]
    if r.count('A') == 1 and r.count('B') == 1:
        maxi = max(maxi, len(r))
print(maxi)
'''


# Тип 24 №63040
# Определите максимальное количество идущих подряд символов,
# среди которых каждая из букв A и B встречается не более двух раз.
'''
s = open('files/24.txt').readline()
s = s.replace('A', 'A ').replace('B', 'B ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    r = ''.join(s[i:i + 5])[:-1]
    if r.count('A') == 2 and r.count('B') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# Тип 24 №51993
# Определите длину самой длинной цепочки символов, которая начинается
# и заканчивается буквой F, а между двумя последовательными
# буквами F содержит не более двух букв A и произвольное количество других букв.

# FxxxxFxxxxFxxxxFxxxxF
# 'F' + xxAxAx'F'xxAxx'F'xxxx'F'xxAxAx + 'F' + xxAxxxAxxAxx+ 'F'
# 'F' + xxAxAx'F'xxAxx'F'xxxx'F'xxAxAx + 'F'

s = open('files/24.txt').readline()
s = s.split('F')
r = 'F' + 'F'.join([x if x.count('A') <= 2 else '*' for x in s]) + 'F'
print(max([len(x) for x in r.split('*')]))



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке: Разбирать задачи по типу арифметика и символ X 80 раз (как 51993 решу егэ)
