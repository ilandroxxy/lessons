# region Домашка: ******************************************************************


# № 7038 Danov2303 (Уровень: Средний)
'''
a = [int(i) for i in open("0. files/17.txt")]
b = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        x, y = a[i], a[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            b.append(x + y)
print(len(b), max(b))
'''


# № 7038 (Уровень: Средний) 🌶
'''
a = [int(i) for i in open("0. files/17.txt")]
# M = [x for x in a if abs(x) % 10 == 1]
M = [x for x in a if str(x)[-1] == '1']

B = []
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x in M) + (y in M) == 1:
        B.append((x + y) / 2)

# максимального среднего значения пары среди всех пар отвечающих предыдущему условию.
maxi = max(B)

cnt = 0
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x in M) + (y in M) == 1:
        if (x < maxi) and (y < maxi):
            cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Способы открытия файла для 9 номера
'''
cnt = 0
for s in open('0. files/9.csv'):
    print(s)  # 5;45;16;39
    M = [int(x) for x in s.split(';')]

cnt = 0
for s in open('0. files/9.txt'):
    print(s)  # 5 45 16 39
    M = [int(x) for x in s.split()]
'''


# Перестановки элементов без дублирования элементов
'''
from itertools import permutations
M = [13, 22, 3]
for p in permutations(M):
    print(p)
    # (13, 22, 3)
    # (13, 3, 22)
    # (22, 13, 3)
    # (22, 3, 13)
    # (3, 13, 22)
    # (3, 22, 13)
'''


# https://education.yandex.ru/ege/task/5c54e314-516a-44fb-b41f-b06ffe3345af

from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    # сумма чисел в строке чётна
    if sum(M) % 2 == 0:
        # максимальное число строки меньше суммы трёх оставшихся чисел
        if max(M) < sum(M) - max(M):
            # четыре числа строки можно разбить на две пары чисел с равными суммами
            if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
                cnt += 1
print(cnt)



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: