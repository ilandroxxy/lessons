# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Номер 9 (24087)
'''
for s in open('files/9.csv'):
    m = [int(x) for x in s.split(',')]
    p4 = [x for x in m if m.count(x) == 4]
    p1 = [x for x in m if m.count(x) == 1]
    if len(p4) == 4 and len(p1) == 3:
        if sum(m) / len(m) >= p4[0]:
            print(sum(m))
            break
'''

# Номер 14 (24086)
'''
def per(n, b):
    m = ''
    while n > 0:
        m = str(n % b) + m
        n //= b
    return m

k = 0
for x in range(1, 3000+1):
    n = 5 * 7 ** 156 + 3 * 7 ** 10 - x ** 31
    if per(n, 7).count('0') == 15:
        k += 1
print(k)


k = 0
for x in range(1, 3000+1):
    n = 5 * 7 ** 156 + 3 * 7 ** 10 - x ** 31
    cnt = 0
    while n > 0:
        r = n % 7
        if r == 0:
            cnt += 1
        n //= 7
    if cnt == 15:
        k += 1
print(k)
'''


# № 29354 Открытый вариант 2026 (Уровень: Базовый)
#
# Текстовый файл состоит из заглавных букв латинского алфавита A, B, C, D, E и F.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых пара символов BC (в указанном порядке) встречается ровно 190 раз.
# В ответе запишите число – количество символов в найденной последовательности.
# Для выполнения этого задания следует написать программу.
'''
s = open('files/24.txt').readline()
s = s.split('BC')
maxi = 0
for i in range(len(s)-190):
    r = 'C' + 'BC'.join(s[i:i+191]) + 'B'
    maxi = max(maxi, len(r))
print(maxi)


# BC встречается ровно 5 раз.
s = 'xxxxxBCxxxxxBCxxxxxxBCxxxxxBCxxxxBCxxxxxBCxxxxBCxxxxx'
# ['xxxxx', 'xxxxx', 'xxxxxx', 'xxxxx', 'xxxx', 'xxxxx', 'xxxx', 'xxxxx']
s = s.split('BC')
for i in range(len(s)-5):
'''


'''
s = open('files/24.txt').readline()
s = s.split('25')
maxi = 0
R = []
for i in range(len(s)-302):
    r = '25'.join(s[i:i+303])
    R.append(r.count('E'))
    if r.count('E') == 75:
        maxi = max(maxi, len(r))
print(maxi)
print(max(R))
'''


# Номер 27
'''
from math import dist
clustersA = [[], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

def center(cl):
    r = []
    for p in cl:
        summa = sum(dist(p, g) for g in cl)
        r.append([summa, p])
    return min(r)[1]

centersA = [center(cl) for cl in clustersA]
pxA = min([x for x, y in centersA]) * 10000
pyA = max([y for x, y in centersA]) * 10000
print(int(pxA), int(pyA))
'''

from itertools import permutations
from math import dist

cA = [[], []]
pA = [[], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y > 15:
        cA[0].append([x, y])
        pA[0].append(z)
    else:
        cA[1].append([x, y])
        pA[1].append(z)

# print(len(cA[0]), len(pA[0]))
# print(len(cA[1]), len(pA[1]))


cB = [[], [], []]
pB = [[], [], []]

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y, z = [i for i in s.split()]
    x, y = float(x), float(y)
    if y < 30:
        cB[0].append([x, y])
        pB[0].append(z)
    else:
        if x > 16:
            cB[1].append([x, y])
            pB[1].append(z)
        else:
            cB[2].append([x, y])
            pB[2].append(z)

# print(len(cB[0]), len(pB[0]))
# print(len(cB[1]), len(pB[1]))
# print(len(cB[2]), len(pB[2]))


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]

# Для файла А определите координаты центра каждого кластера, затем найдите два числа
# Ax и Ay – абсциссу и ординату красного гиганта, ближайшего к центру кластера,
# который содержит наименьшее количество точек.

print(len(cA[0]))  # 121
print(len(cA[1]))  # 114

def A(cl, cent, p):
    R = []
    for i in range(len(cl)):
        if 'M' in p[i] and 'III' in p[i]:
            R.append([dist(cl[i], cent), cl[i]])
    return min(R)[1]

Ax, Ay = A(cA[1], center(cA[1]), pA[1])
print(int(Ax * 10000), int(Ay * 10000))


# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – расстояние между центрами кластеров
# с наименьшим и наибольшим количеством оранжевых гигантов, и
# B2 – наибольшее расстояние между жёлтыми карликами одного кластера.

def B1(cl, p):
    cnt = 0
    for i in range(len(cl)):
        if 'K' in p[i] and 'III' in p[i]:
            cnt += 1
    return cnt

print(B1(cB[0], pB[0]))  # 87
print(B1(cB[1], pB[1]))  # 25
print(B1(cB[2], pB[2]))  # 28

B1 = dist(center(cB[0]), center(cB[1]))
B1 = int(B1 * 10000)

def B2(cl, p):
    M = []
    for i in range(len(cl)):
        if 'G' in p[i] and 'V' in p[i] and 'I' not in p[i]:
            M.append(cl[i])
    R = []
    for x in permutations(M, r=2):
        R.append(dist(x[0], x[1]))
    return max(R)

print(B2(cB[0], pB[0]))  # 3.402952125891432
print(B2(cB[1], pB[1]))  # 2.0958719542209643
print(B2(cB[2], pB[2]))  # 2.922566402694216

B2 = int(3.402952125891432 * 10000)
print(B1, B2)



# 137
# 36
# 50


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 14, 16, 25]
# на следующем уроке:  15 номера руками


# region 📖 Пробник (Вариант 2)

# Студент #Дарья
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 4, 5, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27
# ⛔️ Неверно: 3, 6, 7, 10, 24, 26
# ❔ Без ответа: Нет
# Итог: 22/29 первичных балла ~ 83 вторичных

# Студент #Маша
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 21, 23
# ⛔️ Неверно: 10, 18
# ❔ Без ответа: 9, 17, 22, 24, 25, 26, 27
# Итог: 18/29 первичных балла ~ 72 вторичных

# Студент #Вика
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 6, 7, 8, 13, 14, 16, 17, 19, 20, 21, 25, 27
# ⛔️ Неверно: 5, 9, 12, 15, 23
# ❔ Без ответа: 3, 4, 10, 11, 18, 22, 24, 26
# Итог: 15/29 первичных балла ~ 65 вторичных

# endregion 📖 Пробник (Вариант 2)

