# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# 6901
'''
from itertools import *
count = 0
for i in product(sorted('БАРШ'), repeat=5):
    count += 1
    p = ''.join(i)

    tempB = sum([1 if x in 'БРШ' else 0 for x in p]) <= 3
    tempA = sum([p.count(x) for x in p])==7
    if tempA and tempB:
        print(count)
'''

'''
from itertools import *
n = 0
for i in product(sorted('БАРШ'), repeat=5):
    word = ''.join(i)
    n += 1
    if len([x for x in word if x in 'БРШ']) <= 3:
        copied = [x for x in word if word.count(x) == 2]
        uncopied = [x for x in word if word.count(x) == 1]
        if len(copied) == 2 and len(uncopied) == 3:
            print(n)
'''

# https://education.yandex.ru/ege/task/4361eddf-5383-491c-a4a7-a67acaf27b9a
'''
from itertools import *
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if max(M) < M[0] + M[1] + M[2]:
        if any(p[0] + p[1] == p[2] + p[3]  for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/4361eddf-5383-491c-a4a7-a67acaf27b9a

# Определите количество строк таблицы с числами, для которых работают не менее двух из трёх условий:
#
# в строке одно число повторяется трижды, остальные различны
# чётных чисел больше, чем нечётных
# сумма двух наибольших значений больше, чем в два раза превышает сумму остальных значений

cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    copied3 = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(uncopied) == 3:
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) > len(nechet):
        flag += 1
    M = sorted(M)
    if (M[-1] + M[-2]) > 2 * (M[0] + M[1] + M[2] + M[3]):
        flag += 1
    if flag >= 2:
        cnt += 1
print(cnt)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 14, 15]
# КЕГЭ = []
# на следующем уроке: 12, 23, 25, 26/27, 19-21


# Первый пробник 7.03.25:
# Лев 8/46 -> _ вторичных баллов +[2, 5, 15, 16, 19, 20, 23, 25] -[8, 9, 12, 21]
