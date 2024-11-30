# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 8 https://education.yandex.ru/ege/task/e73090d1-5401-4307-8b8c-bd1af02cefc0
'''
# Вариант 1
s = sorted('МАРИЯ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                if word == 'АРИЯ':
                    print(n)

# Вариант 2
from itertools import *
n = 0
for p in product(sorted('МАРИЯ'), repeat=4):
    word = ''.join(p)
    n += 1
    if word == 'АРИЯ':
        print(n)

# Вариант 3

from itertools import *

for n, p in enumerate(product(sorted('МАРИЯ'), repeat=4), 1):
    word = ''.join(p)
    if word == 'АРИЯ':
        print(n)
'''


# Задание 8
'''
cnt = 0
from itertools import *
for p in permutations('КАБИНЕТ'):
    word = ''.join(p)
    if word[-1] not in 'АИЕ':
        cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/bf49516c-39dc-461d-9b19-3462210daa1b
'''
cnt = 0
from itertools import *
for p in product('ЛЕГКО', repeat=6):
    word = ''.join(p)
    if word.count('О') <= 1:
        if word[0] != 'Г' and word[-1] not in 'ЕО':
            cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/b19825e6-aafc-48ed-9bd7-99033090c53c
'''
cnt = 0
from itertools import *
for p in product('012345', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('2') == 1:
            num = num.replace('3', '1').replace('5', '1')
            if '12' not in num and '21' not in num:
                cnt += 1
print(cnt)
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
