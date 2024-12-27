# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17799 (Уровень: Средний)
'''
s = sorted('АРГУМЕНТ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                if len(word) == len(set(word)):
                    if list(word) == sorted(word):
                        print(n, word)


from itertools import *
n = 0
for p in product(sorted('АРГУМЕНТ'), repeat = 4):
    word = ''.join(p)
    n += 1
    if len(word) == len(set(word)):
        if list(word) == sorted(word):
            print(n, word)
'''


# № 17798 (Уровень: Базовый)
'''
s = sorted('МИНУС')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                sogl = [x for x in word if x in 'МНС']
                glas = [x for x in word if x in 'ИУ']
                if len(sogl) >= len(glas):
                    print(n)
'''


# № 15320 Досрочная волна 2024 (Уровень: Базовый)
'''
s = sorted('ПАРУС')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('У') <= 1:
                        if 'АА' not in word:
                            print(n, word)
                            exit()
'''


# 18042 (Уровень: Базовый)
'''
s = 'ЛЮСТРА'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if word.count('Ю') <= 2:
                        if e not in 'ЛСТР':
                            cnt += 1
print(cnt)
'''


# № 18923 Новогодний вариант 2025 (Уровень: Базовый)
'''
s = 'ВЬЮГА'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        if 'ЮГ' in word:
                            cnt += 1

print(cnt)
'''


# № 14412 (Уровень: Базовый)
'''
s = 'АЛГОРИТМ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        if word.count('Л') <= 1:
                            if a not in 'Р' and f not in 'ЛГРТМ':
                                cnt += 1
print(cnt)
'''

# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        # if a in '0246':
                        if a not in '1357':
                            if e not in '26':
                                if num.count('7') <= 2:
                                    cnt += 1
print(cnt)
'''


# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
'''
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if a != '0':
                                if num.count('0') + num.count('2') + num.count('4') + num.count('6') == 2:
                                # chet = [x for x in num if x in '0246']
                                # if len(chet) == 2:
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
# ФИПИ = [2, 5, 6, 12, 13, 14]
# КЕГЭ  = []
# на следующем уроке:

