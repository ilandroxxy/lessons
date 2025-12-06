# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 21703 ЕГКР 19.04.25 (Уровень: Базовый)
# Все шестибуквенные слова, в составе которых могут быть только буквы П, О, Б, Е, Д, А,
# записаны в алфавитном порядке и пронумерованы начиная с 1.
# 1. AAAAAA
# 2. АААААБ
# 3. АААААД
# 4. AAAAAE
# Определите последний чётный номер слова, которое начинается с буквы О
# и в котором каждая буква встречается ровно один раз.
'''
RES = []
s = sorted('ПОБЕДА')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if n % 2 == 0:
                            if a == 'О':
                                if len(word) == len(set(word)):
                                    RES.append(n)
print(max(RES))


n = 0
RES = []
from itertools import product
for p in product(sorted('ПОБЕДА'), repeat=6):
    word = ''.join(p)
    # a, b, c, d, e, f = word
    n += 1
    if n % 2 == 0:
        if word[0] == 'О':
            if len(word) == len(set(word)):
                RES.append(n)
print(max(RES))
'''


# № 21407 Досрочная волна 2025 (Уровень: Базовый)
# Виктор составляет таблицу кодовых слов для передачи сообщений, каждому
# сообщению соответствует своё кодовое слово. В качестве кодовых слов Виктор
# использует 5-буквенные слова, в которых могут быть только буквы Д, Г, И, А, Ш, Э,
# причём слово не должно начинаться с гласной и не должно заканчиваться согласной.
# Сколько различных кодовых слов может использовать Виктор?
'''
cnt = 0
s = 'ДГИАШЭ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if a not in 'АИЭ' and e not in 'ДГШ':
                        cnt += 1
print(cnt)


cnt = 0
from itertools import product
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    if word[0] not in 'АИЭ' and word[-1] not in 'ДГШ':
        cnt += 1
print(cnt)
'''


# № 19480 (Уровень: Средний)
# (Л. Шастин) Леонид составляет коды перестановкой букв слова ПАРИЖАНКА.
# При этом в этих кодах ровно один раз встречаются две идущие подряд
# гласные буквы. Сколько различных кодов может составить Леонид?
'''
RES = []
from itertools import permutations
for p in permutations('ПАРИЖАНКА'):
    word = ''.join(p)
    slovo = word
    word = word.replace('И', 'А')
    if word.count('АА') == 1 and 'ААА' not in word:
        RES.append(slovo)
print(len(set(RES)))
'''


# № 21894 Открытый вариант 2025 (Уровень: Базовый)
# Сколько существует десятичных четырёхзначных чисел,
# в которых все цифры различны и никакие две чётные
# или две нечётные цифры не стоят рядом?
'''
cnt = 0
from itertools import permutations
for p in permutations('0123456789', r=4):
    num = ''.join(p)
    if num[0] != '0':
        for x in '02468':
            num = num.replace(x, '2')
        for x in '13579':
            num = num.replace(x, '1')
        if '22' not in num and '11' not in num:
            cnt += 1
print(cnt)
'''


# № 21975 (Уровень: Базовый)
#
# (Л. Шастин) Сколько существует шестизначных чисел, записанных
# в семнадцатеричной системе счисления, в которых все цифры различны
# и никакие три чётные или три нечётные цифры не стоят рядом?
'''
cnt = 0
from itertools import permutations
for p in permutations('0123456789ABCDEFG', r=6):
    num = ''.join(p)
    if num[0] != '0':
        for x in '02468ACEG':
            num = num.replace(x, '2')
        for x in '13579BDF':
            num = num.replace(x, '1')
        if '111' not in num and '222' not in num:
            cnt += 1
print(cnt)
'''


# № 20898 Апробация 05.03.25 (Уровень: Базовый)
# Определите количество девятеричных пятизначных чисел,
# в записи которых ровно одна цифра 0, при этом никакая нечётная
# цифра не стоит рядом с цифрой 0.
'''
cnt = 0
from itertools import product
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 1:
            for x in '1357':
                num = num.replace(x, '1')
            if '10' not in num and '01' not in num:
                cnt += 1
print(cnt)
'''


# № 17862 Демоверсия 2025 (Уровень: Базовый)
# Определите количество 12-ричных пятизначных чисел,
# в записи которых ровно одна цифра 7 и не более трёх цифр
# с числовым значением, превышающим 8.
'''
cnt = 0
from itertools import product
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            if len([x for x in num if x > '8']) <= 3:
                cnt += 1
print(cnt)
'''


# № 14413 (Уровень: Базовый)
#
# (Л. Шастин) Леонид составляет коды перестановкой букв слова СОРТИРОВКА.
# При этом в кодах никакие три согласные или три гласные буквы не должны стоять рядом.
# Сколько различных кодов может составить Леонид?

RES = []
from itertools import permutations
for p in permutations('СОРТИРОВКА'):
    word = ''.join(p)
    slovo = word
    for x in 'ОИА':
        word = word.replace(x, '*')
    for x in 'СРТВК':
        word = word.replace(x, '+')
    if '***' not in word and '+++' not in word:
        RES.append(slovo)
print(len(set(RES)))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 13, 14, 15, 16, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
