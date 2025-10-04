# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



'''
from itertools import product, permutations

# Всевозможные перестановки с повторением букв
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

# Всевозможные перестановки без повторений букв
for p in permutations('abc', 2):
    word = ''.join(p)
    print(p, word)
    # ('a', 'b') ab
    # ('a', 'c') ac
    # ('b', 'a') ba
    # ('b', 'c') bc
    # ('c', 'a') ca
    # ('c', 'b') cb
'''


'''
print('АЯ ЯА ОЯ ЯО АО ОА'.split())  # ['АЯ', 'ЯА', 'ОЯ', 'ЯО', 'АО', 'ОА']
print('12.255.23.54'.split('.'))  # ['12', '255', '23', '54']

print(' '.join(['АЯ', 'ЯА', 'ОЯ', 'ЯО', 'АО', 'ОА']))  # 'АЯ ЯА ОЯ ЯО АО ОА'
print('.'.join(['12', '255', '23', '54']))  # '12.255.23.54'
'''


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
s = sorted('СТРОКА')
RES = []
n = 0
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
'''

# Вариант 2
'''
from itertools import product
RES = []
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''

# Вариант 3
'''
from itertools import product
RES = []
for n, p in enumerate(product(sorted('СТРОКА'), repeat=5), 1):
    word = ''.join(p)
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''


# № 11298 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
n = 0
for p in product(sorted('АОЖПЮЗ'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] == 'А':
            if word.count('З') >= 2:
                cnt += 1
print(cnt)
'''


# № 11295 (Уровень: Базовый)
#
# (М. Ишимов) Все 4-буквенные слова, составленные из букв Щ, Э, Д, С, Р,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ДДДД
# 2. ДДДР
# 3. ДДДС
# 4. ДДДЩ
# 5. ДДДЭ
# 6. ДДРД
# ...
# Под каким номером стоит слово ЩДЩД?
'''
from itertools import product
n = 0
for p in product(sorted('ЩЭДСР'), repeat=4):
    word = ''.join(p)
    n += 1
    if word == 'ЩДЩД':
        print(n)
'''


# № 9849 (Уровень: Средний)
# (В. Ген) Даша составляет 6-буквенные слова, содержащие в
# себе только те заглавные буквы латинского алфавита, которые
# содержатся в шестнадцатиричной системе счисления.
# Сколько различных слов может составить Даша с учётом того,
# что гласная не может стоять в начале и в конце слова?

# alp36 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# print(alp36[:16])  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
'''
from itertools import product
cnt = 0
for p in product('ABCDEF', repeat=6):
    word = ''.join(p)
    a, b, c, d, e, f = word
    if a not in 'AE' and f in 'BCDF':
        cnt += 1
print(cnt)
'''


# № 8417 (Уровень: Базовый)
#
# Ярослав составляет коды из букв, входящих в слово ЯРОСЛАВ.
# Код должен состоять из 5 букв, буквы в коде не должны повторяться,
# согласных в коде должно быть больше, чем гласных,
# две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Ярослав?
'''
from itertools import permutations
cnt = 0
for p in permutations('ЯРОСЛАВ', r=5):
    word = ''.join(p)
    sogl = [x for x in word if x in 'РСЛВ']
    glas = [x for x in word if x in 'ЯОА']
    if len(sogl) > len(glas):
        if all(x not in word for x in 'АЯ ЯА ОЯ ЯО АО ОА'.split()):
            cnt += 1
print(cnt)
'''


# № 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
# Петя составляет слова путём перестановки букв в слове ПРОСТО.
# Сколько он сможет составить слов, если запрещено ставить рядом две одинаковые буквы?
'''
from itertools import permutations
RES = []
for p in permutations('ПРОСТО'):
    word = ''.join(p)
    # if all(x not in word for x in 'ПП РР СС ТТ ОО'.split()):
    if 'ОО' not in word:
        RES.append(word)
print(len(set(RES)))
'''


# № 10090 Демоверсия 2024 (Уровень: Базовый)
# Сколько существует восьмеричных пятизначных чисел,
# не содержащих в своей записи цифру 1, в которых все цифры различны
# и никакие две чётные или две нечётные цифры не стоят рядом?
'''
from itertools import permutations
cnt = 0
for p in permutations('01234567', r=5):
    num = ''.join(p)
    if num[0] != '0':
        if '1' not in num:
            # if len(num) == len(set(num)):  # в которых все цифры различны
            for x in '0246':
                num = num.replace(x, '*')
            for x in '1357':
                num = num.replace(x, '+')
            if '**' not in num and '++' not in num:
                cnt += 1
print(cnt)
'''


# № 17521 Основная волна 07.06.24 (Уровень: Базовый)
# Определите количество восьмеричных пятизначных чисел,
# которые не начинаются с нечётных цифр, не оканчиваются
# цифрами 2 или 6, а также содержат не более двух цифр 7.
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
from itertools import product
cnt = 0
for p in product('0123456', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        chet = [x for x in num if x in '0246']
        if len(chet) == 2:
            cnt += 1
print(cnt)
'''

# № 12462 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)

# Сколько существует различных трёхзначных и пятизначных чисел,
# записанных в шестнадцатеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?

'''
from itertools import permutations

cnt = 0
for i in permutations('0123456789ABCDEF', r=3):
    m3 = ''.join(i)
    if list(m3) == sorted(m3)[::-1]:
        cnt += 1

for i in permutations('0123456789ABCDEF', r=5):
    m5 = ''.join(i)
    if list(m5) == sorted(m5)[::-1]:
        cnt += 1

print(cnt)
'''


# № 13094 (Уровень: Средний)
# Сколько существует 9-значных девятеричных чисел,
# в записи которых не встречается цифра 0, любые две соседние цифры
# имеют разную чётность, и никакая цифра не повторяется больше 3 раз?

from itertools import product
k = 0
for p in product('12345678', repeat=9):
    s = ''.join(p)
    if s[0] != '0':
        copied = [x for x in s if s.count(x) <= 3]
        if len(copied) == 9:
            for x in '24568':
                s = s.replace(x, '*')
            for x in '1357':
                s =  s.replace(x, '+')
            if '**' not in s and '++' not in s:
                k += 1
                print(k)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 14, 17]
# КЕГЭ = []
# на следующем уроке:
