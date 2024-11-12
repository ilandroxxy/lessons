# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import product, permutations

# product делает всевозможные комбинации символов с дубликатами

for p in product('01', repeat=3):
    s = ''.join(p)
    print(p, s)

    # ('0', '0', '0') 000
    # ('0', '0', '1') 001
    # ('0', '1', '0') 010
    # ('0', '1', '1') 011
    # ('1', '0', '0') 100
    # ('1', '0', '1') 101
    # ('1', '1', '0') 110
    # ('1', '1', '1') 111

# permutations комбинирует всевозможные перестановки символов без дубликатов

for p in permutations('0123', r=2):
    s = ''.join(p)
    print(p, s)
    # ('0', '1') 01
    # ('0', '2') 02
    # ('0', '3') 03
    # ('1', '0') 10
    # ('1', '2') 12
    # ('1', '3') 13
    # ('2', '0') 20
    # ('2', '1') 21
    # ('2', '3') 23
    # ('3', '0') 30
    # ('3', '1') 31
    # ('3', '2') 32
'''
import time

# Задание 8 https://education.yandex.ru/ege/task/e73090d1-5401-4307-8b8c-bd1af02cefc0
'''
# Вариант 1
s = sorted('МАРИЯ')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                if word == 'АРИЯ':
                    print(n)

# Вариант 2
from itertools import *
n = 0
for p in product(sorted('МАРИЯ'), repeat=4):
    word = ''.join(p)
    n += 1
    if word == 'АРИЯ':
        print(n)

# Вариант 3
from itertools import *
# for n, p in enumerate([], 1):
for n, p in enumerate(product(sorted('МАРИЯ'), repeat=4), 1):
    word = ''.join(p)
    if word == 'АРИЯ':
        print(n)
'''


# Задание 8 https://education.yandex.ru/ege/task/93ac0c3b-ddee-4791-a179-b256cda73ea2
'''
from itertools import *
n = 0
cnt = 0
for p in product(sorted('КЦИЧП'), repeat=6):
    word = ''.join(p)
    n += 1
    if word.count('И') == 3:
        cnt += 1
print(cnt)


from itertools import *
cnt = 0
for p in product('КЦИЧП', repeat=6):
    word = ''.join(p)
    if word.count('И') == 3:
        cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/4b7aa1a3-0a20-4901-b4dc-cafda6f242e6
'''
from itertools import *
n = 0
R = []
for p in product(sorted('БМЮРН'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 != 0 and word[0] != 'М':
        if word.count('Р') >= 2 and 'Ю' not in word:
            R.append(n)
print(max(R))
'''


# Задание 8 https://education.yandex.ru/ege/task/32ce37ef-fe98-4fdb-8097-513dd9b46730
'''
from itertools import *
cnt = 0
for p in product('ЭТАН', repeat=5):
    word = ''.join(p)
    if word.count('А') + word.count('Э') == 1:
        print(word)
        cnt += 1
print(cnt)
'''

'''
from itertools import *
cnt = 0
for p in product('ДРАКОН', repeat=8):
    word = ''.join(p)
    if word.count('А') == 1 and word.count('О') == 1:
        cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9
'''
from itertools import *
cnt = 0
for p in product('ГИПЕРБОЛА', repeat=6):
    word = ''.join(p)
    if word[0] in 'ГПРБЛ' and word[-1] not in 'ИЕОА':
        for x in 'ИЕОА':
            word = word.replace(x, 'А')
        for x in 'ГПРБЛ':
            word = word.replace(x, 'Б')
        if 'БАБ' not in word:
            print(word)
            cnt += 1
print(cnt)
'''

# Задание 8 https://education.yandex.ru/ege/task/d73b5f1e-ee81-4928-94f5-ea2abff0a9a0
'''
from itertools import *
cnt = 0
for p in permutations('01234567', r=4):
    num = ''.join(p)
    if num[0] != '0':
        if num[0] == '3' and num[-1] == '0':
            # if all(x not in num for x in '20 02 04 40 60 06......'):
            num = num.replace('0', '2').replace('4', '2').replace('6', '2')
            if '22' not in num:
                cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/9e6dd0d9-26fd-4eb9-a0e4-26994d401db5
'''
from itertools import *
cnt = 0
for p in product('012345', repeat=7):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('2') == 1:
            # print('02 20 42 24'.split())  # ['02', '20', '42', '24']
            if all(x not in num for x in '02 20 42 24'.split()):
                cnt += 1
print(cnt)
'''

# Задание 8 https://education.yandex.ru/ege/task/6f7a985f-c404-4ebe-a856-f7ed7e6d5b46
'''
from itertools import *
cnt = 0
for p in permutations('01234567', r=6):
    num = ''.join(p)
    if num[0] != '0':
        if int(num, 8) % 5 == 0:  # десятичная запись которых делится на 5?
            num = num.replace('0', '2').replace('4', '2').replace('6', '2')
            num = num.replace('3', '1').replace('5', '1').replace('7', '1')
            if '11' not in num and '22' not in num:
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
# ФИПИ = [8]
# КЕГЭ  = []
# на следующем уроке:
