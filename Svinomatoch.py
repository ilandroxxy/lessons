# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import product, permutations

for p in permutations('ABCD', r=3):
    print(p)
    # ('A', 'B', 'C')
    # ('A', 'B', 'D')
    # ('A', 'C', 'B')
    # .....

for p in (product('ABC', repeat=2)):
    print(p)
    # ('A', 'A')
    # ('A', 'B')
    # ('A', 'C')
    # ('B', 'A')
    # ('B', 'B')
    # ('B', 'C')
    # ('C', 'A')
    # ('C', 'B')
    # ('C', 'C')
'''

'''
count = 0
from itertools import product, permutations
for p in permutations('ABCD', r=3):
    count += 1
print(count)  # 24 - получилось 24 перестановки элементов


count = 0
from itertools import *
for p in product('ABCD', repeat=3):
    count += 1
print(count)
# TypeError: unsupported operand type(s) for +=: 'type' and 'int'
'''


# № 31354 Пересдача 08.07.26(Уровень: Базовый)
# Все шестибуквенные слова, составленные из букв С, О, Л, Н, Ц, Е,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. EEEEEE
# 2. ЕЕЕЕЕЛ
# 3. ЕЕЕЕЕН
# 4. EEEEEO
# 5. EEEEEC
# 6. ЕЕЕЕЕЦ
# Определите, под каким номером в этом списке стоит последнее слово
# с нечётным номером, которое не начинается с букв Ц или Н и при этом
# содержит в своей записи ровно одну букву Ц и ровно одну букву Н.

# Вариант 1
'''
s = sorted('СОЛНЦЕ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if n % 2 != 0:
                            if word[0] not in 'ЦН':
                                if word.count('Ц') == 1 and word.count('Н') == 1:
                                    print(n)
'''

# Вариант 2
'''
from itertools import *
n = 0
for p in product(sorted('СОЛНЦЕ'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] not in 'ЦН':
            if word.count('Ц') == 1 and word.count('Н') == 1:
                print(n)
'''

# Вариант 3
'''
from itertools import *
for n, p in enumerate(product(sorted('СОЛНЦЕ'), repeat=6), 1):
    word = ''.join(p)
    if n % 2 != 0:
        if word[0] not in 'ЦН':
            if word.count('Ц') == 1 and word.count('Н') == 1:
                print(n)
'''




# № 31505 Демоверсия 2027(Уровень: Базовый)
# Все пятибуквенные слова, составленные из букв А, К, Ц, Е, Н, Т,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ААААА
# 2. ААААЕ
# 3. ААААК
# 4. ААААН
# 5. ААААТ
# 6. ААААЦ
# Определите, под каким номером в этом списке стоит первое слово с чётным номером,
# которое не начинается с букв А, Е или К и при этом содержит в своей записи
# не менее одной буквы Т.
'''
s = sorted('АКЦЕНТ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if n % 2 == 0:
                        if word[0] not in 'АЕК':
                            if word.count('Т') >= 1:
                                print(n)
                                exit()
'''
'''
n = 0
from itertools import product
for i in product(sorted('АКЦЕНТ'), repeat=5):
    word = ''.join(i)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АЕК':
            if word.count('Т') >= 1:
                print(n)
                exit()
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14]
# КЕГЭ = []
# на следующем уроке:

