# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# from itertools import product, permutations
'''
from itertools import product, permutations

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

for p in permutations('abc', r=3):
    word = ''.join(p)
    print(p, word)
    # ('a', 'b', 'c') abc
    # ('a', 'c', 'b') acb
    # ('b', 'a', 'c') bac
    # ('b', 'c', 'a') bca
    # ('c', 'a', 'b') cab
    # ('c', 'b', 'a') cba
'''
from multiprocessing.pool import worker
from os import confstr_names
from time import process_time_ns

# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
RES = []
s = sorted('СТРОКА')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if n % 2 == 0:
                        if a not in 'АСТ':
                            if word.count('О') == 2:
                                RES.append(n)
print(max(RES))
'''
# Вариант 2
'''
from itertools import product
n = 0
RES = []
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''

# Вариант 3
'''
from itertools import product

RES = []
for n, p in enumerate(product(sorted('СТРОКА'), repeat=5), 1):
    word = ''.join(p)
    print(n, word)
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''


# № 18963 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('КОТБУС', repeat=8):
    word = ''.join(p)
    if 'КОТ' in word:
        if word[0] not in 'ОУ':
            cnt += 1
print(cnt)
'''


# № 18942 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('ДИОНСЙ', repeat=6):
    word = ''.join(p)
    if ('Д' in word) + ('Н' in word) == 1:
        if all(p not in word for p in 'ДД ИИ ОО НН СС ЙЙ'.split()):
            cnt += 1
print(cnt)
'''


# № 6479 (Уровень: Базовый)
'''
from itertools import permutations
cnt = 0
for p in permutations('КАРПЫ'):
    word = ''.join(p)
    # if len(word) == len(set(word)):
    if 'АЫ' not in word and 'ЫА' not in word:
        if 'Р' in word[1:-1]:
            cnt += 1
print(cnt)
'''


# № 6261 Danov2302 (Уровень: Средний)
# (А.Богданов) Определите количество десятизначных чисел,
# записанных в восьмеричной системе счисления,
# в записи которых ровно пять цифр 7 и при этом
# никакая нечетная цифра не стоит рядом с цифрой 7.
'''
from itertools import product
cnt = 0
for p in product('01234567', repeat=10):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 5:
            for x in '135':
                num = num.replace(x, '*')
            if '*7' not in num and '7*' not in num and '77' not in num:
                cnt += 1
                print(cnt)
'''

# № 6040 ФИПИ 04.02.23 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('0123456', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            for x in '0246':
                num = num.replace(x, '*')
            for x in '135':
                num = num.replace(x, '+')
            if '**' not in num and '++' not in num:
                cnt += 1
print(cnt)
'''


# № 6015 ФИПИ 03.02.23 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('012345678', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            if num[-1] not in '02468':
                if num[0] not in '1357':
                    cnt += 1
print(cnt)
'''


# 4696
'''
from itertools import product
otv = 0
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            for i in '1357':
                num = num.replace(i, '#')
            if '#6' not in num and '6#' not in num:
                otv += 1
print(otv)
'''

# 4099
'''
from itertools import product
n = 0
for p in product(sorted('АБКЛУ'), repeat=4):
    word = ''.join(p)
    n += 1
    if len(set(word)) == len(word):
        print(n)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14]
# КЕГЭ = []
# на следующем уроке:
