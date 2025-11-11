# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23192 Основная волна 10.06.25 (Уровень: Базовый)
'''
s = sorted('ТЕОРИЯ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if n % 2 != 0:
                            if a not in 'РТЯ':
                                if word.count('И') >= 2:
                                    print(n)

from itertools import product
n = 0
for p in product(sorted('ТЕОРИЯ'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] not in 'РТЯ':
            if word.count('И') >= 2:
                print(n)


from itertools import product
for n, p in enumerate(product(sorted('ТЕОРИЯ'), repeat=6), 1):
    word = ''.join(p)
    if n % 2 != 0:
        if word[0] not in 'РТЯ':
            if word.count('И') >= 2:
                print(n)
'''
from zipfile import compressor_names

'''
from itertools import product, permutations

for p in permutations('abc'):
    word = ''.join(p)
    print(p, word)
    # ('a', 'b', 'c') abc
    # ('a', 'c', 'b') acb
    # ('b', 'a', 'c') bac
    # ('b', 'c', 'a') bca
    # ('c', 'a', 'b') cab
    # ('c', 'b', 'a') cba

for p in product('abc', repeat=2):
    word = ''.join(p)
    print(p, word)
    # ('a', 'a') aa
    # ('a', 'b') ab
    # ('a', 'c') ac
    # ('b', 'a') ba
    # ('b', 'b') bb
    # ('b', 'c') bc
    # ('c', 'a') ca
    # ('c', 'b') cb
    # ('c', 'c') cc
'''


# № 22417 (Уровень: Базовый)
'''
from itertools import product
n = 0
cnt = 0
for p in product(sorted('ЦИФЕРБЛАТ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] not in 'ИЕА':
            if word.count('Ц') == word.count('Ф'):
                cnt += 1
print(cnt)
'''


# № 18042 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('ЛЮСТРА', repeat=5):
    word = ''.join(p)
    if word.count('Ю') <= 2:
        if word[-1] not in 'ЛСТР':
            cnt += 1
print(cnt)
'''


# № 17627 Основная волна 19.06.24 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('0123456789ABCDE', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            if len([x for x in num if x > '9']) >= 2:
                cnt += 1
print(cnt)
'''


# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] not in '1357':
            if num[-1] not in '26':
                if num.count('7') <= 2:
                    cnt += 1
print(cnt)
'''


# № 16319 Открытый вариант 2024 (Уровень: Базовый)
'''
from itertools import product
n = 0
for p in product(sorted('ПАРУС'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('У') <=1:
        if 'AA' not in word:
            print(n)
'''


# № 17549 Основная волна 08.06.24 (Уровень: Базовый)
'''
from itertools import product
n = 0
for p in product(sorted('ФОКУС'), repeat=5):
    word = ''.join(p)
    n += 1
    if 'Ф' not in word:
        if word.count('У') == 2:
            print(n)
'''

# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
'''
from itertools import product
cnt= 0
for p in product(sorted('0123456'), repeat=7):
    word =''.join(p)
    if word[0] != '0':
        if len([x for x in word if x in '0246']) == 2:
            cnt += 1
print(cnt)
'''


# № 12240 ЕГКР 16.12.23 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product(sorted('012345678'), repeat=5):
    word =''.join(p)
    if word[0] != '0':
        if word.count('5') == 1:
            if all(p not in word for p in '00 11 22 33 44 55 66 77 88'.split()):
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
# ФИПИ = [2, 5, 8, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
