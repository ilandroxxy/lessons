# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19552 (Уровень: Базовый)
'''
M = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + '100'
    else:
        s = s + '011'
    r = int(s, 2)
    if r > 300:
        M.append(n)

print(min(M))
'''


# № 19551 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for n in range(1, 10000):
    s = convert(n, 3)
    s = s.replace('2', '*').replace('0', '2').replace('*', '0')
    r = int(s, 3)
    res = abs(n - r)
    if res == 378:
        print(n)
        break
'''


# № 19240 ЕГКР 21.12.24 (Уровень: Базовый)
'''
from itertools import *
M = []
n = 0
for p in product(sorted('ЯНВАРЬ'), repeat=5):
    slovo = ''.join(p)
    n += 1
    if slovo[0] != 'Я' and slovo.count('Ь') <= 1 and 'ЯЯ' not in slovo:
        M.append(n)
print(max(M))
'''


# № 18484 (Уровень: Средний)
'''
from itertools import *
M = []
n = 0
for p in product(sorted('ПАВСКИЙ'), repeat=6):
    slovo = ''.join(p)
    if any(p in slovo for p in ('ИИ', 'АА', 'АИ', 'ИА')):
        n += 1
        if slovo == 'КАКААА':
            print(n)
'''


# № 14412 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('АЛГОРИТМ', repeat=6):
    slovo = ''.join(p)
    if slovo.count('Л') <= 1:
        if slovo[0] != 'Р':
            if slovo[-1] not in 'ЛГРТМ':
                cnt += 1
print(cnt)
'''


# № 14413 (Уровень: Базовый)
'''
from itertools import *
cnt = []
for p in permutations('СОРТИРОВКА'):
    slovo = ''.join(p)
    word = slovo
    for x in 'СРТВК':
        word = word.replace(x, 'Б')
    for x in 'ОАИ':
        word = word.replace(x, 'А')
    if 'ААА' not in word and 'БББ' not in word:
        cnt.append(slovo)
print(len(set(cnt)))
'''


# № 18260 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('0123456789AB', repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('B') == 1:
            chet = [x for x in num if x in '02468A']
            nechet = [x for x in num if x in '13579B']
            if len(chet) == len(nechet):
                cnt += 1
print(cnt)
'''


# № 18973 (Уровень: Средний)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet)
cnt = 0
from itertools import *
for p in product(alphabet[:25], repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        chet = [x for x in num if x in alphabet[:25:2]]
        if len(chet) >= 1:
            D = [x for x in num if x > 'F']
            if len(D) > 2:
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
# ФИПИ = [2, 5, 6, 8, 12, 14, 16]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
