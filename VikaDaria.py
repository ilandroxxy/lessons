# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Три строки для начала 9 номера
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
'''


# https://education.yandex.ru/ege/inf/task/5c54e314-516a-44fb-b41f-b06ffe3345af
'''
from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if sum(M) % 2 == 0:
        if max(M) < sum(M) - max(M):
            if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
                cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/a943862d-a8ae-447e-9b9b-5d5a819cc660
# Все числа различны.
# Сумма чисел кратна трём.
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if sum(M) % 3 == 0:
        if len(M) == len(set(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/4e1f6f1f-125e-463a-b14e-77bb37d1dec0
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied = [x for x in M if M.count(x) > 1]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(set(copied)) == 2:
        if sum(set(copied)) < sum(not_copied):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/342217d2-3e89-4933-a422-940d9668bfa3
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        if sum(copied) ** 2 > sum(not_copied) ** 2:
            cnt += 1
print(cnt)
'''


# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# квадрат наибольшего значения больше произведения остальных чисел;
# сумма двух наибольших значений как минимум вдвое больше суммы остальных значений в строке.
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    M.sort()
    if M[-1]**2>M[0]*M[1]*M[2]*M[3]:
        if M[-1]+M[-2]>=2*(M[0]+M[1]+M[2]):
            cnt+=1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
# Определите количество строк таблицы, для чисел которых выполнены оба условия:
# в строке есть два числа, каждое из которых повторяется дважды,
# остальные три числа различны;
# среднее арифметическое всех повторяющихся чисел строки меньше
# среднего арифметического всех её чисел.
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied2 = [x for x in M if M.count(x)==2]
    copied1 = [x for x in M if M.count(x)==1]
    if len(copied2)==4 and len(copied1)==3:
        if sum(copied2)/len(copied2)<sum(M)/len(M):
            cnt+=1
print(cnt)
'''




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 9, 13, 14, 15, 16, 17, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке: 27
