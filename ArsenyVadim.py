# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 23
# 1. Прибавь 8
# 2. Умножь на 3
# 3. Увеличь на разряд единиц

# Первая из них увеличивает число на экране на 8,
# вторая увеличивает число на экране в 3 раза,
# третья увеличивает число на экране на значение разряда единиц
# (например число 12 увеличится на 2, а число 25 на 5).
# Программа для исполнителя – это последовательность команд.

# Сколько существует программ, для которых при исходном числе 4 результатом
# является число 174, если известно, что нельзя повторять команду, сделанную на предыдущем шаге.

'''
def F(a, b, c):
    if a >= b:
        return a == b and '11' not in c and '22' not in c and '33' not in c
    return F(a + 8, b, c+'1') + F(a * 3, b, c+'2') + F(a + (a % 10), b, c+'3')

print(F(4, 174, ''))
'''

'''
def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return 1
    h = []
    if c != 1:
        h += [f(a + 8, b, 1)]
    if c != 2:
        h += [f(a * 3, b, 2)]
    if c != 3:
        h += [f(a + (a % 10), b, 3)]
    return sum(h)

print(f(4, 174, 0))
'''

# № 5926 (Уровень: Средний)
'''
def F(a, b, c):
    if b == 24:
        return a == b and '11' not in c and '22' not in c and '33' not in c
    return F(a + 1, b+1, c+'1') + F(a + 7, b+1, c+'2') + F(a * 4, b+1, c+'3')

print(F(1, 0, ''))
'''


# 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copy2 = [x for x in M if M.count(x) == 2]
    copy1 = [x for x in M if M.count(x) == 1]
    if len(copy2) == 4 and len(copy1) == 3:
        if (sum(copy2) / 4) < (sum(copy1) / 3):
            cnt += 1
print(cnt)
'''


# 17
'''
M = []
S = []
R = []
for s in open('files/17.txt'):
    M.append(int(s))
for i in M:
    if i % 100 == 29:
        S.append(i)
print(max(S))  # 99429
cnt = 0
for i in range(len(M) - 2):
    if (len(str(abs(M[i]))) == 5) +  (len(str(abs(M[i + 1]))) == 5) + (len(str(abs(M[i + 2]))) == 5) == 2:
        if M[i] + M[i + 1] + M[i + 2]<= 99429:
            R.append(M[i] + M[i + 1] + M[i + 2])
            cnt += 1
print(cnt, max(R))


M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# Номер 25
'''
from re import *
for x in range(0, 10**8, 2023):
    if fullmatch('2[0-9]*1[0-9]71', str(x)):
        print(x, x // 2023)
'''


# Номер 27
'''
from math import *

clustersA = [[], []]
clustersB = [[], [], [], []]

def center(cl):
    S = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        S.append([summa, p])
    return (min(S)[1])



# A) y = -4
for s in open('files/27A.csv'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split(';')]
    if y > -4:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# B) 1. x = -6 2. x > -6 y < -6 3. x < -6 y > -6 y < -2 4. x > -6 y > -2
for s in open('files/27B.csv'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split(';')]
    if x < -6:
        clustersB[0].append([x, y])
    else:
        if y < -6:
            clustersB[1].append([x, y])
        elif -6 < y < -2:
            clustersB[2].append([x, y])
        elif y > -2:
            clustersB[3].append([x, y])

print(center(clustersA[0])) # [-8.20044973776254, 0.638981709687434]
print(center(clustersA[1])) # [-10.9058807055978, -10.2047099777569]
print(center(clustersB[0]))  # [-7.80262523553593, -6.10946094263275]
print(center(clustersB[1]))  # [-3.5245365973449, -7.61967069886266]
print(center(clustersB[2]))  # [-2.22718188693554, -3.79446965518536]
print(center(clustersB[3]))  # [-2.00777686513898, -0.890289719710631]


print((-8.20044973776254 + -10.9058807055978) / 2) # -9.553165221680171
print((0.638981709687434 + -10.2047099777569) / 2) # -4.7828641340347335
print((-7.80262523553593 + -3.5245365973449 + -2.22718188693554 + -2.00777686513898) / 4) # -7.781060292477674
print((-6.10946094263275 + -7.61967069886266 + -3.79446965518536 + -0.890289719710631) / 4) # -9.2069455081957
print(-9.553165221680171 * 10000, -4.7828641340347335 * 10000, -7.781060292477674 * 10000, -9.2069455081957 * 10000)
'''



# № 2419 (Уровень: Базовый)
# В текстовом файле находится цепочка из символов латинского алфавита A, B, C длиной не более 10**6 символов.
# Найдите длину самой длинной подцепочки, состоящей из символов C

# Вариант 1 - Решение через: ctrl + F
s = open('files/24.txt').readline()
print(s)
print(len('CCCCCCCCCCC'))

# Вариант 2 - Решение ака 17 номер

s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'C' and s[i+1] == 'C':
    if s[i:i+2] == 'CC':
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)

# Вариант 3 - Решение через замену

s = open('files/24.txt').readline()
s = s.replace('A', 'B').replace('B', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 4 - Решение через import re

from re import *
s = open('files/24.txt').readline()
pat = '(ABC)[C]*'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [11]
# на следующем уроке: 7


# Студент #Арсений
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 3, 9, 17, 22, 27
# ❔ Без ответа: 6, 24, 25, 26
# Итог: 19/29 первичных балла ~ 75 вторичных
