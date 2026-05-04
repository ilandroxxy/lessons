# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#27
'''from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('file/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x > 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])


for s in open('file/'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if -2 < y < 2 and -6 < x < -3:
        clustersB[0].append([x, y])
    if -2 < x < 1 and -8 < y < -4:
        clustersB[1].append([x, y])
    if -6 < x < -3 and -10 < y < -6:
        clustersB[2].append([x, y])

print(clustersA[0])
print(clustersA[1])
print(clustersB[0])
print(clustersB[1])
print(clustersB[2])

def center(cl):
    R = []
    for p in cl:
        sums = 0
        for q in cl:
            sums += dist(p, q)
        R.append((sums, p))
    return min(R)[1]

centersB = [center(clustersB[0]), center(clustersB[1]), center(clustersB[2])]

sizesB = [len(clustersB[0]), len(clustersB[1]), len(clustersB[2])]
min_idx = sizesB.index(min(sizesB))
max_idx = sizesB.index(max(sizesB))
Q1 = centersB[min_idx][1]
Q2 = centersB[max_idx][1]

print(abs(int(Q1 * 10000)), abs(int(Q2 * 10000)))'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [5, 11, 19-21, 25]
# на следующем уроке: (26)


# region 📖 Пробник (Вариант 2)

# Студент #Татьяна
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 3, 4, 6, 7, 10, 11, 14, 16, 17, 19, 20, 21, 22, 23, 25
# ⛔️ Неверно: 5, 8, 12
# ❔ Без ответа: 9, 13, 15, 18, 24, 26, 27
# Итог: 17/29 первичных балла ~ 70 вторичных


# Студент #Анна
# Дата: #Суббота #28Февраля2026
# ✅ Верно: 1, 2, 4, 7, 8, 11, 12, 14, 15, 16, 17, 18, 23, 25
# ⛔️ Неверно: 3, 5, 6, 10, 19, 20, 21, 27
# ❔ Без ответа: 9, 13, 22, 24, 26
# Итог: 14/29 первичных балла ~ 62 вторичных

# endregion 📖 Пробник (Вариант 2)


