# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 8 https://education.yandex.ru/ege/task/27d33ca7-25ea-4a12-984d-a4b80d21455d
'''
# Вариант 1
s = sorted('АВЛОС')
n = 0
R = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                if a == 'Л':
                    R.append(n)

print(min(R))

# Вариант 2
from itertools import *
n = 0
for p in product(sorted('АВЛОС'), repeat=4):
    word = ''.join(p)
    n += 1
    if word[0] == 'Л':
        print(n)
        break

# Вариант 3
from itertools import *

for n, p in enumerate(product(sorted('АВЛОС'), repeat=4), 1):
    word = ''.join(p)
    if word[0] == 'Л':
        print(n)
        break
'''


# Задание 8 https://education.yandex.ru/ege/task/ec40e795-ecb6-454f-9e64-291da6044f52
# Джобс Е.
'''
from itertools import *
n = 0
cnt = 0
for p in product(sorted('АПРЕЛЬ', reverse=True), repeat=5):
    word = ''.join(p)
    n += 1

    if word[-1] == 'Ь':
        cnt += 1
        print(word)

    if n >= 387:
        break

print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/65351d01-6be4-467f-8c36-6d951bf990bb
'''
from itertools import *
cnt = 0
for p in product('ДРАКОН', repeat=8):
    word = ''.join(p)
    if word.count('А') == 1 and word.count('О') == 1:
        cnt += 1
print(cnt)
'''

# Задание 8 https://education.yandex.ru/ege/task/787e3e6e-9284-4a9d-953a-8c3d24123b2a
'''
from itertools import *
cnt = 0
for p in permutations('Артём'.upper(), r=5):
    word = ''.join(p)
    if not(word[0] in 'АЁ' and word[-1] in 'АЁ'):
        cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/b19825e6-aafc-48ed-9bd7-99033090c53c
'''
from itertools import *
cnt = 0
for p in product('012345', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('2') == 1:
            if all(x not in num for x in '21 12 23 32 52 25'.split()):
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
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
