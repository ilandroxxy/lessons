# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Статргад номер 5 от 3.03.26
'''
from math import prod
for n in range(1, 10000):
    M = [int(x) for x in sorted(str(n))]
    P = prod([x for x in M if x != 0])
    S = max(M) - min(M)
    T1 = P + S
    T2 = P * S + 1
    R = ''.join([str(x) for x in sorted([T1, T2])])
    if R == '25127':
        print(n)
'''


# Статргад номер 17 от 3.03.26
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3]
B = [x for x in M if x > 0 and x % 100 == 77]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if (x in A) + (y in A) + (z in A) <= 1:
        if (x + y + z) >= min(B):
            R.append(x + y + z)
print(len(R), min(R))
'''


# Статргад номер 24 от 3.03.26
'''
s = open('files/24.txt').readline()
for x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(x, '*')
print(max([len(x) for x in s.split('*') if all(p in x for p in '0123456789')]))

R = []
for x in s.split('*'):
    if all(p in x for p in '0123456789'):
        R.append(len(x))
print(max(R))
'''

'''
cnt = 0
from itertools import product
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        nechet = [x for x in num if x in '13579B']
        if len(nechet) == 3:
            if any(p*3 in num for p in '13579B'):
                cnt += 1
print(cnt)
'''


'''
from math import dist
def G(cl1, cl2):
    R = []
    for p in cl1:
        for g in cl2:
            R.append([dist(p, g), p, g])
    return max(R)[1:]
'''


# № 29075 (Уровень: Средний)
'''
from math import dist
clustersA = [[], []]
paramsA = [[], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 10:
        clustersA[0].append([x, y])
        paramsA[0].append(z)
    if y < 10:
        clustersA[1].append([x, y])
        paramsA[1].append(z)


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# A1 – абсцисса центра кластера с минимальным количеством гигантов, и
# A2 – ордината центра кластера с максимальным количеством гигантов.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

def red(cl, param):
    cnt = 0
    for i in range(len(cl)):
        if 'Y' in param[i] and 'III' in param[i]:
            cnt += 1
    return cnt

print(red(clustersA[0], paramsA[0]))  # 1
print(red(clustersA[1], paramsA[1]))  # 3

A1 = 7.0391548 * 10000
A2 = 6.1225014 * 10000
print(int(A1), int(A2))
'''

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

