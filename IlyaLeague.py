



# Пару слов про itertools
'''
from itertools import product, permutations

s = 'abcd'
for p in permutations(s, r=3):
    word = ''.join(p)
    print(p, word)
    # ('a', 'b', 'c') abc
    # ('a', 'b', 'd') abd
    # ('a', 'c', 'b') acb
    # ('a', 'c', 'd') acd
    # ('a', 'd', 'b') adb

s = 'abcd'
for p in permutations(s):
    word = ''.join(p)
    print(p, word)
    # ('a', 'b', 'c', 'd') abcd
    # ('a', 'b', 'd', 'c') abdc
    # ('a', 'c', 'b', 'd') acbd
    # ('a', 'c', 'd', 'b') acdb
    # ('a', 'd', 'b', 'c') adbc
    # ('a', 'd', 'c', 'b') adcb


for p in product(s, repeat=3):
    word = ''.join(p)
    print(p, word)
    # ('d', 'c', 'b') dcb
    # ('d', 'c', 'c') dcc
    # ('d', 'c', 'd') dcd
    # ('d', 'd', 'a') dda
    # ('d', 'd', 'b') ddb
    # ('d', 'd', 'c') ddc
    # ('d', 'd', 'd') ddd
'''


# s = '11.43.2.56'
# print(s.split('.'))  # ['11', '43', '2', '56']
# p = '11.43.2.56'.split('.')
# word = ','.join(p)
# print(word)  # 11,43,2,56




# № 27620 Апробация 04.03.26(Уровень: Базовый)
#
# Все пятибуквенные слова, в составе которых могут
# быть только русские буквы Ц, И, Т, Р, У, С, записаны в алфавитном
# порядке и пронумерованы.
# Ниже приведено начало списка.
# 1. ИИИИИ
# 2. ИИИИР
# 3. ИИИИС
# 4. ИИИИТ
# 5. ИИИИУ
# 6. ИИИИЦ
# 7. ИИИРИ
# ...
# Под каким номером в списке идёт последнее слово, которое содержит
# ровно две буквы И и не содержит букв Ц, стоящих рядом?
'''
# Вариант 1
RES = []
s = sorted('ЦИТРУС')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if word.count('И') == 2:
                        # if word.count('ЦЦ') == 0:  # не содержит букв Ц
                        if 'ЦЦ' not in word:
                            RES.append(n)
print(max(RES))

# Вариант 2
from itertools import *
n = 0
RES = []
for p in product(sorted('ЦИТРУС'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('И') == 2:
        if 'ЦЦ' not in word:
            RES.append(n)
print(max(RES))


# Вариант 3
from itertools import *
RES = []
for n, p in enumerate(product(sorted('ЦИТРУС'), repeat=5), 1):
    word = ''.join(p)
    if word.count('И') == 2:
        if 'ЦЦ' not in word:
            RES.append(n)
print(max(RES))
'''

# № 26117 (Уровень: Базовый)
# Все шестибуквенные слова, составленные из букв М, У, Ж, Ч, И, Н, А,
# записаны в алфавитном порядке и пронумерованы.

# 1.  АААААА
# 2.  АААААЖ
# 3.  АААААИ
# 4.  АААААМ
# 5.  АААААН
# 6.  АААААУ
# 7.  АААААЧ

# Определите в этом списке количество слов с чётными номерами,
# которые не начинаются с буквы Ж и при этом содержат в своей записи не
# более одной буквы Ч.
'''
from itertools import *
n = 0
RES = []
for p in product(sorted('МУЖЧИНА'), repeat=6):
    word = ''.join(p)
    a, b, c, d, e, f = word
    n += 1
    if n % 2 == 0:
        # if word[0] != 'Ж':
        if a != 'Ж':
'''


'''
from itertools import *
n = 0
cnt = 0
for p in product(sorted('МУЖЧИНА'), repeat=6):
    # word = ''.join(p)
    a, b, c, d, e, f = p
    word = a + b + c + d + e + f
    n += 1
    if n % 2 == 0:
        if word[0] != 'Ж':
            if word.count('Ч') <= 1:
                cnt += 1
print(cnt)
'''



# № 25132 (Уровень: Средний)
# (В. Лашин) Все шестибуквенные слова, составленные из букв С, Д, А, Й, Е, Г, Э записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. АААААА
# 2. АААААГ
# 3. АААААД
# 4. АААААЕ
# 5. АААААЙ
# 6. АААААС
# 7. АААААЭ
#
# Найдите сумму номеров всех слов, которые содержат сочетание букв "ЕГЭ"
'''
from itertools import product
n = 0
summa = 0
RES = []
for p in product(sorted('СДАЙЕГЭ'), repeat=6):
    word = ''.join(p)
    n += 1
    if 'ЕГЭ' in word:
        summa += n
        RES.append(n)
print(summa, sum(RES))
'''


# № 1985 (Уровень: Средний)
# Петя составляет 8-буквенные слова из букв А, Б, И, К, О, Л, У, Н.
# Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить
# подряд две гласные или две согласные. Сколько различных кодов может составить Петя?
'''
from itertools import permutations
cnt = 0
for p in permutations('АБИКОЛУН', r=8):
    word = ''.join(p)
    for x in 'АИОУ':
        word = word.replace(x, 'А')
    for x in 'БКЛН':
        word = word.replace(x, 'Б')
    if 'ББ' not in word and 'АА' not in word:
        cnt += 1
print(cnt)
'''


# № 822 Джобс 14.12.2020(Уровень: Средний)
# Катя составляет палиндромы – последовательности букв, которые
# читаются одинаково как слева направо, так и справа налево – путем
# перестановки букв фразы «Не гни папин ген». Сколько последовательностей
# может составить Катя?
'''
from itertools import permutations
cnt = 0
for p in permutations('негнипапинген'):
    word = ''.join(p)
    if word == word[::-1]:
        cnt += 1
        print(cnt, word)
print(cnt)
'''


# № 9831 Основная волна 27.06.23(Уровень: Базовый)
# Сколько существует шестнадцатеричных трёхзначных чисел,
# в которых все цифры различны и никакие две чётные или две нечётные
# цифры не стоят рядом?
'''
from itertools import permutations
cnt = 0
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in permutations(alp[:16], r=3):
    num = ''.join(p)
    if num[0] != '0':
        for x in alp[0::2]:
            num = num.replace(x, '2')
        for x in alp[1::2]:
            num = num.replace(x, '1')
        if '11' not in num and '22' not in num:
            cnt += 1
print(cnt)
'''

# Среда 18:00, 19:00, 21:00, 22:00
# Четверг 17:00, 18:00, 20:00













