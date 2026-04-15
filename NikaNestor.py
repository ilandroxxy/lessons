# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 28765 Досрочная волна 2026 (Уровень: Базовый)
'''
s = open('files/24.txt').readline()
s = s.split('BC')
R = []
for i in range(len(s)-180):
    r = 'B' + 'BC'.join(s[i:i+181]) + 'C'
    R.append(len(r))
print(max(R))
'''


# № 28755 Досрочная волна 2026 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке
# четыре натуральных числа. Определите количество строк таблицы,
# для чисел которых выполнены оба условия:
# – наибольшее число строки меньше суммы трёх других;
# – четыре числа нельзя разбирать на две пары с равными суммами.
'''
from itertools import permutations
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if max(M) < sum(M) - max(M):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M, r=4)):
            cnt += 1
print(cnt)
'''

# Номер 16 Досрочная волна
'''
# F(n) = (n + 4) * F(n - 5)  при n >= 10
# F(257487) = (257487 + 4) * F(257482)
# F(257482) = (257482 + 4) * F(257477)
# F(257477) = (257477 + 4) * F(257472) / F(257472)
half1 = ((257487 + 4) * (257482 + 4) * (257477 + 4) * 1) / 683

# F(257477) = (257477 + 4) * F(257472) / F(257472)
half2 = ((257477 + 4) * 1) / 67

print(half1 + half2)  # 24994252796625
'''


# Номера 19-21 Досрочная волна
# 2 кучи: a+1, s+1, a*3, s*3 | a + s >= 65 | a = 6 | 1 <= s <= 58
'''
def F(a, s, n):
    if a + s >= 65:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 1, s, n-1), F(a, s + 1, n-1), F(a * 3, s, n-1), F(a, s * 3, n-1)]
    # return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 58+1) if F(6, s, n=2)])
print([s for s in range(1, 58+1) if F(6, s, n=3) and not F(6, s, n=1)])
print([s for s in range(1, 58+1) if F(6, s, n=4) and not F(6, s, n=2)])
'''


# № 23382 Резервный день 19.06.25 (Уровень: Средний)
# Напишите программу, которая перебирает целые числа, большие 6 651 220, в порядке
# возрастания и ищет среди них числа, представленные в виде произведения ровно
# двух простых множителей, не обязательно различных, каждый из которых содержит в
# своей записи ровно одну цифру 2.
# В ответе в первом столбце таблицы запишите первые 5 найденных чисел в порядке
# возрастания, а во втором столбце - для каждого из чисел соответствующий им наибольший
# из найденных множителей.
# Количество строк в таблице для ответа избыточно.

def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
from itertools import product
for x in range(6_651_220+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        if any(p[0] * p[1] == x and str(p[0]).count('2') == 1 and str(p[1]).count('2') == 1 for p in product(d, repeat=2)):
            print(x, max(d))
            cnt += 1
            if cnt == 5:
                break

# x = 9
# divisors(x) [1, 3, 9]
# d [3, 9]
# for p in product(d, repeat=2)
#     p[0] * p[1] == x
#     3 * 3 == 9
#     3 * 9 == 9
#     9 * 3 == 9
#     9 * 9 == 9



# № 28711 (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

def good(p):
    s = str(p)
    return '4' in s or '7' in s

cnt = 0
from itertools import permutations
for x in range(2400000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 2]
    if len(d) > 0:
        if any((p[0] * p[1] * p[2] == x) and (good(p[0]) and good(p[1]) and good(p[2])) for p in permutations(d, r=3)):
            print(x, max(d))
            cnt += 1
            if cnt == 5:
                break
'''


# № 28766 Досрочная волна 2026 (Уровень: Базовый)

from math import dist
from itertools import permutations

clustersA = [[], []]
paramsA = [[], []]

clustersB = [[], [], []]
paramsB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    print(x, y, z)
    if y > 10:
        clustersA[0].append([x, y])
        paramsA[0].append(z)
    else:
        clustersA[1].append([x, y])
        paramsA[1].append([x, y])


for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()[:-1]]
    z = s.split()[-1]
    if y > 22:
        clustersB[0].append([x, y])
        paramsB[0].append(z)
    if y < 22 and x < 20:
        clustersB[1].append([x, y])
        paramsB[1].append(z)
    if y < 22 and x > 20:
        clustersB[2].append([x, y])
        paramsB[2].append(z)


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]



# Для файла А определите координаты центра каждого кластера, затем найдите два числа:
# A1 – минимальное расстояние от центра кластера с наименьшим количеством точек до красного гиганта, и
# A2 – максимальное расстояние от центра кластера с наименьшим количеством точек до красного гиганта.

print(center(clustersA[0]))  # [7.0391548, 12.3587258]
print(center(clustersA[1]))  # [3.8471735, 6.1225014]

print(len(clustersA[0]))  # 92
print(len(clustersA[1]))  # 131

def A1(cl, center, param):
    R = []
    for i in range(len(cl)):
        if 'Y' in param[i] and 'III' in param[i]:  # Y1III
            R.append(dist(center, cl[i]))
    return min(R)

A1 = A1(clustersA[0], center(clustersA[0]), paramsA[0])
print(int(A1 * 10000))  # 4940




# Для файла Б определите координаты центра каждого кластера, затем найдите два числа:
# B1 – минимальное расстояние между двумя различными жёлтыми сверхгигантами, расположенными в одном и том же кластере, и
# B2 – расстояние между центрами кластеров с минимальным и максимальным количеством жёлтых сверхгигантов.

print(center(clustersB[0]))  # [13.9823808, 26.4800432]
print(center(clustersB[1]))  # [15.861917, 18.8540334]
print(center(clustersB[2]))  # [26.6431823, 12.4121727]


def B1(cl, param):
    M = []
    for i in range(len(cl)):
        if 'Z' in param[i] and 'I' in param[i] and 'V' not in param[i] and 'II' not in param[i]:
            M.append(cl[i])
    R = []
    for p in permutations(M, r=2):
        R.append(dist(p[0], p[1]))
    return min(R)

print(B1(clustersB[0], paramsB[0]) * 10000)
print(B1(clustersB[2], paramsB[2]) * 10000)
B1 = int(1035.4459340095964)

def yellow(cl, param):
    cnt = 0
    for i in range(len(cl)):
        if 'Z' in param[i] and 'I' in param[i] and 'V' not in param[i] and 'II' not in param[i]:
            cnt += 1
    return cnt

print(yellow(clustersB[0], paramsB[0]))  # 3
print(yellow(clustersB[1], paramsB[1]))  # 1
print(yellow(clustersB[2], paramsB[2]))  # 9

B2 = dist(center(clustersB[1]), center(clustersB[2]))
print(B1, int(B2 * 10000))  # 125591


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [23]
# на следующем уроке: посмотреть 16 номера на лркуэш в какую сторону перебор и 15 номера ака ЕГКР
# С нуля 24 номера


# region Пробник 2

# Вероника
# Пробник №2
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17,
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных


# Нестор
# Пробник №2
# Дата: #Воскресенье #01Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных

# endregion Пробник 2
