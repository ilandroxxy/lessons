# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Номер 17 Пробник 2
# В файле содержится последовательность целых чисел от -100 000 до 100 000
# включительно. Определите количество троек элементов последовательности, в которых
# из трёх элементов тройки пятизначными числами являются только два, а сумма элементов
# тройки не больше максимального элемента последовательности, оканчивающегося на 29.
# В ответе запишите кол-во найденных троек чисел, затем максимальную из сумм элементов
# таких троек. Под тройкой подразумевается три идущих подряд элемента
# последовательности.
'''
m = [int(x) for x in open('files/17.txt')]
maxi = [x for x in m if abs(x) % 100 == 29]
k = 0
ma = 0
for i in range(len(m) - 2):
    x, y, z = m[i], m[i + 1], m[i + 2]
    if (9999 < abs(x) < 100000) + (9999 < abs(y) < 100000) + (9999 < abs(z) < 100000) == 2:
        if (x + y + z) <= max(maxi):
            k += 1
            ma = max(x + y + z, ma)
print(k, ma)


m = [int(x) for x in open('files/17.txt')]
maxi = [x for x in m if abs(x) % 100 == 29]
# pat = [x for x in m if 9999 < abs(x) < 100000]
pat = [x for x in m if len(str(abs(x))) == 5]
k = 0
ma = 0
for i in range(len(m) - 2):
    x, y, z = m[i], m[i + 1], m[i + 2]
    if (x in pat) + (y in pat) + (z in pat) == 2:
        if (x + y + z) <= max(maxi):
            k += 1
            ma = max(x + y + z, ma)
print(k, ma)


m = [int(x) for x in open('files/17.txt')]
maxi = [x for x in m if abs(x) % 100 == 29]
pat = [x for x in m if len(str(abs(x))) == 5]
R = []
for i in range(len(m) - 2):
    x, y, z = m[i], m[i + 1], m[i + 2]
    if (x in pat) + (y in pat) + (z in pat) == 2:
        if (x + y + z) <= max(maxi):
            R.append(x + y + z)
print(len(R), max(R))


m = [int(x) for x in open('files/17.txt')]
maxi = [x for x in m if abs(x)%100 == 29]
pat = [x for x in m if 9999 < abs(x) < 100000]
k = 0
ma = 0
for i in range(len(m)-2):
    x,y,z = m[i],m[i+1],m[i+2]
    if ((x in pat) and (y in pat) and (z not in pat)) or ((z in pat) and (y in pat) and (x not in pat)) or ((x in pat) and (z in pat) and (y not in pat)):
         if (x+y+z) <= max(maxi):
            k += 1
            ma = max(x+y+z, ma)
print(k,ma)
'''


# Номер 27 Пробник 2
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y < -4:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > -2:
        clustersB[0].append([x, y])
    if -5 < y < -2:
        clustersB[1].append([x, y])
    if y < -5 and x > -5:
        clustersB[2].append([x, y])
    if y < -5 and x < -5:
        clustersB[3].append([x, y])

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]


print(center(clustersA[0]))  # [-10.905880705597788, -10.204709977756867]
print(center(clustersA[1]))  # [-8.200449737762538, 0.6389817096874344]
pxA = (-10.905880705597788 + -8.200449737762538) / 2 * 10000
pyA = (-10.204709977756867 + 0.6389817096874344) / 2 * 10000

centers = [center(cl) for cl in clustersA]
pxA = sum([x for x, y in centers]) / 2 * 10000
pyA = sum([y for x, y in centers]) / 2 * 10000

print(int(pxA), int(pyA))  # -95531 -47828

print(center(clustersB[0]))  # [-2.0077768651389816, -0.8902897197106308]
print(center(clustersB[1]))  # [-2.227181886935543, -3.794469655185359]
print(center(clustersB[2]))  # [-3.524536597344898, -7.61967069886266]
print(center(clustersB[3]))  # [-7.802625235535932, -6.109460942632754]
pxB = (-2.0077768651389816 + -2.227181886935543 + -3.524536597344898 + -7.802625235535932) / 4 * 10000
pyB = (-0.8902897197106308 + -3.794469655185359 + -7.61967069886266 + -6.109460942632754) / 4 * 10000
print(int(pxB), int(pyB))  # -38905 -46034
'''


# Номер 24 Пробник 2
'''
s = open('files/24.txt').readline()
s = s.split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''
# 4363


# № 66 Джобс 31.08.2020 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 латинских символов К, О, Т.
# Определите максимальное количество подряд идущих комбинаций КОТ.
'''
from re import *
s = open('files/24.txt').readline()
pat = '(KOT)+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
print(max([len(x) for x in M]) / 3)
'''

# № 105 Джобс 07.09.2020 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 символов
# F, A, I, L. Определите максимальное количество подряд
# идущих одинаковых букв.
'''
from re import *
s = open('files/24.txt').readline()
pat = '([F]+|[A]+|[L]+|[I]+)'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''


# № 318 (Уровень: Средний)
#
# (П.Е. Финкель) Текстовый файл состоит не более чем из 106
# символов и содержит только заглавные латинские буквы и десятичные цифры.
# Определите максимальное нечётное число, записанное в этом файле.
'''
from re import *
s = open('files/24.txt').readline()
pat = '[1-9][0-9]*[13579]'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([int(x) for x in M]))
'''


# № 322 (Уровень: Средний)
# (П.Е. Финкель) Текстовый файл состоит не более чем из 106 символов
# и содержит только заглавные латинские буквы и десятичные цифры.
# Под словом подразумевается последовательность букв, ограниченная цифрами.  Определите количество четырёхбуквенных слов.
# Словом считается любая произвольная последовательность букв.

from re import *
s = open('files/24.txt').readline()
pat = '[0-9][A-Z][A-Z][A-Z][A-Z][0-9]'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(len(M))


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = []
# на следующем уроке:


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
