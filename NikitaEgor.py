# region Домашка: ******************************************************************

# № 1933 (Уровень: Базовый)
'''
R = []
from itertools import permutations
for p in permutations('КЛАБХАУС'):
    word = ''.join(p)
    # if 'АА' not in word:
    # if all(x not in word for x in 'АА ЛЛ КК ББ ХХ СС УУ'.split()):
    if all(word[i] != word[i+1] for i in range(len(word)-1)):
        R.append(word)
print(len(set(R)))
'''

'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# x[i], x[i+1]
# 1 2
# 2 3
# 3 4
# 4 5
'''


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
n = 0
L = []
s = sorted('СТРОКА')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    n += 1
                    word = a + b + c + d + e
                    if n % 2 == 0:
                        if word[0] not in 'АСТ':
                            if word.count('О') == 2:
                                L.append(n)
print(max(L))
'''

# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
# https://stepik.org/lesson/1038667/step/14?unit=1062772
'''
cnt = 0
from itertools import product
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] not in '1357':
            if num[-1] not in '26':
                if num.count('7') <= 2:
                    cnt += 1
print(cnt)
'''


# № 4613 Основная волна 2022 (Уровень: Базовый)
# Определите количество пятизначных чисел, записанных в девятеричной системе счисления,
# которые не начинаются с нечетных цифр, не оканчиваются цифрами 1 или 8,
# а также содержат в своей записи не более одной цифры 3.
'''
cnt = 0
from itertools import product
for p in product('012345678', repeat = 5):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] not in '1357':
            if num[-1] not in '18':
                if num.count('3') <= 1:
                    cnt += 1
print(cnt)
'''


# № 4668 Резервный день 2022 (Уровень: Базовый)
# Определите количество пятизначных чисел, записанных в семеричной системе счисления,
# которые начинаются с четных цифр, не оканчиваются на цифры, меньшие 3, а также
# содержат в своей записи не более одной цифры 4.
'''
cnt = 0
from itertools import product
for p in product('0123456', repeat = 5):
    num = ''. join(p)
    if num[0] != '0':
        if num[0] in '246':
            if num[-1] not in '012':
                if num.count('4') <= 1:
                    cnt += 1
print(cnt)
'''

# № 4696 Демоверсия 2023 (Уровень: Базовый)
# Определите количество пятизначных чисел, записанных в восьмеричной системе счисления,
# в записи которых только одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6.
'''
cnt = 0
from itertools import product

for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            for x in '1357':
                num = num.replace(x, '*')
            if '*6' not in num and '6*' not in num:
                cnt += 1
print(cnt)
'''


# № 5114 /dev/inf 11.22 (Уровень: Базовый)
# (А. Рогов) Определите количество пятизначных чисел, записанных в семеричной системе счисления,
# в записи которых ровно одна цифра 5, при этом никакая четная цифра не стоит рядом с цифрой 5.
'''
cnt = 0
from itertools import product
for p in product('0123456', repeat = 5):
    num = ''. join(p)
    if num[0] != '0':
        if num.count('5') == 1:
            for x in '0246':
                num = num.replace(x, '*')
            if '*5' not in num and '5*' not in num:
                cnt += 1
print(cnt)
'''


# № 6591 Пробник ИМЦ СПб (Уровень: Средний)
# Определите количество пятизначных чисел, записанных в семеричной системе счисления, в записи которых:
# 1. только одна цифра 6;
# 2. сумма четных цифр числа меньше суммы нечетных цифр числа.

cnt = 0
from itertools import product
for p in product('0123456', repeat = 5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            chet = [int(x) for x in num if x in '0246']
            nechet = [int(x) for x in num if x in '135']
            if sum(chet) < sum(nechet):
                cnt += 1
print(cnt)


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: *************************************************************





# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 8, 14, 15, 16, 23, 19-21]
# КЕГЭ = []
# на следующем уроке:
