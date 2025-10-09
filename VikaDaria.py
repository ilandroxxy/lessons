# region Домашка: ******************************************************************

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36+1):
    for x in alp[:p]:
        for y in alp[:p]:
            A = int(f'5{x}83', p)
            B = int(f'{x}9{x}9', p)
            C = int(f'{y}20{y}', p)
            if A + B == C:
                print(int(x + y + y + x, p))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import product, permutations

for p in permutations('abc', r=3):
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


# № 23267 Основная волна 11.06.25 (Уровень: Базовый)
# Все пятибуквенные слова, составленные из букв С, Т, Р, О, К, А,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. AAAAA
# 2. ААААК
# 3. ААААО
# 4. AAAAP
# 5. AAAAC
# 6. AAAAT
# Определите, под каким номером этом списке стоит последнее слово с
# нечетным номером, которые не начинается с букв А или Л и при этом
# содержит в своей записи ровно одну букву С.

# Вариант 1
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
                    if n % 2 != 0:
                        if a not in 'АЛ':
                            if word.count('С') == 1:
                                RES.append(n)
print(max(RES))

# Вариант 2
from itertools import product
RES = []
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    # a, b, c, d, e = word
    n += 1
    if n % 2 != 0:
        if word[0] not in 'АЛ':
            if word.count('С') == 1:
                RES.append(n)
print(max(RES))


# Вариант 3
from itertools import product
RES = []
for n, p in enumerate(product(sorted('СТРОКА'), repeat=5), 5):
    word = ''.join(p)
    print(n, word)
    # a, b, c, d, e = word
    if n % 2 != 0:
        if word[0] not in 'АЛ':
            if word.count('С') == 1:
                RES.append(n)
print(max(RES))
'''


# № 21407 Досрочная волна 2025 (Уровень: Базовый)
#
# Виктор составляет таблицу кодовых слов для передачи сообщений, каждому
# сообщению соответствует своё кодовое слово. В качестве кодовых слов
# Виктор использует 5-буквенные слова, в которых могут быть только
# буквы Д, Г, И, А, Ш, Э, причём слово не должно начинаться с гласной
# и не должно заканчиваться согласной.
# Сколько различных кодовых слов может использовать Виктор?
'''
cnt = 0
from itertools import product
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    if word[0] not in 'ИАЭ':
        if word[-1] in 'ИАЭ':
            cnt += 1
print(cnt)
'''


# № 11201 (Уровень: Средний)
# (С. Якунин) Полина составляет слова, переставляя буквы в слове ПАЙТОН.
# Сколько слов может составить Полина, если известно, что сумма
# порядковых номеров гласных букв, в каждом из них, равна 6?
# Буквы нумеруются слева направо, начиная с единицы.
'''
cnt = 0
from itertools import permutations
for p in permutations('ПАЙТОН'):
    word = ''.join(p)
    summa = 0
    for x in word:
        if x == 'А':
            summa += word.find(x) + 1
        if x == 'О':
            summa += word.find(x) + 1
    if summa == 6:
        cnt += 1
print(cnt)
'''


# № 20898 Апробация 05.03.25 (Уровень: Базовый)
# Определите количество девятеричных пятизначных чисел,
# в записи которых ровно одна цифра 0,
# при этом никакая нечётная цифра не стоит рядом с цифрой 0.
'''
from itertools import product
cnt = 0
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 1:
            # if all(x not in num for x in '01 10 30 03 50 05 70 07'.split()):
            for x in '1357':
                num = num.replace(x, '*')
            if '*0' not in num and '0*' not in num:
                cnt += 1
print(cnt)
'''


# № 17862 Демоверсия 2025 (Уровень: Базовый)
# Определите количество 12-ричных пятизначных чисел, в записи которых
# ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8.
'''
from itertools import product
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            if len([x for x in num if x > '8']) <= 3:
                cnt += 1
print(cnt)
'''


# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
# Определите количество восьмеричных пятизначных чисел,
# которые не начинаются с нечётных цифр, не оканчиваются цифрами 2 или 6,
# а также содержат не более двух цифр 7.
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


# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
# Сколько существует семизначных семеричных чисел,
# которые содержат в своей записи ровно две чётные цифры?
'''
cnt = 0
from itertools import *
for p in product('0123456', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        for x in '0246':
            num = num.replace(x, '*')
        if num.count('*') == 2:
            cnt += 1
print(cnt)
'''


# № 15413 (Уровень: Средний)
# (А. Вдовин) Найдите количество четырехзначных чисел
# в девятеричной системе счисления, в которых есть ровна одна цифра 8,
# а сумма цифр слева от нее равна сумме цифр справа от нее.
# Примечание: если слева или справа от 8 цифр нет, то сумма считается равной нулю

cnt = 0
from itertools import *
for p in product('012345678', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            i = num.index('8')
            # 0 1 2 3     i = 2
            summa1 = sum([int(x) for x in num[:i]])
            summa2 = sum([int(x) for x in num[i+1:]])
            if summa1 == summa2:
                cnt += 1
print(cnt)



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
