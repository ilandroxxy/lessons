# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: *************************************************************


#  № 6901 (Уровень: Средний)
'''
L = []
s = sorted('БАРШ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    sogl = [x for x in word if x in 'БРШ']
                    copied1 = [x for x in word if word.count(x) == 1]
                    copied2 = [x for x in word if word.count(x) == 2]
                    if len(sogl) <= 3:
                        if len(copied2) == 2 and len(copied1) == 3:
                            L.append(n)
print(max(L))
'''


# № 5553 (Уровень: Средний)
'''
R = []
from itertools import permutations
for p in permutations('СОТОЧКА'):
    word = ''.join(p)
    if 'ОА' in word or 'АО' in word or 'ОО' in word:
        R.append(word)
print(len(set(R)))
'''


# № 13094 (Уровень: Средний)
# Сколько существует 9-значных девятеричных чисел, в записи
# которых не встречается цифра 0, любые две соседние цифры имеют
# разную чётность, и никакая цифра не повторяется больше 3 раз?
'''
cnt = 0
s = '12345678'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                for p in s:
                                    num = a + b + c + d + e + f + g + h + p
                                    copied = [x for x in num if num.count(x) <= 3]
                                    if len(copied) == 9:
                                        for x in '02468':
                                            num = num.replace(x, '2')
                                        for x in '1357':
                                            num = num.replace(x, '1')
                                        if '11' not in num and '22' not in num:
                                            cnt += 1
print(cnt)
'''

# № 13094 (Уровень: Средний)
'''
cnt = 0
from itertools import product
for p in product('12345678', repeat=9):
    num = ''.join(p)
    copied = [x for x in num if num.count(x) <= 3]
    if len(copied) == 9:
        for x in '02468':
            num = num.replace(x, '2')
        for x in '1357':
            num = num.replace(x, '1')
        if '11' not in num and '22' not in num:
            cnt += 1
print(cnt)
'''



# № 17627 Основная волна 19.06.24 (Уровень: Базовый)
# Определите количество 15-ричных пятизначных чисел, в записи которых ровно
# одна цифра 8 и не менее двух цифр с числовым значением, превышающим 9.
'''
cnt = 0
s = '0123456789ABCDE'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('8') == 1:
                            B = [x for x in num if x > '9']
                            if len(B) >= 2:
                                cnt += 1
print(cnt)

cnt = 0
from itertools import product
for p in product('0123456789ABCDE', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            B = [x for x in num if x > '9']
            if len(B) >= 2:
                cnt += 1
print(cnt)
'''



# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
# Определите количество восьмеричных пятизначных чисел, которые
# не начинаются с нечётных цифр, не оканчиваются цифрами 2 или 6,
# а также содержат не более двух цифр 7.
'''
cnt = 0
s = '01234567'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num[0] not in '1357':
                            if num.count('7') <= 2:
                                if num[-1] not in '26':
                                    cnt += 1
print(cnt)
'''


# № 4613 Основная волна 2022 (Уровень: Базовый)
# Определите количество пятизначных чисел, записанных в девятеричной
# системе счисления, которые не начинаются с нечетных цифр,
# не оканчиваются цифрами 1 или 8, а также содержат в своей записи
# не более одной цифры 3.
'''
cnt = 0
from itertools import product
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] not in '1357':
            if num.count('3') <= 1:
                if num[-1] not in '18':
                    cnt += 1
print(cnt)
'''


# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
# Сколько существует семизначных семеричных чисел, которые содержат
# в своей записи ровно две чётные цифры?
'''
cnt = 0
s = '0123456'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if num[0] != '0':
                                chet = [x for x in num if x in '0246']
                                if len(chet) == 2:
                                # if num.count('0') + num.count('2') + num.count('4') + num.count('6') == 2:
                                    cnt += 1
print(cnt)
'''


# № 4588 Основная волна 2022 (Уровень: Базовый)
# Определите количество пятизначных чисел, записанных в восьмеричной
# системе счисления, в записи которых ровно одна цифра 6, при этом
# никакая нечётная цифра не стоит рядом с цифрой 6.

cnt = 0
from itertools import product
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            for x in '1357':
                num = num.replace(x, '1')
            if '16' not in num and '61' not in num:
                cnt += 1
print(cnt)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 8, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
