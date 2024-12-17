# region Домашка: ******************************************************************

# № 48393 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:8]:
    for y in alphabet[:8]:
        A = int(f'{y}04{x}5', 11)
        B = int(f'253{x}{y}', 8)
        if (A + B) % 117 == 0:
            M.append((A + B) // 117)
print(min(M))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import product, permutations

for p in product('01', repeat=2):
    word = ''.join(p)
    print(p, word)
    # ('0', '0') 00
    # ('0', '1') 01
    # ('1', '0') 10
    # ('1', '1') 11

print('................')

for p in permutations('01', r=2):
    word = ''.join(p)
    print(p, word)
    # ('0', '1') 01
    # ('1', '0') 10
'''

# 8 https://education.yandex.ru/ege/task/6420d873-dfac-4b7d-a0ff-4f1762b24476
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
                if n == 211:
                    print(word)

# Вариант 2

from itertools import *
n = 0
for p in product(sorted('МАРИЯ'), repeat=4):
    word = ''.join(p)
    n += 1
    if n == 211:
        print(word)

# Вариант 3

from itertools import *
for n, p in enumerate(product(sorted('МАРИЯ'), repeat=4), 1):
    word = ''.join(p)
    if n == 211:
        print(word)
'''


# 8 https://education.yandex.ru/ege/task/78b6e053-eaf4-40bc-a7d1-53fad9f7eee4
'''
from itertools import *
n = 0
R = []
for p in product(sorted('БАТЫР'), repeat=5):
    word = ''.join(p)
    n += 1
    if 'Ы' not in word and 'АА' not in word:
        R.append(n)
print(max(R))
'''


# 8 https://education.yandex.ru/ege/task/60c1a00c-2fd4-472e-b4aa-50791d6bddb8
'''
from itertools import *
cnt = 0
for p in permutations('КАБИНЕТ'):
    word = ''.join(p)
    if word[0] not in 'АИЕ':
        cnt += 1
print(cnt)
'''


# 8 https://education.yandex.ru/ege/task/7ddd002e-129b-40c6-8fcf-431d15434fa8
'''
from itertools import *
cnt = 0
for p in product('БАНДЕРОЛЬ', repeat=7):
    word = ''.join(p)
    if word.count('Ь') <= 1:
        for x in 'БРНДЛ':
            word = word.replace(x, '*')
        if '*Е' not in word and 'Е*' not in word:
            cnt += 1
print(cnt)
'''


# todo разобрать 8 https://education.yandex.ru/ege/task/e680d278-78ba-4399-b8e4-d90c7e4b2d4e
'''
from itertools import *
cnt = 0
for p in permutations('01234567', r=5):
    num = ''.join(p)
    if num[0] != '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1')
        if '111' not in num and '222' not in num:
            print(num)
            num = num[1:-1]
            print(num)
            cnt += 1
print(cnt)
'''


# 8 https://education.yandex.ru/ege/task/e327b270-8faa-450f-a350-e313a28bbee9
'''
from itertools import *
cnt = 0
for p in product('0123', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if any(num.count(x) >= 2 for x in num):
            cnt += 1
print(cnt)
'''


# todo 8 https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9

from itertools import *
cnt = 0
for p in product('ГИПЕРБОЛА', repeat=6):
    word = ''.join(p)
    if word[0] not in 'ИЕОА' and word[-1] not in 'ИЕОА':
        for x in 'ИЕОА':
            word = word.replace(x, 'A')
        for x in 'ГПРБЛ':
            word = word.replace(x, 'Б')
        if 'БАБ' not in word:
            cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
