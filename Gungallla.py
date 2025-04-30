# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 20954 (Уровень: Базовый)

# Вариант 1
'''
s = sorted('МАКС')
s = 'АКМС'
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if word.count('С') == 0:  # if 'С' not in word:
                            if 'М' not in word:
                                if 'КК' not in word:
                                    print(n, word)
'''

# Вариант 2
'''
from itertools import product, permutations
n = 0
for p in product('АКМС', repeat=6):
    word = ''.join(p)
    n += 1
    if 'С' not in word:
        if 'М' not in word:
            if 'КК' not in word:
                print(n, word)
'''


#
# № 19240 ЕГКР 21.12.24 (Уровень: Базовый)
'''
from itertools import *
n = 0
for p in product(sorted('ЯНВАРЬ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word[0] != 'Я':
        if word.count('Ь') <= 1:
            if 'ЯЯ' not in word:
                print(n, word)
'''


# № 18484 (Уровень: Средний)
'''
from itertools import *
n = 0
for p in product(sorted('ПАВСКИЙ'), repeat=6):
    word = ''.join(p)
    if 'АА' in word or 'ИИ' in word or 'АИ' in word or 'ИА' in word:
        n += 1
        if word == 'КАКААА':
            print(n)
'''


# № 18120 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
n = 0
for p in product(sorted('ПРЕСТОЛ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[-1] in 'ЕО':
            for x in 'ПРСТЛ':
                word = word.replace(x, 'Т')
            if word.count('Т') <= 3:
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
# ФИПИ = [2, 6, 8.1, 12]
# КЕГЭ  = []
# на следующем уроке:
