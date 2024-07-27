# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#
# № 17671 Передача 04.07.24 (Уровень: Базовый)
# Все пятибуквенные слова, в составе которых могут быть только русские буквы Л, А, Й, М,
# записаны в алфавитном порядке и пронумерованы начиная с 2.
# Вот начало списка:
# 1. ААААА
# 2. ААААЙ
# 3. ААААЛ
# 4. ААААМ
# 5. АААЙА
# …
# Под каким номером в списке идёт последнее слово, которое не содержит ни одной буквы М,
# ни одной буквы Л и не содержит букв Й стоящих рядом?
'''
# Вариант 1
s = sorted('ЛАЙМ')
num = 0
R = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    num += 1
                    if 'М' not in word and word.count('Л') == 0:
                        if 'ЙЙ' not in word:
                            R.append(num)
print(max(R))


# Вариант 2

from itertools import product
R = []
num = 0
for p in product(sorted('ЛАЙМ'), repeat=5):
    word = ''.join(p)
    num += 1
    if 'М' not in word and word.count('Л') == 0:
        if 'ЙЙ' not in word:
            R.append(num)
print(max(R))
'''


#
# № 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
# Петя составляет слова путём перестановки букв в слове ПРОСТО.
# Сколько он сможет составить слов, если запрещено ставить рядом две одинаковые буквы?
'''
from itertools import permutations
cnt = set()
for p in permutations('ПРОСТО'):
    word = ''.join(p)
    if 'ОО' not in word:
        cnt.add(word)
print(len(cnt))
'''
'''
from itertools import permutations
R = []
for p in permutations('ПРОСТО'):
    word = ''.join(p)
    if 'ОО' not in word:
        R.append(word)
print(len(set(R)))
'''

'''
my_list = [1, 2, 3]
L = []  # L = list()

my_tuple = (1, 2, 3)
T = ()  # T = tuple()

my_set = {1, 2, 3}
S = set()

D = {}  # D = dict()
print(type(D))  # <class 'dict'>
my_dict = {1: 'один', 2: 'два'}
'''


#
# № 17627 Основная волна 19.06.24 (Уровень: Базовый)
# Определите количество 15-ричных пятизначных чисел,
# в записи которых ровно одна цифра 8 и не менее двух
# цифр с числовым значением, превышающим 9.
'''
s = '0123456789ABCDE'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0' and num.count('8') == 1:
                        if len([x for x in num if x > '9']) >= 2:
                            cnt += 1
print(cnt)
'''

# Вариант 2
'''
from itertools import product
cnt = 0
for p in product('0123456789ABCDE', repeat=5):
    num = ''.join(p)
    if num[0] != '0' and num.count('8') == 1:
        if len([x for x in num if x > '9']) >= 2:
            cnt += 1
print(cnt)
'''


# № 15413 (Уровень: Средний)
# (А. Вдовин) Найдите количество четырехзначных чисел в девятеричной
# системе счисления, в которых есть ровна одна цифра 8,
# а сумма цифр слева от нее равна сумме цифр справа от нее.
#
# Примечание: если слева или справа от 8 цифр нет,
# то сумма считается равной нулю
'''
s = '012345678'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                num = a + b + c + d
                if num[0] != '0':
                    if num.count('8') == 1:
                        i = num.index('8')
                        num = [int(x) for x in num]
                        if sum(num[:i]) == sum(num[i+1:]):
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
# ФИПИ = [5, 8, 14]
# КЕГЭ  = []
# на следующем уроке:
