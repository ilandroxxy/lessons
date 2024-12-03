# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 8 https://education.yandex.ru/ege/task/b3ba0f73-8f32-4ae0-be90-8b727190e93f

# Вариант 1
'''
s = sorted('ЦАПЛЯ')
M = []
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('А') <= 1 and word.count('Ц') == 2 and 'Л' not in word:
                        M.append(n)

print(min(M))


# Вариант 2

from itertools import *
n = 0
for p in product(sorted('ЦАПЛЯ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('А') <= 1 and word.count('Ц') == 2 and 'Л' not in word:
        print(n)
        break

# Вариант 2

from itertools import *

for n, p in enumerate(product(sorted('ЦАПЛЯ'), repeat=5), 1):
    word = ''.join(p)
    if word.count('А') <= 1 and word.count('Ц') == 2 and 'Л' not in word:
        print(n)
        break
'''


# Задание 8 https://education.yandex.ru/ege/task/787e3e6e-9284-4a9d-953a-8c3d24123b2a
'''
from itertools import *
cnt = 0
for p in permutations(sorted('АРТЕМ'), 5):
    word = ''.join(p)
    if not(word[0] in 'АЕ' and word[-1] in 'АЕ'):
        cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/bf49516c-39dc-461d-9b19-3462210daa1b

from itertools import *
cnt = 0
for p in product('ЛЕГКО', repeat=6):
    word = ''.join(p)
    if word.count('О') <= 1:
        if word[0] != 'Г' and word[-1] not in 'ЕО':
            cnt += 1
print(cnt)




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
