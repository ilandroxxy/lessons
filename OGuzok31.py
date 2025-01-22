# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19240 ЕГКР 21.12.24 (Уровень: Базовый)
'''
# Вариант 1
R = []
s = sorted('ЯНВАРЬ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if a != 'Я':
                        if word.count('Ь') <= 1:
                            if 'ЯЯ' not in word:
                                R.append(n)
print(max(R))


# Вариант 2
from itertools import *
R = []
n = 0
for p in product(sorted('ЯНВАРЬ'), repeat=5):
    word = ''.join(p)
    n += 1
    # a, b, c, d, e = word
    # if a != 'Я':
    if word[0] != 'Я':
        if word.count('Ь') <= 1:
            if 'ЯЯ' not in word:
                R.append(n)
print(max(R))

# Вариант 3
from itertools import *
R = []
for n, p in enumerate(product(sorted('ЯНВАРЬ'), repeat=5), 1):
    word = ''.join(p)
    if word[0] != 'Я':
        if word.count('Ь') <= 1:
            if 'ЯЯ' not in word:
                R.append(n)
print(max(R))
'''


# № 18923 Новогодний вариант 2025 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('ВЬЮГА', repeat=6):
    word = ''.join(p)
    if 'ЮГ' in word:
        cnt += 1
print(cnt)
'''


# № 1941 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in permutations('СОТКАПЛЗ', r=5):
    word = ''.join(p)
    if word[-1] not in 'ОА':
        if 'ЗЛО' not in word:
            cnt += 1
print(cnt)
'''


# № 12453 (Уровень: Базовый)
'''
from itertools import *
cnt = set()
for p in permutations('СОВЕСТЬ'):
    word = ''.join(p)
    new_word = word
    for x in 'ОЕЬ':
        word = word.replace(x, 'A')
    for x in 'СВТ':
        word = word.replace(x, 'B')
    if not('AA' in word and 'BB' in word):
        cnt.add(new_word)
print(len(cnt))
'''


# № 12240 ЕГКР 16.12.23 (Уровень: Базовый)
# Сколько существует девятеричных пятизначных чисел,
# содержащих в своей записи ровно одну цифру 5,
# в которых никакие две одинаковые цифры не стоят рядом?
'''
from itertools import *
cnt = 0
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('5') == 1:
            if all(pair not in num for pair in '00 11 22 33 44 55 66 77 88'.split()):
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
# ФИПИ = [1, 2? сопоставление, 3, 4, 5, 7, 8, 9-, 11-, 12-, 13-, 14, 15-, 16-, 19-21-, 22]
# КЕГЭ  = []
# на следующем уроке: 15
