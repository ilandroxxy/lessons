# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# № 18042 (Уровень: Базовый)
# (Л. Шастин) Ваня составляет 5-буквенные слова, в которых могут
# быть использованы только буквы Л, Ю, С, Т, Р, А, причём
# буква Ю используется не более двух раз. Также слово не должно оканчиваться
# согласными буквами. Словом считается любая допустимая последовательность букв,
# не обязательно осмысленная. Сколько существует таких слов, которые может написать Ваня?
'''
cnt = 0
from itertools import product
for p in product('ЛЮСТРА', repeat=5):
    word = ''.join(p)
    if word.count('Ю') <= 2:
        if word[-1] not in 'ЛСТР':
            cnt += 1
print(cnt)
'''
from multiprocessing.pool import worker
from tkinter.constants import WORD
from traceback import print_tb

# № 14412 (Уровень: Базовый)
# (Л. Шастин) Вася составляет 6-буквенные слова, в которых
# могут быть использованы только буквы А, Л, Г, О, Р, И, Т, М, причём буква Л используется
# не более одного раза. Каждая из других допустимых букв может встречаться в слове любое
# количество раз или не встречаться совсем. Слово не должно начинаться с буквы Р и оканчиваться
# согласными буквами. Словом считается любая допустимая последовательность букв, не обязательно
# осмысленная. Сколько существует таких слов, которые может написать Вася?
'''
cnt = 0
from itertools import product
for p in product('АЛГОРИТМ', repeat=6):
    word = ''.join(p)
    if word.count('Л') <= 1:
        if word[0] != 'Р':
            if word[-1] not in 'ЛГРТМ':
                cnt += 1
print(cnt)
'''


# № 19480 (Уровень: Средний)
# (Л. Шастин) Леонид составляет коды перестановкой букв слова ПАРИЖАНКА.
# При этом в этих кодах ровно один раз встречаются две идущие подряд
# гласные буквы. Сколько различных кодов может составить Леонид?
'''
R = []
from itertools import permutations
for p in permutations('ПАРИЖАНКА'):
    word = ''.join(p)
    if ('АА' in word) + ('АИ' in word) + ('ИА' in word) == 1:
        if 'ААА' not in word:
            R.append(word)
print(len(set(R)))  


R = []
from itertools import permutations
for p in permutations('ПАРИЖАНКА'):
    word = ''.join(p)
    slovo = word
    word = word.replace('И', 'А')
    if word.count('АА') == 1 and 'ААА' not in word:
        R.append(slovo)
print(len(set(R)))
'''



# № 14413 (Уровень: Базовый)
# (Л. Шастин) Леонид составляет коды перестановкой букв слова СОРТИРОВКА.
# При этом в кодах никакие три согласные или три гласные буквы не должны
# стоять рядом. Сколько различных кодов может составить Леонид?
'''
R = []
from itertools import permutations
for p in permutations('СОРТИРОВКА'):
    word = ''.join(p)
    slovo = word
    for x in 'АИО':
        word = word.replace(x, 'А')
    for x in 'СРТВК':
        word = word.replace(x, 'В')
    if 'ААА' not in word and 'ВВВ' not in word:
        R.append(slovo)
print(len(set(R)))
'''



# № 14415 (Уровень: Базовый)
# (Л. Шастин) Определите количество пятизначных чисел, записанных
# в двенадцатеричной системе счисления, в записи которых ровно две цифры A,
# и при этом никакая чётная цифра не стоит рядом с цифрой 7.
'''
cnt = 0
from itertools import product
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('A') == 2:
            for x in '02468A':
                num = num.replace(x, '*')
            if '*7' not in num and '7*' not in num:
                cnt += 1
print(cnt)
'''



# № 14414 (Уровень: Базовый)
# (Л. Шастин) Определите количество семизначных чисел, записанных
# в девятеричной системе счисления, в записи которых только одна цифра 6,
# и при этом никакие две чётные или две нечётные цифры не стоят рядом.
'''
cnt = 0
from itertools import product
for p in product('012345678', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            for x in '02468':
                num = num.replace(x, '2')
            for x in '1357':
                num = num.replace(x, '1')
            if '22' not in num and '11' not in num:
                cnt += 1
print(cnt)
'''

# Илья
# № 21894 Открытый вариант 2025(Уровень: Базовый)
# Сколько существует десятичных четырёхзначных чисел,
# в которых все цифры различны и никакие две чётные
# или две нечётные цифры не стоят рядом?
'''
cnt = 0
from itertools import permutations

for p in permutations('0123456789', r=4):
    word = ''.join(p)
    if word[0] != '0':
        for x in '02468':
            word = word.replace(x, '2')
        for x in '13579':
            word = word.replace(x, '1')
        if '11' not in word:
            if '22' not in word:
                cnt += 1
print(cnt)
'''

# Дима
# № 20898 Апробация 05.03.25(Уровень: Базовый)
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


'''
s = '3458970'
print(all(x in '0123456789' for x in s))  # True

s = '3458970a'
print(all(x in '0123456789' for x in s))  # False
'''


# № 13094 (Уровень: Средний)
# Сколько существует 9-значных девятеричных чисел,
# в записи которых не встречается цифра 0, любые две
# соседние цифры имеют разную чётность, и никакая цифра не повторяется больше 3 раз?
'''
cnt = 0
from itertools import product
for p in product('012345678', repeat=9):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 0:
            if all(num.count(x) <= 3 for x in num):
                for x in '02468':
                    num = num.replace(x, '2')
                for x in '1357':
                    num = num.replace(x, '1')
                if '11' not in num and '22' not in num:
                    cnt += 1
print(cnt)   # 483840
'''




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [8, ]
# КЕГЭ = []
# todo на следующем уроке: 15 - рассказать про all

# 2, 5, 18