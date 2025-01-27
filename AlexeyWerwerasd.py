# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************
'''
s = sorted('ЯНВАРЬ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if a != 'Я' and word.count('Ь') <= 1 and 'ЯЯ' not in word:
                        print(n)
'''


'''
s = sorted('ПРЕСТОЛ')
n = 0
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if n % 2 != 0 and e in 'ЕО' and word.count('П') + word.count('Р') + word.count('С') + word.count(
                            'Т') + word.count('Л') <= 3:
                        cnt += 1
print(cnt)
'''


# № 18042 (Уровень: Базовый)
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


# № 9363 Джобс 10.06.23 (Уровень: Средний)
'''
from itertools import *
cnt = 0
for p in permutations('ХОЧУНАБЮДЖЕТ'):
    word = ''.join(p)
    for x in 'ОУАЮЕ':
        word = word.replace(x, 'А')
    if 'ААААА' not in word:
        cnt += 1
        print(word, cnt)
'''


#
# № 8417 (Уровень: Базовый)

print('ЯО ОЯ АО ОА ЯА АЯ'.split())

s = 'ЯРОСЛАВ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if len(set(word)) == len(word):  # буквы в коде не должны повторяться,
                        sogl = [x for x in word if x in 'РСЛВ']
                        glas = [x for x in word if x in 'ЯОА']
                        if len(sogl) > len(glas):
                            if all(p not in word for p in 'ЯО ОЯ АО ОА ЯА АЯ'.split()):
                                cnt += 1
print(cnt)


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 22, 23, 25]
# КЕГЭ = [5, 8]
# на следующем уроке: 18, 19-21, 26
