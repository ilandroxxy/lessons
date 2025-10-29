# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
s = 'abc'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            cnt += 1
            print(cnt, a, b, c)
'''


'''
from itertools import product

for p in product('abc', repeat=3):
    word = ''.join(p)
    print(p, word)
'''

'''
from itertools import permutations
for p in permutations('abc', r=3):
    word = ''.join(p)
    print(p, word)
'''


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
# Вариант 1
s = sorted('СТРОКА')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1  # n = n + 1
                    if n % 2 == 0:
                        if a not in 'АСТ':
                            if word.count('О') == 2:
                                print(n)
'''
# Вариант 2
'''
RES = []
from itertools import product
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    a, b, c, d, e = word
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
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


# № 17862 Демоверсия 2025 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            # if num.count('9') + num.count('A') + num.count('B') <= 3:
            if len([x for x in num if x > '8']) <= 3:
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
# ФИПИ = [2, 5, 6, 8, 13, 14]
# КЕГЭ = []
# на следующем уроке:
