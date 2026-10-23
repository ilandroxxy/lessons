# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
ip = '34.243.56.3'
IP = ip.split('.')  # ['34', '243', '56', '3']
ip = ','.join(IP)  # 34,243,56,3


ip = '34 243    56        3'
IP = ip.split()  # ['34', '243', '56', '3']
ip = '* *'.join(IP)  # 34* *243* *56* *3
print(ip)
'''



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

# Определите, под каким номером в этом списке стоит первое
# слово с чётным номером, которое не начинается с букв А, Е или К
# и при этом содержит в своей записи не менее одной буквы Т.
'''
# Вариант 1
RES = []
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
                        if a not in 'АЕК':
                            if word.count('Т') >= 1:
                                RES.append(n)
print(min(RES))


# Вариант 2

n = 0
RES = []
from itertools import product
for p in product(sorted('АКЦЕНТ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АЕК':
            if word.count('Т') >= 1:
                RES.append(n)
print(min(RES))

# Вариант 3

RES = []
from itertools import product
for n, p in enumerate(product(sorted('АКЦЕНТ'), repeat=5), 1):
    word = ''.join(p)
    if n % 2 == 0:
        if word[0] not in 'АЕК':
            if word.count('Т') >= 1:
                RES.append(n)
print(min(RES))
'''


# № 29340 Открытый вариант 2026(Уровень: Базовый)
'''
n = 0
RES = []
from itertools import *
for p in product(sorted('АПРЕЛЬ'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[0] not in 'АЛ':
            if word.count('П') >= 2:
                RES.append(n)
print(min(RES))
'''


# № 7 Демоверсия 2021(Уровень: Базовый)
# Игорь составляет таблицу кодовых слов для передачи сообщений,
# каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Игорь использует трёхбуквенные слова,
# в которых могут быть только буквы Ш, К, О, Л, А, причём
# буква К появляется ровно 1 раз. Каждая из других допустимых
# букв может встречаться в кодовом слове любое количество раз
# или не встречаться совсем. Сколько различных кодовых слов
# может использовать Игорь?
'''
cnt = 0
from itertools import product
for p in product('ШКОЛА', repeat=3):
    word = ''.join(p)
    if word.count('К') == 1:
        cnt += 1
print(cnt)
'''

# № 198 (Уровень: Базовый)
# Вася составляет 5-буквенные коды из букв Н, И, Ч, Ь, Я.
# Каждую букву нужно использовать ровно 1 раз, при этом код
# не может начинаться с буквы Ь и не может содержать сочетания ЬИЯ.
# Сколько различных кодов может составить Вася?
'''
cnt = 0
from itertools import permutations
for p in permutations('НИЧЬЯ', r=5):
    word = ''.join(p)
    if word[0] != 'Ь' and 'ЬИЯ' not in word:
        cnt += 1
print(cnt)
'''


# № 199 (Уровень: Средний)
# Петя составляет 5-буквенные слова из букв К, О, Л, У, Н.
# Каждую букву нужно использовать ровно 1 раз, при этом код
# при этом нельзя ставить подряд две гласные или две согласные.
# Сколько различных кодов может составить Петя?
'''
cnt = 0
from itertools import permutations
for p in permutations('КОЛУН', r=5):
    word = ''.join(p)
    for x in 'КЛН':
        word = word.replace(x, 'Н')
    for x in 'ОУ':
        word = word.replace(x, 'О')
    if 'НН' not in word and 'ОО' not in word:
        cnt += 1
print(cnt)
'''

# № 201 (Уровень: Базовый)
# Маша составляет 7-буквенные коды из букв П, Е, С, К, А, Р, Ь.
# Каждую букву нужно использовать ровно 1 раз, при этом код
# буква Ь не может стоять на первом месте, а также перед буквами Е, А и Р.
# Сколько различных кодов может составить Маша?
'''
cnt = 0
from itertools import permutations
for p in permutations('ПЕСКАРЬ', r=7):
    word = ''.join(p)
    if word[0] != 'Ь':
        for x in 'ЕАР':
            word = word.replace(x, '*')
        if 'Ь*' not in word:
            cnt += 1
print(cnt)
'''


# № 425 Джобс 05.10.2020(Уровень: Базовый)
# Женя составляет слова переставляя буквы З, А, П, И, С, Ь.
# Сколько слов может составить Женя, если известно, что Ь не может
# стоять на первом месте и после гласной?
'''
cnt = 0
from itertools import permutations
for p in permutations('ЗАПИСЬ'):
    word = ''.join(p)
    if word[0] != 'Ь':
        for x in 'АИ':
            word = word.replace(x, '*')
        # if '*Ь' not in word:
        if word.count('*Ь') == 0:
            cnt += 1
print(cnt)
'''


# № 209 Джобс 14.09.2020(Уровень: Средний)
# Сколько существует чисел, делящихся на 5, десятичная запись
# которых содержит 7 цифр, причём все цифры
# различны и никакие две чётные и две нечётные цифры не стоят рядом.

cnt = 0
from itertools import permutations
for p in permutations('0123456789', r=7):
    num = ''.join(p)
    if num[0] != '0':
        # if int(num) % 5 == 0:
        if num[-1] in '05':
            for x in '02468':
                num = num.replace(x, '+')
            for x in '13579':
                num = num.replace(x, '*')
            if '++' not in num and '**' not in num:
                cnt += 1
print(cnt)






# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [8.1, 19-21, 16]
# КЕГЭ = []
# todo на следующем уроке:  5, 14, 23  - что-то смотрели
