# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 23746 Демоверсия 2026 (Уровень: Базовый)
# Все пятибуквенные слова, составленные из букв С, Т, Р, О, К, А,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААО
# 4. ААААР
# 5. ААААС
# 6. ААААТ
# ……
# Определите, под каким номером в этом списке стоит последнее слово
# с чётным номером, которое не начинается с букв А, С или Т
# и при этом содержит в своей записи ровно две буквы О.
'''
RES = []
n = 0
s = sorted('СТРОКА')
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

# Вариант 2

n = 0
RES = []
from itertools import product
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    # a, b, c, d, e = word
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''

'''
from itertools import permutations
for p in permutations('abc', r=3):
    print(p)


from itertools import product
for p in product('abc', repeat=10):
    print(p)
'''


# № 23554 Пересдача 03.07.25 (Уровень: Базовый)
#
# Все пятибуквенные слова, составленные из букв А, Л, Г, О, Р, И, Т, М,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ААААА
# 2. ААААГ
# 3. ААААИ
# 4. ААААЛ
# 5. AAAAM
# 6. ААААО
# 7. AAAAP
# Определите, под каким номером в этом списке стоит первое слово
# с чётным номером, которое не начинается с букв А или Г и при этом
# содержит в своей записи не менее двух букв Р.
'''
n = 0
RES = []
from itertools import product
for p in product(sorted('АЛГОРИТМ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АГ':
            if word.count('Р') >= 2:
                RES.append(n)
print(min(RES))
'''


# № 21407 Досрочная волна 2025 (Уровень: Базовый)
# Виктор составляет таблицу кодовых слов для передачи сообщений,
# каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Виктор использует 5-буквенные слова,
# в которых могут быть только буквы Д, Г, И, А, Ш, Э, причём
# слово не должно начинаться с гласной и не должно заканчиваться согласной.
# Сколько различных кодовых слов может использовать Виктор?
'''
cnt = 0
from itertools import product
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    if word[0] not in 'ИАЭ' and word[-1] not in 'ДГШ':
        cnt += 1
print(cnt)
'''


# № 5218 (Уровень: Базовый)
# Василий составляет 6-буквенные слова из букв А, Р, Б, У, З.
# Каждую букву можно использовать любое количество раз, при этом
# слово содержит три буквы А, две из которых стоят рядом, а третья
# отдельно от них. Сколько различных слов может составить Василий?
'''
cnt = 0
from itertools import product
for p in product('АРБУЗ', repeat=6):
    word = ''.join(p)
    if word.count('А') == 3:
        if 'АА' in word and 'ААА' not in word:
            cnt += 1
print(cnt)
'''


# № 24888 (Уровень: Базовый)
# Сколько существует шестнадцатеричных четырёхзначных чисел,
# содержащих в своей записи ровно одну цифру 3, в которых
# никакие две одинаковые цифры не стоят рядом?
'''
cnt = 0
from itertools import product
for p in product('0123456789ABCDEF', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('3') == 1:
            # if '00' not in num and '11' not in num ...
            if all(pair not in num for pair in '00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE FF'.split()):
                cnt += 1
print(cnt)
'''


# № 22419 (Уровень: Базовый)
# (Л. Шастин) Сколько существует тринадцатеричных семизначных чисел,
# в которых все цифры различны и никакая нечётная цифра не стоит рядом с цифрой B?
'''
cnt = 0
from itertools import permutations
for p in permutations('0123456789ABC', r=7):
    num = ''.join(p)
    if num[0] != '0':
        if all(pair not in num for pair in '1B B1 3B B3 5B B5 7B B7 9B B9'.split()):
            cnt += 1
print(cnt)


cnt = 0
from itertools import permutations
for p in permutations('0123456789ABC', r=7):
    num = ''.join(p)
    if num[0] != '0':
        for x in '13579':
            num = num.replace(x, '*')
        if '*B' not in num and 'B*' not in num:
            cnt += 1
print(cnt)
'''


# № 19753 (Уровень: Средний)
# Сколько существует шестизначных десятичных чисел, делящихся на 4,
# в которых каждая цифра может встречаться только один раз, при этом
# никакие две чётные цифры не стоят рядом.
'''
cnt = 0
from itertools import permutations
for p in permutations('0123456789', r=6):
    num = ''.join(p)
    if num[0] != '0':
        if int(num) % 4 == 0:
            for x in '02468':
                num = num.replace(x, '*')
            if '**' not in num:
                cnt += 1
print(cnt)
'''


# № 19480 (Уровень: Средний)
# (Л. Шастин) Леонид составляет коды перестановкой букв слова ПАРИЖАНКА.
# При этом в этих кодах ровно один раз встречаются две идущие подряд гласные буквы.
# Сколько различных кодов может составить Леонид?
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


# № 17862 Демоверсия 2025 (Уровень: Базовый)
# Определите количество 12-ричных пятизначных чисел, в записи которых
# ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8.
'''
cnt = 0
from itertools import product
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
# ФИПИ = [1, 2, 5, 8, 13, 14, 15, 16, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 25, 17, 9, 27
